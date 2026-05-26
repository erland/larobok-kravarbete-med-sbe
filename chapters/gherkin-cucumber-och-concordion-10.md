# Kapitel 10: Gherkin, Cucumber och Concordion

## Varför detta kapitel finns

Fram till nu har boken behandlat SBE som ett arbetssätt för att skapa gemensam förståelse och bättre dokumentation. Vi har beskrivit regler, exempel, scenarier, workshops och dokumentationslager utan att göra verktyg till huvudfråga. Det är avsiktligt. SBE börjar inte med ett verktyg. Det börjar med att rätt personer tillsammans förstår ett beteende tillräckligt konkret för att kunna beskriva det, granska det och använda det.

Samtidigt kommer frågan om verktyg förr eller senare. När exempel och scenarier blir tydliga uppstår ofta en naturlig fortsättning:

- Kan vi skriva detta i Gherkin?
- Kan Cucumber köra scenarierna automatiskt?
- Är Concordion bättre om vi vill ha mer läsbar dokumentation?
- Ska kravanalytikerna skriva scenarierna?
- Ska testarna äga dem?
- Ska verksamheten kunna läsa dem?
- Hur undviker vi att levande dokumentation blir teknisk testkod?

Det här kapitlet hjälper dig att göra dessa avvägningar. Fokus ligger inte på installation, kod eller verktygskonfiguration. Fokus ligger på hur en erfaren kravanalytiker kan förstå formaten, välja rätt nivå och samarbeta med test och utveckling utan att tappa SBE:s kärna.

Kapitlet bygger vidare på dokumentationsmönstret från kapitel 8 och workshoparbetet från kapitel 9. Vi använder fortfarande caset med brottsutredningsstödet, särskilt regler kring sökning, arbetslista, åtkomst och delegation.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara vad Gherkin är och när formatet passar i SBE-arbete
- skriva ett läsbart Gherkin-scenario på verksamhetsnära nivå
- skilja mellan verksamhetsscenario, automatiserbart scenario och teknisk testimplementation
- beskriva hur Cucumber kan användas för att köra Gherkin-scenarier
- beskriva när Concordion kan vara ett bättre val än Gherkin/Cucumber
- välja mellan tabell, scenario, Gherkin, Concordion och vanlig SBE-dokumentation
- identifiera vanliga anti-patterns när organisationer gör SBE till testautomatisering för tidigt
- dokumentera verktygsnära specifikationer så att de fortfarande fungerar för både verksamhet och IT

## Innan vi börjar

Det är lätt att hamna fel i detta område eftersom flera begrepp ofta blandas ihop. Därför börjar vi med en enkel princip:

> Gherkin, Cucumber och Concordion är möjliga uttrycks- och automationsformer för SBE. De är inte SBE i sig.

SBE är arbetssättet där konkreta exempel används för att skapa gemensam förståelse. Gherkin är ett strukturerat textformat för att beskriva beteenden, ofta med `Given`, `When` och `Then`. Cucumber är ett verktygsekosystem som kan köra Gherkin-scenarier mot kod. Concordion är ett verktyg för körbara specifikationer där specifikationen kan skrivas mer som ett dokument, ofta med tabeller, text och exempel som kopplas till testkod.

För en kravanalytiker är den viktigaste frågan inte vilket verktyg som är mest elegant. Den viktigaste frågan är:

> Vilken dokumentationsform hjälper verksamhet, IT och test att förstå samma beteende utan att skapa onödig teknisk friktion?

Ibland är svaret Gherkin. Ibland är svaret en beslutstabell. Ibland är svaret ett Concordion-liknande dokument. Ibland är svaret att inte automatisera alls ännu.

## Verktyg kommer efter förståelse

I många organisationer introduceras SBE genom ett verktyg. Någon har hört om BDD, Cucumber eller automatiserade acceptanstester. Teamet börjar skriva `Given`, `When`, `Then` innan man har lärt sig att formulera bra exempel. Resultatet blir ofta svaga scenarier som ser strukturerade ut men fortfarande innehåller samma tolkningsproblem som tidigare kravtext.

Ett traditionellt krav kan vara otydligt:

> Systemet ska endast visa ärenden som användaren har behörighet att se.

Ett dåligt Gherkin-scenario kan vara lika otydligt:

```gherkin
Feature: Behörighet

Scenario: Visa rätt ärenden
  Given att användaren är behörig
  When användaren söker efter ärenden
  Then visas rätt ärenden
```

Scenariot har form men inte innehåll. Det säger inte vad behörig betyder, vilka ärenden som ska visas, vilka som ska döljas eller vilket utfall som gäller vid undantag.

Ett bättre SBE-arbete börjar i stället med att teamet konkretiserar regler och exempel:

| Fall | Användarens relation till ärendet | Ärendets status | Särskild sekretess | Förväntat resultat |
|---|---|---|---|---|
| E1 | Tilldelad handläggare | Aktivt | Nej | Ärendet visas |
| E2 | Annan utredningsgrupp | Aktivt | Nej | Ärendet visas inte |
| E3 | Giltig delegation | Aktivt | Nej | Ärendet visas |
| E4 | Giltig delegation | Aktivt | Ja | Ärendet visas inte utan särskilt beslut |
| E5 | Utgången delegation | Aktivt | Nej | Ärendet visas inte |

Först när sådana exempel är begripliga, granskade och accepterade är det meningsfullt att fråga om de ska uttryckas i Gherkin, Concordion eller någon annan form.

## Vad Gherkin är

Gherkin är ett strukturerat textformat för att beskriva systembeteende med ett begränsat antal nyckelord. Det mest kända mönstret är:

```gherkin
Given [ett utgångsläge]
When [något händer]
Then [förväntat resultat]
```

På svenska kan man välja att behålla de engelska nyckelorden eller använda svenska varianter om verktyg och team stödjer det. I många organisationer behåller man engelska nyckelord eftersom de är etablerade i verktyg, dokumentation och testkod, medan själva innehållet skrivs på svenska.

Exempel:

```gherkin
Feature: Arbetslista för utredare

Scenario: Tilldelat aktivt ärende visas i arbetslistan
  Given att utredaren är tilldelad som handläggare för ärendet
  And att ärendet är aktivt
  And att ärendet inte har särskild sekretess
  When utredaren öppnar sin arbetslista
  Then visas ärendet i arbetslistan
```

Formatet ger en tydlig sekvens:

- `Given` beskriver förutsättningarna.
- `When` beskriver händelsen eller handlingen.
- `Then` beskriver det förväntade resultatet.
- `And` används för att lägga till fler rader inom samma del.
- `Feature` grupperar scenarier som hör till samma funktion eller beteende.
- `Scenario` beskriver ett konkret beteende.

