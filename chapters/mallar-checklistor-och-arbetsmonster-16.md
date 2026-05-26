# Kapitel 16: Mallar, checklistor och arbetsmönster

## Varför detta kapitel finns

De tidigare kapitlen har visat hur kravarbete med SBE förändrar både tänkesätt, samarbete och dokumentation. Vi har följt brottsutredningsstödet från traditionella kravformuleringar till exempelbaserade specifikationer, workshops, Gherkin, Concordion, testkopplingar, kvalitetsgranskning, generella krav, icke-funktionella krav och organisatoriskt införande.

Det här kapitlet samlar bokens viktigaste arbetssätt i praktiska mallar, checklistor och arbetsmönster. Syftet är inte att skapa en ny tung metodhandbok. Syftet är att ge dig ett startpaket som går att anpassa till din organisation.

För en erfaren kravanalytiker är den stora utmaningen sällan att förstå en mall. Den stora utmaningen är att använda rätt mall vid rätt tillfälle, på rätt detaljnivå och med rätt deltagare. En mall kan hjälpa, men den kan också skada om den används som ersättning för samtal, exempel och gemensam förståelse.

I ett SBE-arbetssätt är därför mallarna inte slutprodukten. De är stödstrukturer för att upptäcka, formulera, pröva och underhålla verksamhetens regler och exempel.

## Lärandemål

Efter kapitlet ska du kunna:

- välja rätt arbetsmönster för olika typer av kravsituationer
- använda en lättviktig mall för SBE-specifikationer
- planera och genomföra en exempelworkshop med tydligt resultat
- granska om en specifikation fungerar för både verksamhet och IT
- avgöra när Gherkin, Cucumber, Concordion eller icke-automatiserad dokumentation passar bäst
- strukturera generella krav och kvalitetskrav utan att blanda ihop dem med funktionella scenarier
- använda checklistor för införande, förvaltning och kontinuerlig förbättring

## Innan vi börjar

Det här kapitlet bygger på tre principer från resten av boken.

Den första principen är att **exempel är ett arbetsredskap för förståelse**. Exempel ska inte bara skrivas efter att kravet redan är klart. De ska användas för att upptäcka vad kravet egentligen betyder.

Den andra principen är att **dokumentation ska ha flera läsare**. Verksamheten ska kunna känna igen sitt arbete. IT ska kunna omsätta dokumentationen i lösning, test och förvaltning. Dokumentationen ska därför vara tydlig nog för verksamheten och precis nog för IT.

Den tredje principen är att **levande dokumentation kräver rytm och ansvar**. Om ingen äger dokumentationen efter leverans blir den snabbt en historisk artefakt. Om den ska vara levande behöver den ingå i det ordinarie arbetet.

I det här kapitlet använder vi ordet mall för en återanvändbar struktur. Vi använder ordet checklista för en gransknings- eller beslutshjälp. Vi använder ordet arbetsmönster för en återkommande sekvens av aktiviteter.

## Så ska du använda kapitlets mallar

Mallar fungerar bäst när de används pragmatiskt. Det betyder att du bör börja med det som hjälper samtalet och ta bort det som inte behövs.

Använd därför inte alla mallar samtidigt. Välj ut den mall som svarar mot situationen:

- när ni ska utforska ett nytt område: använd workshopmallen
- när ni ska dokumentera ett funktionellt kravområde: använd SBE-specifikationsmallen
- när ni ska avgöra format: använd beslutsstödet för dokumentationsformat
- när ni ska granska kvalitet: använd granskningschecklistan
- när ni ska beskriva generella krav: använd mallen för tvärgående regler
- när ni ska beskriva kvalitetskrav: använd mallen för kvalitetskriterier
- när ni ska införa arbetssättet: använd införandemönstret

Mallen ska hjälpa gruppen att tänka. Den ska inte bli ett formulär där alla fält måste fyllas i för sakens skull.

## Grundmall för en SBE-specifikation

Den här mallen är avsedd för ett funktionellt område, till exempel “sökning efter ärenden”, “behörighetsstyrd ärendevisning” eller “registrering av utredningsåtgärd”.

