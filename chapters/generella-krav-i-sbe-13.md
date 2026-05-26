# Kapitel 13: Generella krav i ett SBE-arbetssätt

## Varför detta kapitel finns

Hittills har boken främst behandlat funktionella krav: situationer där en användare gör något, systemet reagerar och resultatet kan beskrivas med regler, exempel och scenarier. Det är ofta där SBE ger snabbast effekt, eftersom abstrakta krav kan ersättas eller kompletteras med konkreta exempel.

Men alla krav passar inte naturligt in i ett enskilt flöde.

I många system finns krav som återkommer över flera funktioner. De beskriver principer, standardbeteenden, gemensamma regler eller tvärgående förväntningar. De kan påverka många användningsfall utan att själva vara ett användningsfall. De kan vara funktionella till sin karaktär, men ändå generella i sin placering.

I brottsutredningsstödet kan det till exempel handla om att alla ändringar i ett ärende ska spåras, att bara behöriga roller får se känsliga uppgifter, att sökresultat alltid ska filtreras utifrån åtkomst, eller att vissa informationsfält ska visas på samma sätt oavsett var i systemet de förekommer.

Det här kapitlet handlar om hur sådana generella krav kan hanteras i ett SBE-arbetssätt. Målet är att undvika två vanliga problem:

- att generella krav blir vaga principtexter som alla nickar åt men ingen riktigt använder
- att samma regel upprepas i många scenarier tills dokumentationen blir tung, motsägelsefull och svår att underhålla

SBE löser inte detta automatiskt. Men SBE ger ett sätt att konkretisera generella regler med exempel, utan att förlora överblicken.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan funktionella flödeskrav, generella krav och icke-funktionella krav
- identifiera när ett krav bör dokumenteras som en tvärgående regel i stället för i varje enskilt scenario
- konkretisera generella krav med exempel utan att skapa onödig upprepning
- strukturera generella krav så att de fungerar för både verksamhet och IT
- beskriva hur generella krav påverkar scenarier, test, implementation och förvaltning
- använda brottsutredningsstödet som modell för behörighet, spårbarhet, söklogik och gemensamma beteenden

## Innan vi börjar

Ett generellt krav är inte samma sak som ett vagt krav. Det är inte heller automatiskt ett icke-funktionellt krav.

Ett generellt krav är ett krav som gäller på flera ställen i systemet. Det kan vara en verksamhetsregel, ett standardbeteende, en gemensam hanteringsprincip eller ett återanvändbart mönster. Skillnaden ligger främst i räckvidden.

Ett funktionellt flödeskrav kan låta så här:

> När en utredare ändrar status på ett ärende från preliminärt till aktivt ska systemet kräva att ansvarig utredare är angiven.

Ett generellt krav kan låta så här:

> Alla ändringar av ärendestatus ska loggas med tidpunkt, användare, tidigare status och ny status.

Det andra kravet kan påverka flera flöden: skapa ärende, ändra status, avsluta ärende, återöppna ärende och korrigera felaktig status. Det är fortfarande ett beteende som systemet ska ha, men det hör inte bara hemma i ett enskilt scenario.

I SBE behöver vi därför kunna dokumentera krav på flera nivåer:

- specifika scenarier för ett avgränsat beteende
- regler som förklarar varför scenarierna ska fungera som de gör
- generella regler som gäller över flera funktioner
- kvalitetskrav som ofta behöver mätbara kriterier eller arkitekturbeslut

Det här kapitlet fokuserar på den tredje nivån: generella regler och tvärgående funktionella krav.

## Vad menas med generella krav?

Generella krav är krav som har bred räckvidd. De påverkar flera funktioner, flera skärmar, flera informationsobjekt eller flera roller.

I traditionell kravdokumentation hamnar de ofta i avsnitt som heter något i stil med:

- generella krav
- övergripande krav
- gemensamma krav
- systembeteenden
- regelverk
- övriga krav
- krav som gäller hela lösningen

Problemet är inte att sådana avsnitt finns. Problemet är att de ofta blir en blandning av olika kravtyper.

I samma avsnitt kan man hitta verksamhetsregler, användbarhetskrav, säkerhetskrav, tekniska designbeslut, formuleringar från policydokument och allmänna ambitioner. För läsaren blir det svårt att se vad som faktiskt ska byggas, vad som ska testas och vad som bara är bakgrund.

I ett SBE-arbetssätt behöver generella krav därför sorteras efter hur de påverkar beteendet.

En användbar första sortering är:

| Typ av generellt krav | Fråga att ställa | Exempel i brottsutredningsstödet |
|---|---|---|
| Tvärgående verksamhetsregel | Vilken regel ska alltid gälla? | Ett avslutat ärende får inte ändras utan särskild behörighet |
| Standardbeteende | Hur ska systemet normalt bete sig? | Tomma fält ska inte visas i sammanfattningsvyn |
| Gemensam validering | Vilka kontroller gäller på flera ställen? | Personnummer ska kontrolleras innan koppling till personpost sparas |
| Gemensam behörighetsprincip | Vem får se eller göra vad? | En användare får bara se ärenden inom sin behörighetsdomän |
| Gemensam spårbarhetsregel | Vad ska kunna följas upp i efterhand? | Alla åtkomster till skyddade personuppgifter ska loggas |
| Återanvändbar informationsregel | Hur ska information tolkas eller presenteras? | Ärendestatus ska visas med samma benämningar i alla vyer |