Gherkin är användbart när beteendet kan beskrivas som en händelse med tydliga förutsättningar och ett observerbart resultat. Det gör formatet särskilt lämpligt för användarinteraktioner, flöden, valideringar och regler där systemets respons är central.

## Vad Gherkin inte löser

Gherkin gör inte ett dåligt exempel bra. Det gör inte en oklar regel tydlig. Det löser inte konflikter mellan verksamhet och IT. Det ersätter inte workshop, förfining eller domänförståelse.

Ett vanligt misstag är att använda Gherkin som en ny mall för krav. Då skrivs gamla krav om i nytt format utan att konkretiseras.

Traditionell kravtext:

> Systemet ska hantera sekretess enligt gällande regler.

Dålig Gherkin-version:

```gherkin
Scenario: Hantera sekretess
  Given att sekretess gäller
  When systemet hanterar ärendet
  Then ska sekretessreglerna följas
```

Detta är inte ett exempel. Det är en vag kravtext uppdelad på tre rader.

En användbar Gherkin-version behöver konkretisera vad som gäller:

```gherkin
Scenario: Särskilt sekretessmarkerat ärende visas inte trots giltig delegation
  Given att utredaren har en giltig delegation för ärendet
  And att ärendet är särskilt sekretessmarkerat
  And att inget särskilt åtkomstbeslut finns
  When utredaren öppnar sin arbetslista
  Then visas inte ärendet i arbetslistan
```

Nu har vi ett faktiskt beteende. Vi vet vilka villkor som gäller och vilket resultat som förväntas.

## När Gherkin passar bra

Gherkin passar särskilt bra när scenariot har en tydlig beteendekedja. I caset med brottsutredningsstödet kan det vara:

- en utredare söker efter ett ärende
- systemet filtrerar sökträffar utifrån åtkomst
- en delegation börjar eller upphör att gälla
- en användare försöker öppna ett spärrat ärende
- en arbetslista visar ärenden utifrån roll och ansvar
- en användare registrerar en åtgärd som påverkar ärendestatus

Gemensamt för dessa situationer är att det finns ett observerbart beteende. Något är sant före handlingen. Någon gör något. Systemet ska svara på ett visst sätt.

Ett bra Gherkin-scenario har ofta följande egenskaper:

- Det beskriver ett beteende, inte en teknisk lösning.
- Det är konkret nog för att kunna granskas.
- Det använder domänens språk.
- Det har ett tydligt förväntat resultat.
- Det innehåller inte fler detaljer än vad beteendet kräver.
- Det kan förstås av verksamhet, test och utveckling.
- Det kan eventuellt automatiseras, men är inte skrivet enbart för automationen.

## När Gherkin passar sämre

Gherkin passar sämre när informationen egentligen är en regelmatris, en lång lista av villkor eller en generell princip som gäller över många funktioner.

Anta att teamet behöver beskriva hur olika roller får se olika typer av ärendeinformation. Om det finns många kombinationer av roll, relation, ärendestatus, sekretessnivå och åtgärd kan en beslutstabell vara tydligare än många Gherkin-scenarier.

Exempel:

| Roll | Relation till ärende | Sekretess | Åtgärd | Tillåtet |
|---|---|---|---|---|
| Utredare | Tilldelad | Nej | Visa ärendedetaljer | Ja |
| Utredare | Inte tilldelad | Nej | Visa ärendedetaljer | Nej |
| Utredare | Delegation | Nej | Visa ärendedetaljer | Ja |
| Utredare | Delegation | Ja | Visa ärendedetaljer | Nej |
| Förundersökningsledare | Ansvarig | Ja | Visa ärendedetaljer | Ja om särskilt beslut finns |

Att skriva varje rad som ett eget Gherkin-scenario kan bli tungt och svårläst. En tabell kan ge bättre överblick. Däremot kan ett eller två Gherkin-scenarier användas för att visa centrala beteenden ur tabellen.

Gherkin passar också sämre för krav som inte handlar om ett specifikt beteende över tid, till exempel:

- övergripande arkitekturprinciper
- informationsklassningsregler
- generella loggningskrav
- tillgänglighetsriktlinjer
- prestandamål
- juridiska hänvisningar
- designprinciper

Sådana krav kan ibland konkretiseras med exempel, men själva huvudformen bör ofta vara en annan än Gherkin.

## Från workshopmaterial till Gherkin

Workshopmaterial är sällan färdigt Gherkin. Det är ett råmaterial som behöver förädlas. En bra arbetsgång kan vara:

1. Samla exempel i workshop.
2. Identifiera regler och öppna frågor.
3. Rensa bort dubbletter och oklara fall.
4. Välj vilka exempel som bör bli referensexempel.
5. Avgör vilka referensexempel som passar som Gherkin-scenarier.
6. Formulera scenarier på verksamhetsnära nivå.
7. Låt verksamhet, test och utveckling granska scenarierna.
8. Avgör först därefter om de ska automatiseras.

I kapitel 9 använde vi en workshop kring arbetslistan. Där kom bland annat denna regel fram:

> Ett ärende visas om utredaren har en giltig delegation för ärendet, förutsatt att särskild sekretess inte överstyr åtkomsten.

Ett första referensexempel kan vara:

| Fall | Förutsättning | Förväntat resultat |
|---|---|---|
| Giltig delegation utan särskild sekretess | Utredaren har delegation till aktivt ärende och ärendet är inte särskilt sekretessmarkerat | Ärendet visas i arbetslistan |

Det kan bli följande Gherkin-scenario:

```gherkin
Feature: Arbetslista för utredare

Scenario: Ärende med giltig delegation visas i arbetslistan
  Given att utredaren har en giltig delegation för ärendet
  And att ärendet är aktivt
  And att ärendet inte är särskilt sekretessmarkerat
  When utredaren öppnar sin arbetslista
  Then visas ärendet i arbetslistan
```

Ett undantagsexempel kan bli:

| Fall | Förutsättning | Förväntat resultat |
|---|---|---|
| Giltig delegation men särskild sekretess | Utredaren har delegation men ärendet är särskilt sekretessmarkerat och inget särskilt åtkomstbeslut finns | Ärendet visas inte |

Det kan bli:

```gherkin
Scenario: Särskilt sekretessmarkerat ärende visas inte trots giltig delegation
  Given att utredaren har en giltig delegation för ärendet
  And att ärendet är särskilt sekretessmarkerat
  And att inget särskilt åtkomstbeslut finns
  When utredaren öppnar sin arbetslista
  Then visas inte ärendet i arbetslistan
```