```md
# [Funktionellt område]

## Syfte

Beskriv varför området finns och vilket verksamhetsproblem det löser.

## Läsare och användning

Beskriv vem som ska läsa specifikationen och hur den ska användas.

## Omfattning

Beskriv vad området omfattar och vad det inte omfattar.

## Centrala begrepp

- Begrepp:
  - Definition:
  - Exempel:

## Regler

### Regel 1: [Regelnamn]

Beskriv regeln i verksamhetsspråk.

Exempel:

| Situation | Förutsättning | Förväntat resultat |
|---|---|---|
|  |  |  |

### Regel 2: [Regelnamn]

Beskriv regeln i verksamhetsspråk.

Exempel:

| Situation | Förutsättning | Förväntat resultat |
|---|---|---|
|  |  |  |

## Scenarier

### Scenario: [Scenarionamn]

Givet att ...
När ...
Så ...

## Undantag och gränsfall

- Undantag:
  - Varför det är viktigt:
  - Förväntat beteende:

## Öppna frågor

| Fråga | Ägare | Behöver svar senast | Status |
|---|---|---|---|
|  |  |  |  |

## Kopplingar

- Relaterade generella regler:
- Relaterade kvalitetskrav:
- Relaterade beslut:
- Relaterade tester:
- Relaterade processer:

## Ändringshistorik

| Datum | Ändring | Beslutad av |
|---|---|---|
|  |  |  |
```

Mallen kan se lång ut, men den ska inte fyllas ut mekaniskt. För ett litet regelområde kan vissa delar vara mycket korta. Det viktiga är att specifikationen visar syfte, regler, exempel, öppna frågor och kopplingar.

### Exempel: behörighetsstyrd ärendevisning

För brottsutredningsstödet kan ett område börja så här:

```md
# Behörighetsstyrd ärendevisning

## Syfte

Utredare ska bara kunna se ärenden som de har rätt att arbeta med eller ta del av. Syftet är att skydda känslig information, stödja korrekt handläggning och minska risken för otillåten informationsspridning.

## Omfattning

Området omfattar visning av ärenden i sökresultat, ärendelistor och direktöppning via ärendenummer.

Området omfattar inte teknisk autentisering eller administration av behörighetsroller.

## Regler

### Regel 1: Utredare ser ärenden i sin behörighetsdomän

En utredare får se ett ärende om ärendet tillhör samma behörighetsdomän som utredaren och ärendet inte är särskilt skyddat.

Exempel:

| Utredare | Ärende | Särskilt skyddat | Förväntat resultat |
|---|---|---|---|
| Anna, domän Nord | Ärende i Nord | Nej | Ärendet visas |
| Anna, domän Nord | Ärende i Syd | Nej | Ärendet visas inte |
| Anna, domän Nord | Ärende i Nord | Ja | Ärendet visas inte utan särskild behörighet |
```

Det här formatet fungerar för verksamheten eftersom regeln är formulerad i verksamhetstermer. Det fungerar också för IT eftersom exemplet innehåller villkor och förväntat resultat.

## Mall för exempelworkshop

En exempelworkshop ska inte bara producera dokumentation. Den ska producera gemensam förståelse, beslut och tydliga öppna frågor.

### Före workshopen

```md
# Workshopförberedelse

## Område

Vilket funktionellt område ska behandlas?

## Syfte

Vad behöver vi förstå eller besluta?

## Deltagare

- Verksamhet:
- Krav:
- Test:
- Utveckling:
- Arkitektur:
- Informationssäkerhet/juridik:
- Beslutsfattare:

## Förkunskap

Vad behöver deltagarna läsa eller känna till före mötet?

## Ingångsmaterial

- Befintliga krav:
- Acceptanskriterier:
- Processbeskrivningar:
- Beslut:
- Regelverk:
- Felrapporter:
- Statistik eller observationer:

## Förväntat resultat

Efter workshopen ska vi ha:

- identifierade regler
- exempel på normalfall
- exempel på undantag
- öppna frågor
- beslut eller beslutsbehov
- överenskommen nästa åtgärd
```

### Under workshopen

```md
# Workshopanteckningar

## Område

## Regler vi tror gäller

- Regel:
  - Exempel:
  - Osäkerhet:

## Exempel

| Namn | Situation | Förutsättning | Förväntat resultat | Kommentar |
|---|---|---|---|---|
|  |  |  |  |  |

## Undantag

- Undantag:
  - När uppstår det?
  - Hur ska systemet bete sig?
  - Vem behöver bekräfta?

## Frågor

| Fråga | Varför frågan är viktig | Ägare | Nästa steg |
|---|---|---|---|
|  |  |  |  |

## Beslut

| Beslut | Konsekvens | Beslutsfattare |
|---|---|---|
|  |  |  |
```

### Efter workshopen

Efter workshopen bör kravanalytikern inte bara renskriva anteckningar. Kravanalytikern bör förädla materialet till en specifikation som kan granskas.

Checklistan efter workshopen är enkel:

- Har varje viktig regel minst ett konkret exempel?
- Finns minst ett exempel på normalfall?
- Finns minst ett exempel på relevant undantag?
- Är öppna frågor ägda av någon?
- Är beslut dokumenterade separat från antaganden?
- Är språket begripligt för verksamheten?
- Finns tillräcklig precision för test och utveckling?
- Har vi markerat vad som inte omfattas?

## Arbetsmönster: från traditionellt krav till SBE

När en organisation redan har krav i form av text och acceptanskriterier är det sällan klokt att börja om från noll. Använd i stället ett översättande arbetsmönster.

### Steg 1: Läs kravet som en hypotes

Börja med att betrakta den befintliga kravformuleringen som en hypotes om verksamhetens behov, inte som en färdig sanning.

Exempel:

> Systemet ska endast visa ärenden som användaren är behörig att se.

Det här är inte fel, men det är inte tillräckligt. Det säger inte vad behörighet betyder, vilka situationer som finns eller hur undantag ska hanteras.

### Steg 2: Identifiera dolda begrepp

Fråga vilka ord i kravet som behöver förklaras.

I exemplet ovan finns flera dolda begrepp:

- systemet
- visa
- ärende
- användare
- behörig
- behörig att se

Varje sådant begrepp kan bära regler, undantag och antaganden.

### Steg 3: Formulera första regeln

Skriv en regel i verksamhetsspråk.

Exempel:

> En utredare får se ett ärende om ärendet tillhör utredarens behörighetsdomän och ärendet inte har särskilt skydd.

Regeln är fortfarande kort, men den är mer konkret än det ursprungliga kravet.

### Steg 4: Skapa exempeltabell

Fyll på med exempel som prövar regeln.

| Situation | Utredarens domän | Ärendets domän | Särskilt skydd | Förväntat resultat |
|---|---|---|---|---|
| Samma domän, inget särskilt skydd | Nord | Nord | Nej | Ärendet visas |
| Annan domän | Nord | Syd | Nej | Ärendet visas inte |
| Samma domän, särskilt skydd | Nord | Nord | Ja | Ärendet visas inte utan särskild behörighet |

### Steg 5: Hitta frågor och beslut

Exemplen avslöjar ofta frågor som inte fanns i kravtexten.

Exempel:

- Vad räknas som särskild behörighet?
- Ska en chef kunna se ärenden över flera domäner?
- Ska direktöppning via ärendenummer ge samma resultat som sökning?
- Ska nekad åtkomst loggas?
- Ska användaren se ett felmeddelande eller bara inte se ärendet?

### Steg 6: Välj dokumentationsformat

När regler och exempel är tydliga kan du välja format. Ibland räcker en läsbar specifikation i markdown eller wiki. Ibland passar Gherkin. Ibland passar Concordion. Ibland ska exemplen inte automatiseras alls.

Arbetsmönstret är därför:

1. förstå verksamhetsregeln
2. hitta exempel
3. hitta frågor
4. fatta beslut
5. välja dokumentationsformat
6. först därefter bedöma automatisering

## Beslutsstöd: välj dokumentationsformat

Alla SBE-specifikationer behöver inte skrivas i samma format. Valet bör styras av läsare, komplexitet, automatiseringsbehov och underhåll.

| Situation | Rekommenderat format | Varför |
|---|---|---|
| Verksamheten behöver främst förstå och bekräfta regler | Läslig specifikation med regler och exempeltabeller | Låg tröskel och hög begriplighet |
| Scenarierna är tydliga, sekventiella och lämpar sig för automatisering | Gherkin | Bra för given-when-then och Cucumber-liknande arbetssätt |
| Specifikationen behöver vara dokumentnära och samtidigt körbar | Concordion-liknande upplägg | Bra när läsbar dokumentation är viktigare än scenariolistor |
| Regeln är komplex och tabellbaserad | Beslutstabell eller exempeltabell | Gör kombinationer och gränsfall tydliga |
| Kravet är ett kvalitetskrav med mätvärde | Kvalitetskriterium med verifieringsmetod | Bättre än funktionellt scenario |
| Kravet är tvärgående och återanvänds över många områden | Generell regel med länkar till exempel | Minskar duplicering |
| Automatisering skulle kräva stor teknisk investering men ge låg nytta | Icke-automatiserad levande dokumentation | Bevarar förståelsen utan onödig verktygstyngd |

### När Gherkin passar

Gherkin passar ofta när beteendet kan beskrivas som tydliga scenarier med startläge, händelse och förväntat resultat.

Exempel:

```gherkin
Scenario: Utredare ser ärende i egen behörighetsdomän
  Givet att utredaren Anna tillhör behörighetsdomän Nord
  Och ärende A-100 tillhör behörighetsdomän Nord
  Och ärende A-100 inte är särskilt skyddat
  När Anna söker efter ärende A-100
  Så visas ärende A-100 i sökresultatet
```

