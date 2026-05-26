# Kapitel 6: Från traditionella krav till exempelbaserad specifikation

## Varför detta kapitel finns

I tidigare kapitel har vi identifierat vilka funktionella krav som ofta lämpar sig för SBE. Nästa steg är att faktiskt förändra dokumentationen.

Det är här många erfarna kravanalytiker märker att omställningen blir praktisk. Man kan förstå idén med Specification by Example, hålla med om värdet av konkreta exempel och ändå vara osäker på hur ett befintligt krav ska skrivas om. Ska kravtexten tas bort? Ska acceptanskriterierna ersättas? Ska allt bli Gherkin? Ska varje regel ha exempel? Hur undviker man att skapa en ny typ av dokumentation som bara IT förstår?

Det här kapitlet visar en praktisk transformationskedja: från traditionell kravformulering till exempelbaserad specifikation. Vi använder brottsutredningsstödet och arbetar med ett kravområde som redan har förekommit i tidigare kapitel: sökning, behörighet och sekretessmarkerade uppgifter.

Målet är inte att visa den enda rätta mallen. Målet är att visa hur du kan tänka när du stegvis förvandlar traditionell kravtext till dokumentation som både verksamhet och IT kan använda.

## Lärandemål

Efter kapitlet ska du kunna:

- analysera en traditionell kravformulering och hitta vad som behöver förtydligas med exempel,
- skilja mellan övergripande kravtext, verksamhetsregel, exempel, scenario och öppen fråga,
- omvandla acceptanskriterier till tydligare regler och konkreta exempel,
- använda exempel för att upptäcka luckor, undantag och felaktiga antaganden,
- skapa en exempelbaserad specifikation som är begriplig för verksamheten och användbar för IT,
- avgöra när Gherkin-liknande scenarier är lämpliga och när tabeller eller fri text är bättre.

## Innan vi börjar

En vanlig missuppfattning är att SBE innebär att all kravdokumentation ska ersättas av scenarier. Det leder nästan alltid fel.

En bra exempelbaserad specifikation innehåller normalt flera typer av information:

- en kort beskrivning av vilket verksamhetsbeteende som avses,
- en eller flera regler som uttrycker hur beteendet ska fungera,
- konkreta exempel som visar regeln i specifika situationer,
- eventuella scenarier som visar ett sammanhängande flöde,
- öppna frågor som ännu inte är avgjorda,
- ibland tekniska konsekvenser eller hänvisningar till andra artefakter.

Det är kombinationen som gör dokumentationen användbar. Verksamheten behöver kunna läsa och bekräfta innebörden. IT behöver kunna designa, implementera och testa. Test behöver kunna härleda vad som ska verifieras. Förvaltning behöver förstå varför beteendet finns och när det kan ändras.

## Startpunkten: ett traditionellt krav

Vi börjar med en kravformulering som är typisk för många kravdokument.

> KR-124: Systemet ska visa sökresultat för utredningsärenden utifrån användarens behörighet.

Vid första anblick är kravet rimligt. Det är kort, funktionellt och kopplat till ett tydligt systembeteende. Men det är också ett exempel på ett krav som riskerar att skapa olika bilder hos olika personer.

En verksamhetsrepresentant kan läsa kravet och tänka att utredare ska se sina egna ärenden.

En utvecklare kan läsa kravet och tänka att det behövs en behörighetskontroll mot användarens roller.

En testare kan läsa kravet och undra vilka kombinationer som ska testas.

En jurist eller säkerhetsansvarig kan fråga om sökförsök utan behörighet ska loggas.

En systemförvaltare kan fråga var behörighetsreglerna ska administreras.

Kravet är inte fel. Problemet är att det försöker bära för mycket betydelse i en enda mening.

## Första analysen: vad är oklart?

Innan vi skriver om kravet behöver vi analysera vilka beslut och antaganden som gömmer sig i formuleringen.

Formuleringen innehåller minst fyra begrepp som behöver förtydligas:

- vad som menas med sökresultat,
- vad som räknas som utredningsärende,
- vad användarens behörighet bygger på,
- vad systemet ska göra när användaren saknar behörighet.

Den innehåller också flera möjliga variationer:

- användaren kan vara utredare, förundersökningsledare, analytiker eller administratör,
- ärendet kan vara öppet, pausat, avslutat eller arkiverat,
- ärendet kan vara sekretessmarkerat eller inte,
- användaren kan tillhöra samma organisatoriska enhet eller en annan,
- användaren kan vara tilldelad ärendet eller sakna relation till det,
- systemet kan visa allt, visa begränsad information, dölja ärendet eller visa en informationsmarkering.