Det viktiga är inte bara formatet. Det viktiga är att scenarierna synliggör skillnaden mellan normalfallet och undantaget.

## Skriv scenarier på rätt nivå

Ett vanligt problem är att scenarier skrivs antingen för abstrakt eller för tekniskt.

För abstrakt:

```gherkin
Scenario: Behörighet kontrolleras
  Given att användaren har rätt behörighet
  When användaren använder systemet
  Then ska systemet visa rätt information
```

För tekniskt:

```gherkin
Scenario: API returnerar 200 för arbetslista
  Given att JWT-token innehåller claim groupId med värde 4711
  And att databastabellen delegation innehåller rad med valid_to större än current_timestamp
  When klienten anropar GET /api/v2/worklist?user=E123
  Then returnerar API statuskod 200
  And JSON-fältet caseItems[0].caseId har värde "B-2026-18472"
```

Det första scenariot är för vagt för att skapa förståelse. Det andra kan vara användbart som tekniskt test, men det är inte lämpligt som verksamhetsnära SBE-specifikation.

En bättre nivå är:

```gherkin
Scenario: Utredare ser ärende när delegationen är giltig
  Given att utredaren har en delegation för ärendet
  And att delegationen gäller dagens datum
  And att ärendet inte är spärrat av särskild sekretess
  When utredaren öppnar sin arbetslista
  Then visas ärendet i arbetslistan
```

Detta scenario är konkret men inte tekniskt bundet. Det går att diskutera med verksamheten. Det går att använda av test. Det ger utveckling relevant beteendeinformation utan att föreskriva API, databas eller implementation.

## Scenario Outline och exempelrader

När samma beteende ska prövas med flera datauppsättningar kan Gherkin använda `Scenario Outline` och `Examples`. Det kan vara praktiskt när en regel har flera variationer men samma struktur.

Exempel:

```gherkin
Scenario Outline: Delegation avgör om ärende visas i arbetslistan
  Given att utredaren har en delegation med status "<delegationsstatus>"
  And att ärendet har sekretess "<sekretess>"
  When utredaren öppnar sin arbetslista
  Then ska ärendet "<utfall>"

Examples:
  | delegationsstatus | sekretess | utfall |
  | giltig | ingen särskild sekretess | visas |
  | utgången | ingen särskild sekretess | inte visas |
  | giltig | särskild sekretess utan särskilt beslut | inte visas |
  | giltig | särskild sekretess med särskilt beslut | visas |
```

Detta kan vara effektivt, men det finns en risk. Om tabellen blir för stor blir scenariot svårt att läsa. Då kan en vanlig beslutstabell i dokumentationen vara bättre, och bara några utvalda exempel kan göras till automatiserade scenarier.

En tumregel är:

> Använd `Scenario Outline` när variationerna är få, samma beteende prövas och tabellen fortfarande är begriplig för en verksamhetsläsare.

Om tabellen kräver att läsaren förstår tekniska koder, systemstatusar eller databasfält har den sannolikt hamnat på fel nivå för verksamhetsnära SBE-dokumentation.

## Gherkin som dokumentation

Gherkin kan fungera som dokumentation, men bara om organisationen behandlar scenarierna som dokumentation. Det kräver mer än att de ligger i ett testrepository.

För att Gherkin ska fungera som dokumentation behöver scenarierna:

- vara skrivna i domänspråk
- vara grupperade på ett begripligt sätt
- ha scenarionamn som uttrycker beteende
- undvika tekniska detaljer i stegen
- hållas aktuella när regler ändras
- vara tillgängliga för relevanta läsare
- kopplas till övrig dokumentation utan dubbeldokumentation

Ett scenario som bara utvecklare hittar i en kodbas fungerar sällan som gemensam dokumentation för verksamhet och IT. Det kan vara ett bra automatiserat test, men det är inte självklart levande dokumentation för hela organisationen.

Därför behöver teamet bestämma var Gherkin-scenarierna hör hemma i dokumentationsstrukturen. I bokens dokumentationsmönster kan de placeras i specifikationslagret, med kopplingar till regler och exempel-ID:n.

Exempel:

| Element | Exempel |
|---|---|
| Regel-ID | ARB-R4 |
| Regel | Särskild sekretess överstyr delegation om inget särskilt åtkomstbeslut finns |
| Referensexempel | ARB-E12 |
| Gherkin-scenario | `Scenario: Särskilt sekretessmarkerat ärende visas inte trots giltig delegation` |
| Teststatus | Automatiserat i Cucumber eller manuellt verifierat |
| Öppna frågor | Ingen |

På så sätt blir Gherkin en del av helheten, inte en parallell värld.

## Vad Cucumber tillför

Cucumber kan köra Gherkin-scenarier genom att koppla varje steg till så kallade step definitions i kod. För en kravanalytiker räcker det ofta att förstå principen:

- Gherkin beskriver beteendet i text.
- Step definitions kopplar textstegen till kod.
- Testkoden förbereder data, utför handlingar och kontrollerar resultat.
- Körningen visar om systemet fortfarande beter sig enligt scenarierna.

Ett förenklat exempel:

```gherkin
Scenario: Ärende med giltig delegation visas i arbetslistan
  Given att utredaren har en giltig delegation för ärendet
  When utredaren öppnar sin arbetslista
  Then visas ärendet i arbetslistan
```

Bakom stegen kan det finnas kod som:

- skapar testdata för utredare, ärende och delegation
- loggar in som utredaren eller simulerar användarens behörighet
- öppnar arbetslistan via användargränssnitt eller API
- kontrollerar att ärendet finns i resultatet

Detta är kraftfullt eftersom scenariot kan bli en körbar kontroll. Om systemet ändras på ett sätt som bryter beteendet kan testet signalera det.

Men Cucumber tillför också kostnader:

- någon måste skriva och underhålla step definitions
- testdata måste hanteras
- scenarier behöver hållas stabila när systemet förändras
- tekniska detaljer kan läcka in i Gherkin-texten
- körningarna kan bli långsamma eller sköra om nivå och strategi är fel
- teamet behöver tydligt ägarskap

Därför bör Cucumber ses som ett möjligt nästa steg efter att specifikationen är bra, inte som beviset på att SBE fungerar.

## När Cucumber passar

Cucumber passar särskilt bra när organisationen vill automatisera beteenden som är viktiga, återkommande och relativt stabila. Det kan vara:

- centrala regler som ofta påverkas av ändringar
- beteenden där regressioner är kostsamma
- flöden där verksamhet, test och utveckling behöver en gemensam notation
- scenarier som kan köras på en rimlig teknisk nivå
- områden där teamet har kapacitet att underhålla automationen

I caset kan Cucumber vara relevant för exempelvis:

- arbetslista
- sökträffar och åtkomstfiltrering
- delegationsregler
- statusövergångar
- validering av obligatoriska uppgifter
- händelseloggning för tydligt avgränsade beteenden

Ett lämpligt Cucumber-scenario är ofta ett som både verksamhet och test kan läsa, och som utveckling kan automatisera utan att behöva gissa vad som menas.

## När Cucumber inte passar

Cucumber passar sämre när:

- scenarierna egentligen beskriver teknisk implementation
- verksamheten inte kommer att läsa eller granska dem
- teamet saknar kapacitet att underhålla automationen
- området förändras mycket snabbt
- testdata är extremt svårt att kontrollera
- scenarierna blir långa, sköra eller fulla av tekniska steg
- organisationen tror att Cucumber ersätter kravarbete

Ett anti-pattern är att använda Cucumber för alla tester. Då riskerar Gherkin att bli ett extra lager ovanpå vanlig testkod. Testerna blir långsammare att skriva, svårare att underhålla och mindre läsbara.

Ett annat anti-pattern är att kravanalytikern skriver Gherkin utan dialog med test och utveckling. Då kan scenarierna se bra ut i dokumentationen men bli svåra eller olämpliga att automatisera.

Ett tredje anti-pattern är att testare eller utvecklare skriver Gherkin enbart för testautomation. Då kan scenarierna bli tekniskt korrekta men sakna värde som gemensam specifikation.

## Vad Concordion tillför

Concordion har en annan tyngdpunkt än Cucumber. Där Gherkin ofta ger en scenariostruktur med `Given`, `When`, `Then`, gör Concordion det möjligt att skriva specifikationer mer som läsbara dokument med text, tabeller och exempel som kan kopplas till körbar testkod.

Det kan passa när specifikationen behöver mer förklarande text eller när en tabell är mer uttrycksfull än flera scenarier.

I caset kan en Concordion-liknande specifikation beskriva en regel så här:

> När en utredare öppnar sin arbetslista ska systemet bara visa ärenden som utredaren har rätt att arbeta med. Delegation kan ge tillfällig åtkomst, men särskild sekretess kan begränsa åtkomsten även när delegation finns.

Sedan kan dokumentet innehålla en tabell:

| Delegation | Särskild sekretess | Särskilt åtkomstbeslut | Förväntat resultat |
|---|---|---|---|
| Giltig | Nej | Nej | Ärendet visas |
| Utgången | Nej | Nej | Ärendet visas inte |
| Giltig | Ja | Nej | Ärendet visas inte |
| Giltig | Ja | Ja | Ärendet visas |

Med Concordion kan en sådan tabell göras körbar, men dokumentet kan fortfarande se ut som en specifikation snarare än en samling testscenarier.

För en kravanalytiker är det viktiga att Concordion ofta passar bättre när:

- verksamheten behöver sammanhängande förklarande dokumentation
- regler uttrycks bäst med tabeller
- dokumentet ska fungera som läsbar specifikation
- teamet vill kombinera text, exempel och körbara kontroller
- Gherkin-scenarier skulle bli för många eller för fragmenterade

## När Concordion passar

Concordion passar särskilt bra för regelområden där en läsbar specifikation behöver innehålla både förklaring och exempel. I caset kan det vara:

- behörighetsmatriser
- sök- och filtreringsregler
- beslutstabeller för ärendevisning
- valideringsregler
- statusövergångar
- generella regler som används i flera flöden

Concordion kan vara ett bra val när dokumentationen ska läsas som en sammanhängande text snarare än som separata scenarier.

Exempel på dokumentnära struktur:

| Del | Innehåll |
|---|---|
| Syfte | Varför regeln finns |
| Begrepp | Vad delegation, särskild sekretess och åtkomstbeslut betyder |
| Regel | Verksamhetsregel i text |
| Exempel | Tabell med konkreta fall |
| Förväntat resultat | Tydliga utfall per fall |
| Automationskoppling | Körbar kontroll kopplad till tabellen |
| Öppna frågor | Osäkerheter som inte ska döljas |

Denna struktur ligger nära bokens tidigare dokumentationsmönster och kan därför vara lättare att införa i organisationer där verksamheten är van vid dokument snarare än feature-filer.

## När Concordion inte passar

Concordion passar sämre om teamet främst vill beskriva interaktiva flöden i korta scenarier, eller om organisationen redan har etablerat ett tydligt Cucumber-arbetssätt som fungerar väl.

Det kan också passa sämre om:

- teamet saknar teknisk kompetens att koppla dokumentet till testkod
- specifikationen blir ett stort dokument som ingen äger
- dokumentet fylls med för mycket bakgrund och för få prövbara exempel
- automationen blir svår att förstå för test och utveckling
- verktygsstödet inte passar organisationens tekniska miljö

Precis som med Cucumber är Concordion inte en genväg förbi SBE-arbetet. Det är ett sätt att uttrycka och eventuellt köra en specifikation som redan är väl genomarbetad.

## Gherkin eller Concordion?

Valet mellan Gherkin/Cucumber och Concordion bör inte göras utifrån vad som är trendigast. Det bör göras utifrån vilken form som bäst stödjer förståelse, granskning och underhåll.

En förenklad jämförelse:

| Fråga | Gherkin/Cucumber passar ofta när | Concordion passar ofta när |
|---|---|---|
| Dokumentationsform | Kortare scenarier med tydlig Given-When-Then-struktur | Sammanhängande dokument med text och tabeller |
| Beteendetyp | Flöden, interaktioner, händelser och observerbara resultat | Regler, matriser, tabeller och förklarande specifikation |
| Läsare | Team vana vid BDD-format | Verksamhet och IT som behöver dokumentnära specifikation |
| Automatisering | Scenarier kopplas till step definitions | Dokument och tabeller kopplas till testkod |
| Risk | Scenarier blir tekniska testskript | Dokument blir för långt eller otydligt |
| Styrka | Tydlig beteendestruktur | Läsbarhet och rikare dokumentationsform |

I praktiken behöver organisationen inte välja ett enda format för allt. Man kan använda:

- vanlig SBE-dokumentation för tidiga och utforskande områden
- beslutstabeller för komplexa regler
- Gherkin för centrala beteendescenarier
- Cucumber för automatiserade beteendekontroller
- Concordion för dokumentnära körbara specifikationer

Det viktigaste är att undvika formatförvirring. Teamet bör veta vilket format som används för vilket syfte.

## Beslutsstöd för formatval

När du ska välja dokumentationsform kan du använda följande frågor.

