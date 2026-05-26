# Kapitel 1: Varför traditionellt kravarbete inte alltid räcker

## Varför detta kapitel finns

Erfarna kravanalytiker vet redan att kravarbete sällan misslyckas för att någon glömde att skriva en mening i ett dokument. Det misslyckas oftare för att olika personer läser samma mening och drar olika slutsatser.

En verksamhetsrepresentant kan läsa ett krav och tänka på den vanliga arbetsdagen. En utvecklare kan läsa samma krav och tänka på datamodell, gränssnitt och felhantering. En testare kan läsa det och undra vilka varianter som behöver verifieras. En arkitekt kan se risker kopplade till säkerhet, integration eller spårbarhet. Alla kan ha läst rätt, men ändå förstått olika saker.

Det är här traditionellt kravarbete ofta når sin gräns. Textuella krav och acceptanskriterier kan vara nödvändiga, men de räcker inte alltid för att skapa gemensam förståelse. De kan beskriva vad systemet ska göra, men lämna för mycket utrymme för antaganden om hur regeln fungerar i verkliga situationer.

I den här boken använder vi Specification by Example, SBE, som ett sätt att minska det glappet. Vi börjar inte med verktyg, testautomation eller Gherkin. Vi börjar med problemet: varför välskriven kravtext ändå kan leda till fel system.

## Lärandemål

Efter kapitlet ska du kunna:

- Förklara varför traditionell kravtext ofta skapar tolkningsutrymme även när den verkar tydlig.
- Identifiera vanliga mönster där acceptanskriterier blir för abstrakta, för tekniska eller för lösningsnära.
- Se skillnaden mellan att dokumentera krav och att skapa gemensam förståelse.
- Känna igen dubbeldokumentation mellan krav, testfall, designbeskrivningar och användarstöd.
- Analysera ett traditionellt krav och hitta vilka exempel som saknas.

## Innan vi börjar

Det här kapitlet utgår från att du redan kan grunderna i kravarbete. Du är sannolikt van vid att skriva krav, acceptanskriterier, användarberättelser, processbeskrivningar, informationsmodeller eller annan kravdokumentation. Du har kanske arbetat med formuleringar som “systemet ska”, “användaren ska kunna” eller “givet att, när, så ska”.

SBE ersätter inte allt detta. Det viktiga är att förstå när traditionella arbetssätt behöver kompletteras eller förändras.

Ett återkommande tema i kapitlet är att krav inte bara är dokumentation. Krav är också ett sätt att skapa samordning mellan människor. Om dokumentationen inte hjälper människor att fatta samma beslut i konkreta situationer är den inte tillräckligt användbar, oavsett hur välformulerad den ser ut.

## Ett till synes tydligt krav

Vi börjar med ett exempel från bokens genomgående case: ett brottsutredningsstöd inom en myndighet.

Anta att ett team får följande krav:

> En utredare ska kunna söka efter utredningsärenden och se ärenden som utredaren har behörighet till.

Vid första anblick kan kravet se rimligt ut. Det säger vem som gör något, vad användaren ska kunna göra och att behörighet ska påverka resultatet. Det är inte ovanligt att ett sådant krav kompletteras med acceptanskriterier:

- Utredaren kan söka på ärendenummer.
- Utredaren kan söka på personnummer.
- Sökresultatet visar endast ärenden som utredaren har behörighet till.
- Om inga ärenden hittas visas ett meddelande.
- Sökningen loggas.

Detta är bättre än en ensam kravmening. Ändå finns flera frågor kvar:

- Vad betyder “har behörighet till”?
- Ska utredaren se ärenden från sin organisatoriska enhet?
- Ska utredaren se ärenden som hen själv är tilldelad?
- Ska en förundersökningsledare se fler ärenden än en utredare?
- Ska sökresultatet visa att det finns träffar som användaren saknar behörighet till?
- Ska känsliga eller sekretessbelagda ärenden döljas helt eller visas med begränsad information?
- Ska alla sökningar loggas, även när inga resultat visas?
- Ska loggningen omfatta sökord, träffar, öppnade ärenden eller endast själva sökhändelsen?

Kravet var inte fel. Acceptanskriterierna var inte heller fel. Problemet är att de lämnade viktiga verksamhetsbeslut otydliga.

## Tolkningsutrymme är inte ett skrivproblem