Den här sorteringen gör det lättare att avgöra hur kravet ska dokumenteras. Vissa generella krav bör beskrivas som regler med exempel. Andra bör beskrivas som principer med hänvisningar till scenarier. Några hör snarare hemma i kapitlet om icke-funktionella krav, särskilt om de handlar om prestanda, tillgänglighet, säkerhetsnivåer eller tekniska kvaliteter.

## Skillnaden mellan generella och icke-funktionella krav

Generella krav och icke-funktionella krav blandas ofta ihop. Det är förståeligt, eftersom båda kan gälla över flera funktioner. Men de fyller inte samma roll.

Ett generellt krav beskriver ofta ett beteende som systemet ska ha i många situationer.

Ett icke-funktionellt krav beskriver ofta en kvalitet hos systemet eller en begränsning för hur systemet ska fungera.

Jämför dessa två krav:

| Krav | Typ | Varför |
|---|---|---|
| Alla ändringar i ett ärende ska loggas med användare, tidpunkt och ändrad uppgift | Generellt funktionellt krav | Det beskriver ett konkret beteende som ska ske vid flera händelser |
| Loggning ska kunna hantera minst 10 000 händelser per minut utan märkbar påverkan på svarstid | Icke-funktionellt krav | Det beskriver kapacitet och prestanda |

Båda kan handla om loggning. Men det första kravet säger vad systemet ska göra. Det andra säger hur väl systemet behöver klara det.

Samma sak gäller behörighet.

| Krav | Typ | Varför |
|---|---|---|
| En utredare får bara öppna ärenden som tillhör den egna behörighetsdomänen | Generellt funktionellt krav | Det beskriver en regel för åtkomst |
| Behörighetskontroll ska ske för varje skyddad resurs och inte kunna kringgås via direktlänk | Icke-funktionellt eller arkitektoniskt säkerhetskrav | Det beskriver en säkerhetsegenskap och teknisk begränsning |

I praktiken behöver de ofta dokumenteras tillsammans, men inte som om de vore samma sak. SBE kan hjälpa till med den funktionella regeln genom exempel. Det icke-funktionella kravet kan behöva kompletteras med säkerhetsprinciper, arkitekturbeslut, granskningspunkter eller mätbara acceptanskriterier.

## Varför generella krav ofta blir svåra

Generella krav blir svåra av tre skäl.

För det första är de ofta sanna på en övergripande nivå men otydliga i detaljerna.

Formuleringen “systemet ska tillämpa behörighetsstyrning” säger nästan ingenting om vad som ska hända när en utredare söker efter ett ärende, öppnar ett ärende, exporterar uppgifter, ser en notifiering eller försöker komma åt en direktlänk.

För det andra påverkar de många funktioner. Om kravet beskrivs i varje scenario kan dokumentationen svälla snabbt. Om kravet bara beskrivs en gång riskerar scenarierna att bli vilseledande, eftersom de inte visar att regeln faktiskt påverkar beteendet.

För det tredje ägs de ofta av flera intressenter. En behörighetsregel kan beröra verksamhet, juridik, informationssäkerhet, arkitektur, utveckling, test och förvaltning. Om ingen äger helheten blir regeln antingen för abstrakt eller för teknisk.

I brottsutredningsstödet kan samma generella regel behöva förstås från flera perspektiv:

- verksamheten behöver veta vem som ska få göra vad
- juristen behöver veta att hanteringen följer regelverk
- säkerhetsansvarig behöver veta att kontrollen inte kan kringgås
- utvecklaren behöver veta var kontrollen ska implementeras
- testaren behöver veta vilka situationer som ska verifieras
- förvaltningen behöver veta hur nya roller och ärendetyper påverkar regeln

Det är därför generella krav behöver en tydlig dokumentationsmodell.

## En dokumentationsmodell för generella krav

Ett generellt krav bör dokumenteras så att läsaren kan förstå fyra saker:

1. Vad regeln säger.
2. Var regeln gäller.
3. Vilka exempel som visar regeln.
4. Hur regeln påverkar specifika scenarier.

En enkel struktur är:

| Del | Syfte |
|---|---|
| Namn | Gör regeln lätt att hänvisa till |
| Syfte | Förklarar varför regeln finns |
| Regel | Beskriver det generella beteendet |
| Räckvidd | Anger var regeln gäller och inte gäller |
| Exempel | Konkretiserar regeln i typiska och viktiga fall |
| Undantag | Synliggör när regeln inte gäller eller kräver särskild hantering |
| Påverkan på scenarier | Visar hur regeln ska hänvisas till i specifika flöden |
| Ägarskap | Anger vem som kan besluta om ändringar |
| Relaterade kvalitetskrav | Kopplar till säkerhet, spårbarhet, prestanda eller andra kvaliteter |

Det viktiga är inte att varje generellt krav måste ha exakt samma mall. Det viktiga är att dokumentationen gör regeln användbar.

En verksamhetsrepresentant ska kunna läsa regeln och känna igen verksamhetslogiken. En utvecklare ska kunna förstå hur regeln påverkar implementationen. En testare ska kunna härleda vilka exempel som behöver verifieras.

