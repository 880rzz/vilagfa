# Világfa – tipográfiai és igazítási contract

Ez a repo az `apple-layout.css` fájlt használja közös szöveg- és igazítási rendszerként. A cél az Apple HIG-hez hasonló vizuális logika: egyértelmű hierarchia, jól olvasható sorszélesség, következetes igazítás és stabil reszponzív tördelés.

## 1. Alapértelmezett igazítás

- Hosszabb olvasószöveg: `text-align: start`.
- Kártyák, listák, programleírások, kapcsolat- és információs blokkok: `text-align: start`.
- Középre igazítás csak rövid, szándékosan szimmetrikus display-elemeknél használható: hero, rövid section-head, idézet, footer headline, CTA/label.
- Egy komponensen belül ne keveredjen indokolatlanul a balra és középre igazítás.

## 2. Sortörés

- Címek: `text-wrap: balance`.
- Olvasószöveg: `text-wrap: pretty`.
- Kerülendő: `word-break: break-all`, általános `overflow-wrap:anywhere`, kézzel beszúrt `<br>` csak vizuális tördelés miatt.
- Magyar szövegnél a böngésző természetes szóhatárainak megőrzése elsődleges.

## 3. Sorszélesség

- Normál olvasószöveg: kb. 48–62 `ch`.
- Rövid leírás / hero subcopy: kb. 31–44 `ch`.
- Display headline: karakteralapú max-width; ne terüljön teljes konténerszélességre.
- Mobilon a szélesség fluid, de a címsorok továbbra is kontrollált karakterhosszúak.

## 4. Reszponzív nézetek

Kötelező ellenőrzési szélességek:

- 320 px
- 390 px
- 640 px
- 768 px
- 1024 px
- 1440 px

A layout nem hozhat létre vízszintes görgetést, túl keskeny szövegoszlopot vagy egy-két szavas „árva” sort pusztán a grid arányai miatt.

## 5. Oldaltípusok

### Főoldal

- Hero és rövid szekcióbevezetők középre rendezhetők.
- Feature-copy, program, tanulási lista, kapcsolat és részvételi információ balra/start igazított.

### Jelentkezési oldal

- Hero lehet középre rendezett.
- Form legend, label, hint, opció, GDPR és összefoglaló balra/start igazított.
- Input- és textarea-szöveg mindig természetes balról-jobbra olvasási irányú.

### Adatvédelmi oldal

- Hero lehet középre rendezett.
- Teljes jogi szövegtörzs balra/start igazított, hosszú olvasási sorszélességgel.

## 6. Forrásigazság

- A valódi főoldal: `index.html`.
- Az `Index.html` csak kompatibilitási redirect lehet; nem tartalmazhat külön dizájnt vagy tartalmi főoldalt.
- Minden publikus HTML oldalnak be kell töltenie az `apple-layout.css` fájlt, kivéve az átirányító stub oldalakat.

## 7. Regressziós szabály

Új komponens hozzáadásakor először az `apple-layout.css` meglévő tokenjeit és mintáit kell használni. Lokális `text-align`, agresszív word-break vagy kézzel kényszerített sortörés csak akkor kerülhet be, ha arra tényleges szemantikai vagy funkcionális ok van.
