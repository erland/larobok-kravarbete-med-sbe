# Kapitel 3: Kravanalytikerns förändrade roll

## Varför detta kapitel finns

När ett team börjar arbeta med SBE förändras inte bara dokumentationsformen. Arbetssättet förändrar också kravanalytikerns roll.

I traditionellt kravarbete blir kravanalytikern ofta den person som samlar in information, tolkar verksamhetens behov, formulerar kraven, skriver acceptanskriterier och skickar vidare ett underlag till utveckling och test. I bästa fall sker det i nära dialog. I sämre fall blir kravanalytikern en översättare mellan flera grupper som inte riktigt möts.

SBE flyttar tyngdpunkten. Kravanalytikern ska fortfarande kunna analysera, strukturera och dokumentera. Men det viktigaste bidraget blir att skapa förutsättningar för gemensam förståelse. Det innebär att leda samtal där verksamhet, IT, test och andra intressenter upptäcker regler, exempel, undantag och öppna frågor tillsammans.

Det här kapitlet visar vad den förändringen betyder i praktiken.

## Lärandemål

Efter kapitlet ska du kunna:

- Beskriva hur kravanalytikerns roll förändras i ett SBE-arbetssätt.
- Skilja mellan att samla in krav och att facilitera upptäckt av krav.
- Förklara varför gemensam förståelse behöver skapas innan dokumentationen stabiliseras.
- Identifiera vilka samtal, frågor och artefakter kravanalytikern behöver styra.
- Känna igen vanliga fallgropar när en organisation försöker införa SBE men behåller ett traditionellt kravbeteende.

## Innan vi börjar

Du som läser kan sannolikt redan skriva tydliga krav och acceptanskriterier. Du är kanske van vid att intervjua verksamhet, hålla kravworkshops, dokumentera beslut, hantera ändringar och se till att kraven går att granska.

Den kompetensen är fortfarande värdefull. SBE gör den inte obsolet. Däremot förändras vad kompetensen ska användas till.

I ett traditionellt upplägg kan kravanalytikern fråga:

- Vad ska systemet kunna göra?
- Vilka acceptanskriterier gäller?
- Vilka undantag ska dokumenteras?
- Vem ska godkänna kravet?

I ett SBE-upplägg behöver kravanalytikern oftare fråga:

- Vilka konkreta situationer visar vad regeln betyder?
- Vilka exempel skulle olika roller tolka olika?
- Vilka antaganden gör vi just nu utan att säga dem högt?
- Vilka exempel måste verksamheten kunna känna igen?
- Vilka exempel behöver IT för att kunna designa, implementera och testa rätt beteende?
- Vilka frågor är fortfarande öppna, och vem behöver besvara dem?

Det är en annan sorts arbete. Det är mindre dokumentinsamling och mer gemensam precisering.

## Huvudförklaring

### Från kravskrivare till förståelsefacilitator

Ett vanligt missförstånd är att SBE främst handlar om att skriva krav i ett nytt format. Då kan organisationen försöka byta från acceptanskriterier till Given-When-Then utan att förändra arbetssättet. Resultatet blir ofta att gamla problem får ny syntax.

Kravanalytikerns viktigaste roll i SBE är därför inte att ensam skriva perfekta scenarier. Rollen är att hjälpa gruppen att komma fram till vilka regler, exempel och undantag som faktiskt beskriver rätt beteende.

Det kan beskrivas som en förflyttning:

| Traditionell tyngdpunkt | SBE-tyngdpunkt |
|---|---|
| Samla in krav från verksamheten | Utforska beteende tillsammans med verksamhet och IT |
| Skriva krav som överlämnas | Skapa gemensam specifikation som flera roller äger |
| Formulera acceptanskriterier i efterhand | Använda exempel tidigt för att upptäcka oklarheter |
| Dokumentera beslut | Dokumentera regler, exempel, antaganden och öppna frågor |
| Säkerställa att kravet är komplett | Säkerställa att specifikationen är begriplig, testbar och användbar |

Förflyttningen är inte en degradering av kravanalytikerns ansvar. Tvärtom kräver den högre analytisk skärpa. Skillnaden är att analysen sker mer öppet och mer kollaborativt.

### Kravanalytikern äger inte sanningen

I ett traditionellt arbetssätt kan kravdokumentet lätt uppfattas som kravanalytikerns produkt. Verksamheten ger input. IT får dokumentet. Test härleder testfall. Kravanalytikern håller ihop helheten.

