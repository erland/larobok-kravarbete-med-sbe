# Kapitel 11: Samspel mellan krav, test och utveckling

## Varför detta kapitel finns

I de tidigare kapitlen har vi byggt upp en SBE-dokumentation som kan förstås av verksamheten och användas av IT. Vi har också tittat på Gherkin, Cucumber och Concordion som möjliga format och verktyg. Nästa fråga är därför inte bara hur scenarier skrivs, utan hur de faktiskt används i samarbetet mellan krav, test och utveckling.

I många organisationer finns en tydlig kedja:

- verksamheten beskriver behov
- kravanalytikern skriver krav
- testare tolkar kraven och skapar testfall
- utvecklare implementerar utifrån krav och kompletterande dialog
- fel och oklarheter upptäcks sent

SBE förändrar den kedjan. Det betyder inte att alla roller försvinner eller att alla gör samma sak. Det betyder att exempel blir en gemensam arbetsyta där rollerna möts tidigare. Kravanalytikern formulerar inte längre enbart text som andra ska tolka. Testaren väntar inte enbart på färdiga krav. Utvecklaren behöver inte gissa vad som menas med ett undantag. Verksamheten får inte bara godkänna en formulering, utan kan pröva om konkreta exempel stämmer med verkligheten.

Det här kapitlet handlar om hur det samspelet kan se ut i praktiken. Vi använder fortfarande caset med brottsutredningsstödet, särskilt kring sökning, behörighet, statusövergångar och loggning. Fokus ligger på funktionella krav, men kapitlet visar också hur krav, test och utveckling kan samarbeta när ett exempel har tekniska konsekvenser.

## Lärandemål

Efter kapitlet ska du kunna:

- beskriva hur SBE förändrar relationen mellan krav, test och utveckling
- använda exempel som gemensam arbetsyta i stället för överlämningsdokument
- skilja mellan kravexempel, testfall, automatiserat test och teknisk implementation
- identifiera vad testare, utvecklare och kravanalytiker behöver bidra med i SBE-arbetet
- formulera exempel så att de stödjer både verksamhetsförståelse och testbarhet
- avgöra när ett exempel bör automatiseras och när det bör ligga kvar som dokumentation
- hantera öppna frågor, tekniska konsekvenser och avvikelser utan att tappa den gemensamma förståelsen

## Innan vi börjar

Det här kapitlet bygger på tre tidigare delar av boken.

För det första bygger det på skillnaden mellan traditionell kravtext och exempelbaserad specifikation. Ett exempel är inte bara en mer detaljerad kravformulering. Det är ett sätt att visa hur en regel ska bete sig i en konkret situation.

För det andra bygger det på dokumentationsmodellen från kapitel 8. SBE-dokumentation behöver ofta flera lager: verksamhetsnära sammanhang, regler, exempel, öppna frågor och ibland tekniska kommentarer. Det är särskilt viktigt i samarbetet mellan krav, test och utveckling.

För det tredje bygger det på kapitel 10 om Gherkin, Cucumber och Concordion. Verktyg kan hjälpa, men de löser inte samspelet. Ett dåligt samarbete blir inte bra för att scenarierna skrivs i Gherkin. Ett otydligt krav blir inte tydligt för att det går att köra automatiskt. SBE:s styrka ligger i den gemensamma preciseringen före och under implementationen.

## Från överlämning till gemensam arbetsyta

Ett vanligt traditionellt mönster är att kravarbete behandlas som en överlämning. Kravanalytikern samlar in information, skriver krav, får dem godkända och lämnar vidare. Testare och utvecklare läser sedan dokumentationen och tolkar vad den betyder.

Det här kan fungera för enkla krav. Men i komplexa domäner leder det ofta till problem:

- Kravtexten beskriver normalfallet men inte undantagen.
- Acceptanskriterierna är formellt korrekta men för abstrakta.
- Testaren hittar gränsfall som aldrig diskuterats med verksamheten.
- Utvecklaren gör tekniska antaganden som inte syns i dokumentationen.
- Verksamheten godkänner krav utan att ha sett konkreta konsekvenser.
- Fel upptäcks först när lösningen demonstreras eller testas sent.

SBE försöker bryta detta genom att göra exemplen till en gemensam arbetsyta. Det innebär att ett krav inte betraktas som färdigpreciserat förrän viktiga beteenden har konkretiserats med exempel som flera roller kan förstå och granska.

I brottsutredningsstödet kan en traditionell formulering vara:

> En utredare ska kunna se ärenden som utredaren har behörighet till.

Det verkar tydligt. Men för test och utveckling är det för oprecist. Vad betyder behörighet? Är det organisatorisk tillhörighet? Ärendetilldelning? Tillfällig delegation? Särskild läsbehörighet? Sekretessmarkering? Vad händer om användaren har flera roller? Vad loggas? Vad visas i sökresultatet?

I SBE blir arbetet i stället att samla rollerna kring konkreta situationer:

| Exempel-ID | Situation | Användare | Relation till ärende | Sekretess | Förväntat resultat |
|---|---|---|---|---|---|
| EX-11-01 | Utredare söker ärende i egen enhet | Utredare A | Samma enhet | Nej | Ärendet visas |
| EX-11-02 | Utredare söker tilldelat ärende i annan enhet | Utredare A | Tilldelad | Nej | Ärendet visas |
| EX-11-03 | Utredare söker ärende utan relation | Utredare A | Ingen relation | Nej | Ärendet visas inte |
| EX-11-04 | Utredare söker sekretessmarkerat ärende i egen enhet | Utredare A | Samma enhet | Ja | Ärendet visas bara om särskild behörighet finns |
| EX-11-05 | Förundersökningsledare söker ärende i sin grupp | Ledare B | Ansvarig grupp | Nej | Ärendet visas |

Tabellen är inte bara testdata. Den är en diskussionsyta. Verksamheten kan säga om exemplen stämmer. Testaren kan se vad som behöver verifieras. Utvecklaren kan se vilka regler som behöver implementeras. Kravanalytikern kan se vilka begrepp som behöver definieras.

## Rollernas bidrag i SBE-arbetet

SBE betyder inte att kravanalytikern, testaren och utvecklaren får identiska roller. Däremot behöver rollerna bidra tidigare och mer sammanflätat.

### Kravanalytikerns bidrag

Kravanalytikerns viktigaste bidrag är att hålla ihop förståelsen. Det handlar om att:

- formulera verksamhetsregler så att de är begripliga
- få fram konkreta exempel från rätt personer
- identifiera luckor, undantag och öppna frågor
- se till att dokumentationen går att läsa av både verksamhet och IT
- hålla ordning på begrepp, regler och exempel
- säkerställa att dokumentationen inte blir en teknisk testsamling

I SBE är kravanalytikern inte bara den som skriver. Rollen blir mer faciliterande och kuraterande. Kravanalytikern hjälper gruppen att skapa en specifikation som är gemensam, prövbar och underhållbar.

### Testarens bidrag

Testaren bidrar med ett särskilt sätt att tänka kring variation, täckning och observerbart beteende. Det handlar om att:

- hitta gränsfall och negativa exempel
- skilja på vad som ska verifieras manuellt och automatiskt
- bedöma om exemplen ger tillräcklig testtäckning
- upptäcka tvetydigheter i förväntat resultat
- föreslå datauppsättningar som gör beteendet prövningsbart
- se risker i att bara testa normalflöden

I brottsutredningsstödet kan testaren exempelvis fråga:

- Vad händer om en utredare tillhör två organisatoriska enheter?
- Vad händer om ett ärende byter enhet medan användaren är inloggad?
- Vad händer om delegation har gått ut?
- Vad händer om sökresultatet innehåller både öppna och sekretessmarkerade ärenden?
- Ska loggning ske även när ärendet inte visas?

Det här är inte testfrågor som bör vänta till testfasen. Det är kravfrågor som behöver hanteras medan regeln fortfarande formas.

### Utvecklarens bidrag

Utvecklaren bidrar med förståelse för implementation, systemgränser och tekniska konsekvenser. Det handlar om att:

- identifiera vilka regler som påverkar domänmodell, tjänster, API:er eller datalager
- se om ett exempel kräver information som systemet inte har
- upptäcka beroenden till andra system
- föreslå enklare eller mer robusta lösningsalternativ
- bedöma vad som är rimligt att automatisera
- identifiera när ett krav behöver brytas ner

I SBE ska utvecklaren inte ta över verksamhetsregeln och göra den teknisk för tidigt. Men utvecklarens frågor är avgörande för att exemplen ska vara genomförbara.

Ett exempel:

> Om en utredare har tillfällig delegation ska ärendet visas.

Utvecklaren kan behöva fråga:

- Var finns delegation registrerad?
- Har delegation en start- och sluttid?
- Gäller delegation för alla ärenden eller ett specifikt ärende?
- Ska behörigheten beräknas vid söktillfället eller cachelagras?
- Vad händer om delegationen återkallas efter att sökresultatet har visats?

