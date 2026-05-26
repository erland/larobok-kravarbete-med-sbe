# Kapitel 5: Att hitta funktionella krav som lämpar sig för SBE

## Varför detta kapitel finns

När caset nu är etablerat kan vi börja använda det på det sätt SBE är som mest värdefullt: för att hitta de delar av kravbilden där konkreta exempel skapar mer förståelse än ännu en generell kravformulering.

Erfarna kravanalytiker är ofta vana vid att formulera funktionella krav som text, kompletterade med acceptanskriterier. Det arbetssättet kan fungera väl när funktionen är enkel, när reglerna är stabila och när alla inblandade redan har samma bild av vad som menas. Men i komplexa verksamheter är det ofta just de funktionella kraven som innehåller flest dolda antaganden.

I brottsutredningsstödet kan ett krav som “utredaren ska kunna se relevanta ärenden” låta rimligt. Men det säger inte tillräckligt om vad som ska visas, vad som ska döljas, när information ska maskeras, när åtkomst ska loggas, hur status påverkar beteendet eller vilka undantag som gäller för olika roller.

SBE hjälper inte lika mycket överallt. Det är därför kravanalytikern behöver kunna välja ut rätt kandidater. Detta kapitel handlar om hur du hittar de funktionella krav som verkligen tjänar på att beskrivas med regler, exempel och scenarier.

## Lärandemål

Efter kapitlet ska du kunna:

- identifiera funktionella krav som är särskilt lämpliga för SBE,
- skilja mellan enkla funktionsbeskrivningar och krav med verksamhetslogik,
- hitta beslutspunkter, statusövergångar, undantag och gränsfall,
- bedöma när exempel ger mer värde än traditionell kravtext,
- välja rätt detaljnivå för exempel i ett myndighetsnära verksamhetscase,
- skapa en första kandidatlista över krav som bör förfinas med SBE.

## Innan vi börjar

I tidigare kapitel har vi etablerat tre viktiga utgångspunkter.

För det första handlar SBE inte om att skriva om all dokumentation till ett nytt format. Det handlar om att använda konkreta exempel där de gör störst nytta.

För det andra är kravanalytikerns roll att skapa gemensam förståelse. Det betyder att du inte bara ska dokumentera vad någon har sagt, utan också hjälpa gruppen att upptäcka vad som ännu inte är förstått.

För det tredje har brottsutredningsstödet en verksamhetskontext där regler, roller, behörigheter, informationsobjekt och arbetsflöden samspelar. Den typen av komplexitet är särskilt lämplig för SBE.

Det här kapitlet tar nästa steg: att välja ut vilka funktionella krav som bör behandlas med SBE.

## Vad menas med funktionella krav i den här boken?

I den här boken använder vi termen funktionellt krav för krav på vad systemet ska göra. Det kan handla om att skapa, ändra, visa, söka, filtrera, beräkna, tilldela, kontrollera, avisera eller exportera information.

Exempel från brottsutredningsstödet kan vara:

- skapa ett nytt utredningsärende,
- söka efter ärenden,
- filtrera sökresultat utifrån behörighet,
- visa en sammanfattning av ett ärende,
- ändra ärendestatus,
- tilldela ett ärende till en utredare,
- logga åtkomst till känslig information,
- markera uppgifter som sekretessbelagda,
- generera ett granskningsunderlag.

Alla dessa är funktionella krav. Men alla är inte lika lämpliga att börja med i SBE.

Ett enkelt krav som “systemet ska kunna spara ett telefonnummer på en kontaktperson” kan behöva en tydlig fältdefinition, valideringsregel och kanske ett par exempel. Men det är troligen inte där en längre SBE-workshop skapar mest värde.

Ett krav som “systemet ska filtrera sökresultat utifrån användarens behörighet, ärendets status och eventuell sekretessmarkering” är däremot en stark kandidat. Det innehåller flera villkor, flera aktörer, flera möjliga utfall och sannolikt flera missförståndsrisker.

## Grundprincipen: börja där beteendet kan misstolkas

Ett funktionellt krav lämpar sig för SBE när det inte räcker att beskriva funktionen på en generell nivå. Det är ofta ett tecken på att flera personer kan läsa samma krav och ändå föreställa sig olika systembeteenden.

En praktisk tumregel är:

> Använd SBE där ett krav behöver exempel för att bli förstått på samma sätt av verksamhet, IT och test.

Det betyder att du inte ska fråga: “Kan detta krav skrivas i Gherkin?” Det är fel startpunkt.

Fråga i stället:

- Kan olika intressenter tolka kravet olika?
- Finns det flera villkor som påverkar beteendet?
- Finns det undantag eller specialfall?
- Finns det gränser där beteendet ändras?
- Behöver verksamheten kunna granska och bekräfta logiken?
- Behöver IT och test förstå exakt vilka kombinationer som ska stödjas?
- Skulle ett par konkreta exempel avslöja viktiga frågor?

Om svaret är ja på flera av frågorna är kravet sannolikt en bra SBE-kandidat.

## SBE-kandidater i brottsutredningsstödet

Låt oss utgå från en första kravlista för brottsutredningsstödet.

| Funktion | Traditionell formulering | SBE-potential |
|---|---|---|
| Söka ärenden | En användare ska kunna söka efter utredningsärenden | Hög |
| Visa ärendedetaljer | En användare ska kunna visa information om ett ärende | Hög |
| Skapa ärende | En behörig användare ska kunna skapa ett nytt utredningsärende | Medel |
| Ändra ärendestatus | En behörig användare ska kunna ändra status på ett ärende | Hög |
| Lägga till anteckning | En användare ska kunna lägga till en anteckning i ett ärende | Medel |
| Markera uppgift som sekretessbelagd | En behörig användare ska kunna sekretessmarkera uppgifter | Hög |
| Logga åtkomst | Systemet ska logga åtkomst till känslig information | Hög |
| Exportera underlag | En användare ska kunna exportera granskningsunderlag | Medel |
| Spara användarinställningar | Systemet ska spara användarens vyinställningar | Låg till medel |

Tabellen är inte en slutlig prioritering. Den visar att SBE-potentialen beror på hur mycket verksamhetslogik, variation och risk som finns i beteendet.

Sökning, behörighetsfiltrering, statusövergångar och sekretess är starka kandidater eftersom de påverkas av regler, roller och kontext. Spara vyinställningar kan fortfarande behöva krav, men ger kanske inte samma effekt av exempelbaserad förfining.

## Sex signaler på att ett krav passar för SBE

### 1. Kravet innehåller beslut

Ett beslut uppstår när systemet behöver avgöra vad som ska hända baserat på vissa villkor. Det kan uttryckas med ord som “om”, “när”, “bara”, “förutom”, “ska inte”, “beroende på” eller “under förutsättning att”.

Exempel:

> Om ärendet är sekretessmarkerat ska endast användare med särskild behörighet kunna se skyddade uppgifter.

Det här är ett beslut. Systemet behöver avgöra om användaren får se informationen. För att förstå beslutet behöver vi veta vilka villkor som påverkar det.

En första regel kan vara:

> En användare får se skyddade uppgifter i ett sekretessmarkerat ärende om användaren är tilldelad ärendet och har särskild behörighet för skyddade uppgifter.

Redan här uppstår frågor:

- Vad händer om användaren är tilldelad men saknar särskild behörighet?
- Vad händer om användaren har särskild behörighet men inte är tilldelad ärendet?
- Gäller samma regel för förundersökningsledare?
- Ska nekad åtkomst loggas?
- Ska användaren se att uppgiften finns men är dold, eller ska den inte visas alls?

Det är precis den typen av frågor SBE ska synliggöra.

### 2. Kravet har flera möjliga utfall

Krav som bara har ett enkelt ja-svar är sällan de mest intressanta SBE-kandidaterna. Krav med flera möjliga utfall är däremot ofta bra kandidater.

Exempel:

> När en utredare söker efter ärenden ska systemet visa ärenden som utredaren har behörighet att se.

Möjliga utfall kan vara:

- ärendet visas med full information,
- ärendet visas med begränsad information,
- ärendet visas inte alls,
- ärendet visas men skyddade fält maskeras,
- åtkomsten kräver motivering,
- åtkomsten nekas och loggas.

När det finns flera utfall behöver gruppen förstå exakt vilket utfall som gäller i vilken situation.

En möjlig exempeltabell kan se ut så här:

| Situation | Relation till ärende | Sekretessmarkering | Särskild behörighet | Förväntat utfall |
|---|---|---|---|---|
| Tilldelad utredare söker vanligt ärende | Tilldelad | Nej | Nej | Ärendet visas |
| Tilldelad utredare söker sekretessmarkerat ärende | Tilldelad | Ja | Nej | Ärendet visas med skyddade uppgifter dolda |
| Tilldelad utredare med särskild behörighet söker sekretessmarkerat ärende | Tilldelad | Ja | Ja | Ärendet visas med skyddade uppgifter |
| Utredare utan relation söker vanligt ärende | Ingen | Nej | Nej | Ärendet visas inte |
| Förundersökningsledare söker ärende i egen grupp | Beslutsroll | Ja | Ja | Ärendet visas och åtkomsten loggas |