I SBE bör specifikationen inte uppfattas som en persons dokument. Den ska vara en gemensam artefakt. Kravanalytikern har fortfarande ansvar för struktur, kvalitet och progression, men inte för att ensam vara sanningskälla.

Det är särskilt viktigt i komplexa domäner, som ett brottsutredningsstöd i myndighetsmiljö. Där kan ingen enskild person fullt ut äga alla perspektiv.

En utredare kan förstå det operativa arbetet. En förundersökningsledare kan förstå beslutsansvar och undantag. En säkerhetsspecialist kan förstå åtkomst och loggning. En testare kan se testbarhet. En utvecklare kan se tekniska konsekvenser. En arkitekt kan se förvaltningsbarhet och systemgränser.

Kravanalytikerns uppgift blir att få dessa perspektiv att mötas utan att samtalet blir för brett, för tekniskt eller för abstrakt.

### Från intervju till exempelarbete

Intervjuer är fortfarande användbara, men de räcker sällan som huvudarena för SBE. En intervju kan ge bakgrund, målbild och problemförståelse. Den kan också hjälpa kravanalytikern att förbereda en workshop.

Men de avgörande upptäckterna sker ofta när flera roller ser samma exempel samtidigt.

Anta att en utredare säger:

> Jag ska kunna se alla ärenden som är relevanta för min utredning.

I en intervju kan kravanalytikern följa upp med frågor och skriva ett krav. I SBE behöver formuleringen snabbt göras konkret.

Exempel att pröva:

| Situation | Användare | Ärende | Förväntat resultat |
|---|---|---|---|
| Utredaren är tilldelad ärendet | Utredare | Ärende A | Ärendet visas |
| Utredaren arbetar i samma utredningsgrupp | Utredare | Ärende B | Ärendet visas med normal detaljnivå |
| Utredaren tillhör annan region men har särskild åtkomst | Utredare | Ärende C | Ärendet visas och åtkomsten loggas |
| Utredaren saknar relation till ärendet | Utredare | Ärende D | Ärendet visas inte |
| Ärendet är sekretessmarkerat | Utredare | Ärende E | Endast begränsad information visas |

När exemplen diskuteras tillsammans kan flera saker hända. Verksamheten kan upptäcka att “relevant” inte är en regel utan flera regler. Testaren kan se att förväntat resultat behöver vara tydligare. Utvecklaren kan fråga var särskild åtkomst kommer ifrån. Säkerhetsspecialisten kan påpeka att åtkomst till sekretessmarkerade ärenden alltid måste loggas.

Det är här SBE skapar värde. Inte genom att kravanalytikern i efterhand skriver ett snyggare krav, utan genom att gruppen upptäcker regelns faktiska form.

### Kravanalytikerns nya huvuduppgifter

I ett SBE-arbetssätt kan kravanalytikerns arbete sammanfattas i sex huvuduppgifter.

### 1. Rama in beteendet som ska utforskas

SBE fungerar bäst när samtalet har en tydlig avgränsning. Om workshopen heter “behörigheter i brottsutredningsstödet” blir den för bred. Om den heter “när ett ärende ska visas i sökresultat” blir den lättare att konkretisera.

Kravanalytikern behöver därför rama in vilket beteende som ska utforskas.

Bra avgränsningar kan vara:

- Visa eller dölja ärenden i sökresultat.
- Skapa nytt utredningsärende.
- Ändra status från pågående till vilande.
- Markera uppgift som skyddsvärd.
- Logga åtkomst till känsliga uppgifter.
- Generera beslutsunderlag för granskning.

Då blir det möjligt att hitta konkreta exempel utan att försöka lösa hela domänen samtidigt.

### 2. Locka fram regler genom exempel

Många verksamhetsregler uttrycks först som allmänna formuleringar:

- “Endast behöriga användare får se uppgifterna.”
- “Systemet ska visa relevanta ärenden.”
- “En ändring ska loggas vid behov.”
- “Handläggaren ska kunna göra en rimlighetskontroll.”

Kravanalytikerns uppgift är att inte nöja sig med formuleringen. Den behöver göras prövbar.

Frågor som hjälper:

- Ge ett konkret exempel där användaren får se uppgiften.
- Ge ett exempel där användaren inte får se uppgiften.
- Vad är skillnaden mellan de två exemplen?
- Finns det någon roll som bryter huvudregeln?
- Vad händer om två regler pekar åt olika håll?
- Vilket resultat skulle vara fel men ändå lätt att råka implementera?

