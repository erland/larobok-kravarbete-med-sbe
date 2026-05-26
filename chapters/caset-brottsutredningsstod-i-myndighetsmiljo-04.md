# Kapitel 4: Caset: ett brottsutredningsstöd i myndighetsmiljö

## Varför detta kapitel finns

De första kapitlen har beskrivit varför traditionellt kravarbete kan skapa tolkningsutrymme, vad Specification by Example innebär och hur kravanalytikerns roll förändras när fokus flyttas från att producera kravtext till att möjliggöra gemensam förståelse. Nu behöver boken ett konkret sammanhang att arbeta i.

Det här kapitlet etablerar det genomgående caset: ett brottsutredningsstöd i en myndighetsmiljö. Caset är fiktivt, men utformat för att likna den typ av komplexitet som ofta uppstår i större offentliga verksamheter. Det innehåller flera användarroller, känslig information, behörighetsregler, juridiska ramar, arbetsflöden, spårbarhetskrav och behov av dokumentation som både verksamhet och IT kan lita på.

Syftet är inte att beskriva en verklig myndighets arbetssätt. Syftet är att skapa en realistisk övningsmiljö där vi kan visa hur SBE används för att analysera, dokumentera och kvalitetssäkra funktionella krav.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva varför ett domänrikt case gör SBE-arbetet mer konkret,
- identifiera centrala aktörer, informationsobjekt och arbetsflöden i caset,
- skilja mellan verksamhetskontext, systemgräns och specifika funktionella krav,
- se vilka delar av caset som lämpar sig väl för exempelbaserad specifikation,
- använda caset som grund för kommande kapitel om regler, scenarier, dokumentation och testbarhet.

## Innan vi börjar

När man arbetar enligt SBE är caset inte bara ett exempel att lägga bredvid kravtexten. Caset är en del av själva analysarbetet. Det hjälper deltagarna att ställa bättre frågor:

- Vem gör detta?
- I vilken situation?
- Med vilken information?
- Vilka regler styr beteendet?
- Vilka undantag finns?
- Vad ska systemet göra?
- Vad ska systemet inte göra?
- Vilka frågor är fortfarande öppna?

I traditionell kravdokumentation kan man ibland beskriva ett systemområde med generella formuleringar: "användaren ska kunna söka", "systemet ska visa relevanta träffar" eller "åtkomst ska styras av behörighet". I SBE behöver vi snabbare komma till konkreta situationer. Det betyder inte att all dokumentation måste vara scenarier. Det betyder att dokumentationen måste vara tillräckligt konkret för att olika parter ska kunna pröva om de menar samma sak.

Det genomgående caset i den här boken hjälper oss att göra just det.

## Caset i korthet

Myndigheten i caset arbetar med utredningar där flera typer av information behöver samlas, struktureras, granskas och delas på ett kontrollerat sätt. Organisationen har beslutat att ta fram ett nytt brottsutredningsstöd som ska hjälpa utredare och andra roller att arbeta mer effektivt och mer enhetligt.

Systemet ska inte ersätta allt arbete runt en utredning. Det ska stödja centrala delar av arbetet:

- att skapa och uppdatera utredningsärenden,
- att söka efter ärenden och uppgifter,
- att visa relevant information utifrån användarens behörighet,
- att hålla reda på status och ansvar,
- att logga åtkomst till känslig information,
- att ge underlag för granskning, beslut och uppföljning.

Det finns också tydliga begränsningar. Systemet ska inte fatta juridiska beslut på egen hand. Det ska inte avgöra skuldfrågor. Det ska inte automatiskt ge alla användare tillgång till all information. Det ska vara ett stöd för människor som arbetar i en reglerad verksamhet.

Redan här ser vi varför caset lämpar sig för SBE. Många krav verkar enkla när de formuleras abstrakt, men blir snabbt mer nyanserade när vi prövar dem med exempel.

## Verksamhetsmål