Tabellen är inte färdig kravdokumentation. Den är ett sätt att få fram vilka regler gruppen faktiskt menar.

### 3. Kravet innehåller undantag

Undantag är ofta där traditionell kravtext tappar precision. De kan gömmas i formuleringar som “normalt”, “i vissa fall”, “kan”, “vid behov” eller “om det är motiverat”.

Exempel:

> Utredare ska normalt bara kunna se ärenden inom den egna enheten, men undantag kan göras vid samverkan mellan enheter.

Detta är en stark SBE-kandidat. Undantaget är troligen viktigare än huvudregeln, eftersom det är där felaktig åtkomst eller felaktig begränsning kan uppstå.

Frågor som behöver konkretiseras:

- Vem beslutar om samverkan?
- Hur syns samverkan i systemet?
- Gäller undantaget hela ärendet eller bara vissa uppgifter?
- Hur länge gäller undantaget?
- Krävs motivering?
- Ska åtkomst loggas annorlunda?
- Kan undantaget återkallas?

Ett exempel kan vara:

| Exempel | Användare | Enhet | Ärendeenhet | Samverkan registrerad | Förväntat beteende |
|---|---|---|---|---|---|
| Ingen samverkan | Utredare A | Nord | Syd | Nej | Ärendet visas inte |
| Samverkan finns | Utredare A | Nord | Syd | Ja | Ärendet visas med tillåtna uppgifter |
| Samverkan har upphört | Utredare A | Nord | Syd | Tidigare, men avslutad | Ärendet visas inte |

Här ser vi att “samverkan” behöver bli ett tydligt verksamhetsbegrepp, inte bara ett ord i en kravtext.

### 4. Kravet påverkas av status

Många system har tillstånd eller statusar. I brottsutredningsstödet kan ett ärende exempelvis vara nytt, pågående, vilande, granskningsklart, avslutat eller arkiverat.

Status påverkar ofta vad användaren får göra.

Exempel:

> En utredare ska kunna ändra status på ett ärende enligt gällande process.

Det kravet är nästan omöjligt att förstå utan exempel. “Enligt gällande process” kan betyda mycket.

En första statusmatris kan se ut så här:

| Nuvarande status | Begärd ny status | Roll | Förväntat beteende |
|---|---|---|---|
| Nytt | Pågående | Utredare | Status ändras |
| Pågående | Granskningsklart | Utredare | Status ändras om obligatoriska uppgifter finns |
| Granskningsklart | Avslutat | Förundersökningsledare | Status ändras |
| Granskningsklart | Pågående | Förundersökningsledare | Status ändras med motivering |
| Avslutat | Pågående | Utredare | Statusändring nekas |
| Arkiverat | Pågående | Förundersökningsledare | Statusändring nekas |

Den här typen av krav passar ofta mycket bra för SBE eftersom exemplen snabbt visar vilka övergångar som är tillåtna, förbjudna eller villkorade.

### 5. Kravet behöver gränsfall

Gränsfall uppstår där beteendet ändras vid en viss gräns. Gränsen kan vara numerisk, tidsmässig, organisatorisk, juridisk eller processuell.

I brottsutredningsstödet kan gränsfall handla om:

- sista dag för komplettering,
- antal träffar i en sökning,
- hur länge åtkomst ska vara tillfälligt giltig,
- när ett ärende blir arkiverat,
- när en anteckning får ändras,
- hur gammal information får vara innan den kräver särskild varning,
- när en användare räknas som tilldelad ett ärende.

Ett krav kan vara:

> Tillfällig åtkomst till ett ärende ska upphöra efter angiven giltighetstid.

Det låter enkelt, men gränsen behöver exempel:

| Exempel | Giltig till | Tidpunkt för åtkomstförsök | Förväntat beteende |
|---|---|---|---|
| Före sista tidpunkt | 2026-06-15 17:00 | 2026-06-15 16:59 | Åtkomst tillåts |
| Exakt vid sista tidpunkt | 2026-06-15 17:00 | 2026-06-15 17:00 | Åtkomst nekas |
| Efter sista tidpunkt | 2026-06-15 17:00 | 2026-06-15 17:01 | Åtkomst nekas |

Det viktiga är inte datumen i sig. Det viktiga är att gruppen behöver bestämma vad “till och med” betyder.

### 6. Kravet är viktigt nog att vara gemensam sanning