Det här är ett viktigt SBE-ögonblick. Vi har ännu inte skrivit ett enda scenario, men vi har redan gjort kravet mer analyserbart.

## Gör inte om kravet direkt till Gherkin

När en organisation börjar med SBE händer det ofta att någon vill hoppa direkt från kravtext till Given-When-Then.

Det kan se ut så här:

```gherkin
Scenario: Visa sökresultat utifrån behörighet
  Given att användaren är inloggad
  When användaren söker efter ärenden
  Then ska systemet visa ärenden som användaren har behörighet till
```

Detta är syntaktiskt ett scenario, men det löser inte problemet. Det upprepar bara den ursprungliga oklarheten i en annan form. Det säger fortfarande inte vad behörighet betyder, vilka ärenden som visas, vad som döljs eller vilka undantag som gäller.

Det första steget är därför inte att välja format. Det första steget är att hitta regeln.

## Steg 1: formulera beteendet i verksamhetens språk

Vi börjar med en kort beteendebeskrivning.

> När en användare söker efter utredningsärenden ska brottsutredningsstödet bara visa ärenden som användaren har rätt att känna till och arbeta med. För ärenden med skyddade uppgifter kan systemet behöva visa begränsad information eller dölja ärendet helt, beroende på användarens relation till ärendet och särskilda behörigheter.

Denna text är fortfarande inte tillräcklig som specifikation, men den gör något viktigt. Den flyttar fokus från teknisk behörighetskontroll till verksamhetsbeteende.

Den säger att frågan inte bara är om användaren har en roll. Frågan är vad användaren får känna till, se och arbeta med i en viss situation.

## Steg 2: bryt ut reglerna

Nästa steg är att uttrycka regler. Reglerna ska vara tillräckligt tydliga för att kunna prövas med exempel, men inte så tekniska att verksamheten tappar bort sig.

Ett första regelutkast kan se ut så här:

- En utredare får se ett ärende i sökresultatet om utredaren är tilldelad ärendet.
- En utredare får se ett ärende i sökresultatet om ärendet tillhör utredarens organisatoriska enhet och inte är sekretessmarkerat.
- Ett sekretessmarkerat ärende får bara visas med full information om användaren har särskild behörighet eller är tilldelad ärendet med rätt åtkomstnivå.
- Om användaren saknar relation till ärendet ska ärendet inte visas i sökresultatet.
- Åtkomst till sekretessmarkerade ärenden ska loggas när ärendet visas med full eller begränsad information.

Reglerna är redan bättre än den ursprungliga kravtexten. Men de är fortfarande inte färdiga. De innehåller begrepp som behöver prövas:

- Vad betyder full information?
- Vad betyder begränsad information?
- Är det alltid tillräckligt att tillhöra samma organisatoriska enhet?
- Ska tilldelning alltid gå före sekretessmarkering?
- Ska nekad åtkomst loggas även när ärendet inte visas?
- Vad händer med avslutade eller arkiverade ärenden?

Här blir exempel viktiga. De hjälper oss att se var reglerna fungerar och var de är för vaga.

## Steg 3: skapa en första exempeltabell

En exempeltabell är ofta bättre än ett scenario när beteendet styrs av kombinationer av villkor. Den gör det möjligt att se variationer på samma regel bredvid varandra.

| Exempel | Roll | Relation till ärende | Organisatorisk enhet | Sekretessmarkerat | Förväntat sökresultat | Loggning |
|---|---|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Annan enhet | Nej | Ärendet visas | Nej |
| 2 | Utredare | Ingen relation | Samma enhet | Nej | Ärendet visas | Nej |
| 3 | Utredare | Ingen relation | Annan enhet | Nej | Ärendet visas inte | Nej |
| 4 | Utredare | Tilldelad | Annan enhet | Ja | Begränsad information visas | Ja |
| 5 | Förundersökningsledare | Ansvarig | Annan enhet | Ja | Full information visas | Ja |
| 6 | Analytiker | Stödroll | Samma enhet | Ja | Begränsad information visas | Ja |
| 7 | Administratör | Ingen relation | Samma enhet | Ja | Ärendet visas inte | Nej |

Tabellen gör flera saker samtidigt.

Den visar konkreta situationer.

Den gör skillnad mellan roll, relation, enhet och sekretessmarkering.