När gruppen svarar på frågorna börjar den egentliga regeln framträda.

### 3. Synliggöra antaganden

SBE gör antaganden synliga. Det är en av metodens största styrkor, men också en av orsakerna till att arbetssättet kan kännas ovant.

I traditionellt kravarbete kan ett antagande ligga dolt länge. En verksamhetsrepresentant antar att “behörig” betyder tilldelad utredare. En utvecklare antar att det betyder roll i behörighetssystemet. En testare antar att det betyder medlemskap i en organisatorisk enhet. Alla läser samma ord men ser olika regler.

Kravanalytikern behöver aktivt leta efter sådana skillnader.

Tecken på dolda antaganden är formuleringar som:

- “Det är självklart att ...”
- “Normalt gör man så här ...”
- “Det borde systemet förstå ...”
- “Det gäller bara vissa ärenden ...”
- “Det beror på behörigheten ...”
- “Det är en verksamhetsregel sedan tidigare ...”

Dessa formuleringar är inte problem i sig. De är signaler om att det finns mer att utforska.

### 4. Hålla isär regel, exempel, beslut och öppen fråga

En SBE-specifikation blir snabbt svår att använda om allt blandas ihop. Kravanalytikern behöver hjälpa gruppen att skilja mellan olika typer av innehåll.

En enkel struktur är:

| Typ av innehåll | Syfte | Exempel |
|---|---|---|
| Regel | Beskriver principen som styr beteendet | En utredare får se ett ärende om utredaren är tilldelad ärendet |
| Exempel | Visar ett konkret fall av regeln | Utredare A är tilldelad ärende 1001 och ärendet visas |
| Beslut | Dokumenterar ett val som gruppen gjort | Samma organisatoriska enhet räcker inte för full åtkomst |
| Öppen fråga | Markerar något som inte är avgjort | Ska historisk tilldelning ge läsrätt efter avslutad utredning? |
| Teknisk konsekvens | Fångar IT-relevant följd utan att gömma verksamhetsregeln | Åtkomstbeslut behöver kunna spåras i logg |

Den här uppdelningen hjälper både verksamhet och IT. Verksamheten kan granska regler och exempel. IT kan se tekniska konsekvenser och öppna frågor utan att behöva gissa.

### 5. Förvalta dokumentationen som arbetsyta

I SBE är dokumentation inte bara en leverans i slutet av analysen. Dokumentationen är en arbetsyta där förståelsen växer fram.

Det betyder att den behöver vara användbar innan den är perfekt.

En tidig specifikation kan innehålla:

- En preliminär regel.
- Tre bekräftade exempel.
- Två exempel som fortfarande diskuteras.
- En öppen fråga till juridik eller informationssäkerhet.
- Ett beslut från senaste workshopen.
- En markering om att Gherkin-format inte är valt ännu.

Det är bättre än ett välformulerat krav som låtsas vara färdigt men döljer osäkerheter.

Kravanalytikern behöver därför skapa en dokumentationskultur där osäkerhet får synas. Öppna frågor är inte ett misslyckande. De är ett tecken på att teamet har hittat något som behöver besvaras innan utveckling eller test bygger på fel antagande.

### 6. Skydda specifikationen från både över- och underdetaljering

SBE kan misslyckas åt två håll.

Det ena felet är underdetaljering. Då skrivs exempel som är så allmänna att de inte hjälper någon.

Exempel:

| Situation | Förväntat resultat |
|---|---|
| Behörig användare söker ärende | Rätt ärenden visas |

Det säger nästan ingenting. Det ersätter en abstrakt kravformulering med ett abstrakt exempel.

Det andra felet är överdetaljering. Då försöker teamet beskriva varje möjlig kombination av data, roller, statusar och undantag. Specifikationen blir tung att läsa och svår att underhålla.

Kravanalytikerns uppgift är att hitta en användbar detaljnivå. Ett bra exempel ska vara konkret nog för att avslöja tolkning, men inte så detaljerat att det bara beskriver testdata.

Frågan är inte “har vi dokumenterat allt?”. Frågan är:

> Har vi dokumenterat tillräckligt för att verksamhet, utveckling och test ska förstå samma beteende och upptäcka viktiga missförstånd i tid?

## Exempel: rollförändringen i brottsutredningsstödet