När krav blir missförstådda är den spontana lösningen ofta att skriva mer text. Kravet görs längre. Acceptanskriterierna kompletteras. Ett avsnitt med förtydliganden läggs till. Ibland skrivs en regeltext, en tabell, en processbild och ett testfall som alla beskriver ungefär samma sak.

Mer text kan hjälpa, men bara om texten minskar rätt osäkerhet. Ofta händer något annat: dokumentationen blir större, men tolkningsutrymmet består.

Tolkningsutrymme uppstår när en formulering kräver att läsaren fyller i detaljer med egna antaganden. I kravarbete är det särskilt vanligt kring ord som:

- behörig
- relevant
- aktuell
- normal
- giltig
- komplett
- rimlig
- känslig
- prioriterad
- standardmässig
- vid behov

Orden är inte förbjudna. De behövs ofta. Men de är varningssignaler. De pekar på regler som behöver konkretiseras.

I brottsutredningsstödet kan ordet “behörig” till exempel betyda flera olika saker:

- Användaren tillhör samma organisatoriska enhet som ärendet.
- Användaren är tilldelad ärendet.
- Användaren har en särskild roll.
- Användaren har fått tillfällig åtkomst.
- Användaren får se ärendets metadata men inte innehållet.
- Användaren får se ärendet men inte vissa bilagor.
- Användaren får söka fram ärendet men måste motivera åtkomst innan det öppnas.

En traditionell kravtext kan försöka räkna upp allt detta. Men utan konkreta exempel är det fortfarande lätt att missa kombinationer och undantag.

## När acceptanskriterier blir för abstrakta

Acceptanskriterier är ofta ett steg i rätt riktning. De gör krav mer testbara och kan hjälpa teamet att förstå när något är klart. Men de kan också bli en ny form av abstrakt kravtext.

Titta på följande acceptanskriterium:

> Sökresultatet ska respektera gällande behörighetsregler.

Det är testbart bara om “gällande behörighetsregler” finns tydligt definierade någon annanstans. Om reglerna är oklara skjuts problemet bara vidare.

Ett annat exempel:

> Användaren ska få ett tydligt felmeddelande vid ogiltig sökning.

Här finns flera öppna frågor. Vad räknas som ogiltig sökning? Är ett tomt sökfält ogiltigt? Är ett felaktigt formaterat personnummer ogiltigt? Är en sökning på ett personnummer som inte finns ogiltig, eller är det en giltig sökning utan träff? Vad är ett tydligt felmeddelande för en erfaren utredare?

Acceptanskriterier kan alltså vara för generella, även när de är skrivna i ett känt format. Formen löser inte problemet. Det gör däremot bra exempel.

## När acceptanskriterier blir för lösningsnära

Det motsatta problemet är att acceptanskriterierna blir för tekniska eller för lösningsnära. Då beskriver de hur systemet ska byggas snarare än vilket beteende verksamheten behöver.

Exempel:

> Sökningen ska anropa behörighetstjänsten innan databasanropet genomförs.

Detta kan vara ett viktigt design- eller arkitekturbeslut, men det är inte nödvändigtvis ett bra funktionellt krav på verksamhetsnivå. Verksamheten behöver veta att obehöriga ärenden inte visas. IT behöver veta hur det ska implementeras säkert och effektivt. Test behöver veta vilka situationer som ska verifieras. Om allt blandas i samma acceptanskriterium blir dokumentationen svår att använda för alla.

En central utmaning i SBE är därför att hålla isär:

- verksamhetsregel
- konkret exempel
- teknisk lösning
- teststrategi
- öppna frågor

När detta blandas ihop får verksamheten dokumentation som känns teknisk och svår att granska. IT får dokumentation som kan vara full av verksamhetsord men sakna precision. Test får något som verkar testbart men saknar tydliga varianter.

## Gemensam förståelse är inte samma sak som godkänd dokumentation

Ett kravdokument kan vara granskat, kommenterat, versionshanterat och formellt godkänt utan att alla berörda faktiskt har samma förståelse.

Det märks ofta först senare:

- Utvecklaren gör en rimlig tolkning som verksamheten inte förväntade sig.
- Testaren hittar ett gränsfall som ingen beslutat om.
- Produktägaren prioriterar en funktion utan att se att en regel påverkar flera andra flöden.
- Förvaltningen upptäcker att dokumentationen inte går att använda för felsökning eller vidareutveckling.
- Verksamheten godkänner ett gränssnitt men reagerar när systemets beteende provas med realistiska exempel.