Den synliggör att sökresultatet kan ha fler utfall än bara visas eller visas inte.

Den visar att loggning är kopplad till vissa utfall.

Den gör det lättare för verksamheten att säga: “Exempel 4 är fel, tilldelad utredare ska se full information även om ärendet är sekretessmarkerat” eller “Exempel 6 får bara gälla om analytikern har ett aktivt uppdrag”.

Den sortens invändningar är inte störningar. De är själva värdet med SBE.

## Steg 4: formulera om reglerna efter exemplen

När exemplen har diskuterats behöver reglerna ofta justeras. Anta att workshopgruppen kommer fram till följande beslut:

- tilldelning till ärende ger rätt att se grundinformation,
- full information i sekretessmarkerade ärenden kräver särskild åtkomstnivå,
- förundersökningsledare med ansvar för ärendet har särskild åtkomstnivå,
- analytiker får bara se begränsad information om stöduppdraget är registrerat,
- visning av sekretessmarkerade ärenden ska loggas,
- ärenden utan relation ska inte synas alls.

Då kan reglerna skrivas om:

- Ett ärende utan sekretessmarkering visas om användaren är tilldelad ärendet eller tillhör ärendets organisatoriska enhet.
- Ett sekretessmarkerat ärende visas med full information om användaren har särskild åtkomstnivå för ärendet.
- Ett sekretessmarkerat ärende visas med begränsad information om användaren är tilldelad ärendet men saknar särskild åtkomstnivå.
- Ett sekretessmarkerat ärende visas med begränsad information för en analytiker om analytikern har ett registrerat stöduppdrag.
- Ett ärende visas inte om användaren saknar relation till ärendet.
- När ett sekretessmarkerat ärende visas, även med begränsad information, ska åtkomsten loggas.

Nu är reglerna mer precisa. De är också mer förankrade i exemplen.

## Steg 5: skapa en stabil specifikationsstruktur

En exempelbaserad specifikation bör vara lätt att läsa. Den ska inte bara vara en samling scenarier.

För det här kravområdet kan dokumentationen struktureras så här:

```md
# Sökresultat för utredningsärenden

## Syfte

Beskriver vilka utredningsärenden som visas när en användare söker, och vilken information som får visas när ärendet är sekretessmarkerat.

## Verksamhetsregler

- Regel 1: Ärenden utan sekretessmarkering visas om användaren är tilldelad ärendet eller tillhör ärendets organisatoriska enhet.
- Regel 2: Sekretessmarkerade ärenden visas med full information om användaren har särskild åtkomstnivå.
- Regel 3: Sekretessmarkerade ärenden kan visas med begränsad information när användaren har en dokumenterad relation men saknar särskild åtkomstnivå.
- Regel 4: Ärenden utan relation visas inte.
- Regel 5: Visning av sekretessmarkerade ärenden loggas.

## Exempel

[Exempeltabell]

## Öppna frågor

- Ska nekade sökträffar loggas?
- Ska användaren se att ett dolt ärende finns?
- Ska begränsad information visa ärendenummer, rubrik, status eller endast en markering?

## Tekniska konsekvenser

- Behörighetskontroll behöver kunna kombinera roll, enhet, tilldelning, stöduppdrag och åtkomstnivå.
- Loggning behöver särskilja full och begränsad visning.
```

Det här är inte tänkt som en exakt mall för alla krav. Poängen är strukturen: först syfte, sedan regler, därefter exempel, öppna frågor och tekniska konsekvenser.

## Exempelbaserad specifikation i färdigare form

Nu kan vi skriva en mer sammanhållen specifikation. Den är fortfarande på kravanalysnivå, inte kodnivå.

### Sökresultat för utredningsärenden

När en användare söker efter utredningsärenden ska brottsutredningsstödet visa de ärenden som användaren har rätt att känna till och arbeta med. Sökresultatet ska samtidigt skydda sekretessmarkerade uppgifter och ge tillräcklig information för att användaren ska kunna arbeta vidare med behöriga ärenden.

### Regler

- Ärenden utan sekretessmarkering visas om användaren är tilldelad ärendet eller tillhör ärendets organisatoriska enhet.
- Sekretessmarkerade ärenden visas med full information om användaren har särskild åtkomstnivå för ärendet.
- Sekretessmarkerade ärenden visas med begränsad information om användaren har en dokumenterad relation till ärendet men saknar särskild åtkomstnivå.
- Ärenden där användaren saknar dokumenterad relation visas inte i sökresultatet.
- När ett sekretessmarkerat ärende visas i sökresultatet ska åtkomsten loggas.
- Sökresultatet får inte avslöja att ett dolt ärende finns, om användaren saknar relation till ärendet.