## Exempel: behörighetsdomän i brottsutredningsstödet

Anta att brottsutredningsstödet används av flera enheter inom en myndighet. Alla utredare ska inte kunna se alla ärenden. Åtkomst styrs av en behörighetsdomän som kan bero på organisatorisk tillhörighet, ärendekategori, sekretessklassning och särskilt tilldelad åtkomst.

Ett traditionellt generellt krav skulle kunna vara:

> Systemet ska säkerställa att användare endast får åtkomst till ärenden de är behöriga att se.

Kravet är rimligt, men otillräckligt. Det säger inte vad “åtkomst” betyder. Det säger inte vad som ska hända i sökresultat, ärendelistor, notifieringar eller direktlänkar. Det säger inte heller om användaren ska få veta att ett ärende finns men inte få öppna det, eller om ärendet inte ska visas alls.

I SBE kan vi göra regeln mer användbar.

### Generell regel

**Regel: Åtkomst till ärende styrs av behörighetsdomän**

En användare får bara se, öppna och bearbeta ärenden som tillhör en behörighetsdomän där användaren har aktiv åtkomst. Om användaren saknar åtkomst ska ärendet inte visas i listor eller sökresultat, och direktförsök att öppna ärendet ska nekas.

### Räckvidd

Regeln gäller för:

- ärendelistor
- fritextsökning
- filtrerad sökning
- direktlänkar
- notifieringar
- ärendeöversikter
- export av ärendedata

Regeln gäller inte för:

- aggregerad statistik där enskilda ärenden inte kan identifieras
- särskilda administrationsvyer för behörighetsförvaltare
- revisionsloggar som hanteras enligt separat åtkomstregel

### Exempel

| Situation | Användarens åtkomst | Ärendets domän | Förväntat beteende |
|---|---|---|---|
| Sökning efter ärenden | Domän A | Domän A | Ärendet visas |
| Sökning efter ärenden | Domän A | Domän B | Ärendet visas inte |
| Direktlänk till ärende | Domän A | Domän B | Åtkomst nekas |
| Notifiering om uppdatering | Domän A | Domän B | Notifiering skickas inte |
| Aggregerad statistik | Domän A | Domän B | Ärendet får bidra till summering om identitet inte röjs |

Här gör exemplen regeln prövbar. De visar också att behörighet inte bara handlar om att öppna ett ärende. Den påverkar sökning, notifieringar och statistik.

### Påverkan på scenarier

I scenarier för sökning behöver vi inte upprepa hela behörighetsregeln varje gång. Men vi kan hänvisa till regeln när den påverkar beteendet.

Exempel:

```gherkin
Scenario: Utredare söker efter ärenden inom sin behörighetsdomän
  Givet att utredaren har åtkomst till behörighetsdomän A
  Och ärende 2026-145 tillhör behörighetsdomän A
  När utredaren söker på ärendenummer 2026-145
  Så ska ärende 2026-145 visas i sökresultatet
```

```gherkin
Scenario: Utredare söker efter ärende utanför sin behörighetsdomän
  Givet att utredaren har åtkomst till behörighetsdomän A
  Och ärende 2026-912 tillhör behörighetsdomän B
  När utredaren söker på ärendenummer 2026-912
  Så ska ärendet inte visas i sökresultatet
```

Scenarierna behöver inte beskriva hela behörighetsmodellen. De visar hur den generella regeln slår igenom i sökfunktionen.

## När ska regeln ligga centralt och när ska den ligga i flödet?

En praktisk tumregel är:

> Dokumentera regeln centralt när den gäller på många ställen. Visa den i flödet när den påverkar ett viktigt beslut eller ett viktigt användarresultat.

Det betyder att en generell regel ofta behöver två typer av dokumentation:

- en central regelbeskrivning
- utvalda scenarier i de flöden där regeln är särskilt viktig

Om behörighetsregeln gäller i hela systemet bör den inte kopieras in i varje kapitel eller varje funktionsspecifikation. Då blir den svår att underhålla. Men om sökfunktionen är ett kritiskt område där behörighet påverkar resultatlistan, behöver sökkapitlet visa exempel på hur regeln används.

En bra fråga är:

> Skulle läsaren missförstå flödet om den generella regeln inte syntes här?

Om svaret är ja bör scenariot visa effekten av regeln. Om svaret är nej räcker det ofta med en hänvisning till den centrala regeln.

## Exempel: standardbeteende för tomma fält

Alla generella krav handlar inte om säkerhet eller juridik. Vissa handlar om konsekvent användarupplevelse och begriplighet.

Anta att brottsutredningsstödet visar sammanfattningsvyer för ärenden, personer, händelser och beslag. Ett återkommande problem är att vissa uppgifter saknas. Om systemet visar alla tomma fält blir vyerna svårlästa. Om systemet döljer fält för aggressivt kan användaren tro att uppgiften inte finns i modellen.

Ett generellt krav kan vara:

> I sammanfattningsvyer ska tomma frivilliga fält döljas, medan obligatoriska men saknade fält ska visas med markeringen “saknas”.

Detta är ett generellt funktionellt krav. Det beskriver ett beteende som påverkar flera vyer.

