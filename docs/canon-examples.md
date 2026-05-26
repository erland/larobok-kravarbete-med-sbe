# Canon-exempel

## Genomgående case

Boken använder ett återkommande fiktivt case: framtagning av ett brottsutredningsstöd inom en myndighet.

## Syfte med caset

Caset ska ge realistisk komplexitet utan att vara beroende av en verklig myndighets interna processer. Det ska vara tillräckligt konkret för att visa regler, exempel, behörigheter, arbetsflöden, spårbarhet och kravdokumentation.

## Återkommande aktörer

| Aktör | Beskrivning |
|---|---|
| Utredare | Använder stödet för att söka, strukturera och dokumentera uppgifter i ett utredningsärende |
| Förundersökningsledare | Har ansvar för beslut, prioriteringar och vissa åtkomst- eller granskningsmoment |
| Analytiker | Hjälper till att se samband och sammanställa information |
| Registrator eller administratör | Hanterar vissa metadata, klassificeringar och registreringsuppgifter |
| Systemförvaltare | Ansvarar för driftnära regler, behörighetsmodeller och förvaltningsbarhet |
| Testare | Använder specifikationer och exempel som grund för testdesign och eventuell automation |
| Utvecklare | Använder regler och exempel för design och implementation |

## Återkommande funktionsområden

- Skapa och uppdatera utredningsärende.
- Söka efter ärenden och uppgifter.
- Filtrera resultat utifrån behörighet.
- Logga åtkomst till känsliga uppgifter.
- Visa sammanfattning av ärende.
- Hantera statusövergångar.
- Markera uppgifter som sekretessbelagda eller särskilt skyddsvärda.
- Generera underlag för granskning eller beslut.

## Exempelregel att återanvända

En utredare får bara se uppgifter i ett ärende om utredaren tillhör rätt organisatorisk enhet, har tilldelats ärendet eller har en särskild behörighet som motiveras och loggas.

## Exempel på dokumentationsspänning

Verksamheten behöver förstå regeln och dess undantag. IT behöver kunna implementera, testa, logga och förvalta beteendet. SBE-dokumentationen ska därför skilja mellan verksamhetsregel, konkreta exempel, tekniska förutsättningar och öppna frågor.


## Exempel etablerade i kapitel 1

### Otydligt sökkrav

Traditionell kravformulering:

> En utredare ska kunna söka efter utredningsärenden och se ärenden som utredaren har behörighet till.

Kravet används för att visa att formuleringar som verkar tydliga ändå kan lämna öppna frågor om behörighet, sekretess, sökresultat, loggning och relationen mellan användare och ärende.

### Behörighet i sökresultat

Följande situationer används som första exempel på hur abstrakta krav kan göras prövbara:

| Situation | Användare | Ärende | Relation till ärende | Förväntat sökresultat |
|---|---|---|---|---|
| Utredare söker ärende i egen enhet | Utredare A | Ärende 1001 | Samma enhet | Ärendet visas |
| Utredare söker tilldelat ärende i annan enhet | Utredare A | Ärende 1002 | Tilldelad ärendet | Ärendet visas |
| Utredare söker ärende utan relation | Utredare A | Ärende 1003 | Ingen relation | Ärendet visas inte |
| Förundersökningsledare söker ärende i sin grupp | Ledare B | Ärende 1004 | Ansvarig grupp | Ärendet visas |
| Utredare söker sekretessmarkerat ärende med tilldelning | Utredare A | Ärende 1005 | Tilldelad men sekretessmarkerat | Begränsad information visas |

Exemplet ska återanvändas i senare kapitel när boken går från traditionell kravtext till regler, exempel, scenarier, Gherkin och eventuellt automatiserbara specifikationer.

## Kapitel 2: åtkomst till sekretessmarkerade uppgifter

Kapitel 2 använder behörighet till sekretessmarkerade uppgifter som första tydliga SBE-exempel.

Regel: En användares åtkomst till ett ärende beror på relationen till ärendet och eventuell särskild behörighet för skyddade uppgifter.

Återanvändbara exempelvärden:

| Roll | Relation till ärende | Särskild behörighet | Förväntat beteende |
|---|---|---|---|
| Utredare | Tilldelad | Nej | Ärendet visas, men skyddade uppgifter döljs |
| Utredare | Ingen relation | Nej | Ärendet visas inte i sökresultat |
| Förundersökningsledare | Beslutsroll | Ja | Ärendet visas och åtkomsten loggas |
| Analytiker | Stödroll | Nej | Ärendet visas med begränsad information |

Öppna frågor att återkomma till:

- Ska dolda skyddade uppgifter indikeras i gränssnittet?
- Ska nekad åtkomst loggas?
- Ska särskild behörighet kunna vara tidsbegränsad?

## Kapitel 3: kravanalytikerns förändrade roll

Kapitel 3 etablerar att kravanalytikern i SBE främst fungerar som förståelsefacilitator. Rollen är att rama in beteenden, locka fram regler genom exempel, synliggöra antaganden och hålla isär regler, exempel, beslut, öppna frågor och tekniska konsekvenser.

Återanvändbart beteende från kapitlet:

> Öppna utredningsärende.

Exempel som kan återanvändas senare:

| Exempel | Roll | Relation till ärende | Ärendestatus | Sekretessmarkerat | Förväntat resultat |
|---|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Pågående | Nej | Ärendet öppnas |
| 2 | Utredare | Ingen relation | Pågående | Nej | Åtkomst nekas |
| 3 | Förundersökningsledare | Ansvarig | Pågående | Ja | Ärendet öppnas och åtkomst loggas |
| 4 | Utredare | Tidigare tilldelad | Avslutat | Nej | Öppen fråga |
| 5 | Analytiker | Särskild behörighet | Pågående | Ja | Ärendet öppnas med begränsad vy och åtkomst loggas |

Kapitel 3 introducerar också dokumentationsuppdelningen regel, exempel, beslut, öppen fråga och teknisk konsekvens. Denna uppdelning ska återkomma i kapitel 8 och 12.

## Kapitel 4: caset och dess kärnobjekt

Kapitel 4 etablerar caset som ett fiktivt brottsutredningsstöd i myndighetsmiljö. Caset ska användas som återkommande analysmiljö, inte som beskrivning av en verklig myndighets interna arbetssätt.

Centrala aktörer att återanvända:

| Aktör | Användning i kommande kapitel |
|---|---|
| Utredare | Primär användare för sökning, läsning och uppdatering av ärenden |
| Förundersökningsledare | Roll för beslut, granskning och vissa statusövergångar |
| Analytiker | Stödroll som ofta behöver begränsad eller särskilt motiverad åtkomst |
| Registrator eller administratör | Roll för metadata och administrativa uppgifter |
| Systemförvaltare | Roll för förvaltningsbarhet, regler och behörighetsmodell |
| Testare | Använder regler och exempel för testdesign och eventuell automation |
| Utvecklare | Använder regler, exempel och tekniska konsekvenser för implementation |

Centrala informationsobjekt att återanvända:

| Objekt | Kort beskrivning |
|---|---|
| Utredningsärende | Sammanhållen struktur för en utredning |
| Uppgift | Informationsdel som kan höra till ett ärende |
| Personkoppling | Koppling mellan ärende och person |
| Organisatorisk enhet | Enhet som användare och ärenden kan tillhöra |
| Tilldelning | Relation mellan användare och ärende |
| Åtkomstlogg | Spår av åtkomst eller åtkomstförsök |
| Ärendestatus | Markering av var ärendet befinner sig i arbetsflödet |

Återanvändbara funktionsområden:

- Sökning efter utredningsärenden.
- Statusövergångar för utredningsärenden.
- Åtkomstloggning vid känslig information.
- Behörighetsstyrd visning av uppgifter.
- Dokumentation av öppna frågor.

Återanvändbar regel om status:

> Ett ärende får bara ändras till "Avslutat" av en förundersökningsledare, och bara om obligatoriska granskningsuppgifter är ifyllda.

Återanvändbara exempel för statusövergångar:

| Exempel | Roll | Nuvarande status | Granskningsuppgifter | Begärd status | Förväntat resultat |
|---|---|---|---|---|---|
| Ledare avslutar komplett ärende | Förundersökningsledare | Under granskning | Kompletta | Avslutat | Status ändras |
| Utredare försöker avsluta ärende | Utredare | Under granskning | Kompletta | Avslutat | Status ändras inte |
| Ledare avslutar ofullständigt ärende | Förundersökningsledare | Under granskning | Saknas | Avslutat | Status ändras inte och användaren får felmeddelande |
| Ledare återöppnar avslutat ärende | Förundersökningsledare | Avslutat | Kompletta | Pågående | Öppen fråga |

Återanvändbar regel om behörighetsstyrd sökning:

> En utredare får bara se uppgifter i ett ärende om utredaren tillhör rätt organisatorisk enhet, har tilldelats ärendet eller har en särskild behörighet som motiveras och loggas.

Dokumentationsprincip etablerad i kapitel 4:

| Typ av information | Användning |
|---|---|
| Verksamhetsregel | Beskriver principen i verksamhetens språk |
| Konkret exempel | Prövar att regeln tolkas lika av alla |
| Undantag | Synliggör specialfall eller variationer |
| Teknisk konsekvens | Hjälper IT att se vad beteendet kräver |
| Öppen fråga | Visar vad som behöver beslutas innan specifikationen är stabil |


## Kapitel 5: urval av funktionella krav för SBE

Kapitel 5 etablerar en urvalsmodell för funktionella krav som lämpar sig för SBE. Modellen ska återanvändas i senare kapitel när traditionella krav omvandlas till regler, exempel och scenarier.

### Prioriterade SBE-kandidater i caset

| Prioritet | Kandidat | Varför SBE? | Nästa steg |
|---|---|---|---|
| 1 | Filtrera sökresultat utifrån behörighet | Hög risk, många regler, flera roller | Exempelworkshop med utredare, test och utveckling |
| 2 | Visa sekretessmarkerade uppgifter | Rättssäkerhet och informationssäkerhet | Ta fram exempeltabell för roll, relation och behörighet |
| 3 | Ändra ärendestatus | Statusövergångar styr arbetsflödet | Skapa statusmatris |
| 4 | Logga åtkomst till känsliga uppgifter | Viktigt för spårbarhet och granskning | Skilj funktionellt beteende från kvalitetskrav |
| 5 | Skapa nytt ärende | Viktigt men initialt enklare | Dokumentera huvudflöde och några valideringsexempel |
| 6 | Spara vyinställningar | Låg verksamhetsrisk | Hantera med enklare kravtext |

### Återanvändbar urvalsregel

Ett funktionellt krav är en stark SBE-kandidat när det innehåller flera villkor, flera möjliga utfall, undantag, gränsfall, hög konsekvens vid fel eller behov av gemensam förståelse mellan verksamhet, IT och test.

### Exempel på statusövergångar

| Nuvarande status | Begärd ny status | Roll | Förväntat beteende |
|---|---|---|---|
| Nytt | Pågående | Utredare | Status ändras |
| Pågående | Granskningsklart | Utredare | Status ändras om obligatoriska uppgifter finns |
| Granskningsklart | Avslutat | Förundersökningsledare | Status ändras |
| Granskningsklart | Pågående | Förundersökningsledare | Status ändras med motivering |
| Avslutat | Pågående | Utredare | Statusändring nekas |
| Arkiverat | Pågående | Förundersökningsledare | Statusändring nekas |


## Kapitel 6: från traditionella krav till exempelbaserad specifikation

Kapitel 6 etablerar en transformationskedja för att gå från traditionell kravformulering till exempelbaserad specifikation.

Återkommande traditionellt krav:

> KR-124: Systemet ska visa sökresultat för utredningsärenden utifrån användarens behörighet.

Kapitlet använder kravet för att visa hur en enda kravmening kan delas upp i:

- syfte,
- verksamhetsregler,
- konkreta exempel,
- öppna frågor,
- tekniska konsekvenser.

Återanvändbar exempeltabell:

| Exempel | Roll | Relation till ärende | Enhet | Särskild åtkomstnivå | Sekretessmarkerat | Förväntat resultat | Loggning |
|---|---|---|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Annan | Nej | Nej | Ärendet visas | Nej |
| 2 | Utredare | Ingen relation | Samma | Nej | Nej | Ärendet visas | Nej |
| 3 | Utredare | Ingen relation | Annan | Nej | Nej | Ärendet visas inte | Nej |
| 4 | Utredare | Tilldelad | Annan | Nej | Ja | Begränsad information visas | Ja |
| 5 | Förundersökningsledare | Ansvarig | Annan | Ja | Ja | Full information visas | Ja |
| 6 | Analytiker | Registrerat stöduppdrag | Samma | Nej | Ja | Begränsad information visas | Ja |
| 7 | Administratör | Ingen relation | Samma | Nej | Ja | Ärendet visas inte | Nej |

Centrala öppna frågor från kapitlet:

- Vilka fält ingår i begränsad information?
- Ska sökning på exakt ärendenummer hanteras annorlunda än fritextsökning?
- Ska en användare med nekad åtkomst få ett meddelande eller bara se ett tomt resultat?
- Ska det finnas en särskild granskningsrapport över sökningar som gav sekretessmarkerade träffar?

Kapitlet etablerar även ett andra återkommande exempelområde: statusövergångar för utredningsärenden.

Återanvändbar statusregel:

> Ett avslutat ärende får inte ändras tillbaka till `Pågående` utan återöppningsbeslut.

Statusövergångstabellen kan återanvändas i kapitel 7 när regler, exempel och scenarier förfinas.

## Kapitel 7: regler, exempel och scenarier i praktiken

Kapitel 7 fördjupar skillnaden mellan regel, exempel och scenario.

Kärnprincip:

> En regel beskriver vad som ska gälla. Ett exempel visar vad regeln betyder i en konkret situation. Ett scenario visar hur beteendet uppstår över tid eller genom en interaktion.

Återanvändbar tumregel:

> Använd tabell när du jämför villkor. Använd scenario när du förklarar händelseförlopp.

Exempeltabell för åtkomst till sekretessmarkerade ärenden:

| Exempel | Roll | Relation till ärende | Enhet | Sekretessmarkerat | Särskild åtkomstnivå | Förväntat resultat |
|---|---|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Annan | Nej | Nej | Full information visas |
| 2 | Utredare | Tilldelad | Annan | Ja | Nej | Begränsad information visas |
| 3 | Utredare | Ingen relation | Samma | Nej | Nej | Full information visas |
| 4 | Utredare | Ingen relation | Samma | Ja | Nej | Begränsad information visas |
| 5 | Utredare | Ingen relation | Annan | Nej | Nej | Ärendet visas inte |
| 6 | Förundersökningsledare | Ansvarig | Annan | Ja | Ja | Full information visas |
| 7 | Analytiker | Registrerat stöduppdrag | Samma | Ja | Nej | Begränsad information visas |

Återanvändbart verksamhetsscenario:

```gherkin
Scenario: Tilldelad utredare söker fram ett sekretessmarkerat ärende
  Givet att ärende B-2025-0147 är sekretessmarkerat
  Och att utredare Sara Nyström är tilldelad ärendet
  När Sara söker på ärendenummer B-2025-0147
  Så visas ärendet i sökresultatet med begränsad information
  Och åtkomsten loggas
```

Återanvändbart statusövergångsscenario:

```gherkin
Scenario: Förundersökningsledare återöppnar ett avslutat ärende
  Givet att ärende B-2025-0221 har status Avslutat
  Och att ett återöppningsbeslut finns registrerat
  När förundersökningsledaren väljer att återöppna ärendet
  Så ändras ärendets status till Pågående
  Och systemet registrerar vem som återöppnade ärendet
  Och systemet registrerar tidpunkten för återöppningen
```

Centrala dokumentationsmönster som etableras:

1. Kort syfte.
2. Verksamhetsregel.
3. Exempel eller exempeltabell.
4. Eventuella scenarier.
5. Öppna frågor.
6. Tekniska konsekvenser.
7. Spårning till beslut, process eller förmåga.

Viktiga exempeltyper:

- normalexempel,
- gränsexempel,
- undantagsexempel,
- konfliktexempel,
- referensexempel.



## Kapitel 8: dokumentation som fungerar för både verksamhet och IT

Kapitel 8 etablerar att SBE-dokumentationen ska delas upp i tre lager:

- Verksamhetslager: syfte, behov och verksamhetsregler.
- Specifikationslager: regler, exempel, beslutstabeller och scenarier.
- Tekniskt lager: tekniska konsekvenser för design, implementation, test, integration och förvaltning.

Återkommande exempel från kapitlet:

| Område | Exempel |
|---|---|
| Regel | En användare som inte är tilldelad ett sekretessmarkerat ärende får endast se diarienummer, ärendestatus och ansvarig enhet i sökresultatet |
| Beslutstabell | Tilldelning, organisatorisk enhet och sekretessmarkering styr om full, begränsad eller ingen sökträff visas |
| Öppen fråga | Ska en användare i annan organisatorisk enhet kunna se att ett sekretessmarkerat ärende existerar |
| Teknisk konsekvens | Behörighetskontroll, åtkomstloggning och testdata behöver stödja kombinationer av tilldelning, enhet och sekretess |

Dokumentationsmönstret som introduceras i kapitlet:

1. Syfte
2. Omfattning
3. Verksamhetsregler
4. Exempel och beslutstabeller
5. Scenarier
6. Öppna frågor
7. Tekniska konsekvenser
8. Spårbarhet och status

Fortsatt canon-regel: tekniska konsekvenser får dokumenteras tydligt, men ska inte skrivas som om de vore verksamhetsregeln.


## Exempel etablerade i kapitel 9

### Exempelworkshop för arbetslista

Kapitel 9 etablerar en återkommande workshop där teamet utforskar vilka ärenden som ska visas i utredarens arbetslista.

Workshopens avgränsning:

> Vilka ärenden ska visas i utredarens arbetslista när utredaren loggar in?

Workshopen ska inte lösa hela behörighetsmodellen, hela sökfunktionen eller teknisk implementation.

### Startsexempel för arbetslista

| Fall | Förutsättning | Förväntat resultat |
|---|---|---|
| Utredare tillhör samma utredningsgrupp som ärendet | Ärendet är aktivt och inte särskilt spärrat | Ärendet visas i arbetslistan |
| Utredare tillhör annan grupp | Ingen delegation finns | Ärendet visas inte |
| Utredare har tillfällig delegation | Delegationen är giltig samma dag | Ärendet visas |

### Regler från workshop

| Regel | Beskrivning |
|---|---|
| R1 | Ett aktivt ärende visas om utredaren är tilldelad som handläggare |
| R2 | Ett ärende visas om utredaren har en giltig delegation för ärendet |
| R3 | Ett ärende visas om användaren är registrerad som ansvarig förundersökningsledare |
| R4 | Särskild sekretess överstyr R1, R2 och R3 om inte särskilt beslut om åtkomst finns |
| R5 | Utgången delegation ger inte åtkomst |
| R6 | Systemet ska inte exponera ärendets identitet i arbetslistan när användaren saknar åtkomst |

### Öppna frågor från workshop

| Öppen fråga | Varför den är viktig |
|---|---|
| Ska dold träff räknas i antal sökresultat? | Påverkar både användbarhet och informationssäkerhet |
| Hur snabbt ska spärrad åtkomst slå igenom? | Påverkar arkitektur, risk och användarupplevelse |
| Är delegation utan slutdatum tillåten? | Påverkar regel, datakrav och validering |
| Ska jäv blockera även förundersökningsledare? | Påverkar juridik, ansvar och behörighetsmodell |

### Workshopdeltagare

Följande roller används som standardexempel vid workshopar i caset:

- kravanalytiker som facilitator
- erfaren utredare som verksamhetsexpert
- förundersökningsledare eller produktägare som beslutsför roll
- testare som kvalitetsperspektiv
- utvecklare som realiserbarhets- och designperspektiv
- arkitekt, säkerhet eller juridik vid behov



## Kapitel 10: Verktygsnära specifikationer med Gherkin, Cucumber och Concordion

### Gherkin-scenario för arbetslista

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

### Exempeltabell för automationsurval

| Exempel-ID | Delegation | Särskild sekretess | Särskilt åtkomstbeslut | Förväntat resultat | Automationsstatus |
|---|---|---|---|---|---|
| ARB-E10 | Giltig | Nej | Nej | Ärendet visas | Automatiseras |
| ARB-E11 | Utgången | Nej | Nej | Ärendet visas inte | Automatiseras |
| ARB-E12 | Giltig | Ja | Nej | Ärendet visas inte | Automatiseras |
| ARB-E13 | Giltig | Ja | Ja | Ärendet visas | Vänta tills beslutsmodell är klar |

### Concordion-liknande specifikationsfall

För komplexa behörighets- och åtkomstregler kan en dokumentnära tabell vara tydligare än många Gherkin-scenarier.

| Tilldelad | Ansvarig FUL | Giltig delegation | Särskild sekretess | Särskilt beslut | Jäv/spärr | Visas |
|---|---|---|---|---|---|---|
| Ja | Nej | Nej | Nej | Nej | Nej | Ja |
| Nej | Ja | Nej | Nej | Nej | Nej | Ja |
| Nej | Nej | Ja | Nej | Nej | Nej | Ja |
| Nej | Nej | Ja | Ja | Nej | Nej | Nej |
| Nej | Nej | Ja | Ja | Ja | Nej | Ja |
| Ja | Nej | Nej | Nej | Nej | Ja | Nej |

### Beslutsregel för formatval

- Använd Gherkin när beteendet har tydligt utgångsläge, handling och observerbart resultat.
- Använd beslutstabell när många villkor och utfall behöver överblick.
- Använd Concordion-liknande dokumentation när text, begrepp och tabeller behöver vara läsbara tillsammans.
- Automatisera inte exempel innan regler och öppna frågor är tillräckligt stabila.


## Exempel etablerade i kapitel 11

### Samspel mellan krav, test och utveckling

Kapitel 11 etablerar att exempel används som gemensam arbetsyta mellan kravanalytiker, testare, utvecklare och verksamhet. Exempel ska kunna förstås av verksamheten och samtidigt ge testare och utvecklare tillräcklig precision för testdesign och implementation.

### Sökbehörighet som arbetsyta

Regeln om att en utredare får se ett ärende om utredaren tillhör ärendets ansvariga enhet eller är tilldelad ärendet används för att visa hur samma regel kan påverka krav, testdesign, automation och teknisk implementation.

### Exempel-ID:n för sökbehörighet

Kapitel 11 introducerar exempel-ID:n som `SOK-EX-01` till `SOK-EX-05` för att visa hur regler, exempel, tester och automatiserade scenarier kan kopplas ihop utan tung administration.

### Automation som medvetet val

Kapitel 11 etablerar principen att alla exempel inte ska automatiseras. Exempel bör automatiseras när beteendet är beslutat, observerbart, viktigt att regressionssäkra och tillräckligt stabilt.


## Exempel etablerade i kapitel 12

### Kvalitetsdimensioner för SBE-specifikationer

Kapitel 12 etablerar sex återkommande kvalitetsdimensioner för granskning av SBE-specifikationer:

- begriplighet
- precision
- täckning
- spårbarhet
- underhållbarhet
- beslutsmognad

Dessa dimensioner ska kunna återanvändas i senare kapitel, särskilt vid generella krav, icke-funktionella krav och införande i organisationen.

### Sökbehörighet som granskningsobjekt

Regelområdet sökbehörighet används som exempel på hur en specifikation kan granskas. Följande frågor återkommer:

- Får utredaren se ärendet?
- Ska ärendet döljas helt eller visas begränsat?
- Hur påverkar särskild sekretess utfallet?
- Hur påverkar jäv, spärr eller delegation utfallet?
- Är beteendet beslutat, antaget eller fortfarande öppet?