| Fråga | Om svaret är ja | Möjlig form |
|---|---|---|
| Behöver verksamheten förstå sammanhang och regler i löpande text? | Ja | SBE-dokumentation eller Concordion |
| Handlar beteendet om en tydlig händelse och ett observerbart resultat? | Ja | Gherkin |
| Finns många kombinationer av villkor och utfall? | Ja | Beslutstabell eller Concordion |
| Ska exemplen automatiseras inom kort? | Ja | Gherkin/Cucumber eller Concordion |
| Är området fortfarande osäkert och under utforskning? | Ja | Workshopmaterial och vanlig SBE-dokumentation |
| Är kravet ett generellt kvalitetskrav? | Ja | Kvalitetskriterier, exempel och kompletterande dokumentation |
| Blir scenarierna fulla av API, databas eller tekniska detaljer? | Ja | Flytta tekniken till testlager eller teknisk dokumentation |

Ett praktiskt beslut kan se ut så här:

| Område i brottsutredningsstödet | Rekommenderad form | Motivering |
|---|---|---|
| Arbetslista för utredare | Gherkin för centrala scenarier | Tydlig användarhandling och observerbart resultat |
| Behörighetsmatris | Beslutstabell eller Concordion | Många villkor och utfall behöver överblick |
| Sökning med begränsade träffar | Kombination av beslutstabell och Gherkin | Regler kräver tabell, centrala beteenden kräver scenarier |
| Loggning av åtkomst | SBE-regler och utvalda exempel | Vissa delar är funktionella, andra är generella krav |
| Prestanda för sökning | Icke-funktionella kriterier och exempel | Passar inte som vanlig Given-When-Then-specifikation |
| Juridisk informationsklassning | Förklarande dokumentation med exempel | Kräver bakgrund och tolkning, inte bara scenarioform |

## Verksamhetsnära Gherkin

Ett Gherkin-scenario kan skrivas på flera nivåer. I SBE bör den första versionen vara verksamhetsnära. Det betyder inte att den är vag. Det betyder att den beskriver beteende med domänens språk.

Exempel:

```gherkin
Scenario: Utredare får begränsad sökträff för skyddat ärende
  Given att ett ärende matchar utredarens sökning
  And att utredaren inte har åtkomst till ärendet
  When utredaren söker efter ärendet
  Then visas en begränsad sökträff
  And ärendets känsliga uppgifter visas inte
```

Detta scenario behöver kompletteras med definitioner:

| Begrepp | Definition |
|---|---|
| Begränsad sökträff | En träff som visar att ett relevant ärende finns men döljer känsliga uppgifter |
| Känsliga uppgifter | Uppgifter som enligt åtkomstregler inte får visas för användaren |
| Åtkomst | Rätt att se information enligt roll, relation, delegation och särskilda beslut |

Utan begreppsdefinitioner kan även ett bra scenario bli tvetydigt. Därför behöver Gherkin ofta leva tillsammans med terminologi, regler och exempel.

## Automatiserbar Gherkin

När scenariot ska automatiseras behöver teamet kontrollera att det är möjligt att skapa förutsättningar, utföra handlingen och kontrollera resultatet.

Det verksamhetsnära scenariot ovan kan vara automatiserbart om teamet kan:

- skapa eller identifiera ett ärende som matchar sökningen
- skapa en användare utan åtkomst
- utföra sökningen på en kontrollerbar nivå
- kontrollera att begränsad träff visas
- kontrollera att känsliga uppgifter inte visas

Men man behöver inte skriva in allt detta i Gherkin-texten. De tekniska detaljerna hör hemma i testkod, testdatahantering eller tekniskt lager.

En tekniskt förorenad version kan se ut så här:

```gherkin
Scenario: Sök-API maskerar fält för skyddat ärende
  Given att tabellen case innehåller case_id "B-2026-0182"
  And att ACL-tabellen saknar rad för user_id "U-445"
  When GET /api/search?q=B-2026-0182 anropas med token "U-445"
  Then svarar tjänsten med HTTP 200
  And JSON-fältet $.results[0].masked är true
```

Detta kan vara ett bra tekniskt API-test. Men det bör inte vara bokens primära SBE-specifikation för verksamheten.

Ett bättre arbetssätt är att ha två nivåer:

| Nivå | Syfte | Exempel |
|---|---|---|
| Verksamhetsnära scenario | Gemensam förståelse | Utredare får begränsad sökträff för skyddat ärende |
| Teknisk automatisering | Körbar kontroll | API, testdata, token och JSON-kontroll |

Kopplingen mellan nivåerna kan dokumenteras med exempel-ID och testreferens, inte genom att blanda allt i samma text.

## Step definitions är inte krav

När Cucumber används uppstår step definitions. Det är kod som binder Gherkin-rader till teknisk körning. För kravanalytikern är det viktigt att förstå att step definitions inte är kravdokumentation.

Om en Gherkin-rad säger:

```gherkin
Given att utredaren har en giltig delegation för ärendet
```

kan step definition-koden behöva skapa användare, ärende, delegation, datum och behörigheter i testmiljön. Den tekniska koden kan vara omfattande, men den ändrar inte verksamhetsregeln.

En risk är att teamet börjar definiera betydelsen av stegen i testkoden i stället för i verksamhetsdokumentationen. Då kan regeln bli svår att granska för verksamheten.

Därför bör betydelsen av centrala steg beskrivas i dokumentationen:

| Stegtext | Verksamhetsbetydelse |
|---|---|
| `utredaren har en giltig delegation för ärendet` | Det finns en beslutad delegation som gäller vid tidpunkten för åtkomst och som avser aktuellt ärende |
| `ärendet är särskilt sekretessmarkerat` | Ärendet har markering som begränsar åtkomst utöver vanliga roll- och delegationsregler |
| `begränsad sökträff visas` | Systemet visar en träff utan att exponera känsliga ärendeuppgifter |

Detta minskar risken för att samma steg tolkas olika av verksamhet och testautomation.

## Återanvändning av Gherkin-steg

Återanvändning av steg kan vara bra, men det kan också skapa problem. Om teamet försöker återanvända steg för hårt blir språket ofta tekniskt eller konstlat.

Dåligt återanvänt steg:

```gherkin
Given att användaren har behörighetskontext "CASE_ACCESS_DELEGATED_VALID_NO_SECRET"
```

Detta är tekniskt kompakt men obegripligt för många verksamhetsläsare.

Bättre:

```gherkin
Given att utredaren har en giltig delegation för ärendet
And att ärendet inte är särskilt sekretessmarkerat
```

Återanvändning bör inte gå före läsbarhet. I SBE är scenariets värde att skapa förståelse. Om återanvändning gör scenariot svårare att förstå har man optimerat för fel mål.

