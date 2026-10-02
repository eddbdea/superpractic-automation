# SuperPractic Agent

Agentul este folosit direct în Codex, cu regulile proiectului din `AGENTS.md` și skill-ul local `superpractic-landingpages`.

## Cum trimiți un produs

Deschide o sarcină Codex cu repository-ul `eddbdea/superpractic-automation` și mediul cloud în care este configurat Shopify. Scrie numai:

> START LP

Agentul îți cere un screenshot de la furnizor în care se văd produsul și informațiile despre el: numele/modelul, specificațiile și ce conține pachetul. Atașează fotografia sau mai multe screenshots; apoi începe research-ul. Poți atașa screenshot-ul chiar împreună cu START LP, caz în care agentul îl folosește fără să-l ceară din nou.

Poți adăuga linkul furnizorului și instrucțiuni. Pentru alt produs, începe o sarcină nouă pe același proiect; pentru revizii, continuă sarcina produsului respectiv.

## Ce face agentul

Datele produsului din screenshot → research rapid pe Google despre problemele și obiecțiile cumpărătorilor → text educativ pentru conversie, cu maximum 4–5 headlines → aprobarea textului → generarea unei singure imagini principale de exact 500 × 500 → aprobarea imaginii → produs draft și șablon nou în Shopify.

Research-ul folosește de regulă 2–4 căutări țintite și 3–5 surse utile. Nu se face direct pe Alibaba. Agentul se oprește când are baza necesară pentru copy și verifică suplimentar numai incertitudinile importante; nu inventează dovezi pentru a termina mai repede.

Prețul și publicarea rămân la proprietar. Agentul nu modifică codul temei sau șablonul-model și nu generează imagini suplimentare.

## Starea execuției

Regulile și referințele sunt salvate local în acest checkout. Shopify este configurat în mediul cloud și autentificarea/citirea sunt verificate. Crearea efectivă a produsului, încărcarea imaginii și duplicarea șablonului nu au fost încă testate. Nu există o aplicație web sau un GPT personalizat implementat; acestea nu sunt necesare pentru execuția în Codex.

Instrucțiunile proiectului sunt versionate pe ramura `main`. Pentru o sarcină nouă, selectează repository-ul `eddbdea/superpractic-automation`, ramura `main` și mediul cloud cu Shopify configurat. Salvarea configurației draft nu publică snapshot-ul: folosește Save and publish în onboarding pentru activarea modificărilor mediului. Pornirea unei sarcini noi trebuie verificată separat; nu este confirmată doar prin salvarea configurației sau prin existența fișierelor pe GitHub.

Pentru diagnosticarea conexiunii, rulează `python3 tools/check_shopify_connection.py`. Nu sunt necesare pachete Python externe; scriptul folosește biblioteca standard și credențialele din mediul cloud.