Gherkin passar mindre bra när specifikationen främst består av långa resonemang, många kombinationer i tabeller eller kvalitetskrav som behöver mätas på annat sätt.

### När Cucumber passar

Cucumber passar när organisationen vill koppla Gherkin-scenarier till automatiserade tester och har tekniska förutsättningar att underhålla dessa tester. Det kräver samarbete mellan krav, test och utveckling.

Cucumber passar sämre om verksamheten tror att verktyget i sig löser kravproblemet. Då riskerar scenarierna att bli tekniska testskript i stället för gemensamma exempel.

### När Concordion passar

Concordion passar när man vill att specifikationen ska vara mer dokumentnära, med förklarande text och inbäddade exempel som kan kopplas till automatiserade kontroller. Det kan vara användbart när verksamhetens förståelse kräver mer kontext än korta Gherkin-scenarier.

Concordion passar sämre om teamet egentligen bara behöver enkla scenarier och redan har ett fungerande Gherkin-flöde.

### När icke-automatiserad dokumentation passar

Icke-automatiserad dokumentation är inte ett misslyckande. Den passar när nyttan ligger i gemensam förståelse, beslut och spårbarhet snarare än i automatiserad regressionstestning.

Exempel inom brottsutredningsstödet:

- juridiska tolkningsfrågor
- policyregler som ändras genom beslut
- verksamhetsprinciper för informationsklassning
- kvalitetskrav som kontrolleras genom granskning eller revision
- tidiga utforskande exempel där regeln ännu inte är stabil

## Checklista: kvalitet i en SBE-specifikation

Använd den här checklistan när ett område ska granskas.

### Begriplighet

- Kan en verksamhetsrepresentant läsa specifikationen utan att behöva förstå intern teknik?
- Används verksamhetens egna begrepp konsekvent?
- Är syftet tydligt?
- Framgår vad området omfattar och inte omfattar?
- Är exemplen realistiska?

### Precision

- Har varje viktig regel minst ett konkret exempel?
- Finns förväntat resultat för varje exempel?
- Är villkor och utfall separerade?
- Är undantag beskrivna?
- Är gränsfall identifierade?

### Användbarhet för IT

- Går det att härleda testfall eller verifiering från exemplen?
- Är beroenden till andra regler eller system tydliga?
- Finns länkar eller referenser till kvalitetskrav?
- Är öppna frågor markerade så att de inte misstas för beslut?
- Är detaljnivån tillräcklig utan att låsa implementation i onödan?

### Underhållbarhet

- Finns ägare för specifikationen?
- Finns ändringshistorik?
- Är duplicering undviken?
- Är generella regler separerade från områdesspecifika exempel?
- Finns en rutin för att uppdatera specifikationen när verksamhetsregler ändras?

### Testbarhet

- Är det tydligt vad som kan automatiseras?
- Är det tydligt vad som ska verifieras manuellt eller genom granskning?
- Finns automationsstatus där det behövs?
- Är scenarier skrivna så att de inte blir sköra tekniska skript?
- Finns balans mellan täckning och underhållskostnad?

## Mall för generella krav

Generella krav ska inte gömmas i varje funktionellt område. De bör beskrivas centralt och länkas till relevanta exempel.

```md
# Generell regel: [Namn]

## Syfte

Varför finns regeln?

## Gäller för

Vilka funktionella områden, användargrupper eller informationsobjekt omfattas?

## Regel

Beskriv regeln i verksamhetsspråk.

## Exempel

| Område | Situation | Förväntat resultat |
|---|---|---|
|  |  |  |

## Undantag

- Undantag:
  - Vem får besluta?
  - Hur dokumenteras det?

## Relation till kvalitetskrav

- Säkerhet:
- Loggning:
- Spårbarhet:
- Tillgänglighet:
- Användbarhet:

## Ägare och ändring

- Regelägare:
- Granskningsintervall:
- Senast ändrad:
```

### Exempel: generell regel för nekad åtkomst

```md
# Generell regel: Nekad åtkomst till skyddad information

## Syfte

Regeln ska förhindra att användare får ta del av ärendeinformation som de saknar behörighet för.

## Gäller för

Regeln gäller sökning, ärendelistor, direktöppning av ärende, export och notifieringar.

## Regel

Om användaren saknar behörighet till ett ärende ska systemet inte visa ärendets innehåll. Vid direktförsök att öppna ärendet ska systemet visa ett neutralt meddelande och logga åtkomstförsöket.

## Exempel

| Område | Situation | Förväntat resultat |
|---|---|---|
| Sökning | Användare söker på ärendenummer för skyddat ärende | Ärendet visas inte i resultatet |
| Direktöppning | Användare anger länk till skyddat ärende | Neutralt meddelande visas |
| Export | Användare exporterar lista med blandade ärenden | Endast behöriga ärenden exporteras |
```