### Exempel

| Exempel | Roll | Relation till ärende | Enhet | Särskild åtkomstnivå | Sekretessmarkerat | Förväntat resultat | Loggning |
|---|---|---|---|---|---|---|---|
| 1 | Utredare | Tilldelad | Annan | Nej | Nej | Ärendet visas | Nej |
| 2 | Utredare | Ingen relation | Samma | Nej | Nej | Ärendet visas | Nej |
| 3 | Utredare | Ingen relation | Annan | Nej | Nej | Ärendet visas inte | Nej |
| 4 | Utredare | Tilldelad | Annan | Nej | Ja | Begränsad information visas | Ja |
| 5 | Förundersökningsledare | Ansvarig | Annan | Ja | Ja | Full information visas | Ja |
| 6 | Analytiker | Registrerat stöduppdrag | Samma | Nej | Ja | Begränsad information visas | Ja |
| 7 | Administratör | Ingen relation | Samma | Nej | Ja | Ärendet visas inte | Nej |

### Öppna frågor

- Vilka fält ingår i begränsad information?
- Ska sökning på exakt ärendenummer hanteras annorlunda än fritextsökning?
- Ska en användare med nekad åtkomst få ett meddelande eller bara se ett tomt resultat?
- Ska det finnas en särskild granskningsrapport över sökningar som gav sekretessmarkerade träffar?

### Tekniska konsekvenser

- Behörighetsbeslutet behöver baseras på flera villkor, inte bara användarroll.
- Sökindex eller söktjänst får inte exponera dolda ärenden genom träffantal, sortering eller metadata.
- Loggning behöver göras på visningsnivå, inte bara när användaren öppnar ärendet.
- Reglerna behöver kunna testas med representativa användare, ärenden och åtkomstnivåer.

Den här dokumentationen är längre än den ursprungliga kravmeningen. Men den är inte onödigt längre. Den bär den information som kravet faktiskt kräver för att kunna förstås, byggas och testas.

## Vad hände med acceptanskriterierna?

Många kravanalytiker är vana att arbeta med acceptanskriterier. I ett traditionellt upplägg hade KR-124 kanske kompletterats med något i stil med:

- Användaren ska endast se ärenden som användaren har behörighet till.
- Användaren ska inte se sekretessmarkerade ärenden utan särskild behörighet.
- Åtkomst till sekretessmarkerade ärenden ska loggas.
- Sökresultatet ska uppdateras inom rimlig tid.

Detta är bättre än bara en kravmening, men fortfarande ganska abstrakt.

I ett SBE-arbetssätt kan acceptanskriterierna få en annan funktion. De kan vara en startpunkt för regler, men de bör inte stanna som fristående formuleringar om de behöver exempel för att förstås.

Ett acceptanskriterium som säger “användaren ska inte se sekretessmarkerade ärenden utan särskild behörighet” kan visa sig vara för grovt när exemplen diskuteras. Kanske ska vissa användare se begränsad information. Kanske ska tilldelade utredare se grunddata. Kanske ska förundersökningsledare se full information. Kanske ska vissa fält maskeras.

Det betyder inte att acceptanskriteriet var dåligt. Det betyder att det var en sammanfattning av en regel som behövde förtydligas.

## En praktisk transformationskedja

När du omvandlar ett traditionellt krav till exempelbaserad specifikation kan du använda följande kedja:

1. Identifiera kravets kärnbeteende.
2. Markera begrepp som kan tolkas olika.
3. Lista villkor som påverkar beteendet.
4. Formulera första regelutkastet i verksamhetens språk.
5. Skapa konkreta exempel som prövar regeln.
6. Låt gruppen justera regeln utifrån exemplen.
7. Separera regler, exempel, öppna frågor och tekniska konsekvenser.
8. Kontrollera om specifikationen är läsbar för verksamheten och användbar för IT.
9. Avgör om något bör uttryckas i Gherkin, tabell eller annan dokumentationsform.
10. Uppdatera specifikationen när beslut fattas.

Kedjan är iterativ. Du behöver sällan göra allt perfekt i ett första varv. Tvärtom är det normalt att ett första exempel avslöjar en regel, att regeln avslöjar ett undantag och att undantaget kräver ett nytt exempel.

## När tabell är bättre än scenario

