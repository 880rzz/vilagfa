# Világfa Sárkányai — Gyermek Dobcsapat

A Regélő Fehér Táltos Hagyományőrző Egyesület bécsi gyerek dobcsapatának és a Bécsi Magyar Iskolának a programoldala.

## Fájlszerkezet

- `index.html` — főoldal, program, helyi kapcsolattartó, közös örömzene és kapcsolat
- `jelentkezes.html` — jelentkezési lap
- `adatvedelem.html` — GDPR adatvédelmi tájékoztató
- `google-apps-script.gs` — a jelentkezési form feldolgozója
- `site.css`, `apple-layout.css` — megjelenés és reszponzív elrendezés
- `llms.txt` — a program AI-rendszerek számára olvasható összefoglalója
- `images/andrea-stage-2026.jpg` — a szervezők által küldött színpadi csoportkép
- `images/andrea-family-2026.jpg` — a szervezők által küldött gyermek- és felnőtt dobos csoportkép

## Programadatok

- Korosztály: 6–14 év.
- Gyermekfoglalkozás: havi egy alkalom, 2 óra.
- Egy alkalom: 20 EUR / fő.
- Féléves hozzájárulási díj: 70 EUR / fő.
- Helyi kapcsolattartó: Hupczik Andrea.
- Kapcsolat: +43 670 6539011, `taltosdob@gmail.com`, `www.taltosdob.hu`.
- A program házigazdája és szakmai vezetője: Regélő Fehér Táltos Hagyományőrző Egyesület Dobcsapata.

## Közös örömzene Bécsben

A gyermekfoglalkozást követő közös dobolás és zenélés időtartama 1,5 óra. Zenei vagy dobos előképzettség nem szükséges, hangszereket lehet hozni. A részvételi díj 5 EUR / fő; az előtte lévő dobos foglalkozáson résztvevő gyerekeknek ingyenes. Létszám: 10–30 fő.

## Jelentkezési rendszer

A webes jelentkezés Google Apps Scripten keresztül kerül feldolgozásra. A repóban lévő `google-apps-script.gs` módosítása önmagában nem frissíti a már telepített Apps Script Web Appot; a backend módosításához új Apps Script verzió telepítése szükséges.

A jelentkezési lap a szülő/gondviselő alapadatait, a gyermek nevét és életkorát, az önként megadott nyelvi és zenei tapasztalatot, a közös örömzenéhez való csatlakozási szándékot, valamint a GDPR-hozzájárulást kezeli.