Det övergripande verksamhetsmålet är att ge utredare och beslutsfattare bättre stöd för att hitta, förstå och dokumentera relevant information i ett utredningsärende.

Det kan brytas ned i flera delmål:

- minska tiden det tar att hitta rätt ärende och rätt uppgifter,
- minska risken att känsliga uppgifter visas för fel användare,
- öka spårbarheten kring vem som har tagit del av information,
- göra ärendestatus och ansvar tydligare,
- skapa mer enhetlig dokumentation mellan olika organisatoriska enheter,
- ge testare, utvecklare och förvaltare tydligare regler att arbeta utifrån.

För kravanalytikern är detta viktigt. SBE börjar inte med formatet. Det börjar med att förstå vilket beteende som faktiskt behöver beskrivas. Om verksamhetsmålet är oklart riskerar exemplen att bli tekniska detaljer utan tydlig riktning.

## Systemets gräns

I caset avgränsar vi brottsutredningsstödet till ett verksamhetsnära IT-stöd. Det finns andra system runt omkring, men boken fokuserar på de delar där kravanalytikern behöver förstå funktionellt beteende.

Brottsutredningsstödet kan exempelvis behöva samverka med:

- ett identitets- och behörighetssystem,
- ett ärende- eller diariehanteringssystem,
- register eller informationskällor,
- logg- och uppföljningslösningar,
- dokumenthantering,
- rapport- eller beslutsstöd.

I SBE-dokumentation behöver systemgränsen vara tydlig. Annars blandas lätt tre olika saker ihop:

- vad användaren försöker göra,
- vad brottsutredningsstödet ansvarar för,
- vad andra system eller organisatoriska rutiner ansvarar för.

Ett exempel är behörighet. Brottsutredningsstödet kanske inte är källan till alla behörigheter. Däremot måste det använda behörighetsinformationen korrekt när det avgör vad en användare får se eller göra. Det är ett funktionellt beteende som kan beskrivas med exempel.

## Centrala aktörer

Caset använder ett antal återkommande aktörer. De är inte tänkta som kompletta rollbeskrivningar, utan som stabila analysobjekt i boken.

| Aktör | Primärt behov i systemet | Typiska frågor för SBE |
|---|---|---|
| Utredare | Söka, läsa, strukturera och uppdatera information i ärenden | Vilka ärenden får utredaren se? Vad får uppdateras? När ska åtkomst loggas? |
| Förundersökningsledare | Följa status, fatta eller dokumentera beslut och granska underlag | Vilka beslut kräver särskild behörighet? Vilka ändringar ska vara synliga för ledaren? |
| Analytiker | Se samband, sammanställa uppgifter och bidra med analysunderlag | Vilken information får analytikern se? Hur skiljer sig läsbehörighet från ändringsbehörighet? |
| Registrator eller administratör | Hantera metadata, klassificering och vissa administrativa uppgifter | Vilka fält får ändras administrativt? När påverkar metadata behörighet eller sökbarhet? |
| Systemförvaltare | Förstå regler, konfigurera delar av systemet och stödja förvaltning | Vilka regler måste vara dokumenterade så att de kan förvaltas över tid? |
| Testare | Använda regler och exempel som grund för testdesign och eventuell automation | Vilka exempel är tillräckligt precisa för att testas? Var finns öppna frågor? |
| Utvecklare | Implementera beteenden utifrån regler, exempel och tekniska förutsättningar | Vad är verksamhetsregel, vad är teknisk konsekvens och vad är oklart? |

Tabellen visar varför dokumentationen måste fungera för flera målgrupper. En verksamhetsrepresentant behöver känna igen situationen. En utvecklare behöver förstå vilket beteende som ska implementeras. En testare behöver kunna se vad som är prövbart. En förvaltare behöver förstå varför regeln finns och hur den kan förändras.

## Centrala informationsobjekt

Ett brottsutredningsstöd kretsar kring flera informationsobjekt. För bokens syfte räcker det att etablera några återkommande objekt.