Formellt godkännande är viktigt i många organisationer, särskilt i myndighetsmiljö. Men det bör inte förväxlas med gemensam förståelse.

SBE utgår från att gemensam förståelse skapas genom samtal om konkreta exempel. Dokumentationen blir resultatet av den förståelsen, inte en ersättning för den.

## Dokumentationsglappet mellan verksamhet och IT

I många organisationer uppstår ett glapp mellan dokumentation som verksamheten kan förstå och dokumentation som IT kan använda.

Verksamhetsnära dokumentation kan beskriva mål, regler och flöden på ett begripligt sätt, men sakna precision nog för implementation och test. IT-nära dokumentation kan vara exakt, men uttryckt i tekniska strukturer som verksamheten inte kan granska.

Detta leder ofta till flera parallella dokument:

- kravdokument
- acceptanskriterier
- testfall
- designbeskrivningar
- systemdokumentation
- förvaltningsdokumentation
- användarstöd
- beslutade verksamhetsregler

Varje dokument kan vara motiverat. Problemet uppstår när samma regel finns på flera ställen med små skillnader.

I brottsutredningsstödet kan behörighetsregeln till exempel beskrivas i:

- ett verksamhetskrav om vem som får se ärenden
- en informationssäkerhetsbilaga
- ett testfall för sökning
- en teknisk integrationsbeskrivning mot behörighetstjänsten
- ett användarstöd för utredare
- en förvaltningsinstruktion för behörighetsadministration

När regeln ändras måste alla dokument uppdateras. Om ett dokument missas får organisationen dubbeldokumentation: flera versioner av sanningen.

SBE löser inte automatiskt all dubbeldokumentation. Men det erbjuder ett bättre mål: en specifikation som är tillräckligt konkret för IT och test, men fortfarande läsbar och granskbar för verksamheten.

## Ett konkret exempel på glapp

Låt oss återvända till sökfunktionen.

Traditionellt krav:

> En utredare ska kunna söka efter utredningsärenden och se ärenden som utredaren har behörighet till.

Acceptanskriterium:

> Sökresultatet visar endast ärenden som användaren har behörighet till.

Testfall:

> Logga in som utredare. Sök på ärendenummer. Verifiera att endast behöriga ärenden visas.

Alla tre uttrycken pekar åt samma håll, men inget av dem visar vad som faktiskt ska hända i ett konkret fall.

Ett SBE-inspirerat exempel kan i stället börja så här:

| Situation | Användare | Ärende | Relation till ärende | Förväntat sökresultat |
|---|---|---|---|---|
| Utredare söker ärende i egen enhet | Utredare A | Ärende 1001 | Samma enhet | Ärendet visas |
| Utredare söker tilldelat ärende i annan enhet | Utredare A | Ärende 1002 | Tilldelad ärendet | Ärendet visas |
| Utredare söker ärende utan relation | Utredare A | Ärende 1003 | Ingen relation | Ärendet visas inte |
| Förundersökningsledare söker ärende i sin grupp | Ledare B | Ärende 1004 | Ansvarig grupp | Ärendet visas |
| Utredare söker sekretessmarkerat ärende med tilldelning | Utredare A | Ärende 1005 | Tilldelad men sekretessmarkerat | Begränsad information visas |

Tabellen är inte färdig specifikation. Den väcker snarare bättre frågor:

- Vad innebär “begränsad information”?
- Ska användaren se att ett ärende finns men inte kunna öppna det?
- Ska sekretessmarkering trumfa tilldelning?
- Vilka av dessa situationer behöver loggas extra tydligt?
- Behöver behörighetsmotivering krävas i vissa fall?
- Är reglerna olika för sökning och öppning av ärende?

Det är just poängen. Bra exempel avslöjar beslut som abstrakt kravtext döljer.

## Krav som ser klara ut men inte är beslutade

Ett vanligt mönster i traditionellt kravarbete är att dokumentationen låter mer beslutad än den faktiskt är. Formuleringar som “systemet ska hantera behörighet” eller “sökresultatet ska filtreras enligt regelverket” kan få en funktion att se färdigdefinierad ut, trots att de viktigaste besluten återstår.

SBE gör detta synligt. När teamet försöker formulera konkreta exempel blir luckorna tydliga.