Tabeller passar särskilt bra när beteendet styrs av kombinationer av villkor.

I vårt exempel påverkas resultatet av roll, relation, enhet, åtkomstnivå och sekretessmarkering. Om vi skrev varje rad som ett eget scenario skulle dokumentationen snabbt bli lång och svår att överblicka.

En tabell gör det lättare att se mönster:

- vilka villkor som spelar roll,
- vilka kombinationer som saknas,
- vilka utfall som finns,
- var ett exempel avviker från regeln,
- vilka termer som behöver definieras.

Tabeller är ofta mycket bra för verksamhetsdialog, särskilt när gruppen behöver diskutera beslutspunkter.

Men tabeller har också begränsningar. De visar inte alltid händelseförlopp, användarinteraktion eller sammanhang. Då kan scenarier vara bättre.

## När scenario är bättre än tabell

Scenarier passar bättre när du vill visa ett sammanhängande flöde över tid.

Anta att användaren söker efter ett sekretessmarkerat ärende, väljer en träff med begränsad information och därefter begär utökad åtkomst. Då behöver vi beskriva mer än ett beslut i en tabell. Vi behöver beskriva ett förlopp.

Ett scenario i fri text kan se ut så här:

> En utredare söker efter ett ärende som utredaren är tilldelad men saknar särskild åtkomstnivå för. Systemet visar ärendet med begränsad information. Utredaren begär utökad åtkomst och anger motivering. Förundersökningsledaren godkänner begäran. När utredaren öppnar ärendet på nytt visas full information och åtkomsten loggas.

Det här scenariot visar samspelet mellan sökning, begränsad visning, åtkomstbegäran, beslut och loggning. En tabell kan fortfarande användas för reglerna, men scenariot hjälper gruppen att förstå flödet.

## När Gherkin kan vara lämpligt

Gherkin kan vara användbart när scenariot har en tydlig förutsättning, en händelse och ett förväntat resultat. Det kan också vara värdefullt när organisationen vill koppla specifikationen till automatiserade tester med exempelvis Cucumber.

Ett scenario skulle kunna formuleras så här:

```gherkin
Scenario: Tilldelad utredare ser begränsad information för sekretessmarkerat ärende
  Given att utredaren är tilldelad ärende 1005
  And att ärende 1005 är sekretessmarkerat
  And att utredaren saknar särskild åtkomstnivå för ärendet
  When utredaren söker efter ärende 1005
  Then visas ärendet med begränsad information
  And visningen loggas
```

Det här är mer konkret än det första dåliga Gherkin-exemplet. Det innehåller specifika villkor och ett tydligt förväntat resultat.

Men även detta scenario behöver kompletteras med definitioner. Vad betyder begränsad information? Vad betyder visningen loggas? Vilka fält ingår? Var syns loggen? Vem får granska den?

Gherkin är alltså inte ett sätt att slippa analys. Det är ett format för att uttrycka en del av analysen.

## När Gherkin inte är lämpligt

Gherkin är mindre lämpligt när gruppen ännu inte förstår reglerna. Då riskerar formatet att ge en falsk känsla av precision.

Det är också mindre lämpligt när beteendet främst är en beslutstabell med många kombinationer. Då kan en tabell vara mer läsbar.

Gherkin kan dessutom bli svår för verksamheten om scenarierna blir tekniska, repetitiva eller fyllda med implementationstermer. Om verksamheten inte längre kan läsa och bekräfta specifikationen har dokumentationen förlorat en viktig del av sitt värde.

En bra tumregel är:

> Använd Gherkin när formatet gör beteendet tydligare. Använd inte Gherkin bara för att visa att ni arbetar med SBE.

## Att hålla verksamhet och IT i samma dokumentation

En av de viktigaste vinsterna med SBE är att dokumentationen kan bli en bro mellan verksamhet och IT. Men det händer inte automatiskt.

Om dokumentationen bara består av fri verksamhetstext blir den ofta svår att implementera och testa.

Om dokumentationen bara består av tekniska scenarier blir den ofta svår för verksamheten att äga.

Därför behöver specifikationen ofta ha flera lager:

- en verksamhetsnära beskrivning av syftet,
- regler uttryckta på verksamhetens språk,
- exempel som visar konkreta kombinationer,
- tekniska konsekvenser som hjälper IT utan att förvanska regeln,
- öppna frågor som visar vad som ännu inte är beslutat.