En praktisk regel är:

> Återanvänd steg när det gör scenarierna mer konsekventa, men inte när det gör dem mindre begripliga.

## Språkval i Gherkin

I en svensk bok och svensk myndighetskontext är det rimligt att skriva innehållet på svenska. Frågan är om själva Gherkin-nyckelorden ska vara svenska eller engelska.

Två varianter:

```gherkin
Scenario: Ärende med giltig delegation visas i arbetslistan
  Given att utredaren har en giltig delegation för ärendet
  When utredaren öppnar sin arbetslista
  Then visas ärendet i arbetslistan
```

eller:

```gherkin
Scenario: Ärende med giltig delegation visas i arbetslistan
  Givet att utredaren har en giltig delegation för ärendet
  När utredaren öppnar sin arbetslista
  Så visas ärendet i arbetslistan
```

Båda kan vara läsbara. I praktiken väljer många team engelska nyckelord och svensk domäntext eftersom:

- verktygsexempel ofta använder engelska nyckelord
- testare och utvecklare känner igen formatet
- domäninnehållet ändå blir svenskt
- blandningen fungerar relativt väl

Men om verksamheten störs av engelska nyckelord kan svenska nyckelord vara bättre, förutsatt att verktygsstödet fungerar.

Det viktiga är konsekvens. Byt inte mellan språk och stil utan tydlig anledning.

## Cucumber som bro mellan krav och test

När Cucumber fungerar väl blir det en bro mellan krav och test. Men bron uppstår bara om flera roller delar ansvar.

Kravanalytikern bidrar med:

- domänspråk
- regler
- exempel
- scenarioformulering
- koppling till verksamhetsmål
- granskning med verksamheten

Testaren bidrar med:

- testbarhet
- täckningsbedömning
- riskbaserat urval
- testdatafrågor
- automatiseringsstrategi
- granskning av utfall

Utvecklaren bidrar med:

- realiserbarhet
- lämplig teknisk testnivå
- step definitions
- arkitekturella konsekvenser
- stabil körning
- underhållbarhet

Verksamheten bidrar med:

- bekräftelse av regler
- exempel från verkligheten
- bedömning av undantag
- prioritering av risker
- acceptans av beteende

Om någon av dessa roller saknas riskerar scenarierna att bli snedvridna. De kan bli verksamhetsnära men omöjliga att automatisera, tekniskt körbara men obegripliga, eller testbara men felprioriterade.

## Automatisera inte allt

Ett moget SBE-arbetssätt innebär inte att alla exempel ska automatiseras. Vissa exempel är främst till för förståelse. Andra är till för granskning. Några bör bli automatiserade kontroller.

Urvalet bör styras av risk, stabilitet och värde.

| Exempeltyp | Bör automatiseras? | Motivering |
|---|---|---|
| Central regel som ofta påverkas av ändringar | Ofta ja | Hög regressionsrisk |
| Ovanligt gränsfall med stor konsekvens | Ofta ja | Hög risk trots låg frekvens |
| Exempel som främst förklarar begrepp | Inte nödvändigtvis | Dokumentationsvärde kan räcka |
| Område under kraftig förändring | Vänta ofta | Automation kan bli dyr att underhålla |
| Teknisk integrationsdetalj | Kanske, men inte som SBE-scenario | Hör ofta hemma i tekniskt testlager |
| Juridiskt resonemang eller tolkningsstöd | Sällan direkt | Kräver ofta mänsklig bedömning |

I brottsutredningsstödet kan regler om åtkomst till sekretessmarkerade ärenden vara så riskfyllda att automatisering är motiverad. Däremot kanske ett exempel som förklarar skillnaden mellan delegation och ansvarig handläggare främst behövs för förståelse.

## En dokumentationsstruktur för verktygsnära specifikation

För att Gherkin, Cucumber och Concordion inte ska bli parallella spår bör dokumentationen ha en tydlig struktur.

Ett mönster kan vara:

| Dokumentationsdel | Innehåll |
|---|---|
| Syfte | Varför beteendet finns |
| Begrepp | Centrala domänbegrepp |
| Regler | Verksamhetsregler |
| Exempel | Tabeller eller referensexempel |
| Scenarier | Gherkin eller annat scenarioformat |
| Automationsstatus | Inte automatiserat, planerat, automatiserat, pensionerat |
| Testnivå | UI, API, domänlogik, manuell granskning |
| Ägarskap | Vem ansvarar för innehåll och uppdatering |
| Öppna frågor | Osäkerheter som inte ska döljas |

Exempel:

| Fält | Innehåll |
|---|---|
| Specifikationsområde | Arbetslista |
| Regel-ID | ARB-R4 |
| Regel | Särskild sekretess överstyr delegation om inget särskilt åtkomstbeslut finns |
| Referensexempel | ARB-E12 |
| Format | Gherkin |
| Automationsverktyg | Cucumber |
| Testnivå | API-nära beteendetest |
| Automationsstatus | Planerat |
| Ägare verksamhetsregel | Produktägare för utredningsflöde |
| Ägare automation | Testansvarig i teamet |
| Öppna frågor | Hur snabbt sekretessändring ska slå igenom i arbetslistan |

Detta gör att dokumentationen kan vara användbar även innan automationen är på plats.

## Exempel: från SBE-dokumentation till Gherkin och automation

Vi tar ett konkret exempel från caset.

Verksamhetsregel:

> En utredare med giltig delegation får se ett ärende i arbetslistan om ärendet inte är särskilt sekretessmarkerat.

Undantagsregel:

> Särskild sekretess överstyr delegation om inget särskilt åtkomstbeslut finns.

Exempeltabell:

| Exempel-ID | Delegation | Särskild sekretess | Särskilt åtkomstbeslut | Förväntat resultat |
|---|---|---|---|---|
| ARB-E10 | Giltig | Nej | Nej | Ärendet visas |
| ARB-E11 | Utgången | Nej | Nej | Ärendet visas inte |
| ARB-E12 | Giltig | Ja | Nej | Ärendet visas inte |
| ARB-E13 | Giltig | Ja | Ja | Ärendet visas |

Utvalda Gherkin-scenarier:

```gherkin
Feature: Arbetslista för utredare

Scenario: Ärende med giltig delegation visas när ingen särskild sekretess finns
  Given att utredaren har en giltig delegation för ärendet
  And att ärendet inte är särskilt sekretessmarkerat
  When utredaren öppnar sin arbetslista
  Then visas ärendet i arbetslistan

Scenario: Särskild sekretess överstyr giltig delegation
  Given att utredaren har en giltig delegation för ärendet
  And att ärendet är särskilt sekretessmarkerat
  And att inget särskilt åtkomstbeslut finns
  When utredaren öppnar sin arbetslista
  Then visas inte ärendet i arbetslistan
```