### Exempel-ID:n för kvalitetsgranskning

Kapitel 12 introducerar exempel-ID:n med prefixet `SOK-KV` för att visa hur exempel kan användas vid kvalitetsgranskning. Dessa exempel är analys- och granskningsankare snarare än nödvändigtvis färdiga automatiserade tester.

### Beslutsmognad

Kapitel 12 etablerar statusarna beslutat, antaget, öppen fråga, parkerat och ersatt. Dessa ska användas när specifikationen behöver visa om ett beteende är moget för implementation eller automation.

### Granskningsflöde

Kapitel 12 etablerar ett praktiskt granskningsflöde:

1. avgränsa regelområdet
2. identifiera regler
3. koppla exempel till regler
4. granska täckning
5. granska läsbarhet
6. besluta nästa åtgärd

Flödet kan återanvändas som arbetsmönster i senare kapitel och i bokens avslutande mallkapitel.


## Exempel och arbetsmönster etablerade i kapitel 13

### Generella regelområden i brottsutredningsstödet

Kapitel 13 etablerar följande återkommande regelområden som kan användas i senare kapitel:

- åtkomst och behörighetsdomän
- ärendestatus och statusövergångar
- loggning och händelsespår
- sökning och filtrering
- informationsvisning
- notifieringar
- export och utlämning
- hantering av skyddade uppgifter

### Behörighetsdomän som generell regel

Regeln om att åtkomst till ärende styrs av behörighetsdomän används som huvudexempel på ett generellt funktionellt krav. Den visar hur en central regel kan påverka sökning, direktlänkar, notifieringar, ärendeöversikt och export utan att hela regeln upprepas i varje scenario.

### Tomma och skyddade fält

Kapitel 13 etablerar standardbeteendet att frivilliga tomma fält kan döljas, obligatoriska saknade fält kan visas som “saknas” och behörighetsskyddade fält ska döljas när användaren saknar åtkomst. Detta exempel visar hur generella regler kan samspela och behöva prioriteras.

### Statusövergångar

Ärendestatus används som exempel på ett regelområde där beslutstabell ofta passar bättre än många nästan identiska scenarier. Tabellen över preliminärt, aktivt, avslutat och låst för juridisk granskning kan återanvändas vid senare resonemang om kvalitetskrav, förvaltning och ändringspåverkan.

### Arbetsmönster för generella krav

Kapitel 13 etablerar ett sjustegsflöde:

1. identifiera återkommande regler
2. namnge regelområdet
3. formulera regeln
4. ange räckvidd
5. ta fram exempel
6. koppla till berörda flöden
7. bestäm ägarskap och ändringshantering

Detta arbetsmönster ska återkomma i mallkapitlet.


## Exempel och arbetsmönster etablerade i kapitel 14

### Tre nivåer för kvalitetskrav

Kapitel 14 etablerar ett dokumentationsmönster för kvalitetskrav med tre nivåer:

1. verksamhetsexempel
2. mätbart kriterium
3. kompletterande riktlinje eller beslut

Mönstret ska återanvändas i senare mallar och vid kvalitetsgranskning.

### Svarstid för sökning

Brottsutredningsstödets sökning används som huvudexempel för prestandakrav. Kapitlet skiljer mellan exakt ärendenummersökning, personbaserad standardsökning, bred analytisk sökning och export av större urval. Dessa ska inte behandlas med ett enda generellt svarstidskrav.

### Säkerhet och informationsskydd

Kapitel 14 etablerar exempelområdet `SEC` för åtkomst till skyddade ärenden och visar hur säkerhetskrav bör konkretiseras med situation, relation, behörighetsdomän och förväntat resultat. Exempelområdet kan återanvändas vid senare granskning och mallar.

### Loggning och revisionsbarhet

Loggning behandlas som både generellt kravområde och kvalitetskrav. Kapitel 14 etablerar att loggningskrav bör beskriva händelse, verksamhetsexempel, logginnehåll och kvalitetskriterium.

### Robusthet vid externa beroenden