Den generella regeln kan sedan refereras från flera funktionella specifikationer i stället för att kopieras.

## Mall för icke-funktionella krav och kvalitetskrav

Kvalitetskrav behöver ofta beskrivas med andra byggstenar än funktionella krav. Exempel kan hjälpa, men de räcker inte alltid. Ett kvalitetskrav behöver ofta mätvärde, verifieringsmetod och ägarskap.

```md
# Kvalitetskrav: [Namn]

## Kvalitetsområde

Prestanda, säkerhet, användbarhet, tillgänglighet, robusthet, loggning, spårbarhet eller annat.

## Syfte

Vilken verksamhetsrisk eller verksamhetsnytta hanterar kravet?

## Gäller för

Vilka funktionella områden, informationsobjekt eller användargrupper omfattas?

## Kravformulering

Beskriv kravet i klartext.

## Kvalitetskriterier

| Kriterium | Målvärde | Verifieringsmetod |
|---|---|---|
|  |  |  |

## Exempel

| Situation | Förväntad kvalitet |
|---|---|
|  |  |

## Begränsningar och antaganden

- Antagande:
- Begränsning:

## Ägare

- Kravägare:
- Teknisk ägare:
- Verifieringsansvarig:
```

### Exempel: svarstid vid ärendesökning

```md
# Kvalitetskrav: Svarstid vid ärendesökning

## Kvalitetsområde

Prestanda och användbarhet.

## Syfte

Utredare ska kunna söka fram relevanta ärenden utan att arbetsflödet avbryts av långa väntetider.

## Gäller för

Sökning efter ärende via ärendenummer, personuppgift, registreringsnummer och fritext.

## Kravformulering

Systemet ska ge sökresultat inom en tid som stödjer effektivt utredningsarbete även vid normal belastning.

## Kvalitetskriterier

| Kriterium | Målvärde | Verifieringsmetod |
|---|---|---|
| Sökning på exakt ärendenummer | Resultat inom 1 sekund vid normal belastning | Prestandatest |
| Sökning på personuppgift | Resultat inom 2 sekunder vid normal belastning | Prestandatest |
| Fritextsökning | Första resultatsida inom 4 sekunder vid normal belastning | Prestandatest och användbarhetsgranskning |
```

Här är exemplen stöd för förståelse, men verifieringen kräver mätning.

## Checklista: balans mellan verksamhet och IT

En vanlig svårighet är att dokumentationen antingen blir för verksamhetsnära och oprecis, eller för teknisk och svår att läsa. Använd följande checklista för att hitta balansen.

### För verksamheten

- Känner verksamheten igen situationerna?
- Är exemplen hämtade från realistiska arbetsflöden?
- Är juridiska och organisatoriska begrepp använda korrekt?
- Framgår varför regeln finns?
- Är undantag och specialfall synliga?

### För IT

- Finns tillräcklig precision för att bygga och testa?
- Är datavillkor och förväntade resultat tydliga?
- Är externa beroenden markerade?
- Är kvalitetskrav och generella regler länkade?
- Är beslut och öppna frågor separerade?

### För båda

- Finns ett gemensamt språk?
- Är dokumentationen kort nog att underhålla?
- Är den komplett nog för att minska missförstånd?
- Är exempel och regler placerade där de kommer att hittas?
- Är specifikationen möjlig att uppdatera när verkligheten ändras?

## Arbetsmönster: dokumentationspaket per område

I ett större system bör dokumentationen inte vara en enda stor kravspecifikation. Den bör delas i dokumentationspaket per område.

Ett dokumentationspaket kan innehålla:

- kort syfte och omfattning
- begrepp som används i området
- regler
- exempel och scenarier
- öppna frågor
- beslut
- relaterade generella regler
- relaterade kvalitetskrav
- automationsstatus
- ägare och ändringshistorik

För brottsutredningsstödet kan dokumentationspaketen exempelvis vara:

| Paket | Innehåll | Primära läsare |
|---|---|---|
| Ärendesökning | Regler och exempel för sökning | Utredare, krav, test, utveckling |
| Ärendevisning | Behörighet, skydd, direktöppning | Verksamhet, säkerhet, utveckling |
| Utredningsåtgärder | Registrering, ändring, historik | Utredare, produktägare, test |
| Loggning och revision | Loggregler, åtkomstförsök, spårbarhet | Säkerhet, arkitektur, förvaltning |
| Kvalitetskrav | Prestanda, robusthet, användbarhet | Arkitektur, test, drift, verksamhet |