Det här är inte tekniska sidospår. De kan avgöra hur regeln ska förstås.

### Verksamhetens bidrag

Verksamheten bidrar med domänkunskap, avsikt och prioritering. Det handlar om att:

- bekräfta om exemplen speglar verkliga arbetssituationer
- förklara varför regeln finns
- prioritera vilka undantag som måste hanteras
- avgöra vad som är acceptabelt beteende i oklara situationer
- identifiera juridiska, organisatoriska eller processmässiga begränsningar

I myndighetsmiljö är verksamhetens bidrag särskilt viktigt eftersom regler ofta har både praktiska och formella motiv. En åtkomstregel kan handla om effektivitet, sekretess, rättssäkerhet och spårbarhet samtidigt.

## Kravexempel är inte samma sak som testfall

En av de vanligaste missuppfattningarna i SBE är att exempel automatiskt blir testfall. Det kan de bli, men de är inte samma sak.

Ett kravexempel visar hur verksamhetsregeln ska bete sig i en konkret situation. Det ska vara begripligt för verksamheten och hjälpa flera roller att förstå vad som avses.

Ett testfall beskriver hur ett beteende ska verifieras. Det kan innehålla testdata, testmiljö, steg, förväntade observationer och ibland detaljer om förberedelser och återställning.

Ett automatiserat test är kod eller verktygskonfiguration som kan köras för att kontrollera ett beteende.

En teknisk implementation är den lösning som får systemet att bete sig enligt regeln.

Dessa nivåer bör kopplas ihop, men inte blandas samman.

| Nivå | Syfte | Primär målgrupp | Exempel |
|---|---|---|---|
| Kravexempel | Förklara önskat beteende | Verksamhet, krav, test, utveckling | Utredare utan relation till ärende ser inte ärendet |
| Testfall | Verifiera beteendet | Testare, team | Skapa ärende, användare och relation. Kör sökning. Kontrollera resultat |
| Automatiserat test | Kontrollera beteendet upprepbart | Team, CI/CD, förvaltning | Cucumber-scenario eller integrationstest |
| Implementation | Skapa beteendet i systemet | Utvecklare | Behörighetskontroll i söktjänst |

När nivåerna blandas ihop blir dokumentationen ofta svår att använda. Verksamheten kan inte läsa testdetaljerna. Testare får otydliga regler. Utvecklare får scenarier som beskriver klickvägar i stället för domänbeteende. Kravanalytikern förlorar överblicken över vad som faktiskt är beslutat.

## Exempel som bro mellan analys och testdesign

Ett bra SBE-exempel är tillräckligt konkret för att testaren ska kunna se hur det kan verifieras, men inte så tekniskt att verksamheten slutar känna igen sitt arbete.

Ta regeln:

> En utredare får se ett ärende om utredaren tillhör ärendets ansvariga enhet eller har tilldelats ärendet.

En verksamhetsnära exempeltabell kan se ut så här:

| Exempel-ID | Användare | Ärendets enhet | Användarens enhet | Tilldelad ärendet | Förväntat resultat |
|---|---|---|---|---|---|
| EX-11-06 | Utredare A | Grova brott | Grova brott | Nej | Ärendet visas |
| EX-11-07 | Utredare B | Grova brott | Bedrägeri | Ja | Ärendet visas |
| EX-11-08 | Utredare C | Grova brott | Bedrägeri | Nej | Ärendet visas inte |

Testaren kan sedan härleda testfall från tabellen, men testfallet kan behöva mer detaljer:

- vilken testanvändare som används
- hur ärendet skapas
- vilken sökterm som används
- vilket API eller gränssnitt som testas
- hur resultatet kontrolleras
- vilka loggar som ska verifieras
- hur testdata återställs

Det är viktigt att dessa detaljer inte alltid trycks in i kravexemplet. Annars riskerar specifikationen att bli oläslig för verksamheten. En bättre modell är att låta kravexemplet vara stabilt och verksamhetsnära, medan testdesignen länkar till exemplet.

## Exempel som bro mellan analys och utveckling

För utvecklaren fungerar exemplen som konkretisering av regler och acceptabelt beteende. De hjälper utvecklaren att se vad som måste modelleras, vad som är undantag och vilka beslut som inte får gömmas i kod.

Exemplen kan exempelvis visa att behörighet i sökresultat inte är en enkel ja/nej-kontroll. Den kan bero på flera faktorer:

- organisatorisk tillhörighet
- ärendetilldelning
- roll
- delegation
- sekretessmarkering
- tidsbegränsning
- loggningskrav

Om specifikationen bara säger “behörig användare” kan utvecklaren behöva skapa sin egen tolkning. Om specifikationen däremot visar exempel kan utvecklaren modellera regeln mer medvetet.

En utvecklare kan också bidra med tekniska konsekvenser tillbaka till specifikationen:

| Regel eller exempel | Teknisk konsekvens | Behöver beslutas |
|---|---|---|
| Delegation kan vara tidsbegränsad | Behörighetskontroll måste ta hänsyn till tidpunkt | Vilken tid används: aktuell tid eller söktidpunkt? |
| Sekretessmarkerade ärenden kräver särskild behörighet | Sökresultat måste filtreras före presentation | Ska träffantal visa dolda ärenden? |
| Åtkomst ska loggas | Loggning behövs även vid sökning eller bara vid öppning | Vilka händelser ska räknas som åtkomst? |

Den här typen av tekniska konsekvenser ska inte ersätta verksamhetsregeln. Men de behöver synliggöras, eftersom de ofta påverkar både krav, test och förvaltning.

## Samarbetsmönster före implementation

Ett praktiskt sätt att använda SBE är att etablera en återkommande rytm före implementation. Rytmen behöver inte vara tung, men den behöver vara tydlig.

### Förberedelse

Kravanalytikern samlar in preliminära behov, kända regler och öppna frågor. Målet är inte att skriva färdiga krav, utan att ha tillräckligt material för att gruppen ska kunna arbeta konkret.

För brottsutredningsstödet kan förberedelsen innehålla:

- kort beskrivning av användarens mål
- preliminär regel om sökbehörighet
- exempel på ärenden och användarroller
- kända undantag
- frågor om sekretess och loggning
- tidigare acceptanskriterier eller kravtext

### Gemensam precisering

Kravanalytiker, testare, utvecklare och verksamhetsrepresentant går igenom regeln med exempel. Gruppen letar efter normalfall, undantag och gränsfall. Målet är inte att skapa många exempel, utan rätt exempel.

Frågor som brukar hjälpa är:

- Vilket är det enklaste exempel där regeln gäller?
- Vilket är det enklaste exempel där regeln inte gäller?
- Vilket undantag är viktigast?
- Vilket exempel skulle kunna missförstås av IT?
- Vilket exempel skulle kunna missförstås av verksamheten?
- Vilket exempel är kritiskt för rättssäkerhet, säkerhet eller användarnytta?

### Dokumentation

Efter preciseringen dokumenteras regeln, exemplen och öppna frågor. Dokumentationen bör vara tillräckligt ren för att kunna granskas, men inte så polerad att obesvarade frågor döljs.

En bra dokumentationspost kan innehålla:

- regel-ID
- kort verksamhetsregel
- syfte eller motiv
- exempel
- undantag
- öppna frågor
- tekniska konsekvenser
- koppling till test eller automation
- status

### Teamförankring

Innan implementation startar bör teamet ha en gemensam bild av vad som är beslutat och vad som fortfarande är öppet. Det betyder inte att alla frågor måste vara lösta. Men det ska vara tydligt vilka frågor som blockerar implementation och vilka som kan hanteras senare.

### Återkoppling under implementation

När utveckling och test börjar kan nya frågor uppstå. I SBE ska dessa frågor inte hanteras som informella chattbeslut som aldrig når dokumentationen. De bör återföras till specifikationen.

Exempel:

> Utvecklaren upptäcker att systemet inte kan avgöra om en användare tillhör en enhet historiskt, bara aktuell enhet.

Det kan påverka regeln om sökning i äldre ärenden. Då behöver specifikationen uppdateras med ett beslut eller en öppen fråga. Annars kommer den levande dokumentationen snabbt att tappa förtroende.

## Samarbetsmönster under implementation

SBE är inte bara något som sker före utveckling. Under implementation behöver exemplen fortsätta fungera som referenspunkt.

### Använd exemplen i utvecklingsdialogen

När utvecklaren har en fråga bör frågan formuleras mot ett exempel, inte bara mot en lösningsdetalj.

Mindre bra fråga:

> Ska vi lägga behörighetskontrollen i söktjänsten eller i API-gatewayen?

Bättre SBE-fråga:

> I EX-11-04 ska ett sekretessmarkerat ärende inte visas för en utredare utan särskild behörighet. Behöver samma regel gälla redan i söktjänsten så att ärendet inte heller påverkar träffantalet?

Den andra frågan kopplar teknisk design till ett beslutat beteende.

### Låt testdesignen växa ur exemplen

Testaren kan skapa fler tekniska testfall än de exempel som finns i specifikationen. Det är normalt. Men testdesignen bör kunna visa vilken regel eller vilket exempel den stödjer.

Ett kravexempel kan ge upphov till flera tester:

- ett test via användargränssnitt
- ett API-test
- ett integrationstest mot behörighetstjänsten
- ett manuellt utforskande test
- ett test av loggning
- ett test av felhantering

Alla dessa behöver inte stå i kravdokumentationen. Men de bör kunna spåras tillbaka till den regel som motiverar dem.

### Uppdatera specifikationen när beteendet ändras

Om implementationen leder till ett ändrat beslut ska specifikationen uppdateras. Annars uppstår dubbeldokumentation och dokumentationen blir snabbt historisk.

Ett vanligt anti-pattern är att teamet säger:

> Vi vet att dokumentationen inte stämmer, men testerna gör rätt.

Det är farligt i SBE. Om testerna är den enda sanningen blir dokumentationen inte längre en gemensam arbetsyta för verksamhet och IT. Då har organisationen bara flyttat kravinformationen från ett kravdokument till en testsvit.

## Vad ska automatiseras?

Alla exempel ska inte automatiseras. Det är en viktig princip.

Automation är värdefull när exemplen är stabila, viktiga och möjliga att kontrollera på ett tillförlitligt sätt. Automation är mindre lämplig när exemplen fortfarande är utforskande, ofta ändras eller kräver mänsklig bedömning.

### Exempel som ofta lämpar sig för automation

Exempel lämpar sig ofta för automation när de:

- beskriver tydliga regler med förväntat resultat
- kan köras med kontrollerbar testdata
- är viktiga att regressionssäkra
- har stabila begrepp och beslut
- kan verifieras utan subjektiv bedömning
- inte kräver alltför sköra beroenden

I brottsutredningsstödet kan följande vara kandidater:

- filtrering av sökresultat utifrån behörighet
- statusövergångar för ärenden
- obligatoriska fält vid registrering
- regler för delegation
- synlighet för knappar eller åtgärder utifrån roll
- validering av datum eller ärendestatus

### Exempel som ofta bör vänta

Exempel bör ofta vänta med automation när de:

- används för att utforska domänen
- innehåller öppna frågor
- beskriver policy eller riktlinje snarare än systembeteende
- beror på osäkra externa system
- kräver mänsklig bedömning
- skulle bli mycket dyra att automatisera jämfört med nyttan

Exempel kring användbarhet, arbetsflödeskänsla eller stöd för komplex handläggning kan ibland vara bättre som granskningsscenarier än automatiserade tester.

### Beslutsstöd för automation

En enkel modell är att bedöma varje exempel mot fyra frågor:

| Fråga | Om svaret är ja | Om svaret är nej |
|---|---|---|
| Är beteendet beslutat? | Automation kan övervägas | Vänta och använd exemplet för analys |
| Är resultatet observerbart? | Test kan designas tydligt | Förtydliga förväntat resultat |
| Är beteendet viktigt att regressionssäkra? | Automation kan ge hög nytta | Manuell granskning kan räcka |
| Är testet stabilt nog? | Automation kan vara hållbar | Risk för sköra tester |

Det här gör automation till ett medvetet val, inte en automatisk följd av att ett exempel finns.

## Testbarhet utan att förlora verksamhetsförankring

Ett vanligt problem är att testbarhet tolkas som teknisk detaljrikedom. Då skrivs scenarier som är lätta för ett verktyg att köra, men svåra för verksamheten att förstå.

Exempel på för tekniskt scenario:

```gherkin
Scenario: GET /cases filtrerar bort case utan ACL-matchning
  Given userId "u-123" has orgUnitId "OU-17"
  And caseId "C-1003" has aclEntry "OU-99"
  When GET /api/v2/cases?q=C-1003 is called with bearer token "token-u-123"
  Then the response status should be 200
  And the JSON path "$.items" should be empty
```

Det här kan vara ett relevant API-test. Men som kravspecifikation är det för tekniskt för de flesta verksamhetsrepresentanter.

Ett mer verksamhetsnära exempel:

| Exempel-ID | Situation | Förutsättning | Förväntat beteende |
|---|---|---|---|
| EX-11-09 | Utredare söker efter ett ärende som tillhör annan enhet | Utredaren är inte tilldelad ärendet och saknar särskild behörighet | Ärendet visas inte i sökresultatet |

Det tekniska API-testet kan länka till EX-11-09, men det bör inte ersätta det. På så sätt kan organisationen ha både verksamhetsförankring och testbarhet.

## Spårbarhet som stöd, inte börda

I traditionellt kravarbete blir spårbarhet ibland ett administrativt lager som få använder. I SBE bör spårbarhet vara praktisk. Den ska hjälpa teamet att se sambandet mellan regel, exempel, test, implementation och beslut.

En lättviktig spårbarhetsmodell kan se ut så här:

| Objekt | Exempel på ID | Syfte |
|---|---|---|
| Funktion eller område | SOK | Håller ihop ett funktionsområde |
| Regel | SOK-REG-03 | Beskriver verksamhetsregel |
| Exempel | SOK-EX-03-02 | Konkretiserar regeln |
| Öppen fråga | SOK-OQ-03-01 | Visar vad som inte är beslutat |
| Test | SOK-TST-03-02 | Verifierar regel eller exempel |
| Automatiserat scenario | SOK-AUTO-03-02 | Körbar kontroll av beteende |

Det viktiga är inte exakt ID-format. Det viktiga är att relationen går att följa utan att dokumentationen blir tung.

I brottsutredningsstödet kan en regel om sökbehörighet ha tre exempel och två automatiserade tester. Då bör det gå att se:

- vilken regel exemplen hör till
- vilka exempel som är automatiserade
- vilka exempel som bara är dokumenterade
- vilka tester som täcker vilka exempel
- vilka öppna frågor som fortfarande påverkar regeln

## Hantera avvikelser mellan dokumentation och system

Förr eller senare upptäcks en avvikelse. Systemet gör inte vad specifikationen säger. Eller specifikationen beskriver inte längre vad verksamheten vill. Då behöver teamet undvika reflexen att bara “rätta testet” eller “uppdatera kravet” utan analys.

En avvikelse kan betyda olika saker:

| Avvikelse | Möjlig innebörd | Rekommenderad hantering |
|---|---|---|
| Systemet följer inte exemplet | Fel i implementation | Skapa defekt och behåll specifikationen |
| Exemplet beskriver fel verksamhetsregel | Fel i specifikation | Uppdatera regel, exempel och berörda tester |
| Testet kontrollerar något annat än exemplet | Fel i testdesign | Justera test och spårbarhet |
| Verksamheten har ändrat beslut | Förändrat krav | Uppdatera dokumentation och behandla som ändring |
| Tekniskt beroende gör beteendet omöjligt | Begränsning eller designfråga | Synliggör konsekvens och fatta nytt beslut |

Det här kräver disciplin. Men det är också en av de stora vinsterna med SBE: avvikelser blir synliga på en nivå där flera roller kan förstå dem.

## När krav, test och utveckling drar åt olika håll

SBE fungerar bäst när rollerna ser exemplen som gemensam egendom. Men i praktiken kan olika roller dra åt olika håll.

### När krav vill ha läsbarhet och test vill ha precision

Kravanalytikern kan vilja hålla exemplen enkla och läsbara. Testaren kan vilja lägga till fler variationer och detaljer. Båda behoven är legitima.

Lösningen är ofta att skilja på nivåer:

- specifikationen visar de viktigaste verksamhetsexemplen
- testdesignen kompletterar med fler tekniska variationer
- automatiserade tester länkas till regel eller exempel
- detaljer som inte hjälper verksamheten hålls utanför huvudtexten

### När utveckling vill ha tekniska beslut och verksamheten vill prata mål

Utvecklaren behöver veta hur regler ska implementeras. Verksamheten vill ofta prata om mål och arbetssätt. Kravanalytikerns uppgift är att översätta mellan dessa nivåer utan att blanda ihop dem.

En bra fråga är:

> Vilket konkret beteende behöver systemet ha för att verksamhetsmålet ska uppfyllas?

Det leder ofta från mål till regel, från regel till exempel och från exempel till teknisk konsekvens.

### När testautomation börjar styra specifikationen

Om organisationen lägger för stor vikt vid automation kan scenarierna skrivas för verktyget snarare än för förståelsen. Då riskerar SBE att bli testdriven dokumentation i sämre bemärkelse.

Varningssignaler är:

- verksamheten slutar läsa scenarierna
- scenarierna beskriver tekniska steg i stället för beteende
- små UI-ändringar kräver stora omskrivningar
- step definitions blir viktigare än regler
- öppna frågor hanteras i kod i stället för i specifikation

Motmedlet är att hålla fast vid principen: det viktigaste exemplet är det som skapar gemensam förståelse. Automation är en möjlig förstärkning, inte målet i sig.

## Praktiskt arbetsmönster: från regel till färdig funktion

Här är ett konkret arbetsmönster för brottsutredningsstödet.

### Steg 1: Formulera regel

Regel:

> En utredare får se ett ärende i sökresultatet om utredaren tillhör ärendets ansvariga enhet eller är tilldelad ärendet. Sekretessmarkerade ärenden kräver dessutom särskild behörighet.

### Steg 2: Skapa exempel

| Exempel-ID | Användare | Relation | Sekretess | Särskild behörighet | Förväntat resultat |
|---|---|---|---|---|---|
| SOK-EX-01 | Utredare A | Samma enhet | Nej | Nej | Ärendet visas |
| SOK-EX-02 | Utredare A | Tilldelad ärendet | Nej | Nej | Ärendet visas |
| SOK-EX-03 | Utredare A | Ingen relation | Nej | Nej | Ärendet visas inte |
| SOK-EX-04 | Utredare A | Samma enhet | Ja | Nej | Ärendet visas inte |
| SOK-EX-05 | Utredare A | Samma enhet | Ja | Ja | Ärendet visas |

### Steg 3: Identifiera öppna frågor

- Ska dolda ärenden påverka antal träffar?
- Ska sökning efter exakt ärendenummer visa ett särskilt meddelande om åtkomst saknas?
- Ska nekad åtkomst loggas?
- Hur länge gäller särskild behörighet?
- Vem kan ge särskild behörighet?

### Steg 4: Bedöm tekniska konsekvenser

| Konsekvens | Berörda roller | Kommentar |
|---|---|---|
| Behörighetskontroll måste ske innan resultat visas | Utveckling, test | Påverkar söktjänst och eventuell indexering |
| Sekretessmarkering kräver särskild regel | Verksamhet, krav, utveckling | Behöver definieras tydligt |
| Loggning kan krävas även vid nekad åtkomst | Verksamhet, säkerhet, test | Beror på policy och rättsliga krav |
| Testdata behöver flera användarrelationer | Test | Kräver kontrollerbar testmiljö |

### Steg 5: Bestäm teststrategi

| Exempel | Teststrategi | Kommentar |
|---|---|---|
| SOK-EX-01 | Automatiserat integrationstest | Stabil regel och tydligt resultat |
| SOK-EX-02 | Automatiserat integrationstest | Viktig behörighetsvariant |
| SOK-EX-03 | Automatiserat integrationstest | Viktigt negativt exempel |
| SOK-EX-04 | Automatiserat test plus manuell granskning | Sekretess kräver extra kontroll |
| SOK-EX-05 | Automatiserat test | Kräver testdata för särskild behörighet |

### Steg 6: Länka implementation och uppdatera dokumentation

När funktionen implementeras kan teamet länka tester till regel och exempel. Om implementationen kräver ett beslut om träffantal eller loggning uppdateras specifikationen. Om ett exempel ändras uppdateras berörda tester.

Det här är kärnan i samspelet: dokumentationen är inte en bilaga till utvecklingen. Den är en aktiv referens som förädlas när teamet lär sig mer.

## Vanliga misstag

- **Misstag: Att låta testarna upptäcka kravfrågorna för sent.**
  - Varför det händer: Organisationen ser test som en senare fas.
  - Hur du undviker det: Involvera testare när exempel tas fram, särskilt för gränsfall och negativa exempel.

- **Misstag: Att göra alla exempel till automatiserade tester.**
  - Varför det händer: Levande dokumentation misstolkas som fullständig automation.
  - Hur du undviker det: Bedöm varje exempel utifrån stabilitet, nytta, observerbarhet och underhållskostnad.

- **Misstag: Att skriva scenarier för verktyget i stället för för förståelsen.**
  - Varför det händer: Teamet börjar i Cucumber eller Concordion för tidigt.
  - Hur du undviker det: Skriv först verksamhetsnära exempel. Automatisera därefter de exempel som passar.

- **Misstag: Att tekniska beslut försvinner från specifikationen.**
  - Varför det händer: Beslut tas informellt under implementation.
  - Hur du undviker det: Dokumentera tekniska konsekvenser och uppdatera regeln eller exemplen när beslut påverkar beteendet.