Kapitel 14 använder behörighetstjänst och dokumenttjänst som exempel på externa beroenden. Robusthetskrav ska beskriva verksamhetskonsekvens, förväntat systembeteende, loggning, larm och eventuell manuell hantering.

### Kvalitetskrav kopplade till funktionella områden

Kapitel 14 etablerar principen att kvalitetskrav ska kunna samlas centralt men länkas till funktionella regelområden. Sökning används som exempel med referenser till prestanda, informationsskydd, loggning och användbarhet.

### Automationsstatus för kvalitetskrav

Kapitel 14 etablerar följande statusar för verifiering av kvalitetskrav:

- ej automatiserat
- delvis automatiserat
- automatiserat i testmiljö
- övervakas i drift
- kräver periodisk granskning

## Införande av SBE

Kapitel 15 etablerar att SBE införs stegvis genom en praktisk förändringsresa, inte genom att först skapa en tung metodhandbok eller införa ett verktyg.

### Rekommenderat pilotområde

Brottsutredningsstödet använder “behörighetsstyrd ärendevisning” som återkommande exempel på ett lämpligt pilotområde. Området är viktigt, avgränsat, regelintensivt och begripligt för både verksamhet och IT.

### Alternativa pilotområden

Kapitel 15 nämner även ärendesökning, statusövergångar i utredningsflödet och registrering av åtgärder i ärendeloggen som möjliga pilotområden.

### Införandeprincip

Införandet ska börja med en konkret problembild, exempelvis sena missförstånd, dubbeldokumentation, otydliga regler, svag koppling mellan krav och test eller för sen involvering av juridik och informationssäkerhet.

### Verktygsmognad

Kapitel 15 etablerar principen att organisationen bör börja med exempel i naturligt språk och välja Gherkin, Cucumber, Concordion eller annan form först när arbetssättet och dokumentationsbehoven är tydliga.

### Dokumentationsägarskap

Kapitel 15 etablerar att SBE-specifikationen behöver en ägare efter leverans. I brottsutredningsstödet kan regler påverkas av verksamhetsprocesser, juridiska tolkningar, säkerhetsbeslut och organisationsförändringar.



## Mallar och arbetsmönster

Kapitel 16 etablerar en praktisk verktygslåda för resten av boken. Mallarna ska användas pragmatiskt och anpassas till situationen, inte införas som obligatoriska formulär.

### SBE-specifikationsmall

Grundmallen för ett funktionellt område innehåller syfte, läsare, omfattning, centrala begrepp, regler, exempel, scenarier, undantag, öppna frågor, kopplingar och ändringshistorik.

### Dokumentationspaket

Brottsutredningsstödet använder dokumentationspaket som princip för större områden. Exempel på paket är ärendesökning, ärendevisning, utredningsåtgärder, loggning och revision samt kvalitetskrav.

### Formatval

Kapitel 16 etablerar beslutsstödet att Gherkin passar tydliga beteendescenarier, Cucumber passar när sådana scenarier ska automatiseras, Concordion passar mer dokumentnära körbara specifikationer och icke-automatiserad dokumentation kan vara rätt när nyttan främst är förståelse, beslut eller granskning.

### Öppna frågor och beslut

Öppna frågor, beslut och antaganden ska dokumenteras separat. En fråga får inte döljas som brödtext och ett antagande får inte skrivas som om det vore ett beslut.

### Införandeprincip

Kapitel 16 sammanfattar införandet som ett arbetsmönster: välj pilotområde, formulera problem, samla roller, ta fram exempel, dokumentera, granska, välj automationsnivå, följ upp och skala stegvis.

## Redaktionella exempelprinciper efter helhetsgranskning

- Återanvänd caset med brottsutredningsstödet för att visa progression, inte för att introducera nya orelaterade funktioner i varje kapitel.
- Låt återkommande exempel visa skillnaden mellan verksamhetsregel, konkret exempel, scenario, testbar kontroll och öppen fråga.
- Använd myndighetskontexten för att förklara behörighet, spårbarhet och kvalitet utan att fastna i teknisk detaljdesign.
