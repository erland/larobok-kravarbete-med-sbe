# Kapitel 7: Regler, exempel och scenarier i praktiken

## Varför detta kapitel finns

I föregående kapitel arbetade vi med omvandlingen från traditionell kravtext till exempelbaserad specifikation. Vi tog ett krav om sökning av utredningsärenden och visade hur det kunde delas upp i syfte, regler, exempel, öppna frågor och tekniska konsekvenser.

Det här kapitlet går ett steg djupare. Nu handlar det inte längre om att förstå att exempel är användbara, utan om att använda dem med precision. En erfaren kravanalytiker behöver kunna avgöra när något är en regel, när något är ett exempel, när något bör bli ett scenario och när dokumentationen håller på att bli för teknisk eller för detaljerad.

Det är också här SBE blir ett praktiskt hantverk. Det räcker inte att lägga till några exempel under ett krav. Exemplen behöver pröva rätt saker. Reglerna behöver uttryckas på en nivå som verksamheten kan bekräfta. Scenarierna behöver visa beteende utan att låsa lösningsdesign i onödan. Dokumentationen behöver samtidigt vara användbar för IT, test och förvaltning.

I brottsutredningsstödet är detta särskilt tydligt. Regler om åtkomst, sekretess, ärendestatus och handläggningsansvar kan inte lämnas som allmänna formuleringar. De behöver konkretiseras. Samtidigt får specifikationen inte bli en ogenomtränglig samling testfall där verksamheten tappar överblicken.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan regel, exempel och scenario i en SBE-specifikation,
- formulera regler så att de är verksamhetsnära och prövbara,
- välja när en exempeltabell passar bättre än ett scenario,
- använda exempel för att hitta gränsfall, undantag och dolda antaganden,
- undvika att exempelbaserad dokumentation blir antingen för abstrakt eller för teknisk,
- skapa dokumentation som både verksamhet och IT kan använda.

## Innan vi börjar

I boken använder vi följande grundtanke:

> En regel beskriver vad som ska gälla. Ett exempel visar vad regeln betyder i en konkret situation. Ett scenario visar hur beteendet uppstår över tid eller genom en interaktion.

Denna skillnad är enkel att säga men svårare att hålla fast vid i praktiken. I många kravdokument blandas regler, exempel, flödesbeskrivningar, lösningsidéer och testförslag i samma text. Det gör dokumentationen svår att granska. Verksamheten kan ha svårt att se om regeln är rätt. IT kan ha svårt att se vad som faktiskt ska implementeras. Test kan ha svårt att se vad som ska verifieras.

SBE hjälper genom att separera dessa delar utan att skapa onödig byråkrati. Syftet är inte att skapa fler dokument. Syftet är att göra specifikationen tydligare.

## Grundmodellen: regel, exempel och scenario

En praktisk SBE-specifikation kan ofta struktureras med tre nivåer:

| Nivå | Fråga den svarar på | Exempel från brottsutredningsstödet |
|---|---|---|
| Regel | Vad ska gälla? | En utredare får se ärenden som tillhör den egna enheten eller där utredaren är tilldelad |
| Exempel | Vad betyder regeln i ett konkret fall? | Utredare A, tilldelad ärende X på annan enhet, får se ärendet |
| Scenario | Hur uppstår beteendet i ett arbetsflöde? | Utredaren söker efter ett ärendenummer och systemet visar ärendet i sökresultatet |

Regeln är den mest kompakta formuleringen. Exemplet prövar innebörden. Scenariot visar användningssituationen.

Alla tre behövs inte alltid. Ibland räcker en regel och några exempel i tabellform. Ibland krävs ett scenario för att förstå ordningen mellan händelser. Ibland är regeln så enkel att ett enda exempel räcker. Det viktiga är att välja form efter vad som behöver förstås, inte efter en mall.

## Regelns uppgift