### Regel

Frivilliga fält utan värde ska inte visas i sammanfattningsvyer. Obligatoriska fält utan värde ska visas med markeringen “saknas”. Fält som är dolda av behörighetsskäl ska inte visas alls.

### Exempel

| Fälttyp | Värde finns | Orsak till saknat värde | Förväntad visning |
|---|---|---|---|
| Frivilligt fält | Ja | Inte relevant | Visa fält och värde |
| Frivilligt fält | Nej | Uppgift ej registrerad | Dölj fältet |
| Obligatoriskt fält | Nej | Uppgift saknas | Visa fält med “saknas” |
| Behörighetsskyddat fält | Ja | Användaren saknar åtkomst | Dölj fältet |
| Behörighetsskyddat fält | Nej | Användaren saknar åtkomst | Dölj fältet |

Här syns också hur generella krav kan samspela. Regeln om tomma fält måste förhålla sig till behörighetsregeln. Om användaren saknar åtkomst ska systemet inte visa ett fält med “saknas”, eftersom det skulle kunna avslöja att en skyddad uppgift finns.

Detta är ett exempel på att generella krav inte kan hanteras som isolerade punktlistor. De behöver kunna relateras till varandra.

## Generella krav som regler, inte önskningar

Många generella krav formuleras som önskningar:

- Systemet ska vara lätt att använda.
- Systemet ska ha bra stöd för sökning.
- Systemet ska hantera behörighet på ett säkert sätt.
- Systemet ska ge tydliga felmeddelanden.
- Systemet ska stödja spårbarhet.

Sådana formuleringar kan vara bra som mål, men de är inte tillräckliga som krav. De behöver brytas ned i regler, exempel och kvalitetskriterier.

Ett generellt krav i SBE bör helst kunna uttryckas som en regel:

- När X gäller ska systemet göra Y.
- Om X saknas ska systemet visa Y.
- En användare med roll X får göra Y men inte Z.
- En händelse av typ X ska registreras med uppgifterna Y och Z.
- Ett objekt med status X får bara ändras genom händelse Y.

Regelformen gör kravet mer granskningsbart. Den tvingar fram villkor och konsekvens.

Jämför:

> Systemet ska ge tydliga felmeddelanden.

Med:

> När en användare försöker spara ett ärende utan obligatorisk uppgift ska systemet markera fältet, beskriva vad som saknas och låta användaren korrigera utan att övriga registrerade uppgifter förloras.

Den andra formuleringen är fortfarande generell om den gäller många formulär. Men den är betydligt lättare att konkretisera med exempel.

## Exempel: gemensam validering av personkoppling

I brottsutredningsstödet kan ett ärende kopplas till personer. Det kan handla om misstänkta, målsägande, vittnen eller andra relevanta personer. Flera funktioner kan skapa eller ändra sådana kopplingar.

Ett generellt krav kan vara:

> Innan en personkoppling sparas ska systemet kontrollera att personposten är identifierad och att relationstypen är angiven.

Detta gäller kanske i flera flöden:

- skapa nytt ärende
- lägga till misstänkt
- lägga till vittne
- importera information från extern källa
- korrigera befintlig personkoppling

I stället för att upprepa hela valideringsregeln i varje flöde kan regeln dokumenteras centralt.

### Regel

En personkoppling får bara sparas om den kopplade personposten är identifierad och relationstypen är angiven. Om personpost eller relationstyp saknas ska systemet stoppa sparandet och visa vilken uppgift som saknas.

### Exempel

| Personpost identifierad | Relationstyp angiven | Förväntat beteende |
|---|---|---|
| Ja | Ja | Kopplingen sparas |
| Ja | Nej | Sparande stoppas och relationstyp efterfrågas |
| Nej | Ja | Sparande stoppas och personpost efterfrågas |
| Nej | Nej | Sparande stoppas och båda uppgifterna efterfrågas |

Den här tabellen är enkel, men den gör regeln tydlig. Den visar också när beslutstabeller passar bättre än Gherkin-scenarier. För kombinationer av villkor är en tabell ofta mer läsbar än flera nästan identiska scenarier.

I ett specifikt flöde kan man sedan visa ett scenario där regeln används:

```gherkin
Scenario: Utredare lägger till vittne utan relationstyp
  Givet att utredaren redigerar ärende 2026-145
  Och har valt personposten Anna Berg
  Men inte valt relationstyp
  När utredaren försöker spara personkopplingen
  Så ska kopplingen inte sparas
  Och systemet ska visa att relationstyp måste anges
```

Här blir scenariot ett exempel på den generella valideringsregeln i ett konkret flöde.

## Räckvidd är viktigare än placering

Ett vanligt dokumentationsproblem är att generella krav hamnar på fel plats. Men den viktigare frågan är inte alltid var kravet ligger, utan om dess räckvidd är tydlig.

En regel kan ligga i ett centralt regelbibliotek, i en funktionsspecifikation, i en domänmodell eller i en levande dokumentationsyta. Oavsett plats behöver läsaren förstå:

- vilka funktioner regeln påverkar
- vilka objekt regeln gäller
- vilka roller regeln gäller
- vilka undantag som finns
- vilka andra regler den samspelar med
- vem som får ändra regeln