| Informationsobjekt | Beskrivning | Exempel på kravfrågor |
|---|---|---|
| Utredningsärende | Sammanhållen struktur för en utredning | När skapas ett ärende? Vem får se ärendet? Vilka statusar finns? |
| Uppgift | En informationsdel som kan höra till ett ärende | När är en uppgift känslig? Hur visas den i sökresultat? |
| Personkoppling | Koppling mellan ärende och person | När får kopplingen visas? Hur hanteras skyddade uppgifter? |
| Organisatorisk enhet | Enhet som användare och ärenden kan tillhöra | Hur påverkar enhet behörighet? |
| Tilldelning | Relation mellan användare och ärende | När ger tilldelning läs- eller ändringsrätt? |
| Åtkomstlogg | Spår av vem som har tagit del av viss information | Vad ska loggas? När ska loggning ske? |
| Ärendestatus | Markering av var ärendet befinner sig i arbetsflödet | Vilka statusövergångar är tillåtna? |

Dessa objekt är medvetet verksamhetsnära. De är inte databasmodeller. De är begrepp som verksamhet och IT behöver kunna samtala om. Senare i boken kan de kopplas till regler, exempel, scenarier och testfall.

## Ett första funktionsområde: söka efter ärenden

För att göra caset konkret börjar vi med ett funktionsområde som återkommer i flera kapitel: sökning efter utredningsärenden.

En traditionell kravformulering skulle kunna vara:

> En utredare ska kunna söka efter utredningsärenden och se ärenden som utredaren har behörighet till.

Formuleringen är inte fel. Den är bara för grov för att bära hela förståelsen. Den väcker flera frågor:

- Vad innebär det att söka efter ett ärende?
- Vilka sökbegrepp ska kunna användas?
- Vad innebär behörighet?
- Ska användaren se att det finns träffar som inte får visas?
- Ska åtkomst loggas redan vid sökning eller först när ett ärende öppnas?
- Vad händer om användaren är tillfälligt tilldelad ett ärende?
- Vad händer om ärendet är sekretessmarkerat?
- Ska förundersökningsledare och utredare ha samma sökbeteende?

SBE gör dessa frågor synliga tidigare. I stället för att bara diskutera om kravet är "godkänt" arbetar gruppen med konkreta situationer.

Ett första exempel kan vara:

| Exempel | Användare | Relation till ärende | Ärendets markering | Förväntat resultat |
|---|---|---|---|---|
| Sökning i egen enhet | Utredare A | Ärendet tillhör samma enhet | Ingen särskild markering | Ärendet visas |
| Sökning på tilldelat ärende | Utredare A | Utredaren är tilldelad ärendet | Ingen särskild markering | Ärendet visas |
| Sökning utan relation | Utredare A | Ingen relation till ärendet | Ingen särskild markering | Ärendet visas inte |
| Sökning på sekretessmarkerat ärende | Utredare A | Samma enhet | Sekretessmarkerat | Öppen fråga: visas ärendet, döljs det eller visas begränsad information? |

Det fjärde exemplet är särskilt viktigt. Ett exempel behöver inte alltid ge ett färdigt svar. I analysfasen kan ett exempel lika gärna visa att gruppen saknar ett beslut. Då ska dokumentationen inte låtsas vara komplett. Den ska synliggöra den öppna frågan.

## Ett andra funktionsområde: statusövergångar

Ett annat område som lämpar sig väl för SBE är statusövergångar. Anta att ett utredningsärende kan ha flera statusar, till exempel:

- Nytt,
- Pågående,
- Vilande,
- Under granskning,
- Avslutat.

Ett traditionellt krav skulle kunna vara:

> Systemet ska stödja statusändringar för utredningsärenden enligt gällande arbetsflöde.

Även här låter kravet rimligt, men det är svårt att implementera och testa utan mer konkretisering. Vad är "gällande arbetsflöde"? Vem får ändra status? Finns det krav på motivering? Får ett avslutat ärende återöppnas?

I SBE kan man börja med en enkel regel:

> Ett ärende får bara ändras till "Avslutat" av en förundersökningsledare, och bara om obligatoriska granskningsuppgifter är ifyllda.

Sedan prövas regeln med exempel:

| Exempel | Roll | Nuvarande status | Granskningsuppgifter | Begärd status | Förväntat resultat |
|---|---|---|---|---|---|
| Ledare avslutar komplett ärende | Förundersökningsledare | Under granskning | Kompletta | Avslutat | Status ändras |
| Utredare försöker avsluta ärende | Utredare | Under granskning | Kompletta | Avslutat | Status ändras inte |
| Ledare avslutar ofullständigt ärende | Förundersökningsledare | Under granskning | Saknas | Avslutat | Status ändras inte och användaren får felmeddelande |
| Ledare återöppnar avslutat ärende | Förundersökningsledare | Avslutat | Kompletta | Pågående | Öppen fråga |

Exemplen hjälper gruppen att skilja mellan tre saker:

- den verksamhetsregel som styr arbetet,
- systemets förväntade beteende,
- beslut som ännu inte är fattade.

Detta är en av de viktigaste vinsterna med caset. Det ger oss återkommande situationer där SBE inte bara blir ett dokumentationsformat, utan ett analysverktyg.

## Ett tredje funktionsområde: åtkomstloggning

Åtkomstloggning är ett bra exempel på ett område där funktionella krav, generella krav och icke-funktionella krav lätt blandas ihop.

Ett krav kan formuleras så här:

> Systemet ska logga åtkomst till känsliga uppgifter.

Det är ett viktigt krav, men det räcker inte. Gruppen behöver förstå vilket beteende som ska ske i konkreta situationer:

- Ska sökning loggas?
- Ska öppning av ärende loggas?
- Ska visning av sökresultat loggas om känsliga uppgifter inte visas?
- Ska export av uppgifter loggas annorlunda än läsning?
- Ska nekad åtkomst loggas?
- Vilka uppgifter ska loggen innehålla?
- Vem får läsa loggen?

Vissa delar kan beskrivas med exempelbaserad specifikation. Andra delar kan behöva kompletteras med säkerhetskrav, tekniska riktlinjer eller juridiska krav.

Ett exempelbaserat första steg kan vara:

| Exempel | Handling | Informationstyp | Åtkomstresultat | Förväntad loggning |
|---|---|---|---|---|
| Utredare öppnar vanligt ärende | Öppnar ärende | Ej särskilt känsligt | Tillåten | Grundläggande åtkomst loggas |
| Utredare öppnar skyddad uppgift | Öppnar uppgift | Särskilt skyddsvärd | Tillåten | Åtkomst loggas med motivering |
| Utredare nekas åtkomst | Försöker öppna ärende | Sekretessmarkerat | Nekad | Nekat försök loggas |
| Utredare ser sökresultat utan känsliga fält | Söker ärende | Blandade uppgifter | Tillåten sökning | Öppen fråga |

Detta exempel kommer senare att vara användbart när vi diskuterar generella krav och icke-funktionella krav. Det visar att vissa krav är funktionella i den meningen att systemet ska göra något observerbart. Samtidigt kan kravet hänga ihop med säkerhet, spårbarhet, juridik och arkitektur.

## Verksamhetsregel, exempel och teknisk konsekvens

I SBE-arbete är det viktigt att inte blanda ihop allt som sägs i en workshop. Caset hjälper oss att separera olika typer av information.

Anta att gruppen diskuterar följande:

> En utredare får bara se uppgifter i ett ärende om utredaren tillhör rätt organisatorisk enhet, har tilldelats ärendet eller har en särskild behörighet som motiveras och loggas.

Detta kan dokumenteras på flera nivåer.