Vi använder nu caset om brottsutredningsstödet.

### Utgångsläge

Organisationen har tidigare arbetat med traditionella krav. Ett krav i en kravlista lyder:

> Systemet ska säkerställa att endast behöriga användare kan öppna ett utredningsärende.

Till kravet finns acceptanskriterier:

- Användare med behörighet ska kunna öppna ärendet.
- Användare utan behörighet ska inte kunna öppna ärendet.
- Åtkomst till sekretessmarkerade ärenden ska loggas.

Kravet är inte dåligt. Men det räcker inte för att utveckling och test ska veta exakt vad som ska byggas och kontrolleras.

### Traditionellt arbetssätt

I ett traditionellt arbetssätt skulle kravanalytikern kanske intervjua verksamheten, skriva om kravet, lägga till acceptanskriterier och skicka det på granskning.

En förbättrad formulering kan bli:

> En användare ska kunna öppna ett utredningsärende om användaren är tilldelad ärendet, har ansvarig roll i ärendet eller har en särskild behörighet. Om ärendet är sekretessmarkerat ska åtkomsten loggas.

Det är tydligare, men flera frågor kvarstår:

- Vad betyder ansvarig roll?
- Gäller särskild behörighet alla ärenden eller bara vissa kategorier?
- Ska tilldelning räcka även om ärendet är avslutat?
- Vad ska användaren se om åtkomst nekas?
- Ska nekade åtkomstförsök loggas?
- Vad visas i sökresultat innan användaren försöker öppna ärendet?

### SBE-arbetssätt

I ett SBE-arbetssätt använder kravanalytikern kravet som startpunkt, inte som slutprodukt. Nästa steg är att facilitera ett exempelarbete.

Kravanalytikern kan rama in samtalet:

> Vi ska inte försöka lösa hela behörighetsmodellen nu. Vi ska fokusera på beteendet “öppna utredningsärende” och ta fram exempel som visar när åtkomst ska beviljas, nekas och loggas.

Sedan kan gruppen arbeta med exempel:

| Exempel | Roll | Relation till ärende | Ärendestatus | Sekretessmarkerat | Förväntat resultat |
|---|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Pågående | Nej | Ärendet öppnas |
| 2 | Utredare | Ingen relation | Pågående | Nej | Åtkomst nekas |
| 3 | Förundersökningsledare | Ansvarig | Pågående | Ja | Ärendet öppnas och åtkomst loggas |
| 4 | Utredare | Tidigare tilldelad | Avslutat | Nej | Öppen fråga |
| 5 | Analytiker | Särskild behörighet | Pågående | Ja | Ärendet öppnas med begränsad vy och åtkomst loggas |

Den viktigaste raden är kanske inte någon av de bekräftade raderna. Det kan vara rad 4: “Öppen fråga”. Den visar att gruppen inte är överens eller att beslut saknas. I traditionell dokumentation kan den typen av osäkerhet döljas. I SBE ska den synas.

### Vad kravanalytikern faktiskt gör

I exemplet ovan gör kravanalytikern flera saker samtidigt:

- Avgränsar samtalet till ett beteende.
- Ser till att rätt roller deltar.
- Hjälper gruppen att formulera exempel.
- Fångar regler som blir synliga.
- Markerar öppna frågor utan att fylla i med egna antaganden.
- Skiljer verksamhetsregel från teknisk konsekvens.
- Förbereder material som senare kan bli dokumentation, testunderlag eller automatiserbar specifikation.

Det är en mer aktiv och mer faciliterande roll än att bara skriva krav efter en intervju.

## Vanliga misstag

- **Misstag: Att kravanalytikern skriver SBE-specifikationen ensam.**
  - Varför det händer: Organisationen är van vid att kravanalytikern producerar kravdokument.
  - Hur du undviker det: Använd specifikationen som gemensam arbetsyta och se till att verksamhet, test och utveckling deltar i exempelarbetet.

- **Misstag: Att byta format utan att byta arbetssätt.**
  - Varför det händer: Gherkin eller tabeller upplevs som det synliga kännetecknet på SBE.
  - Hur du undviker det: Börja med samtalet, reglerna och exemplen. Välj format först när innehållet är begripligt.

- **Misstag: Att dölja öppna frågor för att dokumentationen ska se färdig ut.**
  - Varför det händer: Kravdokument förväntas ofta vara beslutsmogna innan de delas brett.
  - Hur du undviker det: Markera öppna frågor tydligt och gör dem till en del av analysresultatet.