Det här gör dokumentationen lättare att äga och förändra. Det gör det också enklare att se vilka delar som behöver automatiserade tester och vilka som främst behöver granskning eller beslut.

## Mall för öppna frågor och beslut

Öppna frågor är en av de viktigaste artefakterna i SBE. De visar var förståelsen ännu inte är färdig. Men de måste skiljas från beslut.

```md
# Frågor och beslut: [Område]

## Öppna frågor

| ID | Fråga | Varför viktig | Ägare | Behöver svar senast | Status |
|---|---|---|---|---|---|
| F-001 |  |  |  |  | Öppen |

## Beslut

| ID | Beslut | Bakgrund | Konsekvens | Beslutat av | Datum |
|---|---|---|---|---|---|
| B-001 |  |  |  |  |  |

## Antaganden

| ID | Antagande | Risk om fel | Behöver bekräftas av |
|---|---|---|---|
| A-001 |  |  |  |
```

### Exempel: direktöppning av skyddat ärende

| ID | Fråga | Varför viktig | Ägare | Behöver svar senast | Status |
|---|---|---|---|---|---|
| F-014 | Ska användaren få veta att ett skyddat ärende finns om direktlänken anges? | Påverkar informationsskydd, användbarhet och loggning | Informationssäkerhet | Före utvecklingsstart | Öppen |

| ID | Beslut | Bakgrund | Konsekvens | Beslutat av | Datum |
|---|---|---|---|---|---|
| B-009 | Systemet ska visa neutralt meddelande vid nekad direktåtkomst | Att bekräfta att ärendet finns kan röja känslig information | Felmeddelande och loggning behöver utformas därefter | Produktägare och informationssäkerhet | 2026-05-26 |

Ett vanligt misstag är att skriva in antaganden som om de vore beslut. Det skapar falsk trygghet. I SBE bör antaganden vara synliga tills de är bekräftade.

## Mall för automationsstatus

Automatisering bör vara ett medvetet val. Använd en enkel statusmodell.

```md
# Automationsstatus

| Exempel eller regel | Status | Varför | Nästa steg | Ägare |
|---|---|---|---|---|
|  | Ej automatiserat |  |  |  |
|  | Kandidat för automatisering |  |  |  |
|  | Automatiserat |  |  |  |
|  | Verifieras genom granskning |  |  |  |
|  | Övervakas i drift |  |  |  |
```

### Rekommenderade statusar

| Status | Använd när |
|---|---|
| Ej automatiserat | Exemplet används för förståelse men ska inte automatiseras nu |
| Kandidat för automatisering | Exemplet är stabilt och återkommande men ännu inte automatiserat |
| Automatiserat | Exemplet ingår i automatiserad verifiering |
| Verifieras genom granskning | Kravet kontrolleras genom manuell granskning, revision eller beslutsgenomgång |
| Övervakas i drift | Kravet följs upp genom mätning eller driftövervakning |

För brottsutredningsstödet kan behörighetsregler ofta vara bra kandidater för automatisering. Juridiska tolkningsregler kan däremot behöva granskas och beslutas, även om vissa konsekvenser senare kan testas.

## Arbetsmönster: granskningsmöte för SBE-specifikation

Ett granskningsmöte ska inte bara kontrollera om texten är språkligt korrekt. Det ska kontrollera om specifikationen går att använda.

### Förberedelse

Skicka ut specifikationen med tre frågor:

1. Känner du igen verksamhetssituationerna?
2. Finns regler eller undantag som saknas?
3. Är något formulerat så att det kan misstolkas?

### Under mötet

Gå igenom specifikationen i den här ordningen:

1. syfte och omfattning
2. centrala begrepp
3. regler
4. exempel
5. undantag och gränsfall
6. öppna frågor
7. kopplingar till generella krav och kvalitetskrav
8. automationsstatus eller verifieringsmetod

### Efter mötet

Dokumentera bara tre typer av resultat:

- ändringar i specifikationen
- beslut
- öppna frågor

Undvik att skapa långa mötesanteckningar som ingen använder. Om mötet leder till viktig information ska den in i den levande dokumentationen.

## Checklista: när är ett område redo för utveckling?

Ett SBE-område behöver inte vara perfekt för att vara redo. Men det ska vara tillräckligt tydligt för att teamet ska kunna arbeta utan att gissa.