Det kan kännas obekvämt. En erfaren kravanalytiker kan vara van vid att leverera strukturerade, välformulerade krav. SBE kan initialt upplevas som att kraven blir mer röriga, eftersom fler frågor kommer upp tidigare.

Men det är bättre att upptäcka osäkerhet i kravarbete än i systemtest, inför driftsättning eller i produktion.

## Det farliga med “alla förstår”

I en verksamhet med stark domänkunskap finns ofta begrepp som alla tror sig förstå. Det kan gälla “ärende”, “åtgärd”, “behörighet”, “sekretess”, “status”, “komplettering”, “avslut” eller “granskning”.

Problemet är att begreppen ofta betyder olika saker i olika sammanhang.

I brottsutredningsstödet kan “ärende” exempelvis användas för:

- en formell utredning
- en intern arbetsyta
- en registrerad händelse
- ett samlingsobjekt för dokument och åtgärder
- ett objekt i ett annat system som speglas in

Om kravet säger “sök efter ärende” men olika personer menar olika sak med ärende, hjälper det inte att acceptanskriteriet är korrekt formulerat. Teamet behöver exempel som visar vilka objekt som ska sökas fram i vilka situationer.

SBE tvingar inte organisationen att skapa perfekta begreppsmodeller innan arbetet börjar. Däremot gör exemplen det lättare att upptäcka när begreppen glider.

## När kravdokumentation blir en överlämning i stället för ett arbetsredskap

Traditionell kravdokumentation används ofta som överlämning. Kravanalytikern samlar in information, skriver dokumentation, får den granskad och lämnar vidare till utveckling och test.

Det kan fungera när domänen är stabil, reglerna är enkla och risken för missförstånd är låg. Men i komplexa verksamheter blir överlämningen ofta en svag punkt. Den som tar emot dokumentationen behöver ändå ställa följdfrågor, skapa egna exempel och tolka regelverk.

SBE förändrar synen på dokumentationen. Den ska inte bara vara ett kontrakt mellan faser. Den ska vara ett levande arbetsredskap för gemensam förståelse.

Det betyder inte att allt måste automatiseras. Levande dokumentation handlar först om att dokumentationen används, granskas och uppdateras som en del av arbetet. Automation kan förstärka detta, men den ersätter inte samtalet.

## Vad traditionellt kravarbete fortfarande är bra på

Det vore fel att säga att traditionellt kravarbete är dåligt. Tvärtom finns många saker som textuell kravdokumentation gör bra.

Traditionell kravtext kan vara bra för att:

- beskriva syfte och bakgrund
- formulera övergripande mål
- dokumentera avgränsningar
- beskriva ansvar och roller
- sammanfatta regelverk
- fånga icke-funktionella krav på hög nivå
- dokumentera beslut och motiveringar
- ge kontext till exempel och scenarier

SBE innebär alltså inte att all kravtext ska ersättas med tabeller, Gherkin-scenarier eller automatiserade tester. En mogen SBE-specifikation innehåller ofta både förklarande text, regler, exempel, öppna frågor och ibland körbara scenarier.

Skillnaden är att texten inte får stå ensam där konkret beteende behöver förstås.

## Ett mönster: från påstående till prövbar situation

En användbar tumregel är att många traditionella krav är påståenden. SBE hjälper oss att göra dem till prövbara situationer.

Traditionellt påstående:

> Endast behöriga användare ska kunna se känsliga ärendeuppgifter.

Prövbara situationer:

- En tilldelad utredare öppnar ett ärende utan sekretessmarkering.
- En tilldelad utredare öppnar ett sekretessmarkerat ärende.
- En utredare i samma enhet men utan tilldelning söker efter ärendet.
- En förundersökningsledare granskar ärendet.
- En administratör ser ärendets metadata men inte innehåll.
- En användare med tillfällig behörighet öppnar ärendet efter motivering.

Varje situation kan leda till ett exempel. Varje exempel kan avslöja en regel eller ett undantag. Tillsammans skapar de en specifikation som är lättare att diskutera än en abstrakt formulering.

## Vanliga misstag

- **Misstag: Att tro att mer kravtext automatiskt skapar mer tydlighet.**
  - Varför det händer: När ett krav missförstås är det naturligt att vilja skriva mer.
  - Hur du undviker det: Lägg till konkreta exempel innan du lägger till mer allmän text.