- **Misstag: Att låta IT-perspektivet ta över för tidigt.**
  - Varför det händer: Exempel kan snabbt översättas till testdata, systemfält och tekniska lösningar.
  - Hur du undviker det: Håll fast vid verksamhetsbeteendet först. Lägg tekniska konsekvenser separat.

- **Misstag: Att verksamhetsperspektivet blir för abstrakt.**
  - Varför det händer: Verksamheten beskriver ofta principer, policyer och normalfall.
  - Hur du undviker det: Be alltid om konkreta fall, undantag och exempel på när regeln inte gäller.

## Övningar

### Övning 1: Gör rollen synlig

Utgå från följande traditionella krav:

> Systemet ska ge användaren rätt åtkomst till ärenden baserat på roll och behörighet.

Besvara frågorna:

1. Vilka roller behöver vara med i ett SBE-samtal om detta krav?
2. Vilket beteende skulle du avgränsa först?
3. Vilka tre exempel skulle du använda för att starta diskussionen?
4. Vilka öppna frågor tror du snabbt skulle uppstå?

### Övning 2: Skilj mellan innehållstyper

Klassificera följande som regel, exempel, beslut, öppen fråga eller teknisk konsekvens:

| Påstående | Klassificering |
|---|---|
| En tilldelad utredare får öppna ett pågående ärende | |
| Utredare A öppnar ärende 1001 och får full vy | |
| Ska avslutade ärenden vara läsbara för tidigare utredare? | |
| Åtkomst till sekretessmarkerade ärenden ska loggas | |
| Loggen behöver innehålla användar-ID, tidpunkt och ärende-ID | |

Diskutera sedan vilka av påståendena verksamheten måste kunna bekräfta och vilka IT behöver för implementation eller test.

### Fördjupning

Titta på ett krav du själv har arbetat med där acceptanskriterierna var tydliga men där missförstånd ändå uppstod. Försök identifiera:

- Vilket ord eller begrepp tolkades olika?
- Vilket konkret exempel hade kunnat avslöja missförståndet tidigare?
- Vilka roller borde ha sett exemplet samtidigt?
- Vilken öppen fråga borde ha dokumenterats?

## Snabb sammanfattning

- I SBE förändras kravanalytikerns roll från kravskrivare till facilitator av gemensam förståelse.
- Kravanalytikern ska inte ensam äga sanningen, utan hjälpa flera perspektiv att mötas.
- Intervjuer kan ge bakgrund, men SBE behöver gemensamt exempelarbete.
- Bra SBE-dokumentation skiljer mellan regler, exempel, beslut, öppna frågor och tekniska konsekvenser.
- Öppna frågor är värdefulla analysresultat, inte misslyckanden.
- Kravanalytikern behöver skydda specifikationen från både för abstrakta exempel och för detaljerad testdata.
- Det viktigaste är inte att skriva i rätt format, utan att skapa en specifikation som verksamhet och IT kan förstå och använda tillsammans.

## Quiz/reflektionsfrågor

1. Vad är den viktigaste skillnaden mellan att samla in krav och att facilitera kravupptäckt?
2. Varför är det riskabelt om kravanalytikern skriver alla SBE-exempel ensam?
3. Hur kan öppna frågor bidra till bättre kravkvalitet?
4. När kan ett exempel vara för abstrakt?
5. När kan ett exempel vara för detaljerat?
6. Vilka delar av en SBE-specifikation behöver verksamheten kunna läsa?
7. Vilka delar behöver IT särskilt kunna använda?
8. Hur märker du att en organisation bara har bytt dokumentationsformat men inte arbetssätt?

## Koppling till bokens röda tråd

Rollen förändras inte genom att kravanalytikern lämnar dokumentationen, utan genom att dokumentationen blir ett resultat av gemensam utforskning. Därför återkommer boken till hur kravanalytikern kan hålla ihop verksamhetens språk, IT:s behov av precision och testets behov av verifierbarhet.


## Nästa steg

I nästa kapitel etablerar vi det genomgående caset mer ordentligt: brottsutredningsstödet i myndighetsmiljö. Där sätter vi ramarna för aktörer, mål, arbetsflöden, informationsobjekt och begränsningar. Caset blir sedan den gemensamma grund som kommande kapitel använder när vi går djupare in i funktionella krav, dokumentationsstruktur, Gherkin, testbarhet och införande.