SBE kräver tid. Det ska användas där gemensam förståelse är värdefull. Ett krav kan vara tekniskt möjligt att beskriva med exempel men ändå inte vara värt en större SBE-insats.

Starka kandidater är ofta krav som:

- påverkar rättssäkerhet,
- påverkar informationssäkerhet,
- påverkar användarnas centrala arbetsflöden,
- ofta missförstås,
- ofta ändras,
- behöver kunna förvaltas länge,
- berör flera team eller system,
- är svåra att testa utan tydliga exempel.

I brottsutredningsstödet innebär det att behörighet, sekretess, status, sökning, loggning och spårbarhet bör prioriteras högre än enklare skärminställningar.

## En enkel urvalsmodell

När du har en kravlista kan du använda en enkel urvalsmodell. Syftet är inte att skapa en exakt poängsättning, utan att hjälpa teamet välja var SBE ger mest effekt.

Bedöm varje krav utifrån följande frågor:

| Fråga | Låg signal | Hög signal |
|---|---|---|
| Finns flera villkor? | Ett enkelt beteende | Många villkor samverkar |
| Finns flera utfall? | Ett tydligt resultat | Olika resultat beroende på situation |
| Finns undantag? | Inga kända undantag | Flera undantag eller specialfall |
| Finns gränsfall? | Inga tydliga gränser | Tidsgränser, statusgränser eller regelgränser |
| Är konsekvensen av fel stor? | Liten påverkan | Rättssäkerhet, sekretess eller verksamhetskritik |
| Behöver flera parter förstå samma regel? | En lokal detalj | Verksamhet, IT, test och förvaltning berörs |

Ett krav som får hög signal på flera frågor är en bra SBE-kandidat.

## Exempel: första urval i caset

Anta att teamet har samlat följande funktionella kravkandidater för en första leverans av brottsutredningsstödet:

| ID | Kravkandidat | SBE-prioritet | Motivering |
|---|---|---|---|
| FK-01 | Söka efter utredningsärenden | Hög | Sökresultat påverkas av behörighet, sekretess och relation till ärende |
| FK-02 | Visa ärendesammanfattning | Hög | Olika roller ska se olika informationsnivåer |
| FK-03 | Skapa nytt utredningsärende | Medel | Viktigt arbetsflöde, men initialt färre komplexa beslut |
| FK-04 | Ändra ärendestatus | Hög | Statusövergångar styr vad som får göras |
| FK-05 | Lägga till fri anteckning | Medel | Kräver regler för ändring, synlighet och historik |
| FK-06 | Markera uppgift som sekretessbelagd | Hög | Verksamhetskritiskt och påverkar visning, sökning och loggning |
| FK-07 | Spara användarens filterinställningar | Låg | Mest användarpreferens, få verksamhetsregler |
| FK-08 | Generera granskningsunderlag | Medel | Kan kräva exempel, men beror på dokumentets komplexitet |

Ett rimligt första fokus kan vara FK-01, FK-02, FK-04 och FK-06. Dessa krav har hög verksamhetsrisk och många villkor. FK-03 och FK-05 kan hanteras med enklare exempel först och fördjupas senare om de visar sig vara mer komplexa än väntat.

## Att skilja mellan kravkandidat och SBE-specifikation

En vanlig fallgrop är att försöka skriva den färdiga SBE-specifikationen direkt när kravet identifieras. Det leder ofta till för tidig detaljering.

I detta kapitel är målet bara att hitta kandidater. En kandidat kan dokumenteras kort:

| Fält | Innehåll |
|---|---|
| Kandidat | Filtrera sökresultat utifrån behörighet |
| Varför SBE? | Många villkor, flera roller, sekretess, hög risk vid fel |
| Berörda aktörer | Utredare, förundersökningsledare, systemförvaltare, testare |
| Första regelidé | En användare ska bara se ärenden som användaren har en giltig relation till |
| Exempel att utforska | Tilldelad utredare, annan enhet, sekretessmarkerat ärende, tillfällig åtkomst |
| Öppna frågor | Vad räknas som giltig relation? Ska nekad åtkomst loggas? |

Det här är tillräckligt för att planera en förfining eller workshop. Den färdiga specifikationen kommer senare.

## Funktioner som ofta passar bra

I många verksamhetssystem passar följande typer av funktionella krav särskilt bra för SBE.

### Behörighet och åtkomst

Behörighet är nästan alltid en stark kandidat, särskilt när behörighet inte bara är rollbaserad. I myndighetsmiljö påverkas åtkomst ofta av roll, organisatorisk tillhörighet, ärenderelation, sekretess, delegation, tillfälligt beslut och loggningskrav.