- **Misstag: Att formulera acceptanskriterier som nya abstrakta krav.**
  - Varför det händer: Teamet använder ett kravformat men fyller det med samma otydliga begrepp som tidigare.
  - Hur du undviker det: Kontrollera om kriteriet går att pröva med en konkret situation.

- **Misstag: Att blanda verksamhetsregel, teknisk lösning och testfall.**
  - Varför det händer: Alla perspektiv behövs, men de hamnar i samma dokumentationsyta.
  - Hur du undviker det: Dela upp dokumentationen i regel, exempel, tekniska kommentarer och öppna frågor.

- **Misstag: Att se SBE som ett verktygsval.**
  - Varför det händer: SBE kopplas ofta till BDD, Gherkin, Cucumber eller andra verktyg.
  - Hur du undviker det: Börja med exempel och gemensam förståelse. Verktyg kommer senare.

- **Misstag: Att vänta med svåra frågor till testfasen.**
  - Varför det händer: Abstrakta krav kan se färdiga ut även när detaljerna saknas.
  - Hur du undviker det: Använd exempel tidigt för att synliggöra beslut, undantag och gränsfall.

## Övningar

### Övning 1: Hitta tolkningsutrymmet

Utgå från följande krav:

> Systemet ska visa relevanta ärenden för användaren baserat på roll och behörighet.

Identifiera minst fem ord eller formuleringar som kan tolkas olika. Skriv sedan om kravet som frågor som behöver besvaras.

Exempel på start:

- Vad betyder “relevanta”?
- Vilka roller finns?
- Är roll och behörighet samma sak eller olika saker?

### Övning 2: Gör kravet konkret

Utgå från samma krav och skapa fem konkreta situationer. Varje situation ska innehålla:

- användare
- roll
- relation till ärendet
- eventuell särskild markering
- förväntat resultat

Försök att få med både normalfall och undantag.

### Övning 3: Identifiera dubbeldokumentation

Tänk på ett kravområde du själv har arbetat med. Lista vilka dokument eller artefakter som beskrev samma regel.

Exempel:

- kravspecifikation
- acceptanskriterier
- testfall
- processbeskrivning
- användarstöd
- teknisk dokumentation

Markera sedan var risken var störst för att dokumenten skulle börja säga olika saker.

### Fördjupning

Välj ett traditionellt krav från ett tidigare projekt. Svara på följande frågor:

1. Vilka antaganden behövde läsaren göra för att förstå kravet?
2. Vilka exempel hade kunnat minska tolkningsutrymmet?
3. Vilka frågor upptäcktes sent i projektet?
4. Hade de frågorna kunnat upptäckas tidigare genom exempel?

## Snabb sammanfattning

- Traditionell kravtext kan vara korrekt men ändå lämna för stort tolkningsutrymme.
- Acceptanskriterier hjälper, men kan själva bli abstrakta om de inte kopplas till konkreta situationer.
- Målet är inte bara godkänd dokumentation utan gemensam förståelse.
- Dubbeldokumentation uppstår när samma regel beskrivs i flera artefakter med små skillnader.
- SBE hjälper teamet att gå från påståenden till prövbara exempel.
- Verktyg och automation är sekundära i början. Det första steget är bättre samtal om konkreta exempel.

## Quiz/reflektionsfrågor

1. Varför kan ett krav vara formellt godkänt men ändå inte skapa gemensam förståelse?
2. Vilka ord i kravtext brukar signalera risk för tolkningsutrymme?
3. Vad är skillnaden mellan ett abstrakt acceptanskriterium och ett konkret exempel?
4. Varför kan dubbeldokumentation bli ett problem i förvaltning?
5. När bör traditionell kravtext behållas även i ett SBE-arbetssätt?

## Koppling till bokens röda tråd

Det centrala problemet i kapitlet är inte att kravanalytiker skriver för dåligt, utan att traditionell dokumentation ofta bär för mycket implicit kunskap. I resten av boken återkommer därför samma fråga: hur gör vi beslutslogik, undantag och förväntat systembeteende tillräckligt konkreta för att både verksamhet och IT ska kunna använda samma underlag?


## Nästa steg

I det här kapitlet har vi sett varför traditionellt kravarbete ofta behöver kompletteras. Nästa kapitel går vidare med vad SBE är och inte är. Där skiljer vi mellan SBE som arbetssätt, BDD som samarbetspraktik, Gherkin som format och verktyg som Cucumber och Concordion. Målet är att placera SBE rätt innan vi börjar använda det praktiskt i caset.