Utan tydlig räckvidd riskerar generella krav att antingen överanvändas eller missas.

Exempel:

> Alla ärenden ska kunna avslutas.

Det låter generellt, men är oklart. Gäller det preliminära ärenden? Gäller det ärenden som är låsta för juridisk granskning? Gäller det ärenden med obesvarade kompletteringsbegäranden? Vem får avsluta? Vad händer med pågående uppgifter?

En mer användbar regel är:

> Ett aktivt ärende får avslutas av ansvarig utredare när alla obligatoriska avslutsuppgifter är angivna och inga spärrande kompletteringsbegäranden är öppna. Ärenden som är låsta för juridisk granskning får bara avslutas av användare med särskild avslutsbehörighet.

Nu går det att skapa exempel. Nu går det också att se att regeln påverkar ärendestatus, behörighet, kompletteringsflöden och juridisk granskning.

## Referera utan att gömma

När en generell regel används i många scenarier är det frestande att bara skriva “behörighet kontrolleras enligt generella regler”. Det kan vara korrekt, men det kan också gömma det viktigaste beteendet.

En hänvisning är bra när regeln är stödjande. Den är dålig när den döljer ett centralt beslut.

Jämför dessa två scenarier:

```gherkin
Scenario: Utredare öppnar ärende
  Givet att ärendet finns
  När utredaren öppnar ärendet
  Så ska ärendet visas
  Och behörighet hanteras enligt generella regler
```

Det scenariot säger nästan ingenting om användarens åtkomst. Det är svårt att granska.

Ett bättre scenario är:

```gherkin
Scenario: Utredare öppnar ärende inom sin behörighetsdomän
  Givet att utredaren har åtkomst till behörighetsdomän A
  Och ärendet tillhör behörighetsdomän A
  När utredaren öppnar ärendet
  Så ska ärendeöversikten visas
```

Och ett kompletterande scenario:

```gherkin
Scenario: Utredare försöker öppna ärende utanför sin behörighetsdomän
  Givet att utredaren har åtkomst till behörighetsdomän A
  Och ärendet tillhör behörighetsdomän B
  När utredaren försöker öppna ärendet
  Så ska åtkomst nekas
  Och ärendets uppgifter ska inte visas
```

Här behöver scenariot inte upprepa hela behörighetsmodellen. Men det visar den effekt som är viktig i just flödet.

## Generella krav och spårbarhet

Generella krav har ofta hög påverkan. Därför behöver de vara spårbara.

Spårbarhet betyder inte att varje regel måste ha ett tungt administrativt regelverk runt sig. Det betyder att det ska gå att förstå:

- varför regeln finns
- vem som beslutat den
- vilka scenarier och funktioner som påverkas
- vilka testfall eller automatiserade kontroller som verifierar den
- vilka ändringar som kräver omgranskning

I brottsutredningsstödet kan en regel om åtkomst till skyddade personuppgifter påverka många delar av systemet. Om regeln ändras behöver man kunna hitta alla berörda specifikationer.

En enkel spårbarhetsmodell för generella krav kan bestå av:

| Spårbarhetsdel | Exempel |
|---|---|
| Regel-ID | REG-BEH-001 |
| Regelnamn | Åtkomst till ärende styrs av behörighetsdomän |
| Beslutsägare | Verksamhetsansvarig för åtkomstmodell |
| Relaterade funktioner | Sökning, ärendeöversikt, notifieringar, export |
| Relaterade kvalitetskrav | Säkerhet, loggning, spårbarhet |
| Exempel | Sökning inom och utanför behörighetsdomän |
| Automatisering | Urval av kritiska scenarier i regressionstest |
| Ändringspåverkan | Ändrad domänlogik kräver granskning av sökning, direktlänkar och notifieringar |

Det här gör dokumentationen mer användbar för både verksamhet och IT. Verksamheten kan se ansvar och innebörd. IT kan se påverkan.

## Generella krav i levande dokumentation

Levande dokumentation handlar inte bara om automatiserade tester. Det handlar om dokumentation som hålls användbar och aktuell genom att den är nära arbetet.

För generella krav är detta extra viktigt. Om de placeras i ett dokument som ingen läser blir de snabbt en sorts kravarkiv. Om de i stället kopplas till exempel, scenarier och ändringsflöden kan de fortsätta vara relevanta.

En praktisk struktur i levande dokumentation kan vara:

- en sida eller sektion för varje generellt regelområde
- tydligt namn och kort syfte
- regler med räckvidd
- exempel i tabellform eller scenarioform
- länkar till funktioner där regeln används
- öppna frågor och beslut
- historik över viktiga ändringar

För brottsutredningsstödet kan regelområdena vara:

- åtkomst och behörighetsdomän
- ärendestatus och statusövergångar
- loggning och händelsespår
- sökning och filtrering
- informationsvisning
- notifieringar
- export och utlämning
- hantering av skyddade uppgifter

Detta är inte nödvändigtvis kapitel i en bok eller sidor i ett kravverktyg. Det är logiska områden som hjälper organisationen att hålla ihop reglerna.

## När generella krav bör automatiseras

Vissa generella krav lämpar sig väl för automatiserade kontroller. Andra gör det inte.