En regel ska uttrycka verksamhetens avsikt. Den ska inte bara beskriva en teknisk validering och inte heller vara så vag att den inte går att pröva.

En svag regel kan se ut så här:

> Systemet ska hantera behörighet korrekt.

Problemet är inte att meningen är fel. Problemet är att den inte säger vad korrekt betyder. Den går inte att diskutera på ett meningsfullt sätt utan kompletterande antaganden.

En bättre regel är:

> En användare får se ett utredningsärende om användaren är tilldelad ärendet, tillhör ärendets ansvariga enhet eller har särskild åtkomstnivå.

Den regeln är fortfarande inte komplett, men den är prövbar. Den pekar ut villkor. Den går att bekräfta, utmana och komplettera.

En ännu mer användbar regel kan också ange begränsningar:

> Om ärendet är sekretessmarkerat får användaren endast se begränsad information, om inte användaren har särskild åtkomstnivå eller ansvarar för ärendet som förundersökningsledare.

Nu blir det tydligt att åtkomst inte bara är en fråga om att visa eller dölja ärendet. Det kan finnas mellanlägen.

## Kännetecken på en bra regel

En bra regel i SBE är:

- verksamhetsnära,
- prövbar med exempel,
- tydlig med vilka villkor som påverkar utfallet,
- separerad från teknisk implementation,
- tillräckligt stabil för att användas över tid.

Det betyder inte att regeln måste vara perfekt från början. I SBE är det normalt att regler förfinas när exemplen visar att något saknas.

Exempelvis kan regeln om sekretessmarkerade ärenden först låta komplett. Men när gruppen börjar ta fram exempel kan flera frågor uppstå:

- Vad betyder begränsad information?
- Gäller samma regel vid sökning på ärendenummer och fritextsökning?
- Ska användaren se att ett dolt ärende finns?
- Ska nekade åtkomstförsök loggas?
- Gäller regeln även analytiker med registrerat stöduppdrag?

Dessa frågor visar inte att regeln är dålig. De visar att regeln börjar bli verklig.

## Exemplet som precisionsverktyg

Ett exempel är inte bara en illustration. I SBE är exempel ett precisionsverktyg. Det används för att testa om regeln är förstådd på samma sätt av olika personer.

Ett exempel bör därför vara konkret. Det bör innehålla verkliga eller realistiska värden, tydliga villkor och ett förväntat resultat.

Ett svagt exempel:

> En användare söker efter ett ärende och får se det om användaren har behörighet.

Det exemplet tillför nästan inget. Det upprepar regeln utan att pröva den.

Ett starkare exempel:

| Roll | Relation till ärende | Enhet | Sekretessmarkerat | Särskild åtkomstnivå | Förväntat resultat |
|---|---|---|---|---|---|
| Utredare | Tilldelad | Annan | Ja | Nej | Begränsad information visas |

Detta exempel tvingar fram flera beslut. Får en tilldelad utredare på annan enhet se ett sekretessmarkerat ärende? Vad innebär begränsad information? Ska visningen loggas?

Ett bra exempel skapar ofta fler frågor innan det skapar trygghet. Det är en del av värdet.

## Exempeltyper

Alla exempel har inte samma funktion. I praktiskt SBE-arbete är det användbart att skilja mellan flera typer.

| Exempeltyp | Syfte | När det används |
|---|---|---|
| Normalexempel | Visa det vanligaste förväntade beteendet | När regeln först introduceras |
| Gränsexempel | Pröva precis vid en regelgräns | Vid tidsgränser, belopp, statusar eller behörighetsnivåer |
| Undantagsexempel | Visa när regeln inte ska gälla | När verksamheten ofta säger “utom när...” |
| Konfliktexempel | Pröva två regler som verkar krocka | När sekretess, roll och ansvar drar åt olika håll |
| Referensexempel | Fungera som återkommande ankare | När samma beteende behöver återanvändas i flera kapitel eller diskussioner |