SBE kan hjälpa gruppen se skillnaden mellan:

- vem som får se att ett ärende finns,
- vem som får öppna ärendet,
- vem som får se skyddade uppgifter,
- vem som får ändra information,
- vem som får fatta beslut,
- när åtkomst måste motiveras,
- när åtkomst ska loggas.

Det är sällan tillräckligt att skriva “systemet ska kontrollera behörighet”.

### Sökning och filtrering

Sökning verkar ofta enkel men innehåller många regler. Vad ska hända när användaren söker på ett ärendenummer som finns men inte är tillgängligt? Ska systemet visa noll träffar, ett maskerat resultat eller ett meddelande? Ska sökningen loggas? Får användaren söka på personuppgifter? Ska gamla eller arkiverade ärenden inkluderas?

SBE hjälper till att fånga dessa frågor med konkreta exempel.

### Status och arbetsflöden

Statusövergångar är ofta tacksamma för exempel eftersom reglerna kan beskrivas i tabeller och scenarier. Det blir tydligt vilka övergångar som är tillåtna, vilka som kräver extra villkor och vilka som ska nekas.

### Validering av verksamhetsdata

Viss validering är enkel, som att ett obligatoriskt fält måste vara ifyllt. Annan validering är verksamhetslogik.

Exempel:

> Ett ärende får inte markeras som granskningsklart om obligatoriska åtgärder saknar ansvarig utredare.

Detta kräver exempel, eftersom gruppen behöver definiera vilka åtgärder som räknas, vad “saknar ansvarig” betyder och om undantag finns.

### Beräkningar och sammanställningar

Om systemet räknar, summerar, prioriterar, väger samman eller klassificerar information är SBE ofta värdefullt.

I brottsutredningsstödet kan det handla om att visa en sammanfattning av ärendets status, antal öppna åtgärder, riskmarkeringar eller granskningsbehov.

### Notifieringar och händelser

Notifieringar verkar ofta enkla tills man börjar fråga när de ska skickas, till vem, hur ofta, under vilka undantag och vad som händer om status ändras tillbaka.

Exempel:

> Systemet ska meddela ansvarig utredare när ett ärende kräver komplettering.

SBE-frågor:

- Vem är ansvarig utredare om flera är tilldelade?
- Ska förundersökningsledaren också meddelas?
- Ska notifiering skickas direkt eller samlas?
- Ska den skickas igen om kompletteringen inte görs?
- Vad händer om ärendet avslutas innan kompletteringen görs?

## Funktioner som inte alltid behöver SBE

SBE är inte ett mål i sig. Vissa krav kan dokumenteras enklare.

Låg SBE-nytta kan gälla krav som:

- bara beskriver enkel fältvisning,
- har ett självklart beteende utan verksamhetsregler,
- är rent tekniska konfigurationer,
- saknar variation,
- inte är kritiska för verksamhetsförståelsen,
- redan är tillräckligt tydliga genom standardkomponenter eller etablerade designmönster.

Exempel:

> Användaren ska kunna välja antal rader per sida i sökresultatet.

Det kan behöva beskrivas, men kräver kanske inte en workshop med verksamhet, test och utveckling.

Däremot kan ett till synes enkelt krav visa sig ha dolda regler. Om antalet rader per sida påverkar prestanda, informationssäkerhet, export eller användarens möjlighet att få överblick kan det behöva mer analys. Poängen är att välja medvetet, inte att avfärda kategorier mekaniskt.

## Att hitta kandidater i befintlig kravdokumentation

Många organisationer börjar inte från tomt papper. De har kravlistor, epics, user stories, acceptanskriterier, processbeskrivningar, regelverk och mötesanteckningar.

När du letar efter SBE-kandidater i befintligt material kan du söka efter språkliga signaler.

Ord och formuleringar som ofta pekar på SBE-potential:

- “beroende på”,
- “vid behov”,
- “normalt”,
- “i vissa fall”,
- “om möjligt”,
- “behörig användare”,
- “relevant information”,
- “gällande process”,
- “enligt regelverket”,
- “korrekt status”,
- “tillräcklig information”,
- “ska valideras”,
- “ska kontrolleras”,
- “undantag”.

Dessa uttryck är inte fel. Men de visar ofta att kravet behöver konkretiseras.

Ta denna formulering:

> Systemet ska visa relevant ärendeinformation för behöriga användare enligt gällande sekretessregler.

