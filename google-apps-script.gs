/**
 * Világfa Sárkányai — Gyermek Dobcsapat | Jelentkezési form feldolgozó
 * Google Apps Script (Web App)
 *
 * Aktuális frontend: https://taltosdob.magyariskola.at/jelentkezes.html
 *
 * FONTOS: a fájl GitHubon történő módosítása önmagában nem frissíti a már
 * telepített Google Apps Script Web Appot. Módosítás után a Google Apps Scriptben
 * új verziót kell kiadni: Telepítés kezelése -> ceruza -> Új verzió -> Telepítés.
 */

var EMAIL_RECIPIENTS = 'hupczik@gmail.com, marketing@kozpontiszovetseg.at';
var EMAIL_SUBJECT    = 'Új jelentkezés — Világfa Sárkányai Gyermek Dobcsapat';
var SHEET_ID         = '';

var FIELD_LABELS = {
  szuloNev:     'Szülő / gondviselő neve',
  email:        'E-mail cím',
  telefon:      'Telefonszám',
  nyelv:        'Otthoni nyelvhasználat',
  gyermekNev:   'Gyermek neve',
  gyermekKor:   'Gyermek életkora',
  zeneiTudas:   'Előzetes zenei / ritmikai tapasztalat',
  utem:         'Foglalkozások üteme',
  ar:           'Hozzájárulási díj',
  honnan:       'Honnan hallott rólunk',
  felnottDob:   'Csatlakozna a gyermekfoglalkozás utáni közös örömzenéhez',
  megjegyzes:   'Megjegyzés',
  gdprConsent:  'Adatkezelési hozzájárulás',
  program:      'Program',
  bekuldveTime: 'Beküldés időpontja'
};

var REQUIRED_FIELDS = ['szuloNev', 'email', 'telefon', 'gyermekNev', 'gyermekKor', 'gdprConsent'];
var MAX_FIELD_LENGTH = 3000;

function doPost(e) {
  try {
    var data = parsePayload(e);
    validateData(data);
    sendNotificationEmail(data);
    if (SHEET_ID) appendToSheet(data);
    return jsonResponse({ result: 'success' });
  } catch (err) {
    console.error(err);
    return jsonResponse({ result: 'error', message: String(err && err.message ? err.message : err) });
  }
}

function doGet() {
  return ContentService.createTextOutput('Vilagfa Sarkanyai jelentkezes-feldolgozo aktiv. Domain: taltosdob.magyariskola.at').setMimeType(ContentService.MimeType.TEXT);
}

function parsePayload(e) {
  if (e && e.postData && e.postData.contents) {
    try {
      var parsed = JSON.parse(e.postData.contents);
      if (parsed && typeof parsed === 'object') return parsed;
    } catch (ignore) {}
  }
  return (e && e.parameter) ? e.parameter : {};
}

function validateData(data) {
  if (!data || typeof data !== 'object') throw new Error('Érvénytelen beküldési adatok.');
  REQUIRED_FIELDS.forEach(function (key) {
    if (data[key] === undefined || data[key] === null || String(data[key]).trim() === '') throw new Error('Hiányzó kötelező mező: ' + key);
  });
  var email = String(data.email || '').trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw new Error('Érvénytelen e-mail cím.');
  var age = Number(data.gyermekKor);
  if (!isFinite(age) || age < 6 || age > 14) throw new Error('A gyermek életkorának 6 és 14 év között kell lennie.');
  var consent = String(data.gdprConsent || '').toLowerCase();
  if (consent !== 'elfogadva' && consent !== 'igen' && consent !== 'true') throw new Error('Az adatkezelési tájékoztató elfogadása szükséges.');
  Object.keys(data).forEach(function (key) {
    var value = data[key];
    if (value !== undefined && value !== null && String(value).length > MAX_FIELD_LENGTH) throw new Error('Túl hosszú mező: ' + key);
  });
}

function sendNotificationEmail(data) {
  var rows = '';
  var plain = '';
  Object.keys(FIELD_LABELS).forEach(function (key) {
    var label = FIELD_LABELS[key];
    var value = cleanValue(data[key]);
    var safe = escapeHtml(value).replace(/\n/g, '<br>');
    rows += '<tr><td style="padding:9px 12px;border:1px solid #e2dccf;background:#f7f2e7;font-weight:600;vertical-align:top;width:235px;">' + escapeHtml(label) + '</td><td style="padding:9px 12px;border:1px solid #e2dccf;vertical-align:top;">' + safe + '</td></tr>';
    plain += label + ': ' + value + '\n';
  });
  var html = '<div style="font-family:Arial,Helvetica,sans-serif;color:#1f281f;max-width:680px;line-height:1.45;"><h2 style="color:#8b6b2f;margin-bottom:8px;">Új jelentkezés érkezett</h2><p style="margin-top:0;">A Világfa Sárkányai Gyermek Dobcsapat weboldalán keresztül új jelentkezés érkezett.</p><table style="border-collapse:collapse;width:100%;font-size:14px;">' + rows + '</table><p style="margin-top:18px;font-size:12px;color:#777167;">Automatikus értesítés: taltosdob.magyariskola.at/jelentkezes.html</p></div>';
  var replyTo = isValidEmail(data.email) ? String(data.email).trim() : undefined;
  var mailOptions = {to:EMAIL_RECIPIENTS,subject:EMAIL_SUBJECT + (data.gyermekNev ? ' — ' + String(data.gyermekNev).trim() : ''),htmlBody:html,body:plain,name:'Világfa Sárkányai jelentkezés'};
  if (replyTo) mailOptions.replyTo = replyTo;
  MailApp.sendEmail(mailOptions);
}

function appendToSheet(data) {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sheet = ss.getSheetByName('Jelentkezesek') || ss.insertSheet('Jelentkezesek');
  var keys = Object.keys(FIELD_LABELS);
  if (sheet.getLastRow() === 0) sheet.appendRow(keys.map(function (k) { return FIELD_LABELS[k]; }));
  sheet.appendRow(keys.map(function (k) { return (data[k] !== undefined && data[k] !== null) ? String(data[k]) : ''; }));
}
function cleanValue(value) { if (value === undefined || value === null || String(value).trim() === '') return '—'; return String(value).trim(); }
function isValidEmail(value) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(value || '').trim()); }
function escapeHtml(value) { return String(value).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;'); }
function jsonResponse(obj) { return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON); }