Området är redo när:

- syftet är tydligt
- omfattningen är avgränsad
- huvudreglerna är formulerade
- centrala exempel finns
- viktiga undantag är identifierade
- öppna frågor är få, synliga och ägda
- generella regler är länkade
- relevanta kvalitetskrav är identifierade
- test och utveckling förstår förväntat beteende
- verksamheten kan bekräfta att exemplen är rimliga
- teamet vet vad som ska automatiseras och vad som inte ska automatiseras

Om någon punkt saknas betyder det inte automatiskt stopp. Men det betyder att risken ska vara synlig.

## Arbetsmönster: inför SBE utan att skapa metodtyngd

Införande av SBE bör börja i liten skala, men med tillräckligt viktiga problem. Ett bra arbetsmönster är följande:

1. Välj ett pilotområde med verklig verksamhetsnytta.
2. Beskriv problemet med dagens kravarbete.
3. Samla rätt roller till en exempelworkshop.
4. Ta fram regler, exempel och öppna frågor.
5. Dokumentera området i en lättviktig SBE-specifikation.
6. Granska dokumentationen med både verksamhet och IT.
7. Välj automationsnivå efter nytta.
8. Följ upp vad som blev bättre och vad som blev tyngre.
9. Justera mallar och arbetssätt.
10. Skala till nästa område.

För brottsutredningsstödet är behörighetsstyrd ärendevisning ett bra pilotområde. Det är viktigt, riskfyllt, begripligt och regelintensivt. Det involverar verksamhet, informationssäkerhet, test och utveckling. Det gör området lämpligt för att visa värdet av SBE utan att börja med hela systemet.

## Checklista: införande i organisationen

Använd den här checklistan när SBE ska etableras utanför ett enskilt team.

### Syfte

- Vet vi vilket problem SBE ska lösa?
- Har vi exempel på missförstånd, omarbete eller kvalitetsbrister som arbetssättet ska minska?
- Är syftet begripligt för både verksamhet och IT?

### Mandat

- Finns produkt- eller verksamhetsägare som stödjer arbetssättet?
- Finns tid avsatt för workshops och granskning?
- Finns personer som kan fatta beslut när exempel avslöjar otydligheter?

### Arbetssätt

- Finns en enkel rytm för exempelworkshops?
- Finns en dokumentationsstruktur som är lätt att hitta i?
- Finns en överenskommelse om hur öppna frågor hanteras?
- Finns en rutin för att uppdatera levande dokumentation?

### Roller

- Vet kravanalytikern vad rollen innebär i SBE?
- Är test involverat tidigt?
- Är utveckling med innan lösningen låses?
- Är verksamhet och juridik eller informationssäkerhet med när reglerna kräver det?

### Verktyg

- Har organisationen valt verktyg efter arbetssätt, inte tvärtom?
- Är det tydligt när Gherkin ska användas?
- Är det tydligt när Cucumber eller Concordion är aktuellt?
- Finns stöd för dokumentation som inte automatiseras?

### Uppföljning

- Mäts förbättringar i begriplighet, minskat omarbete eller färre sena frågor?
- Följs underhållskostnaden för scenarier och tester upp?
- Justeras arbetssättet utifrån erfarenheter?

## Vanliga misstag

- **Misstag: Att införa mallar innan problemet är tydligt.**
  - Varför det händer: Organisationen vill snabbt standardisera.
  - Hur du undviker det: Börja med ett konkret pilotområde och låt mallarna växa fram ur verkliga behov.

- **Misstag: Att göra alla exempel till automatiserade tester.**
  - Varför det händer: Automatisering uppfattas som målet med SBE.
  - Hur du undviker det: Skilj på exempel för förståelse, exempel för beslut och exempel för automatiserad verifiering.

- **Misstag: Att skriva Gherkin för verksamheten men egentligen prata med testverktyget.**
  - Varför det händer: Scenarierna börjar styras av teknisk implementation.
  - Hur du undviker det: Granska om verksamheten fortfarande kan läsa och bekräfta scenarierna.

- **Misstag: Att duplicera generella regler i varje område.**
  - Varför det händer: Varje team skriver sin egen specifikation utan gemensam struktur.
  - Hur du undviker det: Skapa centrala generella regler och länka till dem.

- **Misstag: Att gömma öppna frågor i löptext.**
  - Varför det händer: Man vill att dokumentationen ska se färdig ut.
  - Hur du undviker det: Ha en tydlig tabell för frågor, ägare och beslutsdatum.

