# Kapitel 8: Dokumentation som fungerar för både verksamhet och IT

## Varför detta kapitel finns

SBE lyckas inte bara genom att gruppen tar fram bättre exempel. Det lyckas när exemplen blir en dokumentation som flera målgrupper faktiskt använder.

I traditionellt kravarbete blir dokumentationen ofta antingen verksamhetsnära men för lös, eller tekniskt användbar men svår att läsa för verksamheten. Kravanalytikern hamnar då i ett mellanläge: verksamheten säger att dokumentet ser rimligt ut, IT tolkar det på sitt sätt, test skapar egna testfall och förvaltningen får senare försöka förstå vilken beskrivning som egentligen gäller.

SBE kan minska det glappet, men bara om dokumentationen struktureras medvetet. En specifikation som bara består av många scenarier blir snabbt svår att överblicka. En specifikation som bara består av regler tappar konkretionen. En specifikation som bara skrivs i ett verktygsformat riskerar att bli begriplig för testautomation men inte för verksamhetsbeslut.

Det här kapitlet visar hur dokumentationen kan byggas så att den fungerar för både verksamhet och IT. Vi utgår från brottsutredningsstödet och fokuserar på hur regler, exempel, scenarier, öppna frågor och tekniska konsekvenser kan hållas ihop utan att blandas ihop.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan dokumentationens verksamhetslager, specifikationslager och tekniska lager
- strukturera en SBE-specifikation så att den är läsbar för verksamheten och användbar för IT
- avgöra vad som bör vara regel, exempel, scenario, beslutstabell, öppen fråga eller teknisk konsekvens
- undvika att SBE-dokumentationen blir antingen för lös, för teknisk eller för omfattande
- skapa spårbarhet utan att återinföra tung dubbeldokumentation

## Innan vi börjar

De tidigare kapitlen har visat hur funktionella krav kan omvandlas från traditionell kravtext till regler, exempel och scenarier. Vi har också sett att olika exempel fyller olika syften: normalexempel visar det vanligaste beteendet, undantagsexempel fångar avvikelser, konfliktexempel prövar regelkrockar och beslutstabeller hjälper när flera villkor samverkar.

Nu behöver vi ta nästa steg. Frågan är inte bara hur en enskild regel skrivs, utan hur hela dokumentationen blir begriplig, sökbar, underhållbar och användbar.

Det är särskilt viktigt i myndighetsnära system. I brottsutredningsstödet behöver verksamheten förstå regler om ärenden, åtkomst, sekretess, tilldelning och beslutsstöd. IT behöver samtidigt kunna omsätta samma regler till användargränssnitt, behörighetskontroller, testfall, loggning och förvaltning. En bra SBE-specifikation ska därför inte vara en kompromiss som ingen riktigt gillar. Den ska vara en gemensam struktur där olika typer av information har tydliga platser.

## Dokumentationens tre lager

En användbar SBE-dokumentation behöver ofta tre lager:

- ett verksamhetslager
- ett specifikationslager
- ett tekniskt lager

Lagren ska hänga ihop, men de ska inte blandas samman i samma mening eller samma tabell.

### Verksamhetslagret

Verksamhetslagret beskriver vad verksamheten behöver uppnå och vilka regler som gäller i domänen. Det ska kunna läsas av verksamhetsspecialister, produktägare, beslutsfattare, testare och utvecklare utan att läsaren behöver förstå implementationen.

I brottsutredningsstödet kan verksamhetslagret till exempel beskriva:

- varför utredare behöver kunna söka efter ärenden
- vilka aktörer som får ta del av olika typer av uppgifter
- vilka statusar ett ärende kan ha
- vilka regler som gäller när ett ärende är sekretessmarkerat
- vilka beslut som kräver särskild motivering eller loggning

Verksamhetslagret ska inte förklara databastabeller, API-anrop, rollnamn i identitetsplattformen eller tekniska felkoder. Sådant kan vara viktigt, men det hör hemma i ett annat lager.

En bra tumregel är att verksamhetslagret ska kunna diskuteras i en workshop utan att deltagarna fastnar i lösningsdesign.

### Specifikationslagret

Specifikationslagret är kärnan i SBE-dokumentationen. Här finns reglerna, exemplen och scenarierna som konkretiserar beteendet. Det är detta lager som gör dokumentationen prövbar.

I brottsutredningsstödet kan specifikationslagret till exempel innehålla regeln:

> En utredare får se fullständig ärendeinformation om utredaren är tilldelad ärendet och ärendet tillhör samma organisatoriska enhet.

Den regeln behöver sedan konkretiseras med exempel:

| Exempel | Utredare tilldelad ärendet | Samma organisatoriska enhet | Förväntat resultat |
|---|---|---|---|
| Tilldelad utredare i samma enhet | Ja | Ja | Fullständig ärendeinformation visas |
| Ej tilldelad utredare i samma enhet | Nej | Ja | Begränsad information visas |
| Tilldelad utredare i annan enhet | Ja | Nej | Åtkomst nekas eller kräver särskild behörighet |

Specifikationslagret är där verksamhet och IT möts. Verksamheten kan granska om exemplen uttrycker rätt regel. IT kan använda exemplen för design, test och implementation.

### Det tekniska lagret

Det tekniska lagret beskriver konsekvenser för lösningen. Det kan handla om integrationer, behörighetsmodeller, loggning, datafält, prestanda, felhantering eller testautomation.

För regeln om åtkomst till ärendeinformation kan tekniska konsekvenser vara:

- behörighetskontrollen behöver känna till tilldelning, organisatorisk enhet och eventuell särskild behörighet
- varje nekad åtkomst till sekretessmarkerade uppgifter ska loggas
- sökresultat behöver kunna visa begränsad information utan att hämta eller exponera skyddade detaljer
- testdata behöver innehålla ärenden med olika enheter, tilldelningar och sekretessnivåer

Det tekniska lagret ska vara kopplat till regeln och exemplen, men inte skrivas som om det vore själva verksamhetsregeln. Om tekniska detaljer blandas in för tidigt blir specifikationen svårare för verksamheten att äga.

## Ett dokumentationsmönster för SBE

För praktiskt arbete kan varje funktionell specifikation följa ett återkommande mönster. Det gör dokumentationen lättare att läsa, lättare att granska och lättare att underhålla.

Ett bra grundmönster är:

1. Syfte
2. Omfattning
3. Verksamhetsregler
4. Exempel och beslutstabeller
5. Scenarier
6. Öppna frågor
7. Tekniska konsekvenser
8. Spårbarhet och status

Mönstret ska inte användas mekaniskt. Mindre beteenden behöver inte alla delar. Komplexa beteenden kan behöva flera sidor, tabeller och scenarier. Poängen är att samma typ av information ska hamna på samma plats.

### Syfte

Syftet svarar på varför beteendet behövs. Det ska vara kort och verksamhetsnära.

Exempel:

> Utredaren behöver kunna se en sammanfattning av ett ärende för att snabbt avgöra om ärendet är relevant för den fortsatta utredningen, utan att känsliga uppgifter exponeras för personer som saknar behörighet.

Syftet ska inte vara:

> Systemet ska implementera en ärendesammanfattningskomponent med behörighetsstyrd rendering.

Den andra formuleringen kan vara relevant för design, men den hjälper inte verksamheten att bekräfta behovet.

### Omfattning

Omfattningen förklarar vad specifikationen täcker och vad den inte täcker. Det är särskilt viktigt i SBE eftersom exempel annars kan tolkas som att de täcker mer än de gör.

Exempel:

- Specifikationen täcker vad en utredare ser i sökresultat och ärendesammanfattning.
- Specifikationen täcker inte fullständig åtkomstprövning för dokumentbilagor.
- Specifikationen täcker inte arkiveringsregler.
- Specifikationen täcker inte prestandakrav för sökning.

Detta minskar risken att ett exempel överanvänds som bevis för beteenden som aldrig diskuterats.

### Verksamhetsregler

Verksamhetsregler ska uttryckas i domänens språk. De ska vara så konkreta att de kan prövas med exempel, men inte så tekniska att de blir lösningsdesign.

En regel kan till exempel vara:

> En användare som inte är tilldelad ett sekretessmarkerat ärende får endast se ärendets diarienummer, ärendestatus och ansvarig enhet i sökresultatet.

Den regeln är tydligare än:

> Systemet ska begränsa sökresultat baserat på sekretess.

Den är också mer verksamhetsnära än:

> API:et ska returnera maskade fält baserat på claim `case:restricted`.

När reglerna skrivs på rätt nivå kan verksamheten granska betydelsen och IT kan härleda implementationen.