Automatisering är särskilt värdefull när regeln är:

- stabil
- viktig
- återkommande
- möjlig att kontrollera med tydliga indata och förväntat resultat
- riskfylld om den bryts

Behörighetsregler, valideringsregler och statusövergångar är ofta bra kandidater. Allmänna principer för begriplighet, användbarhet eller dokumentationskvalitet är svårare att automatisera fullt ut.

Exempel på regel som kan automatiseras:

> En användare utan åtkomst till behörighetsdomän B ska inte få upp ärenden från domän B i sökresultat.

Exempel på regel som kräver annan kvalitetssäkring:

> Sökresultat ska presenteras på ett sätt som stödjer utredarens prioritering.

Det senare kan konkretiseras med exempel och granskas med verksamheten, men är inte lika enkelt att automatisera som ett binärt åtkomstbeslut.

Här är en enkel beslutsmodell:

| Fråga | Om ja | Om nej |
|---|---|---|
| Kan regeln uttryckas med tydliga villkor och förväntat resultat? | Överväg exempel och automatiserad kontroll | Dokumentera som princip, riktlinje eller granskningspunkt |
| Är regeln stabil över tid? | Automatisering kan löna sig | Vänta med automation tills regeln mognat |
| Är risken hög om regeln bryts? | Prioritera kontroll | Manuell granskning kan räcka |
| Gäller regeln på många ställen? | Automatisering kan ge hög effekt | Lokal testning kan vara tillräcklig |

Det viktiga är att inte automatisera för att regeln är generell. Automatisera när det ger faktisk nytta.

## Att undvika upprepning utan att förlora tydlighet

Generella krav kräver balans. För lite upprepning gör dokumentationen svår att förstå i sitt sammanhang. För mycket upprepning gör den svår att underhålla.

En fungerande princip är:

> Beskriv regeln en gång. Visa effekten där den spelar roll.

Det innebär att en regel som “åtkomst styrs av behörighetsdomän” beskrivs centralt. Men i specifikationer för sökning, notifieringar och direktlänkar visar man exempel på hur regeln påverkar användaren.

En annan princip är:

> Upprepa inte formuleringen. Upprepa förståelsen.

Det betyder att vi inte behöver kopiera hela regeltexten. Men vi behöver säkerställa att läsaren förstår konsekvensen i varje relevant flöde.

Då kan en funktionsspecifikation innehålla korta hänvisningar som:

- Denna funktion tillämpar REG-BEH-001 för filtrering av sökresultat.
- Scenarierna nedan visar de användarsynliga effekterna av behörighetsregeln.
- Full regeldefinition och undantag finns i regelområdet “Åtkomst och behörighetsdomän”.

På så sätt hålls regeln central, men funktionen blir inte obegriplig.

## Exempel: statusövergångar som generell regel

Ärendestatus är ett typiskt område där generella krav behövs. Ett ärende kan byta status i flera flöden: när det skapas, aktiveras, kompletteras, avslutas, återöppnas eller låses.

I traditionell dokumentation kan statusövergångar beskrivas utspritt i varje funktionskrav. Det leder ofta till motsägelser. Ett flöde säger att ett ärende kan gå från aktivt till avslutat, ett annat antyder att det kan gå från preliminärt till avslutat, och ett tredje glömmer att juridisk granskning kan låsa ärendet.

I SBE kan statusmodellen dokumenteras som ett generellt regelområde.

### Regelområde: ärendestatus

Ett ärende ska alltid ha exakt en aktuell status. Tillåtna statusövergångar styrs av ärendets nuvarande status, användarens behörighet och om spärrande aktiviteter finns.

### Exempel på tillåtna statusövergångar

| Nuvarande status | Önskad status | Villkor | Förväntat resultat |
|---|---|---|---|
| Preliminärt | Aktivt | Ansvarig utredare är angiven | Status ändras till Aktivt |
| Preliminärt | Avslutat | Inte tillåtet | Statusändring nekas |
| Aktivt | Avslutat | Obligatoriska avslutsuppgifter finns | Status ändras till Avslutat |
| Aktivt | Avslutat | Spärrande komplettering finns | Statusändring nekas |
| Avslutat | Aktivt | Användaren har återöppningsbehörighet | Status ändras till Aktivt |
| Låst för juridisk granskning | Avslutat | Användaren saknar särskild behörighet | Statusändring nekas |

Denna tabell kan vara mer effektiv än många separata scenarier. Den visar regeln som en beslutsmatris. Utvalda scenarier kan sedan visa hur statusregeln påverkar viktiga användarflöden.

## Generella krav och domänmodell

Generella krav blir ofta tydligare när de kopplas till centrala domänbegrepp. I brottsutredningsstödet kan sådana begrepp vara ärende, personpost, utredare, behörighetsdomän, händelse, status, skyddad uppgift och loggpost.

Om reglerna skrivs utan tydliga domänbegrepp blir de lätt svävande.

Jämför:

> Användaren ska bara se relevant information.

Med:

> En utredare ska bara se ärenden vars behörighetsdomän ingår i utredarens aktiva åtkomstprofil.

Den andra formuleringen använder domänbegrepp. Det gör regeln mer exakt. Det gör också att exempel kan byggas med samma begrepp.