- **Misstag: Att skriva för IT och sedan hoppas att verksamheten förstår.**
  - Varför det händer: Dokumentationen hamnar nära implementationen.
  - Hur du undviker det: Börja med verksamhetens språk och lägg tekniska kopplingar separat.

- **Misstag: Att tro att levande dokumentation lever av sig själv.**
  - Varför det händer: Fokus ligger på framtagning, inte förvaltning.
  - Hur du undviker det: Sätt ägare, ändringsrytm och granskningspunkter.

## Övningar

### Övning 1: Skapa ett dokumentationspaket

Välj ett område i brottsutredningsstödet, till exempel ärendesökning eller registrering av utredningsåtgärd.

Skapa ett dokumentationspaket med:

- syfte
- omfattning
- två regler
- tre exempel
- en öppen fråga
- en relaterad generell regel
- ett relaterat kvalitetskrav

Granska sedan om paketet går att läsa av både verksamhet och IT.

### Övning 2: Välj format

Ta samma område och avgör vilket format som passar bäst:

- läsbar specifikation med exempeltabeller
- Gherkin
- Concordion-liknande dokumentation
- icke-automatiserad levande dokumentation
- kombination av flera format

Motivera valet utifrån läsare, automationsbehov, underhåll och risk.

### Övning 3: Gör en granskningscheck

Använd checklistan för kvalitet i en SBE-specifikation på ett befintligt kravdokument från din egen organisation eller på ett exempel från boken.

Identifiera:

- en styrka
- en brist
- en öppen fråga
- en förbättring som skulle göra dokumentationen mer användbar för verksamheten
- en förbättring som skulle göra dokumentationen mer användbar för IT

### Fördjupning

Ta ett traditionellt acceptanskriterium och pröva att skriva det i tre format:

1. som exempeltabell
2. som Gherkin-scenario
3. som dokumentnära specifikation med förklarande text

Jämför sedan vilket format som bäst stödjer gemensam förståelse.

## Snabb sammanfattning

- Mallar i SBE ska stödja samtal, beslut och levande dokumentation.
- En SBE-specifikation bör innehålla syfte, omfattning, begrepp, regler, exempel, frågor och kopplingar.
- Dokumentationen behöver fungera för både verksamhet och IT.
- Gherkin passar tydliga beteendescenarier, Cucumber passar när dessa ska automatiseras och Concordion kan passa när körbar dokumentation behöver vara mer dokumentnära.
- Alla exempel ska inte automatiseras.
- Generella krav bör beskrivas centralt och länkas till funktionella områden.
- Icke-funktionella krav behöver ofta kvalitetskriterier och verifieringsmetod, inte bara scenarier.
- Öppna frågor, beslut och antaganden ska hållas isär.
- Införandet av SBE bör börja med ett verkligt problem och ett avgränsat pilotområde.
- Levande dokumentation kräver ägarskap, rytm och underhåll.

## Quiz och reflektionsfrågor

1. Vad är skillnaden mellan en mall och ett arbetsmönster?
2. Varför bör en befintlig kravformulering behandlas som en hypotes?
3. När passar Gherkin bättre än en vanlig exempeltabell?
4. När kan Concordion vara mer lämpligt än Cucumber?
5. Varför är icke-automatiserad dokumentation ibland rätt val?
6. Vad bör ingå i ett dokumentationspaket för ett funktionellt område?
7. Varför ska generella regler inte dupliceras i varje specifikation?
8. Hur skiljer sig ett kvalitetskrav från ett funktionellt scenario?
9. Vad är risken med att blanda öppna frågor och beslut?
10. Vilka tecken visar att ett område är redo för utveckling?

## Koppling till bokens röda tråd

Mallar och checklistor ska användas som stöd för omdöme, inte som ersättning för omdöme. De sammanfattar bokens huvudlinje: börja med gemensam förståelse, konkretisera med exempel, dokumentera på rätt nivå och välj verktyg först när syftet är tydligt.


## Nästa steg

Med detta kapitel finns nu ett praktiskt startpaket för att använda bokens arbetssätt i verkliga projekt. Nästa naturliga steg är att granska hela boken som helhet.

Vid en helhetsgranskning bör du särskilt kontrollera:

- att begrepp introduceras i rätt ordning
- att brottsutredningsstödet används konsekvent
- att dokumentationsmönstren inte motsäger varandra
- att funktionella krav, generella krav och kvalitetskrav hålls isär
- att Gherkin, Cucumber och Concordion beskrivs som stöd för arbetssättet, inte som mål i sig
- att boken ger tillräckligt stöd för både dokumentation och organisatorisk omställning

När granskningen är gjord kan projektet förberedas för EPUB eller PDF enligt exportpipeline och metadata.
