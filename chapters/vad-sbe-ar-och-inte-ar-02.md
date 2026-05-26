# Kapitel 2: Vad SBE är — och inte är

## Varför detta kapitel finns

I föregående kapitel såg vi varför traditionellt kravarbete ofta får svårt att bära hela vägen från verksamhetsbehov till fungerande lösning. Problemet är sällan att kravanalytiker skriver slarvigt. Problemet är oftare att kravtext, acceptanskriterier, testfall och tekniska tolkningar hamnar i olika artefakter och gradvis börjar beskriva olika versioner av samma behov.

Det här kapitlet introducerar Specification by Example, förkortat SBE, som ett sätt att minska det glappet. Fokus ligger inte på ett nytt dokumentformat i första hand, utan på ett arbetssätt där exempel används för att skapa gemensam förståelse, precisera regler och göra kraven användbara för både verksamhet och IT.

## Lärandemål

Efter kapitlet ska du kunna:

- Förklara vad SBE innebär i praktiskt kravarbete.
- Skilja mellan regel, exempel, scenario och acceptanskriterium.
- Beskriva vad levande dokumentation betyder i ett SBE-sammanhang.
- Förstå relationen mellan SBE, BDD, ATDD, Gherkin, Cucumber och Concordion på en kravanalytikernivå.
- Känna igen vanliga missförstånd om SBE.

## Innan vi börjar

Du som läser är troligen redan van vid att skriva krav i stil med:

- Systemet ska kunna visa en lista över ärenden.
- Endast behöriga användare ska kunna se sekretessbelagda uppgifter.
- Användaren ska kunna filtrera sökresultat på ärendestatus.

Du är kanske också van vid acceptanskriterier som beskriver när ett krav ska betraktas som uppfyllt. SBE ersätter inte behovet av tydliga krav. Det förändrar däremot hur kraven upptäcks, preciseras, dokumenteras och används.

En viktig skillnad är att SBE inte börjar med frågan “hur ska vi formulera kravet?”, utan med frågor som:

- Vilka konkreta situationer måste lösningen hantera?
- Vilken regel styr beteendet i situationen?
- Vilka exempel visar att vi har förstått regeln rätt?
- Vilka undantag eller gränsfall ändrar förväntat resultat?
- Kan verksamhet, utveckling och test läsa samma specifikation och dra samma slutsats?

## Huvudförklaring

### SBE i en mening

Specification by Example är ett arbetssätt där krav uttrycks och förfinas med hjälp av konkreta exempel som visar hur systemet ska bete sig i specifika situationer.

Det betyder inte att all kravdokumentation blir testfall. Det betyder inte heller att allting måste skrivas i Gherkin eller automatiseras. Kärnan är att exempel används för att göra abstrakta regler konkreta, så att olika roller kan upptäcka missförstånd tidigare.

Ett traditionellt krav kan säga:

> En utredare ska bara kunna se ärenden som utredaren har behörighet till.

Det är begripligt, men lämnar många frågor öppna. Vad räknas som behörighet? Är det organisatorisk tillhörighet, tilldelning till ärendet, särskild roll, tillfällig åtkomst eller en kombination? Vad händer om utredaren byter organisatorisk enhet? Vad händer med sekretessmarkerade uppgifter?

I SBE försöker vi komplettera eller omforma kravet genom att synliggöra regler och exempel.

Exempel:

| Situation | Användarens relation till ärendet | Ärendet har sekretessmarkering | Förväntat resultat |
|---|---|---|---|
| Utredaren är tilldelad ärendet | Tilldelad | Nej | Ärendet visas |
| Utredaren tillhör samma enhet men är inte tilldelad | Samma enhet | Nej | Ärendet visas med begränsad detaljnivå |
| Utredaren tillhör annan enhet | Ingen relation | Nej | Ärendet visas inte |
| Utredaren är tilldelad ärendet | Tilldelad | Ja | Ärendet visas om särskild behörighet finns |
| Utredaren har särskild behörighet | Särskild åtkomst | Ja | Ärendet visas och åtkomsten loggas |

Exemplen gör kravet mer konkret. De gör också samtalet bättre. När verksamheten ser tabellen kan den säga: “Nej, samma enhet ska inte räcka i det här fallet” eller “Sekretessmarkerade uppgifter ska aldrig visas utan särskilt beslut”. Det är just den typen av upptäckter SBE försöker skapa tidigt.

### De centrala byggstenarna

SBE bygger ofta på fyra praktiska byggstenar: regler, exempel, scenarier och öppna frågor.

En **regel** beskriver ett beteende eller en verksamhetsprincip som ska gälla. Regeln bör vara begriplig för verksamheten.