### Exempel och beslutstabeller

Exempel konkretiserar reglerna. Beslutstabeller passar när beteendet beror på flera villkor.

För sökresultat i brottsutredningsstödet kan en beslutstabell visa hur tilldelning, organisatorisk enhet och sekretessmarkering påverkar vilken information som visas.

| Exempel | Tilldelad ärendet | Samma enhet | Sekretessmarkerat | Förväntad visning |
|---|---|---|---|---|
| Tilldelad utredare ser normalt ärende | Ja | Ja | Nej | Full sökträff |
| Tilldelad utredare ser sekretessärende | Ja | Ja | Ja | Full sökträff och åtkomst loggas |
| Ej tilldelad kollega ser normalt ärende | Nej | Ja | Nej | Begränsad sökträff |
| Ej tilldelad kollega ser sekretessärende | Nej | Ja | Ja | Endast diarienummer och status |
| Utredare i annan enhet söker sekretessärende | Nej | Nej | Ja | Ingen sökträff eller åtkomst nekas enligt beslutad regel |

Den sista raden visar också hur exempel kan synliggöra en öppen fråga: ska ärendet inte visas alls, eller ska systemet visa att ett ärende finns men kräva särskild motivering? Tabellen ska då inte låtsas att beslutet är taget.

### Scenarier

Scenarier beskriver ett förlopp. De passar när ordning, interaktion eller användarupplevelse är viktig.

Exempel:

```gherkin
Scenario: Utredare öppnar ett sekretessmarkerat ärende som utredaren är tilldelad
  Givet att ärendet är sekretessmarkerat
  Och att utredaren är tilldelad ärendet
  När utredaren öppnar ärendesammanfattningen
  Så ska fullständig ärendeinformation visas
  Och åtkomsten ska loggas
```

Det här scenariot är begripligt för verksamheten om begreppen är förankrade. Det är också användbart för test och utveckling, men det bör inte vara den enda dokumentationen. Regeln och exemplen behöver finnas kvar i en läsbar kontext.

### Öppna frågor

Öppna frågor är inte ett misslyckande. De är ett viktigt resultat av bra analys.

Exempel:

- Ska en användare i annan organisatorisk enhet kunna se att ett sekretessmarkerat ärende existerar?
- Vem får godkänna särskild åtkomst?
- Hur länge ska åtkomstmotivering vara giltig?
- Ska nekade åtkomstförsök visas för systemförvaltare, säkerhetsansvarig eller båda?

Öppna frågor ska ha ägare, status och helst ett datum för när beslut behövs. Annars blir de passiva anteckningar.

### Tekniska konsekvenser

Tekniska konsekvenser ska inte ersätta specifikationen, men de ska dokumenteras när de påverkar design, test eller förvaltning.

Exempel:

- Behörighetskontrollen behöver kunna skilja mellan tilldelning, enhetstillhörighet och särskild behörighet.
- Loggningen behöver inkludera användare, tidpunkt, ärende, åtkomsttyp och motivering när sådan krävs.
- Testmiljön behöver stabila testdata för minst fem åtkomstkombinationer.
- Integration med identitets- och behörighetssystem behöver verifieras innan automatiserade scenarier blir tillförlitliga.

På så sätt får IT det som behövs utan att verksamhetsregeln försvinner in i tekniska detaljer.

### Spårbarhet och status

Spårbarhet i SBE ska vara tillräcklig, inte maximal. Den ska hjälpa gruppen att förstå varför en specifikation finns, var den används och om den är aktuell.

Minsta praktiska spårbarhet kan vara:

- koppling till mål, förmåga eller backloggobjekt
- status för specifikationen
- ägare eller ansvarig grupp
- senaste större beslut
- koppling till test eller automatiserade kontroller om sådana finns
- länk till närliggande regler eller specifikationer

Status bör skilja mellan exempelvis utkast, granskad, beslutad, implementerad och verifierad. Det gör det tydligare vad dokumentationen kan användas till.

## Att skriva för två läsare samtidigt

SBE-dokumentation har minst två centrala läsare:

- verksamhetsläsaren, som behöver förstå om beteendet är rätt
- IT-läsaren, som behöver förstå hur beteendet ska byggas, testas och förvaltas

Det betyder inte att varje mening ska tillfredsställa alla samtidigt. Det betyder att dokumentationen ska vara uppdelad så att varje läsare hittar rätt information.