- **Misstag: Att blanda kravexempel, testfall och implementation i samma text.**
  - Varför det händer: Organisationen vill ha “allt på ett ställe”.
  - Hur du undviker det: Håll ihop nivåerna med spårbarhet, men separera syfte och målgrupp.

## Övningar

### Övning 1: Identifiera rollernas frågor

Utgå från regeln:

> En förundersökningsledare ska kunna omfördela ett ärende till en annan utredare om ärendet är aktivt och mottagaren har rätt behörighet.

Skriv tre frågor från varje roll:

- kravanalytiker
- testare
- utvecklare
- verksamhetsrepresentant

Markera vilka frågor som behöver besvaras innan implementation och vilka som kan hanteras senare.

### Övning 2: Skilj kravexempel från testfall

Skriv ett verksamhetsnära kravexempel för omfördelning av ärende. Skriv sedan ett separat testfall som verifierar samma beteende.

Jämför texterna:

- Vilken text är lättast för verksamheten att läsa?
- Vilken text är mest användbar för testaren?
- Vilka detaljer bör inte ligga i kravexemplet?
- Vilken spårbarhet behövs mellan dem?

### Övning 3: Bedöm automation

Välj fem exempel från ett funktionsområde i brottsutredningsstödet, till exempel sökning, statusövergångar eller behörighet.

Bedöm varje exempel utifrån:

- beslutat beteende
- observerbart resultat
- regressionsvärde
- stabilitet
- kostnad att automatisera

Dela in exemplen i tre grupper:

- automatisera tidigt
- dokumentera men automatisera senare
- använd som analys- eller granskningsscenario

### Fördjupning

Ta ett befintligt acceptanskriterium från din egen organisation. Gör följande:

1. Skriv om det till en verksamhetsregel.
2. Skapa minst tre exempel.
3. Identifiera vilka frågor testare och utvecklare sannolikt skulle ställa.
4. Bestäm vilka exempel som bör automatiseras.
5. Beskriv hur dokumentationen kan hållas begriplig för verksamheten och användbar för IT.

## Snabb sammanfattning

- SBE gör exempel till en gemensam arbetsyta för krav, test, utveckling och verksamhet.
- Kravexempel, testfall, automatiserade tester och implementation bör kopplas ihop men inte blandas samman.
- Testare bör bidra tidigt med gränsfall, variation och testbarhet.
- Utvecklare bör bidra tidigt med tekniska konsekvenser och genomförbarhetsfrågor.
- Verksamheten behöver bekräfta att exemplen speglar verkliga beslut och arbetssituationer.
- Alla exempel ska inte automatiseras.
- Automation är värdefull när beteendet är beslutat, observerbart, viktigt och stabilt.
- Spårbarhet ska hjälpa teamet att följa samband, inte skapa administrativ börda.
- Avvikelser mellan specifikation, test och system ska analyseras innan något ändras.
- SBE fungerar bäst när dokumentationen är både verksamhetsförankrad och praktiskt användbar för IT.

## Quiz/reflektionsfrågor

1. Vad innebär det att exempel fungerar som en gemensam arbetsyta?
2. Varför är ett kravexempel inte samma sak som ett testfall?
3. Vilka frågor kan en testare bidra med innan implementation?
4. Vilka frågor kan en utvecklare bidra med innan implementation?
5. När bör ett exempel automatiseras?
6. När bör ett exempel inte automatiseras direkt?
7. Hur kan spårbarhet stödja SBE utan att bli administrativt tung?
8. Vad bör teamet göra när systemet inte följer ett dokumenterat exempel?
9. Hur kan kravanalytikern hindra att SBE-dokumentationen blir för teknisk?
10. Vilka risker uppstår om testerna blir den enda sanningen?

## Koppling till bokens röda tråd

När SBE fungerar väl blir gränsen mellan krav, test och utveckling mindre av en överlämning och mer av en gemensam arbetsyta. Det betyder inte att rollerna försvinner, utan att varje roll bidrar till samma specifikation med sin särskilda kompetens: domän, precision, verifiering och teknisk genomförbarhet.


## Nästa steg

Nu har vi fördjupat samspelet mellan krav, test och utveckling. Nästa kapitel handlar om kvalitetssäkring av SBE-specifikationer. Där går vi igenom hur man granskar om regler, exempel, scenarier och dokumentationsstruktur faktiskt håller tillräcklig kvalitet för att fungera som gemensam sanning över tid.