I brottsutredningsstödet kan ett normalexempel vara att en tilldelad utredare ser sitt ärende. Ett gränsexempel kan vara att ett återöppningsbeslut registreras samma dag som ärendet avslutats. Ett konfliktexempel kan vara att en användare tillhör rätt enhet men ärendet är sekretessmarkerat och användaren saknar särskild åtkomstnivå.

## Scenario när beteendet behöver tid och ordning

Ett scenario behövs när beteendet inte bara är ett beslut, utan en händelsekedja. Scenarier är särskilt användbara när det finns:

- användarinteraktion,
- ordning mellan steg,
- förändring av status,
- synliga systemreaktioner,
- koppling mellan flera informationsobjekt.

Exempelvis kan åtkomstregeln ofta beskrivas med en tabell. Men om vi vill visa hur utredaren söker fram ett ärende, öppnar detaljvyn och systemet loggar åtkomsten kan ett scenario vara bättre.

Ett verksamhetsnära scenario kan beskrivas så här:

```gherkin
Scenario: Tilldelad utredare söker fram ett sekretessmarkerat ärende
  Givet att ärende B-2025-0147 är sekretessmarkerat
  Och att utredare Sara Nyström är tilldelad ärendet
  När Sara söker på ärendenummer B-2025-0147
  Så visas ärendet i sökresultatet med begränsad information
  Och åtkomsten loggas
```

Det här är inte en rekommendation att alla scenarier alltid ska skrivas i Gherkin. Formatet används här för att visa strukturen: förutsättning, händelse, förväntat resultat. I kapitel 10 återkommer vi till Gherkin, Cucumber och Concordion mer praktiskt.

## När tabell är bättre än scenario

Ett vanligt misstag är att skriva många nästan identiska scenarier när en tabell hade varit tydligare. Om skillnaden mellan exemplen främst ligger i kombinationer av villkor och utfall är en tabell ofta bättre.

Anta att vi vill pröva sökresultat utifrån roll, relation till ärende och sekretess. Då blir en tabell mer överskådlig:

| Exempel | Roll | Relation till ärende | Enhet | Sekretessmarkerat | Särskild åtkomstnivå | Förväntat resultat |
|---|---|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Annan | Nej | Nej | Full information visas |
| 2 | Utredare | Tilldelad | Annan | Ja | Nej | Begränsad information visas |
| 3 | Utredare | Ingen relation | Samma | Nej | Nej | Full information visas |
| 4 | Utredare | Ingen relation | Samma | Ja | Nej | Begränsad information visas |
| 5 | Utredare | Ingen relation | Annan | Nej | Nej | Ärendet visas inte |
| 6 | Förundersökningsledare | Ansvarig | Annan | Ja | Ja | Full information visas |
| 7 | Analytiker | Registrerat stöduppdrag | Samma | Ja | Nej | Begränsad information visas |

Tabellen gör det lättare att se täckning. Den gör också luckor synliga. Om ingen rad visar administratörens situation kanske gruppen behöver diskutera den.

En tumregel:

> Använd tabell när du jämför villkor. Använd scenario när du förklarar händelseförlopp.

## När scenario är bättre än tabell

En tabell kan bli svår att läsa när ordningen mellan steg är viktig. Statusövergångar är ett exempel. En enkel statusregel kan vara:

> Ett avslutat ärende får inte ändras tillbaka till `Pågående` utan återöppningsbeslut.

Den kan prövas i tabellform:

| Startstatus | Begärd ny status | Återöppningsbeslut | Förväntat resultat |
|---|---|---|---|
| Avslutat | Pågående | Nej | Ändring nekas |
| Avslutat | Pågående | Ja | Ärendet återöppnas |
| Pågående | Avslutat | Nej | Ärendet avslutas |
| Pausat | Pågående | Nej | Ärendet återupptas |

Men om det viktiga är att förstå vad användaren gör och vad systemet visar kan ett scenario vara bättre:

```gherkin
Scenario: Förundersökningsledare återöppnar ett avslutat ärende
  Givet att ärende B-2025-0221 har status Avslutat
  Och att ett återöppningsbeslut finns registrerat
  När förundersökningsledaren väljer att återöppna ärendet
  Så ändras ärendets status till Pågående
  Och systemet registrerar vem som återöppnade ärendet
  Och systemet registrerar tidpunkten för återöppningen
```

Här syns inte bara beslutet. Här syns också verksamhetens krav på spårbarhet.

## Skillnaden mellan verksamhetsscenario och testscenario

I SBE är det viktigt att inte för tidigt göra scenarierna till tekniska testscenarier. Ett verksamhetsscenario ska kunna läsas och diskuteras av verksamheten. Det ska beskriva beteende i verksamhetens språk.

Ett tekniskt testscenario kan däremot innehålla detaljer om testdata, API-anrop, mockar, databasposter eller tekniska kontroller. Sådana detaljer kan vara nödvändiga för automatisering, men de hör inte alltid hemma i den gemensamma specifikationen.

Jämför dessa två formuleringar.

Verksamhetsnära:

```gherkin
När utredaren söker på ärendenummer B-2025-0147
Så visas ärendet med begränsad information
```

Tekniknära:

```gherkin
När GET /cases?caseNumber=B-2025-0147 anropas med token för user_482
Så returneras HTTP 200 och fältet restrictedView är true
```

Båda kan vara korrekta i olika sammanhang. Men de har olika målgrupp. Den första hjälper verksamhet och IT att förstå beteendet. Den andra hjälper ett tekniskt team att verifiera ett gränssnitt.

I den här boken prioriterar vi den gemensamma specifikationen. Automatisering behandlas som en möjlig följd, inte som startpunkten.

## Att skriva regler på rätt nivå

En regel kan skrivas på för hög nivå:

> Systemet ska följa gällande sekretessregler.

Det är sant men inte användbart som SBE-regel. Den är för generell och hänvisar till något utanför specifikationen.

En regel kan också skrivas på för låg teknisk nivå:

> Tabellen `case_access` ska innehålla en rad med `access_type = LIMITED` när användaren saknar full behörighet.

Det kan vara relevant i teknisk design, men det är inte en verksamhetsregel.

En bättre nivå är:

> När ett ärende är sekretessmarkerat och användaren saknar full åtkomst ska systemet endast visa begränsad information.

Den regeln kan sedan kompletteras med exempel som visar vad begränsad information betyder.

## Att formulera exempel med verklighetskänsla

Exempel blir bättre när de känns realistiska. Det betyder inte att man måste använda riktiga personuppgifter eller känsliga data. I ett myndighetscase bör man normalt använda fiktiva men trovärdiga namn, ärendenummer, roller och situationer.

Svagt:

| Användare | Ärende | Resultat |
|---|---|---|
| User1 | Case1 | OK |

Bättre:

| Användare | Roll | Ärende | Situation | Förväntat resultat |
|---|---|---|---|---|
| Sara Nyström | Utredare | B-2025-0147 | Tilldelad men annan enhet | Begränsad information visas |

Det andra exemplet är lättare att diskutera. Det väcker frågor som ligger nära verksamheten.

Samtidigt ska exempel inte bli romaner. De ska vara konkreta men fokuserade.

## Att hitta rätt antal exempel

Ett annat vanligt misstag är att tro att fler exempel alltid ger bättre specifikation. Det stämmer inte. För många exempel kan göra dokumentationen tung, svår att granska och dyr att underhålla.

Frågan är inte “har vi alla exempel?”. Frågan är:

> Har vi tillräckligt många exempel för att förstå regeln, hitta viktiga undantag och kunna verifiera beteendet?

En praktisk startpunkt är att ha:

- ett exempel där regeln tydligt gäller,
- ett exempel där regeln tydligt inte gäller,
- ett gränsexempel eller undantagsexempel,
- ett exempel där två regler samspelar.

För åtkomst till sekretessmarkerade ärenden kan det innebära:

| Typ | Exempel | Varför behövs det? |
|---|---|---|
| Regeln gäller | Tilldelad utredare får se begränsad information | Visar normalfallet |
| Regeln gäller inte | Utredare utan relation till annan enhet ser inte ärendet | Visar nekad åtkomst |
| Undantag | Förundersökningsledare med särskild åtkomst ser full information | Visar privilegierat fall |
| Samspel | Analytiker med stöduppdrag ser begränsad information | Visar roll och uppdrag tillsammans |

Om gruppen fortfarande tolkar regeln olika behövs fler exempel. Om alla förstår regeln och ytterligare exempel bara upprepar samma beslut kan man sluta.

## Exempel som hittar öppna frågor

Ett av de viktigaste resultaten av en SBE-session är inte färdiga scenarier, utan öppna frågor. När ett exempel visar att gruppen inte vet vad som ska gälla ska frågan dokumenteras tydligt.

Exempel:

| Fråga | Utlösande exempel | Varför frågan är viktig |
|---|---|---|
| Vilka fält ingår i begränsad information? | Sekretessmarkerat ärende visas för tilldelad utredare | Påverkar både verksamhet, gränssnitt och test |
| Ska nekade sökningar loggas? | Utredare utan relation söker på exakt ärendenummer | Påverkar säkerhet och spårbarhet |
| Ska samma regel gälla vid fritextsökning och ärendenummersökning? | Användaren söker på del av målsägandes namn | Påverkar integritet och sökbeteende |
| Hur länge gäller ett registrerat stöduppdrag? | Analytiker får åtkomst genom stöduppdrag | Påverkar åtkomst över tid |

Öppna frågor ska inte döljas i brödtext. De bör vara synliga i dokumentationen så att de kan ägas, besvaras och följas upp.

## Från exempel till förtydligad regel

När exemplen har diskuterats behöver regeln ofta uppdateras. Det är en viktig del av arbetssättet.

Första regelutkast:

> En användare får se ett ärende om användaren har behörighet.

Efter exempelworkshop:

> En användare får se ett utredningsärende om användaren är tilldelad ärendet, tillhör ärendets ansvariga enhet eller har särskild åtkomstnivå. Om ärendet är sekretessmarkerat visas endast begränsad information, om inte användaren är ansvarig förundersökningsledare eller har särskild åtkomstnivå. Alla visningar av sekretessmarkerade ärenden loggas.

Den andra regeln är längre, men också mycket tydligare. Den innehåller fortfarande öppna frågor, till exempel exakt vad begränsad information innebär, men den har blivit prövbar.

## När exempel visar att flera regler behövs

Ibland försöker man skriva en stor regel som täcker allt. Det blir ofta svårt att läsa. Om exemplen kräver många villkor kan det vara bättre att dela upp regeln.

I brottsutredningsstödet kan åtkomst först se ut som en regel. Men efter analys kan den behöva delas upp:

- grundregel för vilka användare som kan se ärenden,
- särskild regel för sekretessmarkerade ärenden,
- regel för begränsad information,
- regel för loggning,
- regel för stöduppdrag,
- regel för särskild åtkomstnivå.

Det är inte ett misslyckande. Det är ett tecken på att specifikationen börjar spegla verksamhetens komplexitet.

## Att undvika falsk precision

SBE kan skapa en känsla av precision. Tabeller och scenarier ser tydliga ut. Men tydlig form betyder inte automatiskt tydligt innehåll.

Ett exempel kan vara formellt snyggt men fortfarande oklart:

```gherkin
Scenario: Användare söker ärende
  Givet att användaren är behörig
  När användaren söker ärendet
  Så visas rätt resultat
```