Det är särskilt viktigt i myndighetsnära system. Där kan regler ha juridiska, organisatoriska, säkerhetsmässiga och tekniska konsekvenser. Om allt blandas i samma text blir dokumentationen svår att granska. Om allt separeras för hårt uppstår dubbeldokumentation.

Målet är inte att få ett dokument som alla läser på exakt samma sätt. Målet är att få en struktur där olika läsare kan hitta sin del utan att tappa kopplingen till helheten.

## Ett exempel på dålig omvandling

Låt oss titta på en vanlig anti-pattern.

Traditionellt krav:

> Systemet ska visa sökresultat utifrån användarens behörighet.

Dålig SBE-omvandling:

```gherkin
Scenario: Behörigt sökresultat
  Given att användaren är behörig
  When användaren söker
  Then visas behöriga sökresultat
```

Problemet är att scenariot bara byter yta. Det konkretiserar inte beteendet.

Det finns inga specifika roller, inga villkor, inga utfall och inga exempelvärden. Orden “behörig” och “behöriga sökresultat” bär fortfarande hela oklarheten.

En bättre omvandling börjar med att fråga:

- Behörig på vilket sätt?
- Till vilket ärende?
- Med vilken relation?
- Med vilken åtkomstnivå?
- Med vilken typ av information?
- Med vilken loggning?
- Med vilket förväntat resultat?

Först när de frågorna har fått åtminstone preliminära svar är det meningsfullt att välja format.

## Hantera öppna frågor som en del av specifikationen

Öppna frågor är inte ett misslyckande. De är en viktig del av SBE-dokumentationen.

I traditionell kravdokumentation hamnar osäkerheter ofta i kommentarer, mötesanteckningar eller någons minne. Det gör dem svåra att följa upp.

I en exempelbaserad specifikation bör öppna frågor vara synliga där de hör hemma.

Exempel:

- Ska begränsad information innehålla ärenderubrik?
- Ska det synas att ett ärende är sekretessmarkerat?
- Ska nekade sökförsök loggas?
- Ska systemet skilja på sökning från arbetsvy och sökning från administrationsvy?
- Ska arkiverade ärenden följa samma regler som pågående ärenden?

Varje öppen fråga bör ha en ägare eller åtminstone en tydlig väg till beslut. Annars riskerar dokumentationen att se stabil ut fast den egentligen innehåller obesvarade frågor.

## Skillnaden mellan regel och teknisk konsekvens

En annan viktig omställning är att hålla isär verksamhetsregel och teknisk konsekvens.

Verksamhetsregel:

> Ett sekretessmarkerat ärende visas med begränsad information om användaren har en dokumenterad relation till ärendet men saknar särskild åtkomstnivå.

Teknisk konsekvens:

> Sökindex får inte innehålla oskyddade fält som kan exponeras för användare utan särskild åtkomstnivå.

Båda är viktiga, men de har olika funktion.

Verksamhetsregeln ska kunna förstås och bekräftas av verksamheten.

Den tekniska konsekvensen hjälper IT att se vad regeln innebär för design, arkitektur och test.

Om vi blandar ihop dem riskerar specifikationen att bli antingen för teknisk för verksamheten eller för vag för IT.

## En andra omvandling: statusövergångar

Vi tar ett till exempel från brottsutredningsstödet.

Traditionellt krav:

> Systemet ska stödja ändring av ärendestatus enligt gällande arbetsflöde.

Detta är en typisk formulering som ser ordentlig ut men lämnar mycket öppet.

Vad är gällande arbetsflöde? Vilka statusar finns? Vem får ändra status? Finns obligatoriska uppgifter? Finns undantag? Vad händer om ärendet är sekretessmarkerat? Ska statusändringen loggas?

En första regeluppsättning kan vara:

- Ett nytt ärende får status `Registrerat`.
- Ett ärende i status `Registrerat` kan ändras till `Pågående` av en utredare som är tilldelad ärendet.
- Ett ärende i status `Pågående` kan ändras till `Pausat` av tilldelad utredare eller ansvarig förundersökningsledare.
- Ett ärende i status `Pågående` kan ändras till `Avslutat` endast av ansvarig förundersökningsledare.
- Ett avslutat ärende får inte ändras tillbaka till `Pågående` utan återöppningsbeslut.
- Alla statusändringar ska loggas med tidpunkt, användare och tidigare status.

En tabell kan pröva reglerna:

| Exempel | Nuvarande status | Ny status | Roll | Relation | Förväntat resultat |
|---|---|---|---|---|---|
| 1 | Registrerat | Pågående | Utredare | Tilldelad | Status ändras |
| 2 | Registrerat | Avslutat | Utredare | Tilldelad | Statusändring nekas |
| 3 | Pågående | Pausat | Utredare | Tilldelad | Status ändras |
| 4 | Pågående | Avslutat | Förundersökningsledare | Ansvarig | Status ändras |
| 5 | Avslutat | Pågående | Förundersökningsledare | Ansvarig, inget återöppningsbeslut | Statusändring nekas |
| 6 | Avslutat | Pågående | Förundersökningsledare | Ansvarig, återöppningsbeslut finns | Status ändras |

Även här ser vi att omvandlingen inte handlar om att skriva längre text. Den handlar om att göra regelstrukturen synlig.

## Hur mycket av det gamla kravet ska vara kvar?

En vanlig fråga är om den traditionella kravformuleringen ska tas bort när exempelbaserad specifikation införs.

Svaret är: ibland, men inte alltid.

Det kan fortfarande vara värdefullt med en kort övergripande formulering som beskriver syftet. Men den bör inte ensam bära detaljerna.

I stället för att ha:

> KR-124: Systemet ska visa sökresultat för utredningsärenden utifrån användarens behörighet.

kan specifikationen ha:

> Syfte: Sökresultatet ska hjälpa användaren att hitta behöriga utredningsärenden utan att exponera ärenden eller uppgifter som användaren saknar rätt att känna till.

Det är en bättre övergripande text eftersom den uttrycker varför beteendet finns. Detaljerna ligger sedan i regler och exempel.

## Spårbarhet utan att skapa dubbeldokumentation

Organisationer som arbetar med krav behöver ofta spårbarhet. Det kan finnas behov av att koppla specifikationer till epics, features, juridiska krav, arkitekturbeslut, testfall eller leveransplaner.

SBE tar inte bort det behovet. Men det förändrar vad som bör vara den primära sanningen.

Om den traditionella kravtexten säger en sak, exemplen en annan och testerna en tredje, har organisationen inte levande dokumentation. Den har tre konkurrerande sanningar.

En bättre princip är:

- låt exempelbaserad specifikation bära beteendereglerna,
- låt övergripande krav eller features bära mål och avgränsning,
- låt testartefakter härledas från exempel där det är möjligt,
- låt tekniska beslut dokumenteras separat men länkas till reglerna,
- undvik att kopiera samma regel i flera format utan tydligt ägarskap.

Det här kräver disciplin. Det är lätt att fortsätta skriva både traditionella krav, acceptanskriterier, scenarier och testfall som separata versioner av samma sak. Då blir SBE bara ytterligare en dokumentationsbörda.

## Praktisk mall för omvandling

När du arbetar med ett befintligt krav kan följande mall användas i analysen.

| Fråga | Syfte |
|---|---|
| Vilket beteende beskriver kravet? | Hitta kärnan |
| Vilka ord kan tolkas olika? | Hitta begrepp som behöver förtydligas |
| Vilka villkor påverkar beteendet? | Hitta regler och variationer |
| Vilka utfall finns? | Undvik bara ja/nej-tänkande |
| Vilka exempel visar normalfall? | Skapa gemensam startpunkt |
| Vilka exempel visar undantag? | Fånga risk och komplexitet |
| Vilka gränsfall finns? | Hitta regelgränser |
| Vilka frågor är fortfarande öppna? | Synliggör osäkerhet |
| Vilka tekniska konsekvenser behöver IT känna till? | Undvik att tappa implementation och test |
| Vilket format gör specifikationen mest läsbar? | Välj tabell, scenario, Gherkin eller kombination |

Den här mallen kan användas i en workshop, vid förfining av backloggposter eller vid granskning av befintliga kravdokument.

## Vanliga misstag

- **Misstag: Att översätta kravtext till Gherkin utan att förtydliga regeln.**
  - Varför det händer: Formatet känns konkret och ger en känsla av framdrift.
  - Hur du undviker det: Identifiera först begrepp, villkor och utfall. Skriv scenario först när beteendet är tillräckligt förstått.

- **Misstag: Att ta bort all övergripande kravtext.**
  - Varför det händer: Organisationen vill undvika dubbeldokumentation.
  - Hur du undviker det: Behåll kort syftestext och avgränsning, men låt regler och exempel bära detaljerna.