### Verksamhetsläsaren behöver

Verksamhetsläsaren behöver se:

- vilket behov beteendet stödjer
- vilka regler som gäller
- vilka exempel som visar normala fall, undantag och gränsfall
- vilka beslut som är fattade
- vilka frågor som fortfarande är öppna
- vilka konsekvenser beteendet får i arbetssättet

Verksamhetsläsaren ska kunna säga: "Ja, det här är så vi menar att det ska fungera."

### IT-läsaren behöver

IT-läsaren behöver se:

- vilka villkor som styr systemets beteende
- vilka data eller tillstånd som påverkar utfallet
- vilka scenarier som behöver stödjas
- vilka undantag som måste hanteras
- vilka tekniska konsekvenser som är identifierade
- vilka exempel som kan användas för testdesign eller automatisering

IT-läsaren ska kunna säga: "Ja, det här går att designa, implementera och verifiera."

### Kravanalytikerns uppgift

Kravanalytikerns uppgift är att hålla dessa behov förenade men separerade. Det kräver ofta aktiv redigering.

En verksamhetsregel kan behöva skrivas om så att den blir mindre teknisk. En teknisk konsekvens kan behöva flyttas från regeltexten till en egen sektion. Ett scenario kan behöva kompletteras med en beslutstabell. En tabell kan behöva en kort förklaring så att den inte bara blir testdata.

I praktiken är detta en redaktörsroll lika mycket som en analysroll.

## Hur mycket ska dokumenteras?

Ett vanligt misstag är att tro att SBE innebär att allt ska exemplifieras. Det leder till stora mängder scenarier som ingen orkar läsa eller underhålla.

Ett annat misstag är att bara exemplifiera det enkla. Då blir dokumentationen pedagogisk men missar de risker där SBE hade gjort störst nytta.

En rimlig prioritering är att dokumentera mest där något av följande gäller:

- flera roller, statusar eller villkor påverkar utfallet
- konsekvensen av fel beteende är stor
- verksamheten och IT brukar tolka området olika
- tidigare system eller processer har haft problem i området
- beteendet är svårt att testa utan tydliga exempel
- regeln kommer att återanvändas i flera funktioner

För brottsutredningsstödet är åtkomst, sekretess, statusövergångar, sökresultat och loggning typiska områden där mer dokumentation lönar sig. En enkel etikett på en knapp behöver däremot sällan en full SBE-specifikation.

## Dokumentationsnivåer i brottsutredningsstödet

Låt oss jämföra tre möjliga nivåer för samma område: visning av sökresultat.

### För lös dokumentation

> Systemet ska visa relevanta ärenden för behöriga användare.

Detta är lätt att läsa men svårt att använda. Vad betyder relevant? Vad betyder behörig? Vad visas om användaren bara har delvis behörighet? Vad händer med sekretessmarkerade ärenden?

### För teknisk dokumentation

> SearchCaseEndpoint ska filtrera resultat baserat på user claims, case assignment, org unit id och secrecy flag. Response model ska sätta `restrictedView=true` om användaren saknar full access.

Detta kan vara användbart för utveckling, men det är inte rätt plats för verksamheten att bekräfta regeln. Det förutsätter också en viss lösning.

### Balanserad SBE-dokumentation

> En användare ska bara se den ärendeinformation som användaren har rätt att ta del av. Om användaren saknar full åtkomst men ändå får känna till att ärendet finns ska sökresultatet visa en begränsad träff.

| Exempel | Användarens relation till ärendet | Ärendet sekretessmarkerat | Förväntad visning |
|---|---|---|---|
| Tilldelad utredare | Tilldelad | Nej | Full sökträff |
| Tilldelad utredare, sekretess | Tilldelad | Ja | Full sökträff, åtkomst loggas |
| Kollega i samma enhet | Inte tilldelad | Nej | Begränsad sökträff |
| Kollega i samma enhet, sekretess | Inte tilldelad | Ja | Endast diarienummer och status |
| Annan enhet | Ingen relation | Ja | Ingen träff, om inte särskild åtkomst finns |

Den tredje versionen är inte komplett, men den skapar en bättre gemensam bas. Den går att diskutera med verksamheten och använda av IT.

## Hantera kompletterande kravtext

SBE ersätter inte all löpande text. Tvärtom behöver bra SBE-dokumentation ofta korta förklaringar som sätter exemplen i sammanhang.