Ett **exempel** visar hur regeln fungerar i en konkret situation. Exemplet har specifika indata, förutsättningar eller kontext och ett förväntat resultat.

Ett **scenario** beskriver ett sammanhängande händelseförlopp. Det kan skrivas i fri text, i tabellform eller i ett strukturerat format som Gherkin.

En **öppen fråga** markerar något som ännu inte är beslutat eller förstått. I SBE är öppna frågor inte ett misslyckande, utan ett viktigt resultat av arbetet. De visar var specifikationen ännu inte är mogen.

I brottsutredningsstödet kan byggstenarna se ut så här:

- Regel: En användare får bara se sekretessmarkerade uppgifter om användaren har särskild behörighet för ärendet.
- Exempel: En utredare som är tilldelad ärendet men saknar särskild behörighet får se ärendet, men inte de sekretessmarkerade uppgifterna.
- Scenario: Utredaren öppnar ärendet, systemet kontrollerar tilldelning och särskild behörighet, och systemet döljer skyddade uppgifter men visar övrig ärendeinformation.
- Öppen fråga: Ska systemet visa att uppgifter finns men är dolda, eller ska uppgifterna inte synas alls i användargränssnittet?

### Från acceptanskriterier till exempel

Acceptanskriterier och SBE ligger nära varandra, men de fyller inte exakt samma funktion.

Ett acceptanskriterium beskriver ofta ett villkor för att funktionen ska accepteras. Ett exempel visar hur villkoret beter sig i en konkret situation. Skillnaden märks tydligt när kravet innehåller flera villkor, undantag eller gränsfall.

Traditionellt acceptanskriterium:

> Givet att användaren saknar behörighet till ärendet ska ärendet inte visas i sökresultatet.

Det är testbart, men kanske fortfarande för smalt. SBE-frågan blir: vilka olika sätt kan en användare sakna, ha eller delvis ha behörighet?

Då kan vi behöva flera exempel:

| Exempel | Användare | Ärenderelation | Särskild behörighet | Förväntat resultat |
|---|---|---|---|---|
| 1 | Utredare Anna | Tilldelad ärendet | Nej | Ärendet visas |
| 2 | Utredare Bo | Samma enhet | Nej | Ärendet visas enligt grundregel |
| 3 | Utredare Clara | Annan enhet | Nej | Ärendet visas inte |
| 4 | Utredare David | Annan enhet | Ja | Ärendet visas och åtkomsten loggas |
| 5 | Analytiker Eva | Stödroll i ärendet | Nej | Ärendet visas med begränsad information |

Här syns något viktigt: SBE hjälper inte bara till att dokumentera svaret. Det hjälper gruppen att upptäcka att den kanske inte är överens om frågan.

### Levande dokumentation

Begreppet levande dokumentation används ofta i SBE-sammanhang. Det betyder dokumentation som är aktuell, används aktivt och har en tydlig relation till systemets faktiska beteende.

Levande dokumentation är inte automatiskt samma sak som automatiserade tester. Automatisering kan vara ett sätt att hålla dokumentationen levande, men det är inte hela poängen. Dokumentationen är levande när den:

- används i samtal mellan verksamhet och IT,
- uppdateras när regler ändras,
- hjälper utvecklare att förstå förväntat beteende,
- hjälper testare att se vad som ska verifieras,
- hjälper förvaltning att förstå varför systemet beter sig som det gör,
- minskar behovet av separata, motstridiga beskrivningar.

I praktiken kan levande dokumentation bestå av flera delar: korta regelbeskrivningar, tabeller med exempel, Gherkin-scenarier, dokumentnära specifikationer, beslut, öppna frågor och länkar till kompletterande arkitekturbeslut eller juridiska riktlinjer.

För brottsutredningsstödet är detta särskilt viktigt eftersom regler kring behörighet, sekretess, loggning och informationsklassning både måste förstås av verksamheten och kunna realiseras av IT. Om dokumentationen bara fungerar för den ena gruppen uppstår glappet igen.

### SBE, BDD och ATDD

SBE nämns ofta tillsammans med BDD och ATDD. Begreppen överlappar, men de är inte identiska.

**BDD**, Behavior-Driven Development, fokuserar på systemets beteende utifrån konkreta exempel och gemensamt språk. BDD används ofta tillsammans med Gherkin och verktyg som Cucumber.

**ATDD**, Acceptance Test-Driven Development, fokuserar på att definiera acceptanstester innan implementationen görs. Det betonar ofta samarbete mellan verksamhet, utveckling och test.

**SBE** kan ses som ett bredare arbetssätt för att upptäcka, precisera och dokumentera krav med exempel. SBE kan användas med eller utan BDD, med eller utan ATDD, och med eller utan testautomation.