Här är nästan alla viktiga ord otydliga: behörig, söker, rätt resultat. Scenariot ger form men inte precision.

Ett bättre scenario använder konkreta villkor och ett konkret utfall:

```gherkin
Scenario: Utredare utan relation till annan enhet får inte se ärendet
  Givet att ärende B-2025-0188 tillhör en annan enhet
  Och att utredaren inte är tilldelad ärendet
  Och att utredaren saknar särskild åtkomstnivå
  När utredaren söker på ärendenummer B-2025-0188
  Så visas inte ärendet i sökresultatet
```

Detta scenario kan fortfarande behöva kompletteras. Ska sökningen loggas? Ska användaren få ett meddelande? Men kärnbeteendet är tydligare.

## Beslutstabeller som mellanform

För komplexa regler är beslutstabeller ofta en bra mellanform. De hjälper gruppen att se kombinationer av villkor och utfall innan man väljer eventuell scenariestruktur.

En beslutstabell behöver inte täcka alla teoretiska kombinationer. Den ska täcka de kombinationer som behövs för att förstå regeln.

| Villkor | Fråga |
|---|---|
| Roll | Vilken typ av användare gör handlingen? |
| Relation | Har användaren relation till ärendet? |
| Enhet | Tillhör användaren ansvarig enhet? |
| Sekretess | Är ärendet sekretessmarkerat? |
| Särskild åtkomst | Har användaren utökad rätt? |
| Stöduppdrag | Finns ett registrerat stöduppdrag? |

När dessa villkor är identifierade kan gruppen välja representativa exempel. Försök inte skapa en tabell som mekaniskt kombinerar allt med allt om det leder till 64 rader som ingen vill läsa. Välj exempel med avsikt.

## Dokumentationsmönster för en SBE-specifikation

Ett praktiskt dokumentationsmönster för funktionella krav kan se ut så här:

1. Kort syfte.
2. Verksamhetsregel.
3. Exempel eller exempeltabell.
4. Eventuella scenarier.
5. Öppna frågor.
6. Tekniska konsekvenser.
7. Spårning till beslut, process eller förmåga.

I markdown kan en sektion exempelvis struktureras så här:

```md
## Åtkomst till sekretessmarkerade ärenden

Syfte: säkerställa att användare kan hitta ärenden de har rätt att arbeta med utan att sekretesskyddad information exponeras felaktigt.

### Regler

- En användare får se ett utredningsärende om användaren är tilldelad ärendet, tillhör ärendets ansvariga enhet eller har särskild åtkomstnivå.
- Om ärendet är sekretessmarkerat visas endast begränsad information, om inte användaren har full åtkomst.
- Alla visningar av sekretessmarkerade ärenden ska loggas.

### Exempel

| Exempel | Roll | Relation | Sekretess | Förväntat resultat |
|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Ja | Begränsad information visas |

### Öppna frågor

- Vilka fält ingår i begränsad information?
- Ska nekade åtkomstförsök loggas?

### Tekniska konsekvenser

- Sökresultat behöver kunna visa olika informationsnivåer.
- Loggning behöver kopplas till visning av sekretessmarkerade ärenden.
```

Detta är inte en obligatorisk mall, men ett fungerande arbetsmönster. I kapitel 8 fördjupar vi hur dokumentationen kan göras läsbar för både verksamhet och IT.

## Att hålla verksamheten kvar i dokumentationen

Ett av de vanligaste problemen när SBE införs är att dokumentationen snabbt blir IT-dominerad. Scenarier skrivs i tekniska format, exempelvärden blir abstrakta och verksamhetens representanter slutar läsa.

För att undvika det bör specifikationen:

- använda verksamhetens termer,
- visa realistiska situationer,
- separera tekniska konsekvenser från verksamhetsregler,
- undvika tekniska fält- och tabellnamn i huvudspecifikationen,
- ha korta förklaringar av varför regeln finns,
- visa öppna frågor på ett sätt som verksamheten kan besvara.