Det är en klassisk kandidat för SBE. Den innehåller minst fyra ord som kräver förtydligande:

- relevant,
- behöriga,
- gällande,
- sekretessregler.

En möjlig första analys kan vara:

| Otydligt uttryck | Fråga att ställa | Möjlig SBE-väg |
|---|---|---|
| Relevant ärendeinformation | Vilka uppgifter ingår i olika situationer? | Exempel per roll och ärendestatus |
| Behöriga användare | Vad gör användaren behörig? | Regler och exempel för relation till ärende |
| Gällande sekretessregler | Vilka regler påverkar visningen? | Exempel för sekretessmarkerade uppgifter |
| Visa | Full visning, maskering eller ingen träff? | Scenarier med förväntat utfall |

## Att hitta kandidater i samtal

SBE-kandidater dyker ofta upp i samtal innan de syns i dokumentationen. Som kravanalytiker bör du lyssna efter situationer där deltagare uttrycker osäkerhet, motsäger varandra eller använder vaga begrepp.

Typiska signaler:

- “Det beror på.”
- “Så brukar vi inte göra.”
- “Det där gäller bara vissa ärenden.”
- “Det måste juristen svara på.”
- “Utredarna menar nog en annan sak med status.”
- “Test kommer behöva veta exakt hur detta ska fungera.”
- “Det där är självklart.”
- “Det där får inte bli fel.”

Särskilt frasen “det är självklart” är värd att undersöka. I komplexa domäner är det självklara ofta bara självklart för vissa personer.

En bra fråga är:

> Kan du ge ett exempel där det fungerar så, och ett exempel där det inte fungerar så?

Den frågan förflyttar samtalet från abstrakt övertygelse till konkret beteende.

## En praktisk kandidatworkshop

En kort kandidatworkshop kan användas innan man går in i full exempelworkshop. Syftet är att välja ut de funktionella krav som bör förfinas med SBE.

### Förberedelse

Samla ett begränsat material:

- en lista över aktuella funktioner,
- centrala processflöden,
- kända problem eller tolkningsfrågor,
- befintliga acceptanskriterier,
- viktiga verksamhetsregler,
- riskområden från test eller förvaltning.

Bjud in personer som kan bedöma både verksamhetsvärde och genomförbarhet:

- kravanalytiker,
- verksamhetsrepresentant,
- testare,
- utvecklare,
- arkitekt eller lösningsansvarig vid behov,
- systemförvaltare om förvaltning och regler är centrala.

### Genomförande

Gå igenom varje funktion och bedöm:

1. Vilket beteende ska funktionen stödja?
2. Var finns störst tolkningsrisk?
3. Vilka regler påverkar beteendet?
4. Finns flera roller, statusar eller utfall?
5. Vilka exempel skulle hjälpa oss förstå?
6. Vad händer om vi missförstår kravet?
7. Ska detta förfinas med SBE nu, senare eller inte alls?

Dokumentera resultatet som en kandidatlista, inte som färdig specifikation.

### Resultat

Efter workshopen bör ni ha:

- en prioriterad lista över SBE-kandidater,
- en första hypotes om regler och exempel,
- öppna frågor,
- beslut om vilka krav som ska förfinas först,
- insikt om vilka krav som kan dokumenteras enklare.

## Exempel: kandidatlista efter workshop

Efter en första kandidatworkshop för brottsutredningsstödet kan resultatet se ut så här:

| Prioritet | Kandidat | Varför SBE? | Nästa steg |
|---|---|---|---|
| 1 | Filtrera sökresultat utifrån behörighet | Hög risk, många regler, flera roller | Exempelworkshop med utredare, test och utveckling |
| 2 | Visa sekretessmarkerade uppgifter | Rättssäkerhet och informationssäkerhet | Ta fram exempeltabell för roll, relation och behörighet |
| 3 | Ändra ärendestatus | Statusövergångar styr arbetsflödet | Skapa statusmatris |
| 4 | Logga åtkomst till känsliga uppgifter | Viktigt för spårbarhet och granskning | Skilj funktionellt beteende från kvalitetskrav |
| 5 | Skapa nytt ärende | Viktigt men initialt enklare | Dokumentera huvudflöde och några valideringsexempel |
| 6 | Spara vyinställningar | Låg verksamhetsrisk | Hantera med enklare kravtext |

Det här ger gruppen fokus. SBE används där osäkerhet och risk är störst.

## När ett krav är för stort

En annan vanlig fallgrop är att välja krav som är för stora.

Exempel:

> Systemet ska stödja handläggning av brottsutredningsärenden.

