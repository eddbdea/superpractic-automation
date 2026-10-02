# Analiza copy-ului SuperPractic fără SKU TEST-01

## Metodă și acoperire

Catalogul Shopify a fost citit integral prin API, cu paginare până la final: 38 de produse. Au fost verificate toate variantele fiecărui produs. Un produs este exclus dacă oricare variantă are SKU egal cu `TEST-01`, după eliminarea spațiilor de la capete și normalizarea literelor. 30 de produse au fost excluse; 8 rămân, toate cu statut ACTIVE. Au fost citite și toate cele 8 pagini publice, cu răspuns HTTP 200.

Analiza privește conținutul și configurația randată în HTML. Nu validează conversia, eficacitatea afirmațiilor sau funcționarea formularului de comandă.

## Corpusul folosit

| Produs | Headlines în descriere | Ordinea temelor |
| --- | ---: | --- |
| PowerMax | 4 | Putere stabilă → încărcare rapidă → portabilitate → cablu/pachet |
| UltraX | 4 | Dăunători → evitarea substanțelor toxice → confort/odihnă → folosire simplă |
| CurățăPVC | 4 | Aspectul ramelor → pete/murdărie → suprafețe de utilizare → folosire simplă |
| LaPedală | 4 | Murdărie întărită → uzură → compatibilitate → folosire simplă |
| Molistop | 4 | Protejarea hainelor → miros → material/durată → folosire simplă |
| Kit cu abur | 5 | Problema principală → zone greu accesibile → reziduuri/chimicale → folosirea apei → folosire simplă |

ReFilet și TurboBlast au SKU TEST-01 în catalogul citit și nu sunt surse pentru noua regulă editorială. Orice exemple din analiza anterioară care le foloseau sunt înlocuite de corpusul de mai sus.

Două produse fără SKU TEST-01 nu sunt modele potrivite: „Soluție Degresant Lanț si Curățare Bicicleta 750ML” și „5 LAVETE MICROFIBRĂ”. Descrierile produselor sunt goale, iar pagina publică moștenește din șablonul implicit texte despre ChefSlicer, inclusiv mărunțire, motor de 300W și comparații pentru tocător. Aceste probleme au fost observate, nu corectate. Ele stabilesc o verificare necesară pentru agent: să nu rămână beneficii sau nume ale produsului-model după duplicare.

## Reguli extrase

1. Primul headline prezintă rezultatul care răspunde problemei principale. Nu începe cu specificații izolate când cumpărătorul caută o soluție.
2. Headline-urile următoare acoperă beneficii diferite: evitarea unei consecințe, reducerea efortului, compatibilitate, confort, reutilizare sau conținut util al pachetului. Nu repeta aceeași promisiune în trei formulări.
3. Headline-urile sunt scurte, cu verbe concrete și emoji relevante. Exemple observate: „Previne Apariția Moliilor”, „NU Miroase Urât”, „Crește Durata de Viață a Lanțului”, „Ușor de Folosit”.
4. După headline vin, de regulă, unul sau două enunțuri: mecanism/funcție → efect în viața cumpărătorului. Lungimea descrierilor complete observate este aproximativ 575–811 caractere de text extras, fără markup și fără secțiunile comerciale de după descriere. Aceasta este o observație, nu o limită rigidă.
5. Bold-ul accentuează expresii scurte și concrete; emoji-urile nu înlocuiesc explicația.
6. Cinci dintre cele șase descrieri se încheie cu folosirea simplă. PowerMax folosește ultimul bloc pentru cablul inclus și încărcarea simultană.
7. Numele scurt este urmat de o explicație funcțională. Agentul nu impune un nume nou dacă produsul are deja o marcă reală ce trebuie păstrată.
8. Beneficiile de lângă preț sunt rezumate scurte ale descrierii, nu beneficii noi neverificate.

## Limita de headlines

Descrierea noului produs are maximum 5 headlines explicative; ținta normală este 4, în funcție de beneficiile distincte reale. Nu adăuga un al cincilea bloc numai pentru a umple șablonul. Dacă research-ul susține mai puține beneficii distincte, păstrează mai puține. „Cum se folosește” poate constitui ultimul bloc și intră în această limită.

Titlul produsului, titlul global „Angajamentul Nostru” și „De ce [nume]?” sunt elemente separate ale structurii magazinului; nu sunt headlines suplimentare de beneficii în descriere.

## Afirmații și verificare

Corpusul conține afirmații ferme și absolute, inclusiv „ORICE”, „INSTANT”, „100%”, durate și promisiuni despre eficacitate. Copiază stilul concret și concis, fără a transfera automat aceste afirmații la alt produs. Pentru un produs nou verifică specificațiile, compatibilitatea, rezultatele și limitele din surse relevante. Pagina unui produs vechi nu dovedește performanța unui produs nou.

Nu inventa testimoniale, numere de clienți sau rezultate ale testelor. Nu seta prețul, reducerile sau stocul. Păstrează politicile comerciale aprobate fără promisiuni suplimentare.

## Surse locale

- `catalogue-audit.json`: catalog complet, variante și decizia de excludere.
- `corpus-text.txt`: descrierile produselor neexcluse.
- `non-test-pages/page-audit.json`: conținutul public al celor 8 pagini și rezultatul cererilor.

Nu au fost modificate produse, prețuri, imagini sau teme în Shopify în timpul acestei analize.