Automationsbeslut:

| Scenario | Automatiseras? | Kommentar |
|---|---|---|
| Ärende med giltig delegation visas | Ja | Central regel med hög regressionsnytta |
| Särskild sekretess överstyr giltig delegation | Ja | Hög risk och säkerhetsrelevant |
| Utgången delegation visas inte | Ja | Enkel men viktig gränsregel |
| Särskilt åtkomstbeslut ger åtkomst | Vänta | Öppen fråga om beslutsmodell behöver lösas först |

Här syns ett moget arbetssätt. Alla exempel dokumenteras. Några görs till Gherkin. Några automatiseras. Öppna frågor döljs inte.

## Exempel: när Concordion kan vara bättre

Anta att teamet vill beskriva hela åtkomstbeslutet för arbetslistan. Det finns flera villkor:

- tilldelad handläggare
- ansvarig förundersökningsledare
- giltig delegation
- utgången delegation
- särskild sekretess
- särskilt åtkomstbeslut
- jäv eller spärrad åtkomst

Om varje kombination blir ett Gherkin-scenario kan dokumentationen bli lång och svåröverskådlig. En Concordion-liknande specifikation kan i stället ha en förklarande text och en beslutstabell.

Specifikationstext:

> Arbetslistan ska visa ärenden som användaren har ett aktivt arbetsansvar för. Åtkomst kan följa av tilldelning, förundersökningsledaransvar eller delegation. Särskild sekretess begränsar åtkomst om inte ett särskilt åtkomstbeslut finns. Jäv eller spärrad åtkomst överstyr övriga åtkomstgrunder.

Tabell:

| Tilldelad | Ansvarig FUL | Giltig delegation | Särskild sekretess | Särskilt beslut | Jäv/spärr | Visas |
|---|---|---|---|---|---|---|
| Ja | Nej | Nej | Nej | Nej | Nej | Ja |
| Nej | Ja | Nej | Nej | Nej | Nej | Ja |
| Nej | Nej | Ja | Nej | Nej | Nej | Ja |
| Nej | Nej | Ja | Ja | Nej | Nej | Nej |
| Nej | Nej | Ja | Ja | Ja | Nej | Ja |
| Ja | Nej | Nej | Nej | Nej | Ja | Nej |

Denna form kan vara mer läsbar för komplexa regler. Den kan också vara körbar om den kopplas till testkod. Verksamheten får överblick, test får tydliga kombinationer och utveckling får en mer systematisk regelbild.

## Hantera sekretess och känslig information i exempel

I ett brottsutredningsstöd får exempel aldrig bli slarviga med känslig information. Även om boken använder ett fiktivt case är principen viktig i verkligt kravarbete.

Exempel bör inte innehålla:

- riktiga personuppgifter
- verkliga ärendenummer
- verkliga misstankeuppgifter
- känsliga brottsrubriceringar kopplade till identifierbara personer
- intern säkerhetsinformation
- verkliga användar-ID:n eller rolluppsättningar som kan missbrukas

Använd i stället syntetiska data:

| Typ | Exempel |
|---|---|
| Ärende | `Ärende A`, `Ärende B`, `B-EXEMPEL-001` |
| Användare | `Utredare Anna`, `Utredare Bo` |
| Grupp | `Utredningsgrupp Nord` |
| Roll | `Tilldelad handläggare`, `Ansvarig FUL` |
| Datum | `dagens datum`, `2026-05-01` när datum behövs |
| Sekretess | `särskild sekretess`, `ingen särskild sekretess` |

Syntetiska data ska vara realistiska nog för att exempel ska bli meningsfulla, men inte så realistiska att de riskerar att exponera verkliga förhållanden.

## Versionshantering av scenarier

När Gherkin- eller Concordion-specifikationer används i ett utvecklingsteam hamnar de ofta i versionshantering tillsammans med kod. Det kan vara bra, men det påverkar kravanalytikerns arbetssätt.

Fördelar:

- ändringar blir spårbara
- scenarier kan granskas i samma flöde som kod
- automatisering och specifikation hålls nära varandra
- historik finns kvar

Risker:

- verksamheten får svårare att läsa och kommentera
- scenarier blir tekniska artefakter
- kravanalytiker kan tappa direkt inflytande
- dokumentationen kan försvinna in i utvecklingsteamets verktyg

Ett fungerande arbetssätt behöver därför svara på frågor som:

- Var granskar verksamheten scenarier?
- Hur syns föreslagna ändringar för kravanalytiker?
- Vem får ändra Gherkin-texten?
- Hur kopplas scenarier till beslut och regler?
- Hur publiceras aktuell levande dokumentation?
- Hur hanteras scenarier som inte längre gäller?

Detta är inte bara verktygsfrågor. Det är governance för levande dokumentation.

## Ägarskap och ansvar

Ett vanligt problem med automatiserbara specifikationer är oklart ägarskap. Verksamheten tror att test äger dem. Test tror att krav äger dem. Krav tror att utveckling äger dem eftersom de ligger i kodbasen. Utveckling tror att de bara implementerar det som andra har bestämt.

Ett mer hållbart ansvar kan se ut så här:

| Del | Primärt ansvar | Medansvar |
|---|---|---|
| Verksamhetsregel | Produktägare eller beslutsför verksamhetsroll | Kravanalytiker |
| Exempel och scenarioinnehåll | Kravanalytiker som facilitator | Verksamhet, test, utveckling |
| Gherkin-läsbarhet | Kravanalytiker och testare | Utvecklare |
| Automationsdesign | Testare och utvecklare | Kravanalytiker vid nivåfrågor |
| Step definitions | Utvecklare eller testautomatiserare | Testare |
| Levande dokumentation | Teamet gemensamt | Produktägare |
| Publicering och åtkomst | Team eller förvaltningsorganisation | Arkitektur/governance vid behov |

Det viktiga är att ingen behandlar scenarierna som “någon annans dokumentation”.

## Verktygsexempel utan verktygsberoende

Eftersom detta är en lärobok/handbok och inte en installationsguide bör verktygsexempel vara pedagogiska snarare än versionsberoende. Det betyder att boken bör visa:

- hur ett scenario kan se ut
- hur en tabell kan användas
- hur man väljer format
- vilka risker som finns
- hur roller samarbetar

Boken bör inte låsa läsaren vid:

- en viss Cucumber-version
- ett visst programmeringsspråk
- en viss byggpipeline
- en viss testmiljö
- ett visst repositoryupplägg