Ett viktigt arbete för kravanalytikern är därför att hålla ihop terminologi och generella regler. När ett generellt krav introducerar ett nytt begrepp bör begreppet läggas in i canon eller terminologilista. Annars riskerar samma sak att beskrivas med flera ord.

Exempel:

- behörighetsdomän
- åtkomstprofil
- skyddad uppgift
- spärrande komplettering
- statusövergång
- revisionslogg
- händelsespår

I SBE är terminologin inte dekoration. Den är en del av specifikationen.

## Generella krav som beslutsstöd för dokumentationsnivå

Alla generella krav behöver inte lika mycket dokumentation. Kravanalytikern behöver kunna avgöra hur mycket som är lagom.

En praktisk bedömning kan göras med tre frågor:

1. Hur stor risk uppstår om regeln missförstås?
2. Hur många delar av systemet påverkas?
3. Hur stabil är regeln över tid?

Om risken är hög och påverkan bred bör regeln dokumenteras tydligt med exempel, räckvidd och spårbarhet. Om risken är låg och regeln bara påverkar presentation kan en enklare princip räcka.

| Risk | Påverkan | Dokumentationsnivå |
|---|---|---|
| Hög | Bred | Regelområde med exempel, scenarier, spårbarhet och ägarskap |
| Hög | Smal | Lokal regel med tydliga scenarier och ansvarig granskning |
| Låg | Bred | Kort generell princip med några exempel |
| Låg | Smal | Lokal instruktion eller designriktlinje |

I brottsutredningsstödet bör behörighet, loggning och statusövergångar få hög dokumentationsnivå. Standardbeteenden för tomma fält kan få lägre nivå, men ändå behöva tydliga exempel om de påverkar tolkning av känslig information.

## Vanliga misstag

- **Misstag: Att samla alla generella krav i en lång osorterad lista.**
  - Varför det händer: Det känns effektivt att ha ett gemensamt avsnitt för allt som inte passar i ett flöde.
  - Hur man undviker det: Dela upp generella krav i regelområden, till exempel behörighet, status, loggning, sökning och informationsvisning.

- **Misstag: Att kalla allt tvärgående för icke-funktionellt.**
  - Varför det händer: Krav som gäller många funktioner känns övergripande och hamnar därför i samma kategori.
  - Hur man undviker det: Fråga om kravet beskriver ett beteende eller en kvalitet. Beteenden kan ofta beskrivas med regler och exempel.

- **Misstag: Att upprepa samma regel i varje scenario.**
  - Varför det händer: Man vill göra varje scenario komplett.
  - Hur man undviker det: Beskriv regeln centralt och visa bara effekten i de scenarier där den är viktig för förståelsen.

- **Misstag: Att bara hänvisa till generella regler utan att visa effekten.**
  - Varför det händer: Man vill undvika upprepning.
  - Hur man undviker det: Använd regeln centralt, men visa konkreta exempel i kritiska flöden.

- **Misstag: Att dokumentera generella krav utan räckvidd.**
  - Varför det händer: Regeln verkar självklar när den diskuteras i workshoppen.
  - Hur man undviker det: Ange alltid var regeln gäller, var den inte gäller och vilka undantag som finns.

- **Misstag: Att automatisera generella krav för tidigt.**
  - Varför det händer: Generella regler känns viktiga och därför lockande att automatisera.
  - Hur man undviker det: Automatisera först när regeln är stabil, konkret och har tydliga exempel.

- **Misstag: Att låta generella krav sakna ägare.**
  - Varför det händer: Eftersom kraven påverkar många områden antar alla att någon annan ansvarar.
  - Hur man undviker det: Ange beslutsägare eller regelägare för varje viktigt generellt regelområde.

## Praktiskt arbetsmönster

När du arbetar med generella krav enligt SBE kan du använda följande arbetsmönster.

### Steg 1: Identifiera återkommande regler

Gå igenom funktionella flöden och leta efter regler som återkommer. Fråga:

- Dyker samma villkor upp i flera scenarier?
- Påverkar samma regel flera funktioner?
- Har vi samma diskussion i flera workshops?
- Behöver flera team tolka samma princip?
- Finns det risk för att regeln implementeras olika på olika ställen?

I brottsutredningsstödet kan behörighetskontroll i sökning, ärendeöversikt, notifiering och export vara en sådan återkommande regel.

### Steg 2: Namnge regelområdet

Ge regeln ett namn som verksamhet och IT kan använda.

Exempel:

- Åtkomst till ärende styrs av behörighetsdomän
- Statusövergångar för ärende
- Visning av tomma och skyddade fält
- Loggning av ändringar i ärende
- Validering av personkoppling

Namnet ska inte vara för tekniskt, men det ska vara tillräckligt exakt.

### Steg 3: Formulera regeln

Skriv regeln som villkor och konsekvens. Undvik formuleringar som bara uttrycker ambition.

Svag formulering:

> Systemet ska ha bra spårbarhet.

Starkare formulering:

> När en användare ändrar ett ärendes status ska systemet skapa en loggpost med tidigare status, ny status, användare, tidpunkt och orsak om orsak krävs för övergången.

### Steg 4: Ange räckvidd

Beskriv var regeln gäller. Beskriv också viktiga undantag.