För en kravanalytiker är den praktiska poängen denna: börja inte med verktyget. Börja med att få fram de exempel som gör regeln tydlig. När exemplen är tillräckligt bra kan ni avgöra om de ska förbli dokumentation, bli underlag för manuella tester eller automatiseras.

### Gherkin, Cucumber och Concordion i korthet

Gherkin är ett textformat som ofta använder strukturen Given, When, Then. På svenska kan man tänka “givet att”, “när” och “så ska”. Formatet gör scenarier tydliga och kan vara lätt att läsa när beteendet är händelsedrivet.

Exempel:

```gherkin
Scenario: Utredare utan särskild behörighet öppnar sekretessmarkerat ärende
  Given att utredaren är tilldelad ärendet
  And att ärendet innehåller sekretessmarkerade uppgifter
  And att utredaren saknar särskild behörighet
  When utredaren öppnar ärendet
  Then ska ärendet visas
  And de sekretessmarkerade uppgifterna ska döljas
```

Cucumber är ett verktyg som kan köra Gherkin-scenarier som automatiserade tester om scenarierna kopplas till teknisk testkod. Det kan vara kraftfullt när teamet har mognad, stabila beteenden och ett tydligt ägarskap för testautomation.

Concordion är ett verktyg för körbara specifikationer där dokumentationen kan vara mer dokumentnära. Det kan passa när man vill kombinera läsbar specifikation med automatiserad verifiering utan att allt behöver uttryckas som korta Given-When-Then-scenarier.

I den här boken kommer vi att behandla Gherkin, Cucumber och Concordion praktiskt men återhållsamt. De är viktiga verktyg och format, men SBE är större än verktygen.

### Vad SBE inte är

SBE missförstås ofta. Därför är det lika viktigt att beskriva vad det inte är.

SBE är inte en ny kravmall som löser problemet av sig själv. Om organisationen bara byter rubriker i kravdokumentet men fortsätter arbeta sekventiellt, kommer effekten bli begränsad.

SBE är inte bara testautomation. Automatiserade tester kan vara en effekt av bra exempel, men dåliga exempel blir inte bättre för att de automatiseras.

SBE är inte ett krav på att allt ska skrivas i Gherkin. Vissa regler passar bättre som tabeller, beslutsträd, korta regelbeskrivningar eller dokumentnära specifikationer.

SBE är inte ett sätt att slippa analys. Tvärtom kräver SBE ofta mer aktiv analys tidigt, eftersom oklarheter synliggörs innan de göms i generella formuleringar.

SBE är inte bara för utvecklare eller testare. Om verksamheten inte kan läsa, förstå och utmana specifikationen har man tappat en stor del av poängen.

## Exempel

Låt oss jämföra tre sätt att dokumentera samma behov i brottsutredningsstödet.

### Traditionell kravtext

> Systemet ska säkerställa att användare endast får åtkomst till ärendeinformation de är behöriga att se.

Kravet är korrekt på en övergripande nivå, men det räcker inte för att avgöra hur systemet ska bete sig i konkreta situationer.

### Acceptanskriterier

- Om användaren är tilldelad ärendet ska ärendet visas.
- Om användaren inte är behörig ska ärendet inte visas.
- Om ärendet innehåller sekretessmarkerade uppgifter ska endast användare med särskild behörighet kunna se dessa.

Detta är bättre. Men även här finns frågor. Vad betyder “inte behörig”? Vad händer om användaren tillhör samma enhet men inte är tilldelad? Vad visas om bara vissa uppgifter i ärendet är sekretessmarkerade?

### SBE-specifikation

Regel: En användares åtkomst till ett ärende beror på relationen till ärendet och eventuell särskild behörighet för skyddade uppgifter.

| Exempel | Relation till ärendet | Skyddade uppgifter finns | Särskild behörighet | Förväntat resultat |
|---|---|---|---|---|
| Tilldelad utredare öppnar normalt ärende | Tilldelad | Nej | Nej | Hela ärendet visas |
| Tilldelad utredare öppnar ärende med skyddade uppgifter | Tilldelad | Ja | Nej | Ärendet visas, skyddade uppgifter döljs |
| Utredare med särskild behörighet öppnar skyddat ärende | Tilldelad | Ja | Ja | Hela ärendet visas och åtkomsten loggas |
| Utredare utan relation söker ärende | Ingen relation | Nej | Nej | Ärendet visas inte i sökresultat |
| Förundersökningsledare granskar ärende | Beslutsroll | Ja | Ja | Hela ärendet visas och åtkomsten loggas |

Öppna frågor:

- Ska dolda skyddade uppgifter indikeras i gränssnittet?
- Ska loggning ske även när åtkomst nekas?
- Finns det tidsbegränsad särskild behörighet?
- Ska analytiker hanteras enligt samma regel som utredare?