I verkliga projekt behöver sådana beslut dokumenteras i teamets tekniska dokumentation eller arkitekturbeslut, inte i den verksamhetsnära SBE-specifikationen.

## Vanliga misstag

- **Misstag: Att börja med Cucumber innan exemplen är bra.**
  - Varför det händer: Verktyget känns konkret och ger en snabb känsla av framdrift.
  - Hur du undviker det: Börja med regler, exempel och workshopgranskning. Automatisera först när innehållet är stabilt nog.

- **Misstag: Att skriva Gherkin som tekniska testskript.**
  - Varför det händer: Testautomation behöver tekniska detaljer för att köras.
  - Hur du undviker det: Håll Gherkin på beteendenivå och placera tekniska detaljer i step definitions eller tekniskt testlager.

- **Misstag: Att kalla alla exempel för testfall.**
  - Varför det händer: Organisationen är van att krav verifieras genom testfall.
  - Hur du undviker det: Skilj mellan förståelseexempel, referensexempel, granskningsfall och automatiserade kontroller.

- **Misstag: Att använda Gherkin för beslutstabeller som borde vara tabeller.**
  - Varför det händer: Teamet har bestämt att allt ska skrivas i samma format.
  - Hur du undviker det: Välj form efter innehåll. Många villkorskombinationer blir ofta tydligare i tabellform.

- **Misstag: Att verksamheten tappar åtkomst till levande dokumentation.**
  - Varför det händer: Scenarierna flyttas in i kodrepositoryn och blir utvecklingsteamets artefakter.
  - Hur du undviker det: Publicera läsbara vyer, behåll regel- och exempel-ID:n och skapa granskningsrutiner.

- **Misstag: Att återanvända steg så hårt att språket blir onaturligt.**
  - Varför det händer: Teamet vill minska kodduplicering i automationen.
  - Hur du undviker det: Optimera Gherkin för läsbarhet. Optimera teknisk återanvändning i testkoden.

- **Misstag: Att automatisera för tidigt i områden med många öppna frågor.**
  - Varför det händer: Automation ses som kvalitetsstämpel.
  - Hur du undviker det: Markera öppna frågor och vänta med automation tills regeln är tillräckligt beslutad.

## Övningar

### Övning 1: Välj rätt dokumentationsform

Utgå från följande kravområde:

> Systemet ska visa sökträffar olika beroende på om användaren har full åtkomst, begränsad åtkomst eller ingen åtkomst till ärendet.

Gör följande:

1. Skriv en kort verksamhetsregel.
2. Skapa tre konkreta exempel.
3. Avgör om exemplen passar bäst som Gherkin, beslutstabell eller Concordion-liknande dokumentation.
4. Motivera valet.

### Övning 2: Förbättra ett svagt Gherkin-scenario

Förbättra detta scenario:

```gherkin
Scenario: Rätt ärenden visas
  Given att användaren har behörighet
  When användaren söker
  Then visas rätt ärenden
```

Gör scenariot mer konkret genom att:

1. ange vilken roll användaren har
2. ange relationen till ärendet
3. ange åtkomst- eller sekretessvillkor
4. ange förväntat resultat
5. undvika tekniska detaljer

### Övning 3: Dela upp verksamhetsnivå och teknisk nivå

Utgå från detta tekniska scenario:

```gherkin
Scenario: API returnerar maskerad träff
  Given att databasen innehåller case_id "B-001"
  And att user_id "U-100" saknar ACL-rad
  When GET /search?q=B-001 körs
  Then returneras HTTP 200
  And response.results[0].masked är true
```

Gör om det till två delar:

1. ett verksamhetsnära SBE-scenario
2. en kort notering om teknisk automationsnivå

### Fördjupning

Välj ett kravområde från ditt eget arbete där ni använder acceptanskriterier. Gör en enkel bedömning:

- Vilka acceptanskriterier borde bli exempel?
- Vilka exempel borde bli Gherkin-scenarier?
- Vilka exempel borde hellre vara tabeller?
- Vilka borde inte automatiseras ännu?
- Vilka roller behöver vara med för att scenarierna ska bli både begripliga och testbara?

## Snabb sammanfattning

- Gherkin är ett strukturerat format för att beskriva beteenden, ofta med `Given`, `When` och `Then`.
- Cucumber kan köra Gherkin-scenarier genom att koppla dem till testkod.
- Concordion passar ofta när specifikationen behöver vara mer dokumentnära med text, tabeller och körbara exempel.
- SBE börjar inte med verktyg. Verktyg kommer efter gemensam förståelse.
- Gherkin passar bra för tydliga beteenden med förutsättning, handling och resultat.
- Beslutstabeller passar ofta bättre för många villkorskombinationer.
- Automatisering är värdefull när scenarierna är viktiga, stabila och underhållbara.
- Alla exempel ska inte automatiseras.
- Verksamhetsnära scenarier och tekniska tester bör kopplas ihop, men inte blandas ihop.
- Levande dokumentation kräver ägarskap, publicering och uppdatering, inte bara körbara tester.

## Quiz/reflektionsfrågor

1. Varför är det riskabelt att börja SBE-införande med Cucumber snarare än med exempelworkshops?
2. Vad skiljer ett verksamhetsnära Gherkin-scenario från ett tekniskt API-test?
3. När är en beslutstabell tydligare än flera Gherkin-scenarier?
4. Vilka typer av krav i brottsutredningsstödet passar bäst för Cucumber?
5. Vilka typer av krav passar bättre för Concordion-liknande dokumentation?
6. Hur kan ett team säkerställa att Gherkin-scenarier fortfarande är begripliga för verksamheten?
7. Varför bör step definitions inte betraktas som kravdokumentation?
8. Vilka exempel bör inte automatiseras direkt?
9. Hur kan exempel-ID:n och regel-ID:n hjälpa till att koppla dokumentation, Gherkin och test?
10. Vad behöver vara tydligt kring ägarskap när levande dokumentation används?

## Koppling till bokens röda tråd

Gherkin, Cucumber och Concordion placeras här efter dokumentationskapitlen medvetet. Verktyg och format ska förstärka en redan etablerad förståelse, inte ersätta den. Därför bör valet mellan Gherkin, Concordion eller icke-automatiserad dokumentation alltid utgå från vem som behöver läsa specifikationen och vilket beslut eller beteende den ska stödja.


## Nästa steg

Nu har vi placerat Gherkin, Cucumber och Concordion i ett SBE-sammanhang. Nästa kapitel går vidare till samspelet mellan krav, test och utveckling. Där fördjupar vi hur exempel blir användbara över hela kedjan från behov och regel till design, test, implementation och förvaltning, utan att kravdokumentationen förlorar sin verksamhetsförankring.