Det betyder inte att IT-perspektivet ska tonas ned. Tvärtom. IT behöver specifikationen för att förstå design, integrationer, testdata och tekniska risker. Men dessa detaljer bör inte förstöra den gemensamma läsbarheten.

## Att göra specifikationen användbar för IT

För IT blir SBE-specifikationen användbar när den visar:

- vilka regler som styr systembeteendet,
- vilka exempel som definierar viktiga fall,
- vilka undantag som måste hanteras,
- vilka öppna frågor som påverkar design,
- vilka tekniska konsekvenser som följer av verksamhetsreglerna.

Ett exempel:

Verksamhetsregel:

> Alla visningar av sekretessmarkerade ärenden ska loggas.

Tekniska konsekvenser:

- Systemet behöver skilja mellan sökträff, förhandsvisning och öppnad detaljvy.
- Loggposten behöver innehålla användare, ärende, tidpunkt och typ av visning.
- Det behöver vara tydligt om en nekad sökning ska loggas som åtkomstförsök eller inte.
- Loggningen får inte bero på att användaren klickar vidare till detaljvyn om sökresultatet redan visar känslig information.

Här hjälper SBE-specifikationen IT att upptäcka designfrågor utan att verksamhetsregeln förvandlas till teknisk implementation.

## Exempel som inte bör automatiseras direkt

Eftersom SBE ofta kopplas till automatiserade tester kan det vara lockande att snabbt fråga: “Kan vi automatisera det här?”. Det är en rimlig fråga, men den bör inte komma först.

Vissa exempel är bäst som analys- eller granskningsunderlag innan de blir automatiserade. Det gäller särskilt när:

- regeln fortfarande är osäker,
- användargränssnittet inte är beslutat,
- datamodellen är under förändring,
- exemplet kräver komplex testdata,
- verksamheten ännu inte har bekräftat språk och begrepp.

Automatisering av oklara exempel kan skapa falsk trygghet. Man får ett test som går grönt, men det betyder bara att ett oklart antagande har kodats.

## Från specifikation till testbarhet

När en regel och dess exempel är stabila kan teamet bedöma testbarhet. Då kan exemplen användas som grund för:

- manuella acceptanstester,
- automatiserade acceptanstester,
- domännära enhetstester,
- integrationstester,
- regressionstester,
- granskningschecklistor.

Alla exempel behöver inte bli automatiserade acceptanstester. Vissa exempel är främst till för att skapa förståelse. Andra är så centrala att de bör finnas i regressionstest. Ytterligare andra bör testas på lägre teknisk nivå.

Det viktiga är att inte tappa spårbarheten mellan verksamhetsregeln, exemplen och de tester som faktiskt används.

## Vanliga misstag

- **Misstag: Att kalla allt för scenarier.**
  - Varför det händer: Gherkin och BDD har gjort scenarioformatet välkänt.
  - Hur du undviker det: Börja med regel och exempel. Använd scenario när händelseförloppet är viktigt.

- **Misstag: Att skriva tekniska tester i verksamhetens specifikation.**
  - Varför det händer: Teamet vill snabbt komma till automatisering.
  - Hur du undviker det: Separera verksamhetsscenario från tekniskt testscenario.

- **Misstag: Att ha för få exempel.**
  - Varför det händer: Regeln verkar självklar när den diskuteras på hög nivå.
  - Hur du undviker det: Lägg alltid till minst ett undantag eller gränsfall.

- **Misstag: Att ha för många exempel.**
  - Varför det händer: Gruppen försöker täcka alla tänkbara kombinationer.
  - Hur du undviker det: Välj exempel som förklarar regeln, visar gränser och prövar viktiga undantag.

- **Misstag: Att blanda öppna frågor med beslutade regler.**
  - Varför det händer: Man vill att dokumentationen ska se färdig ut.
  - Hur du undviker det: Ha en tydlig sektion för öppna frågor och uppdatera regeln när frågan är besvarad.