- **Misstag: Att göra exemplen för generiska.**
  - Varför det händer: Man vill undvika påhittade data eller tror att abstrakta exempel är mer återanvändbara.
  - Hur du undviker det: Använd konkreta roller, relationer, statusar och förväntade utfall. Byt hellre känsliga detaljer mot fiktiva men realistiska exempelvärden.

- **Misstag: Att blanda verksamhetsregler och teknisk lösning.**
  - Varför det händer: IT-konsekvenserna blir tydliga under analysen och skrivs in direkt i regeln.
  - Hur du undviker det: Dokumentera tekniska konsekvenser separat och länka dem till regeln.

- **Misstag: Att se öppna frågor som brister i dokumentationen.**
  - Varför det händer: Kravdokument uppfattas ofta som något som ska se färdigt ut.
  - Hur du undviker det: Gör öppna frågor synliga, ägda och tidsatta. En synlig fråga är bättre än ett dolt antagande.

## Övningar

### Övning 1: Omvandla ett traditionellt krav

Utgå från följande krav:

> Systemet ska tillåta användare att skapa ett nytt utredningsärende om obligatoriska uppgifter är ifyllda.

Gör följande:

1. Markera ord som kan tolkas olika.
2. Lista villkor som påverkar beteendet.
3. Formulera två eller tre verksamhetsregler.
4. Skapa minst fem konkreta exempel.
5. Skriv minst tre öppna frågor.
6. Beskriv två tekniska konsekvenser utan att blanda in dem i verksamhetsreglerna.

### Övning 2: Välj rätt format

Utgå från följande tre kravområden:

- filtrering av sökresultat utifrån behörighet,
- ändring av ärendestatus,
- begäran om utökad åtkomst.

För varje kravområde, välj om du främst skulle använda:

- tabell,
- fri text-scenario,
- Gherkin-scenario,
- kombination av flera format.

Motivera valet utifrån läsbarhet för verksamheten och användbarhet för IT.

### Fördjupning

Ta ett verkligt krav från din egen organisation, eller ett krav du tidigare arbetat med. Skriv först om det som en kort syftesbeskrivning. Bryt sedan ut regler, exempel, öppna frågor och tekniska konsekvenser.

Jämför den nya strukturen med originalet:

- Vad blev tydligare?
- Vad blev längre?
- Vad blev mer testbart?
- Vad blev lättare för verksamheten att bekräfta?
- Vad blev lättare för IT att bygga eller testa?
- Vilken information saknades i originalkravet?

## Snabb sammanfattning

- SBE innebär inte att all kravtext ersätts av scenarier.
- En bra exempelbaserad specifikation kombinerar syfte, regler, exempel, öppna frågor och tekniska konsekvenser.
- Gherkin är ett möjligt format, men det löser inte otydliga regler i sig.
- Tabeller passar ofta bättre än scenarier när beteendet styrs av kombinationer av villkor.
- Scenarier passar bättre när ett flöde över tid behöver förstås.
- Öppna frågor ska göras synliga, inte gömmas undan.
- Målet är dokumentation som verksamheten kan bekräfta och IT kan använda.
- Undvik att skapa dubbeldokumentation där krav, exempel och tester blir flera konkurrerande sanningar.

## Quiz/reflektionsfrågor

1. Varför är det ofta fel att börja en SBE-omställning med att skriva allt i Gherkin?
2. Vad är skillnaden mellan en verksamhetsregel och en teknisk konsekvens?
3. När är en tabell mer lämplig än ett scenario?
4. Vilken funktion kan en kort övergripande kravtext fortfarande ha i SBE?
5. Hur kan öppna frågor bidra till bättre kravkvalitet?
6. Vad riskerar att hända om acceptanskriterier, exempel och testfall beskriver samma regel på olika sätt?

## Koppling till bokens röda tråd

Omvandlingen från traditionella krav till exempelbaserad specifikation är bokens praktiska kärna. Den visar att SBE inte ersätter all kravtext, utan hjälper kravanalytikern att avgöra vad som bör vara regel, exempel, scenario, öppen fråga eller kompletterande förklaring.


## Nästa steg

I det här kapitlet har vi gått från traditionella krav till exempelbaserad specifikation. Vi har sett hur ett krav kan delas upp i syfte, regler, exempel, öppna frågor och tekniska konsekvenser.

Nästa kapitel går djupare i själva hantverket: hur regler, exempel och scenarier formuleras i praktiken. Där fokuserar vi på kvaliteten i exemplen, hur man hittar rätt detaljnivå och hur man undviker att specifikationen blir antingen för tunn eller för tung.