Det är inte en bra SBE-kandidat i sig. Det är för stort och innehåller många olika beteenden.

Bryt i stället ned det i mer konkreta funktionella beteenden:

- skapa ärende,
- tilldela ansvarig utredare,
- registrera uppgift,
- markera uppgift som skyddsvärd,
- söka ärende,
- visa ärendesammanfattning,
- ändra status,
- generera granskningsunderlag.

Sedan kan varje beteende bedömas utifrån SBE-potential.

En bra SBE-kandidat är tillräckligt avgränsad för att kunna diskuteras konkret, men tillräckligt viktig och komplex för att exempel ska tillföra värde.

## När ett krav är för litet

Det motsatta problemet är krav som är så små att exemplen bara bekräftar självklarheter.

Exempel:

> Fältet “ärendenamn” ska kunna innehålla högst 120 tecken.

Det kan dokumenteras som en valideringsregel. Ett exempel kan vara användbart om det finns gränsfall, men det kräver troligen inte en full SBE-behandling.

Om däremot “ärendenamn” används i sökning, export, sekretessmaskering och arkivering kan det ingå i ett större exempel. Men då är det inte längdregeln i sig som är huvudkandidaten.

## Att hantera beroenden mellan kandidater

Funktionella krav är sällan helt oberoende. I brottsutredningsstödet hänger sökning, behörighet, sekretess och loggning ihop.

Ett vanligt misstag är att behandla varje krav isolerat och missa att samma regel påverkar flera funktioner.

Exempel:

- Behörighet påverkar sökresultat.
- Behörighet påverkar ärendedetaljer.
- Behörighet påverkar export.
- Behörighet påverkar loggning.
- Behörighet påverkar statusändringar.

Här behöver kravanalytikern skilja mellan en återanvändbar regel och flera funktionella beteenden där regeln används.

En möjlig struktur är:

| Typ | Exempel | Dokumentationssätt |
|---|---|---|
| Gemensam regel | Vad räknas som giltig ärenderelation? | Regel med exempel |
| Funktionellt beteende | Sökresultat filtreras utifrån giltig relation | Scenario eller exempeltabell |
| Funktionellt beteende | Ärendedetaljer visas eller maskeras | Scenario eller exempeltabell |
| Teknisk konsekvens | Åtkomstbeslut behöver kunna loggas | Kompletterande teknisk notering |
| Öppen fråga | Ska nekade sökningar loggas? | Öppen fråga tills beslut finns |

Detta förhindrar dubbeldokumentation och gör det lättare att hålla dokumentationen levande.

## Rätt detaljnivå vid urval

När du väljer SBE-kandidater behöver du inte fånga alla exempel direkt. Det räcker att identifiera varför kravet behöver exempel.

För låg detaljnivå:

> Behörighet är viktigt.

För hög detaljnivå i urvalsfasen:

> Om utredare A från enhet Nord söker klockan 14:03 efter ärende 1005 som är sekretessmarkerat, tilldelat genom samverkansbeslut 2026-04-12 och har skyddsvärd uppgift typ B ska systemet visa...

Lagom detaljnivå:

> Filtrering av sökresultat bör förfinas med SBE eftersom resultatet påverkas av relation till ärende, organisatorisk enhet, sekretessmarkering och särskild behörighet. Första exempel bör täcka tilldelad utredare, annan enhet, sekretessmarkerat ärende och förundersökningsledare.

Urvalsfasen ska hjälpa dig välja rätt arbete. Den ska inte ersätta själva förfiningen.

## Vanliga misstag

- **Misstag: Att försöka använda SBE för allt.**
  - Varför det händer: Teamet blir entusiastiskt och vill göra arbetssättet konsekvent över hela kravmassan.
  - Hur du undviker det: Prioritera krav med hög tolkningsrisk, många villkor eller stor konsekvens vid fel.

- **Misstag: Att välja tekniskt intressanta krav i stället för verksamhetskritiska krav.**
  - Varför det händer: IT och test ser snabbt möjligheter till automation.
  - Hur du undviker det: Fråga alltid vilket verksamhetsbeslut eller beteende exemplen ska skapa förståelse kring.

- **Misstag: Att börja med Gherkin innan gruppen har förstått regeln.**
  - Varför det händer: Formatet känns konkret och ger sken av struktur.
  - Hur du undviker det: Börja med verksamhetens språk, regler och exempel. Välj format senare.

- **Misstag: Att behandla återkommande regler som separata krav varje gång.**
  - Varför det händer: Kravlistor är ofta organiserade per funktion eller vy.
  - Hur du undviker det: Identifiera gemensamma regler och dokumentera hur de används i olika funktionella beteenden.