| Typ av information | Exempel från caset | Hur den bör användas |
|---|---|---|
| Verksamhetsregel | Utredare får se ärendet vid rätt enhet, tilldelning eller särskild behörighet | Beskriver principen i verksamhetens språk |
| Konkret exempel | Utredare A från enhet Nord söker ärende 1001 som tillhör enhet Nord och får träff | Prövar att regeln tolkas lika av alla |
| Undantag | Sekretessmarkerat ärende inom samma enhet kanske ändå inte ska visas | Synliggör specialfall eller öppet beslut |
| Teknisk konsekvens | Systemet måste kunna avgöra enhet, tilldelning och särskild behörighet vid sökning | Hjälper IT att förstå vad beteendet kräver |
| Öppen fråga | Ska nekade sökresultat synas som "träff dold" eller inte synas alls? | Behöver beslut innan specifikationen är komplett |

Detta sätt att dela upp dokumentationen är centralt i boken. SBE betyder inte att allt ska skrivas som Given-When-Then. Det betyder att dokumentationen ska bära både förståelse och precision.

## Vad caset inte ska göra

Ett bra case måste också ha gränser. Annars riskerar boken att växa åt fel håll.

Caset ska inte användas för att:

- beskriva verkliga brottsutredningsprocesser i detalj,
- ge juridisk vägledning,
- simulera en fullständig myndighetsarkitektur,
- definiera en komplett informationsmodell,
- visa all testautomation som krävs i ett riktigt system,
- låsa boken till ett visst verktyg eller en viss teknisk plattform.

Caset ska användas för att visa kravarbete. När vi senare använder Gherkin, Cucumber eller Concordion är syftet därför inte att bygga en komplett testsvit. Syftet är att visa hur exempel kan bli mer precisa, mer prövbara och mer användbara i samarbetet mellan verksamhet och IT.

## Hur caset används i resten av boken

I de kommande kapitlen återkommer caset på flera sätt.

Kapitel 5 använder caset för att visa hur man hittar funktionella krav som lämpar sig för SBE. Där kommer vi att skilja mellan funktioner som bör beskrivas med exempel och områden där annan dokumentation är bättre.

Kapitel 6 visar hur traditionella kravformuleringar om sökning, behörighet och status kan omvandlas till exempelbaserade specifikationer.

Kapitel 7 fördjupar arbetet med regler, exempel och scenarier. Då blir caset mer detaljerat och vi arbetar med gränsfall, variationer och felvägar.

Kapitel 8 fokuserar på dokumentationsstruktur. Där använder vi caset för att visa hur samma specifikation kan vara läsbar för verksamheten och samtidigt användbar för IT.

Kapitel 9 använder caset som underlag för exempelworkshops. Vi tittar på vilka frågor som bör ställas, vilka deltagare som behövs och hur öppna frågor dokumenteras.

Kapitel 10 använder delar av caset för att visa Gherkin, Cucumber och Concordion på en kravanalytikernivå.

Kapitel 13 och 14 återvänder till behörighet, loggning och kvalitetsegenskaper för att visa hur generella krav och icke-funktionella krav behöver hanteras mer nyanserat än vanliga funktionella flöden.

## Vanliga misstag

- **Misstag: Att göra caset för verklighetstroget.**
  - Varför det händer: Domänen känns viktig, och deltagare med erfarenhet vill gärna fylla på med fler undantag.
  - Hur du undviker det: Håll caset tillräckligt realistiskt för att skapa bra kravdiskussioner, men inte så omfattande att boken blir en domänhandbok.

- **Misstag: Att börja med verktygsformat för tidigt.**
  - Varför det händer: SBE kopplas ofta snabbt till Gherkin, Cucumber eller automatiserade tester.
  - Hur du undviker det: Börja med regler, exempel och öppna frågor. Välj format först när gruppen förstår vad som behöver beskrivas.

- **Misstag: Att blanda verksamhetsregel och teknisk lösning.**
  - Varför det händer: IT behöver tekniska detaljer, och de hamnar lätt i samma text som verksamhetsregeln.
  - Hur du undviker det: Separera verksamhetsregel, exempel, teknisk konsekvens och öppna frågor i dokumentationen.