- **Misstag: Att använda orealistiska exempelvärden.**
  - Varför det händer: Det känns snabbt och neutralt att skriva User1 och Case1.
  - Hur du undviker det: Använd fiktiva men verksamhetsnära namn, roller och ärendenummer.

## Övningar

### Övning 1: Dela upp ett krav i regel, exempel och scenario

Utgå från följande krav:

> Systemet ska tillåta att ett avslutat ärende återöppnas om det finns ett giltigt beslut.

Gör följande:

1. Skriv en verksamhetsregel.
2. Skapa en exempeltabell med minst fyra rader.
3. Skriv ett scenario där en förundersökningsledare återöppnar ett ärende.
4. Lista minst två öppna frågor.

### Övning 2: Välj tabell eller scenario

För varje område nedan, avgör om du först skulle använda tabell, scenario eller båda:

| Område | Tabell, scenario eller båda? | Motivering |
|---|---|---|
| Behörighet till sekretessmarkerat ärende |  |  |
| Skapa ny uppgift i ett ärende |  |  |
| Statusövergång från Pågående till Avslutat |  |  |
| Validering av obligatoriska fält |  |  |
| Loggning av visning av känslig information |  |  |

### Övning 3: Förbättra ett svagt scenario

Förbättra följande scenario så att det blir mer konkret och verksamhetsnära:

```gherkin
Scenario: Användare ser ärende
  Givet att användaren är behörig
  När användaren söker
  Så visas rätt ärende
```

Försök att:

- ange roll,
- ange relation till ärende,
- ange sökbeteende,
- ange förväntat resultat,
- undvika tekniska detaljer.

### Fördjupning

Välj ett krav från ett eget projekt där ni idag använder acceptanskriterier. Skriv om det som:

- syfte,
- regler,
- exempel,
- scenario,
- öppna frågor,
- tekniska konsekvenser.

Granska sedan om verksamheten skulle kunna läsa och bekräfta specifikationen utan att få den förklarad muntligt.

## Snabb sammanfattning

- En regel beskriver vad som ska gälla.
- Ett exempel visar vad regeln betyder i en konkret situation.
- Ett scenario visar beteende över tid eller genom interaktion.
- Tabeller passar bra när flera villkor och utfall ska jämföras.
- Scenarier passar bra när ordning, användarhandlingar och systemreaktioner är viktiga.
- Bra exempel skapar precision, men kan också synliggöra öppna frågor.
- SBE-dokumentation ska vara läsbar för verksamheten och användbar för IT.
- Alla exempel behöver inte automatiseras, men stabila exempel kan vara en stark grund för testbarhet.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan en regel och ett exempel?
2. När är en tabell ofta bättre än ett scenario?
3. Varför kan ett Gherkin-scenario fortfarande vara otydligt?
4. Vad är risken med att automatisera exempel för tidigt?
5. Hur kan tekniska konsekvenser dokumenteras utan att verksamhetsspecifikationen blir teknisk?
6. Vilka exempeltyper skulle du använda för att pröva en behörighetsregel?
7. Hur kan öppna frågor göras synliga i en SBE-specifikation?

## Koppling till bokens röda tråd

Regel, exempel och scenario är inte tre konkurrerande dokumentationsformer. De fungerar bäst när de svarar på olika frågor: regeln förklarar principen, exemplet prövar förståelsen och scenariot visar ett observerbart beteende. Den uppdelningen används i senare kapitel när dokumentation, test och kvalitetsgranskning kopplas ihop.


## Nästa steg

Nu har vi fördjupat hantverket kring regler, exempel och scenarier. Nästa kapitel tar upp dokumentationsstrukturen mer samlat: hur man skapar en SBE-dokumentation som verksamheten faktiskt kan läsa och som IT samtidigt kan använda för utveckling, test, arkitektur och förvaltning.