Kompletterande kravtext passar när den:

- beskriver syfte och bakgrund
- förklarar begrepp
- anger omfattning och avgränsning
- sammanfattar regelns innebörd
- beskriver ansvar eller beslut
- förklarar varför vissa exempel är viktiga

Kompletterande kravtext passar sämre när den försöker bära hela beteendet ensam. Om en formulering innehåller många "om", "när", "förutom", "såvida inte" och "i vissa fall" är det ofta ett tecken på att regeln behöver exempel eller beslutstabell.

## Dokumentationens livscykel

Levande dokumentation kräver en livscykel. Annars blir även SBE-dokumentation snabbt historisk.

En enkel livscykel kan vara:

1. Utkast: regeln och några exempel finns, men beslut saknas.
2. Förfinad: verksamhet, IT och test har arbetat igenom exempel och öppna frågor.
3. Beslutad: regeln och exemplen är accepterade som grund för utveckling.
4. Implementerad: lösningen stödjer beteendet.
5. Verifierad: beteendet är testat manuellt eller automatiserat.
6. Förvaltad: specifikationen används vid ändringar och hålls aktuell.

Det viktiga är inte exakt vilka statusord som används. Det viktiga är att gruppen vet vad en specifikation får användas till i varje läge.

En specifikation i utkastläge ska inte behandlas som bindande sanning. En beslutad specifikation ska inte ändras tyst. En verifierad specifikation ska inte ligga kvar om systemets beteende ändras.

## Spårbarhet utan tung dubbeldokumentation

Många organisationer har starka behov av spårbarhet. Det gäller särskilt myndighetsnära system där beslut, åtkomst, säkerhet och rättssäkerhet kan behöva följas upp. Samtidigt kan för mycket spårbarhet göra dokumentationen tung och svår att underhålla.

SBE bör därför inte skapa en ny parallell dokumentationsvärld. I stället bör specifikationerna kopplas till befintliga artefakter där det behövs.

Exempel på lättviktig spårbarhet:

| Spårbarhet | Syfte | Exempel |
|---|---|---|
| Förmåga eller mål | Varför beteendet finns | Effektivare sökning i utredningsärenden |
| Backloggobjekt | Vad som ska ändras | "Begränsad sökträff för sekretessmarkerade ärenden" |
| Regel-ID | Stabil referens | REG-ÅTK-03 |
| Exempel-ID | Stabil referens till exempel | EX-ÅTK-03-02 |
| Testkoppling | Verifiering | Manuell testcheck eller automatiserat scenario |
| Beslutslogg | Varför regeln ser ut som den gör | Beslut om att visa diarienummer men inte känsliga uppgifter |

Spårbarhet ska svara på praktiska frågor, inte bara finnas för sin egen skull.

## Vanliga dokumentationsmönster

I en SBE-bok eller ett SBE-projekt är det bra att ha några återkommande dokumentationsmönster. Här är fyra användbara mönster.

### Regel med exempel

Passar när en regel är tydlig men behöver konkretiseras.

Struktur:

- kort syfte
- regel
- exempel i tabell
- öppna frågor
- tekniska konsekvenser

### Arbetsflöde med scenarier

Passar när ordningen mellan steg spelar roll.

Struktur:

- syfte
- aktörer
- förutsättningar
- huvudscenario
- alternativa scenarier
- undantag
- tekniska konsekvenser

### Beslutspunkt med beslutstabell

Passar när flera villkor styr utfallet.

Struktur:

- beslut som systemet ska fatta eller stödja
- villkor
- beslutstabell
- gränsfall
- öppna frågor
- testidéer

### Tvärgående regel

Passar för återkommande regler som påverkar flera funktioner.

Struktur:

- princip
- tillämpningsområde
- exempel från flera funktioner
- undantag
- ansvar
- konsekvenser för implementation och test

Dessa mönster gör dokumentationen lättare att känna igen. De hjälper också nya deltagare att förstå hur de ska läsa och bidra till specifikationerna.

## Vanliga misstag

- **Misstag: Att skriva allt i Gherkin för tidigt.**
  - Varför det händer: Gherkin ser strukturerat och testbart ut.
  - Hur man undviker det: Börja med verksamhetsregel och exempel. Använd Gherkin när scenarioformen tillför tydlighet eller när det finns ett faktiskt automationsbehov.