- **Misstag: Att behandla öppna frågor som svagheter.**
  - Varför det händer: Kravdokument uppfattas ofta som något som ska vara färdigt och komplett.
  - Hur du undviker det: Se öppna frågor som en legitim analysartefakt. De visar var mer beslut eller domänkunskap behövs.

## Övningar

### Övning 1: Identifiera frågor bakom ett enkelt krav

Utgå från kravet:

> En användare ska kunna söka efter utredningsärenden.

Skriv ned minst tio frågor som behöver besvaras innan kravet kan beskrivas som en användbar SBE-specifikation.

Dela gärna upp frågorna i kategorier:

- aktör,
- behörighet,
- sökbegrepp,
- visning av resultat,
- känslig information,
- loggning,
- öppna beslut.

### Övning 2: Skilj mellan regel, exempel och öppen fråga

Utgå från regeln:

> En utredare får se ärenden som tillhör den egna organisatoriska enheten.

Skriv tre konkreta exempel:

1. ett exempel där ärendet ska visas,
2. ett exempel där ärendet inte ska visas,
3. ett exempel som väcker en öppen fråga.

Markera sedan vad som är verksamhetsregel, vad som är exempel och vad som behöver beslutas.

### Fördjupning

Välj ett eget systemområde från din organisation där behörighet, status eller känslig information spelar roll. Beskriv området med:

- en kort verksamhetskontext,
- tre centrala aktörer,
- tre informationsobjekt,
- två funktionella krav som verkar enkla men sannolikt kräver exempel.

Syftet är inte att skriva färdiga scenarier. Syftet är att träna på att se vilka delar av en domän som behöver konkretiseras innan dokumentationen blir användbar.

## Snabb sammanfattning

- Caset i boken är ett fiktivt brottsutredningsstöd i myndighetsmiljö.
- Caset används för att visa realistiskt kravarbete utan att beskriva en verklig myndighets interna processer.
- Centrala aktörer är bland annat utredare, förundersökningsledare, analytiker, administratör, systemförvaltare, testare och utvecklare.
- Centrala informationsobjekt är bland annat utredningsärende, uppgift, personkoppling, organisatorisk enhet, tilldelning, åtkomstlogg och ärendestatus.
- Sökning, statusövergångar och åtkomstloggning är återkommande funktionsområden i boken.
- Caset hjälper oss att skilja mellan verksamhetsregel, konkret exempel, teknisk konsekvens och öppen fråga.
- Ett exempel som visar en öppen fråga är värdefullt, eftersom det synliggör ett beslut som annars kan bli ett sent missförstånd.

## Quiz/reflektionsfrågor

1. Varför är ett realistiskt case särskilt användbart i SBE-arbete?
2. Vilken risk uppstår om systemgränsen är otydlig?
3. Vad är skillnaden mellan ett informationsobjekt och en teknisk databasmodell i detta kapitel?
4. Varför är "en användare ska kunna söka efter ärenden" inte tillräckligt som komplett krav?
5. Hur kan ett exempel användas för att synliggöra en öppen fråga?
6. Varför bör verksamhetsregel och teknisk konsekvens dokumenteras så att de går att skilja åt?
7. Vilka delar av åtkomstloggning kan vara funktionella krav, och vilka delar kan behöva annan typ av dokumentation?

## Koppling till bokens röda tråd

Brottsutredningsstödet används inte som ett fullständigt systemförslag, utan som en stabil domän att pröva arbetssättet i. När samma ärendeflöden, sökregler, behörigheter och loggningsbehov återkommer i senare kapitel blir det lättare att se hur SBE-dokumentation utvecklas över tid.


## Nästa steg

Nu har boken ett gemensamt case att återvända till. Nästa kapitel använder caset för att undersöka hur man hittar funktionella krav som lämpar sig för SBE. Fokus flyttas då från sammanhanget till urvalet: vilka delar av en verksamhetsförmåga bör beskrivas med regler, exempel och scenarier, och vilka delar bör dokumenteras på annat sätt?