Räckvidd kan uttryckas som:

- funktioner
- informationsobjekt
- roller
- statusar
- kanaler
- integrationspunkter
- användningssituationer

### Steg 5: Ta fram exempel

Välj exempel som visar:

- normalfall
- gränsfall
- undantag
- nekade handlingar
- samspel med andra regler

Använd tabeller när många kombinationer ska visas. Använd scenarier när användarflödet är viktigt.

### Steg 6: Koppla till berörda flöden

Ange vilka funktioner och scenarier som påverkas. Lägg inte hela regeltexten överallt, men visa effekten i viktiga flöden.

### Steg 7: Bestäm ägarskap och ändringshantering

Säkerställ att någon kan fatta beslut om regeln. Annars blir regeln svår att förändra och svår att försvara vid konflikt.

## Övningar

### Övning 1: Identifiera generella krav i ett funktionsområde

Utgå från funktionen “sök ärende” i brottsutredningsstödet.

Lista minst fem krav eller regler som kan påverka sökfunktionen men som inte bara gäller sökning.

Exempel på områden att undersöka:

- behörighet
- sekretess
- loggning
- visning av träffar
- sortering
- filtrering
- åtkomst via direktlänk
- hantering av skyddade uppgifter

Markera vilka av kraven som bör dokumenteras som generella regler och vilka som hör hemma direkt i sökfunktionens specifikation.

### Övning 2: Skriv om ett vagt generellt krav

Utgå från formuleringen:

> Systemet ska ge stöd för spårbarhet.

Skriv om den till minst tre konkreta generella regler för brottsutredningsstödet.

För varje regel, ange:

- vad som ska hända
- när det ska hända
- vilka uppgifter som ska sparas eller visas
- ett exempel som konkretiserar regeln

### Övning 3: Välj dokumentationsform

Välj ett av följande regelområden:

- behörighetsdomän
- statusövergångar
- tomma och skyddade fält
- personkopplingar
- notifieringar

Avgör om regelområdet främst bör dokumenteras med:

- regeltext
- beslutstabell
- Gherkin-scenarier
- dokumentnära exempel
- kombination av flera format

Motivera ditt val utifrån vem som ska läsa dokumentationen och hur regeln ska användas.

### Fördjupning: Automatiseringsbeslut

Välj två generella regler från övningarna. Bedöm om de bör automatiseras.

Använd frågorna:

- Är regeln stabil?
- Är den viktig nog att kontrollera löpande?
- Kan den uttryckas med tydliga indata och förväntat resultat?
- Finns det hög risk om den bryts?
- Är automatisering billigare än upprepad manuell kontroll?

Beskriv också vilket format som skulle passa bäst: Gherkin, Concordion-liknande dokumentnära specifikation eller ett annat testupplägg.

## Snabb sammanfattning

- Generella krav är krav som gäller över flera funktioner, flöden eller informationsobjekt.
- Ett generellt krav är inte automatiskt ett icke-funktionellt krav.
- Många generella krav är funktionella regler med bred räckvidd.
- SBE hjälper till att konkretisera generella krav genom regler, exempel, beslutstabeller och scenarier.
- Generella krav bör dokumenteras med namn, syfte, regel, räckvidd, exempel, undantag och påverkan på scenarier.
- Regeln bör beskrivas centralt, men effekten bör visas i viktiga flöden.
- För mycket upprepning gör dokumentationen svår att underhålla.
- För lite konkretisering gör dokumentationen svår att förstå och testa.
- Generella krav behöver ofta tydligt ägarskap och spårbarhet.
- Automatisering passar bäst för stabila, viktiga och tydligt prövbara generella regler.

## Quiz/reflektionsfrågor

1. Vad skiljer ett generellt krav från ett icke-funktionellt krav?
2. Varför räcker det sällan att skriva “behörighet hanteras enligt generella regler” i ett scenario?
3. När bör en regel beskrivas centralt och när bör den visas i ett specifikt flöde?
4. Vilka delar bör ingå i dokumentationen av ett viktigt generellt regelområde?
5. Hur kan beslutstabeller hjälpa vid generella krav?
6. Vilka risker uppstår om samma generella regel upprepas i många scenarier?
7. Varför behöver generella krav ofta en tydlig beslutsägare?
8. Vilka generella krav i brottsutredningsstödet skulle du prioritera för automatisering?

## Koppling till bokens röda tråd

Generella krav kräver särskild disciplin eftersom de påverkar många flöden utan att alltid synas i ett enskilt scenario. I bokens fortsatta struktur behandlas de därför som tvärgående regler som behöver både egen dokumentation och tydliga kopplingar till de funktionella exempel där regeln märks.


## Nästa steg

Generella krav handlar ofta om tvärgående beteenden: vad systemet ska göra i många olika situationer. Nästa kapitel går vidare till icke-funktionella krav och kvalitetskrav.

Där blir frågan delvis en annan. Då handlar det inte bara om vilket beteende systemet ska ha, utan om hur väl systemet måste fungera: hur säkert, snabbt, robust, tillgängligt, spårbart och användbart det behöver vara. Vissa kvalitetskrav kan konkretiseras med exempel, men andra behöver mätetal, arkitekturbeslut, riskanalyser eller särskilda granskningsformer.