- **Misstag: Att blanda verksamhetsregel och teknisk lösning.**
  - Varför det händer: IT behöver svar och tekniska detaljer kommer snabbt upp i diskussionen.
  - Hur man undviker det: Dokumentera tekniska konsekvenser separat från regeln.

- **Misstag: Att dokumentera alla möjliga kombinationer.**
  - Varför det händer: Gruppen vill vara komplett.
  - Hur man undviker det: Välj representativa exempel, gränsfall och riskfall. Använd beslutstabeller när kombinationerna blir många.

- **Misstag: Att göra dokumentationen läsbar men inte prövbar.**
  - Varför det händer: Text känns naturlig för verksamheten.
  - Hur man undviker det: Se till att varje viktig regel har minst ett konkret exempel och att komplexa regler har flera.

- **Misstag: Att göra dokumentationen prövbar men inte läsbar.**
  - Varför det händer: Fokus hamnar på test, automation eller verktygsformat.
  - Hur man undviker det: Behåll syfte, regeltext och förklaringar i verksamhetens språk.

## Övningar

### Övning 1: Dela upp en blandad kravtext

Ta följande kravformulering:

> Systemet ska visa ärenden i sökresultatet baserat på användarens behörighet, tilldelning, organisatoriska enhet och sekretessmarkering, och ska logga åtkomst när känsliga uppgifter visas.

Dela upp den i:

- syfte
- verksamhetsregel
- exempel
- tekniska konsekvenser
- öppna frågor

Målet är inte att skapa en perfekt specifikation, utan att träna på att placera information i rätt lager.

### Övning 2: Gör dokumentationen läsbar för två målgrupper

Välj en funktion från ett eget projekt eller från brottsutredningsstödet. Skriv först en kort version för verksamheten och sedan en kompletterande version för IT.

Kontrollera sedan:

- Kan verksamheten bekräfta regeln utan att förstå tekniska detaljer?
- Kan IT förstå vilka villkor och utfall som behöver stödjas?
- Finns det minst ett exempel som båda grupperna kan diskutera?
- Finns öppna frågor synliga?

### Fördjupning

Skapa ett dokumentationsmönster för en återkommande regel i brottsutredningsstödet, exempelvis åtkomstloggning eller begränsad visning av sökresultat.

Använd strukturen:

- syfte
- princip
- tillämpningsområde
- exempel
- undantag
- tekniska konsekvenser
- status och spårbarhet

Reflektera över vad som bör ligga i samma specifikation och vad som bör vara en separat tvärgående regel.

## Snabb sammanfattning

- SBE-dokumentation behöver vara både läsbar och prövbar.
- Verksamhetsregler, exempel, scenarier och tekniska konsekvenser ska hänga ihop men inte blandas ihop.
- Dokumentationen bör ha tydliga lager: verksamhetslager, specifikationslager och tekniskt lager.
- En bra struktur hjälper både verksamhet och IT att använda samma specifikation utan att ha samma informationsbehov.
- Öppna frågor är en viktig del av dokumentationen och ska inte döljas.
- Spårbarhet ska vara praktiskt användbar, inte administrativt överlastad.
- Levande dokumentation kräver status, ansvar och regelbundet underhåll.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att bara skriva SBE-dokumentation i ett testnära format?
2. Vad är skillnaden mellan verksamhetslager och tekniskt lager?
3. När passar en beslutstabell bättre än ett scenario?
4. Vilka delar behöver finnas för att en specifikation ska vara användbar för både verksamhet och IT?
5. Hur kan spårbarhet stödja SBE utan att skapa tung dubbeldokumentation?
6. Vilka risker uppstår om öppna frågor inte dokumenteras synligt?

## Koppling till bokens röda tråd

Det här kapitlet fungerar som brygga mellan kravarbete och förvaltning. En specifikation som bara är begriplig för verksamheten blir svår att bygga och testa; en specifikation som bara är användbar för IT tappar sin förankring i verksamhetsbesluten. Därför behöver dokumentationen vara lagerindelad men sammanhållen.


## Nästa steg

Det här kapitlet har fokuserat på hur dokumentationen kan struktureras. Nästa kapitel går vidare till hur dokumentationen skapas i samarbete. Där behandlar vi exempelworkshops och gemensam förfining: hur kravanalytikern får verksamhet, IT och test att tillsammans hitta rätt regler, exempel, frågor och beslut.