- **Misstag: Att bara välja krav där verksamheten redan är enig.**
  - Varför det händer: Det känns enklare att börja där det finns konsensus.
  - Hur du undviker det: Använd SBE där det finns risk för missförstånd. Oenighet är ofta ett tecken på att exemplen behövs.

## Övningar

### Övning 1: Bedöm SBE-potential

Läs följande kravkandidater och bedöm om de har låg, medel eller hög SBE-potential.

| Kravkandidat | Din bedömning | Motivering |
|---|---|---|
| Användaren ska kunna söka efter ärenden |  |  |
| Systemet ska spara användarens valda startsida |  |  |
| En utredare ska kunna se skyddade uppgifter om behörighet finns |  |  |
| Ett ärende ska kunna ändra status enligt gällande process |  |  |
| Systemet ska visa datum i formatet ÅÅÅÅ-MM-DD |  |  |
| En förundersökningsledare ska kunna återöppna ett avslutat ärende vid komplettering |  |  |

Jämför din bedömning med följande frågor:

- Finns flera villkor?
- Finns flera möjliga utfall?
- Finns undantag?
- Är konsekvensen av fel stor?
- Behöver flera parter förstå samma beteende?

### Övning 2: Hitta dolda beslut

Utgå från formuleringen:

> Systemet ska visa relevant ärendeinformation för behöriga användare.

Skriv ned minst fem beslut som döljer sig i kravet. Exempel:

- Vad betyder behörig?
- Vilken information är relevant?
- Ska skyddade uppgifter visas, döljas eller maskeras?

Fortsätt med egna frågor tills du har en lista som skulle kunna användas i en kandidatworkshop.

### Övning 3: Skapa en kandidatbeskrivning

Välj ett funktionellt krav från ett eget projekt eller från brottsutredningsstödet. Fyll i följande struktur:

| Fält | Innehåll |
|---|---|
| Kandidat |  |
| Varför SBE? |  |
| Berörda aktörer |  |
| Första regelidé |  |
| Exempel att utforska |  |
| Öppna frågor |  |

Målet är inte att skriva färdig specifikation. Målet är att avgöra om kravet förtjänar SBE-förfining.

### Fördjupning

Välj ett krav som du först bedömde som låg SBE-potential. Försök sedan hitta om det finns någon dold regel, gräns eller verksamhetsrisk. Om du hittar en sådan, ändra bedömningen och förklara varför. Om du inte hittar någon, formulera varför kravet kan dokumenteras enklare.

## Snabb sammanfattning

- SBE ska användas där konkreta exempel skapar gemensam förståelse.
- Funktionella krav med beslut, undantag, flera utfall, statusövergångar eller gränsfall är ofta bra kandidater.
- Alla funktionella krav behöver inte behandlas med SBE.
- Krav som rör behörighet, sökning, sekretess, status och loggning är starka kandidater i brottsutredningsstödet.
- Urvalsfasen ska ge en prioriterad kandidatlista, inte färdiga specifikationer.
- Gherkin, Cucumber eller Concordion bör inte styra urvalet. Först kommer förståelsen, sedan formatet.

## Quiz/reflektionsfrågor

1. Vilka tre signaler tycker du är viktigast när du bedömer om ett funktionellt krav passar för SBE?
2. Varför är krav med flera möjliga utfall ofta bättre SBE-kandidater än krav med ett enkelt huvudflöde?
3. Vad är risken med att börja skriva Gherkin innan verksamhetsregeln är förstådd?
4. Hur kan du skilja mellan en återanvändbar regel och ett funktionellt beteende där regeln används?
5. Vilka krav i brottsutredningsstödet skulle du prioritera för en första SBE-workshop, och varför?

## Koppling till bokens röda tråd

Urvalet av funktionella krav är en styrningsfråga. Om allt dokumenteras med exempel blir materialet tungt; om bara enkla normalfall dokumenteras missar arbetssättet sitt syfte. Resten av boken bygger därför vidare på principen att SBE används där konkret beteende, beslut och undantag behöver delas mellan roller.


## Nästa steg

Nu har vi ett sätt att hitta funktionella krav som lämpar sig för SBE. Nästa kapitel går vidare till själva omställningen: hur traditionella krav och acceptanskriterier kan omvandlas till exempelbaserad specifikation.

Där kommer vi att ta en traditionell kravformulering från brottsutredningsstödet och stegvis bryta ned den i regler, exempel, scenarier och kompletterande förklaringar.