Den sista versionen är längre, men den är också mer användbar. Den gör det möjligt att diskutera beteendet, hitta luckor, skapa testfall, bedöma teknisk påverkan och förvalta regeln över tid.

## Vanliga misstag

- **Misstag: Att tro att SBE är samma sak som Gherkin.**
  - Varför det händer: Gherkin är ett synligt och spritt format i BDD- och SBE-sammanhang.
  - Hur du undviker det: Välj format efter behov. Använd tabeller, regler och fri text när det är mer läsbart.

- **Misstag: Att automatisera innan exemplen är begripliga.**
  - Varför det händer: Organisationer vill snabbt få teknisk nytta och mätbar effekt.
  - Hur du undviker det: Säkerställ först att exemplen är verksamhetsmässigt korrekta och gemensamt förstådda.

- **Misstag: Att skriva exempel som bara upprepar kravtexten.**
  - Varför det händer: Det är lätt att byta format utan att ändra analysnivå.
  - Hur du undviker det: Använd konkreta värden, roller, tillstånd och förväntade resultat.

- **Misstag: Att göra varje detalj till ett scenario.**
  - Varför det händer: När man upptäcker styrkan i exempel är det frestande att beskriva allt på samma sätt.
  - Hur du undviker det: Skilj mellan regler som behöver exempel, generell information och tekniska detaljer som hör hemma någon annanstans.

- **Misstag: Att glömma verksamhetsläsbarheten.**
  - Varför det händer: Verktygsformat och testautomation kan snabbt bli tekniskt orienterade.
  - Hur du undviker det: Låt verksamheten läsa och kommentera specifikationen innan den betraktas som färdig.

## Övningar

### Övning 1: Hitta luckorna i ett traditionellt krav

Utgå från följande krav:

> Systemet ska visa relevanta ärenden för användaren baserat på användarens behörighet.

Svara på frågorna:

1. Vilka ord i kravet behöver förtydligas?
2. Vilka användarroller kan påverka regeln?
3. Vilka exempel skulle du vilja se innan utveckling påbörjas?
4. Vilka öppna frågor bör dokumenteras?

### Övning 2: Omvandla acceptanskriterier till exempel

Utgå från följande acceptanskriterier:

- En utredare ska kunna se tilldelade ärenden.
- En utredare ska inte kunna se ärenden från andra enheter.
- En förundersökningsledare ska kunna se ärenden som kräver beslut.

Skapa en enkel tabell med minst fem exempel. Tabellen ska innehålla roll, relation till ärendet, särskild situation och förväntat resultat.

### Fördjupning

Välj ett krav från ett eget projekt. Skriv först kravet i traditionell form. Skriv sedan:

- en regel,
- tre konkreta exempel,
- ett scenario,
- minst två öppna frågor.

Reflektera över vilken version som är lättast för verksamheten att granska och vilken version som är mest användbar för IT.

## Snabb sammanfattning

- SBE använder konkreta exempel för att precisera krav och skapa gemensam förståelse.
- En regel beskriver vad som ska gälla; ett exempel visar hur regeln fungerar i en konkret situation.
- Scenarier kan skrivas i fri text, tabellform eller Gherkin.
- Levande dokumentation är dokumentation som används, hålls aktuell och speglar systemets faktiska beteende.
- SBE kan kombineras med BDD, ATDD, Cucumber och Concordion, men är inte samma sak som något av dem.
- Verktyg ska väljas efter dokumentationsbehov, samarbetsmognad och nytta, inte tvärtom.

## Quiz/reflektionsfrågor

1. Vad är den viktigaste skillnaden mellan ett abstrakt krav och ett SBE-exempel?
2. När är Gherkin ett bra format, och när kan en tabell vara bättre?
3. Varför är det riskabelt att se SBE som testautomation i första hand?
4. Vad innebär levande dokumentation i en organisation där både verksamhet och IT behöver använda samma kunskap?
5. Vilka typer av krav i brottsutredningsstödet tror du lämpar sig bäst för SBE?

## Koppling till bokens röda tråd

I den här boken används SBE som ett krav- och samarbetsmönster först, och som möjlig grund för automatisering sedan. Det innebär att värdet inte mäts i antal automatiserade scenarier, utan i om exemplen skapar bättre beslut, tydligare dokumentation och färre sena missförstånd.


## Nästa steg

Nu har vi etablerat vad SBE är och vilka byggstenar arbetssättet använder. Nästa kapitel handlar om kravanalytikerns förändrade roll: från att huvudsakligen formulera krav till att skapa förutsättningar för gemensam förståelse, bättre samtal och mer användbar dokumentation.
