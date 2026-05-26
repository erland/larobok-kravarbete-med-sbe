# Kapitel 14: Icke-funktionella krav och kvalitetskrav

## Varför detta kapitel finns

SBE används ofta starkast för funktionella krav: vem gör vad, i vilket sammanhang, enligt vilka regler och med vilket förväntat resultat. Där passar konkreta exempel naturligt. Ett exempel kan visa när en utredare får se ett ärende, när systemet ska dölja känslig information eller när en statusövergång ska stoppas.

Men ett system blir inte användbart bara för att dess funktionella beteende är korrekt.

Ett brottsutredningsstöd måste också vara säkert, tillgängligt, spårbart, begripligt, robust och möjligt att förvalta. Det måste kunna hantera känsliga uppgifter utan att läcka information. Det måste ge rimliga svarstider när en utredare söker i stora datamängder. Det måste logga viktiga händelser på ett sätt som både stödjer revision och skyddar integritet. Det måste vara tillgängligt för användare med olika förutsättningar. Det måste fungera även när angränsande system svarar långsamt eller inte alls.

Den typen av krav brukar kallas icke-funktionella krav, kvalitetskrav eller ibland kvalitetsattribut. De beskriver inte alltid en enskild funktion, utan egenskaper som systemet ska ha.

Det här kapitlet handlar om hur sådana krav kan hanteras i ett SBE-arbetssätt.

Målet är inte att tvinga in alla kvalitetskrav i Gherkin-scenarier eller exempelmallar. Det vore ett misstag. Målet är i stället att visa hur SBE kan hjälpa kravanalytikern att konkretisera kvalitetskrav där exempel skapar värde, och samtidigt visa när andra dokumentationsformer behövs.

En bra SBE-dokumentation för kvalitetskrav behöver ofta kombinera tre saker:

- konkreta exempel som visar vad kravet betyder i verksamhetens vardag
- mätbara kriterier som gör kravet verifierbart
- kompletterande beslut, riktlinjer eller arkitekturdokumentation som förklarar hur egenskapen ska uppnås

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan funktionella krav, generella krav och kvalitetskrav
- identifiera när ett kvalitetskrav kan konkretiseras med exempel
- formulera kvalitetskrav så att de blir begripliga för verksamheten och användbara för IT
- kombinera exempel med mätbara kriterier, riktlinjer och arkitekturbeslut
- hantera säkerhet, prestanda, loggning, spårbarhet, användbarhet, tillgänglighet och robusthet i ett SBE-arbetssätt
- undvika vanliga misstag där kvalitetskrav blir antingen vaga principer eller tekniska detaljkrav utan verksamhetsförankring

## Innan vi börjar

I praktiken blandas kravtyper ofta ihop.

Ett funktionellt krav kan vara:

> När en utredare öppnar ett ärende ska systemet visa ärendets grunduppgifter.

Ett generellt funktionellt krav kan vara:

> Alla åtkomstförsök till sekretessmarkerade ärenden ska loggas.

Ett kvalitetskrav kan vara:

> Systemet ska kunna visa ärendets grunduppgifter med acceptabel svarstid även när många användare arbetar samtidigt.

Alla tre kan gälla samma funktion. De beskriver bara olika aspekter av den.

Det är därför olämpligt att skapa en skarp mur mellan funktionella krav och kvalitetskrav. I ett verkligt kravarbete behöver de hållas ihop. När en utredare söker efter ett ärende spelar det roll både vad sökningen ska göra, vem som får se resultatet, hur snabbt svaret ska komma, hur träffarna ska filtreras, vad som ska loggas och hur systemet ska bete sig vid fel.

SBE hjälper oss att hålla ihop dessa perspektiv genom konkreta situationer. Men SBE ersätter inte all annan kravdokumentation. Ibland räcker ett exempel. Ibland behövs mätvärden. Ibland behövs riskanalys, hotmodellering, arkitekturbeslut, teststrategi eller riktlinjer.

Den professionella frågan är därför inte:

> Kan detta skrivas som ett SBE-scenario?

Den bättre frågan är:

> Vilken kombination av exempel, mätbara kriterier och kompletterande dokumentation gör kravet begripligt, verifierbart och förvaltningsbart?

## Vad menas med kvalitetskrav?

Kvalitetskrav beskriver egenskaper hos systemet, snarare än bara en funktionell reaktion på en användarhandling.

Vanliga områden är:

- prestanda
- säkerhet
- åtkomstkontroll
- loggning och spårbarhet
- användbarhet
- tillgänglighet
- robusthet
- driftsäkerhet
- skalbarhet
- underhållbarhet
- interoperabilitet
- datakvalitet
- informationsskydd
- revisionsbarhet

I brottsutredningsstödet kan kvalitetskrav låta så här:

- Sökning efter ärenden ska ge svar inom en tid som stödjer utredarens arbetsflöde.
- Systemet ska skydda sekretessmarkerade uppgifter från obehörig åtkomst.
- Systemet ska logga åtkomst till känslig information på ett sätt som möjliggör efterhandskontroll.
- Gränssnittet ska kunna användas av handläggare som arbetar med tangentbord och skärmläsare.
- Systemet ska hantera tillfälliga avbrott i externa register utan att felaktiga ärendedata sparas.
- Det ska vara möjligt att förstå varför ett ärende inte visas i en sökträff utan att avslöja skyddad information.

Problemet är att sådana krav ofta skrivs för abstrakt.

Exempel:

> Systemet ska ha hög prestanda.

> Systemet ska vara säkert.

> Systemet ska vara användarvänligt.

> Systemet ska ha god spårbarhet.

Dessa formuleringar uttrycker en ambition, men de räcker inte som krav. De är svåra att granska, svåra att testa och svåra att använda vid prioritering. De leder lätt till sena diskussioner där olika roller trodde att de var överens, men menade olika saker.

SBE kan hjälpa genom att ställa följande frågor:

- I vilken konkret situation märks detta kvalitetskrav?
- Vilken användare eller intressent påverkas?
- Vad är ett acceptabelt utfall?
- Vad är ett oacceptabelt utfall?
- Vilka gränsfall behöver vi pröva?
- Vilka mätvärden behövs för att kravet ska kunna verifieras?
- Vilka risker är kravet tänkt att minska?

## Varför kvalitetskrav ofta blir svåra

Kvalitetskrav är svåra av flera skäl.

För det första är de ofta tvärgående. Ett krav på spårbarhet gäller kanske sökning, ärendevisning, statusändring, export, åtkomst till känsliga uppgifter och integrationer. Det hör inte hemma i bara ett scenario.

För det andra ägs de ofta av flera roller. Verksamheten kan beskriva behovet. Säkerhetsfunktionen kan beskriva risker. Arkitekten kan beskriva tekniska lösningsprinciper. Test kan beskriva verifieringsstrategi. Drift kan beskriva övervakning. Juridik kan beskriva regelverkets krav.

För det tredje är de ofta svåra att uttrycka utan lösningsantaganden. Ett krav på säkerhet kan snabbt bli en teknisk lösning innan verksamhetsbehovet är tydligt. Ett krav på prestanda kan bli ett svarstidsmått utan analys av vilka arbetsflöden som faktiskt kräver snabbhet.

För det fjärde kan kvalitetskrav vara kostnadsdrivande. Skillnaden mellan “sökning ska svara snabbt” och “95 procent av sökningar ska svara inom två sekunder vid 500 samtidiga användare och 10 miljoner ärenden” kan vara mycket stor.

Det gör att kvalitetskrav behöver konkretiseras med omsorg.

SBE kan bidra, men på ett annat sätt än för funktionella krav. För funktionella krav kan exempel ibland vara själva specifikationen. För kvalitetskrav är exempel ofta ett sätt att förstå och avgränsa kravet, medan verifieringen behöver kompletteras med mätbara kriterier och särskilda test- eller granskningsmetoder.

## Tre nivåer för kvalitetskrav i SBE

Ett praktiskt sätt att dokumentera kvalitetskrav är att använda tre nivåer:

1. verksamhetsexempel
2. mätbart kriterium
3. kompletterande riktlinje eller beslut

### Verksamhetsexempel

Verksamhetsexemplet beskriver en konkret situation där kvalitetskravet spelar roll.

Exempel:

> En utredare söker efter ett ärende under ett pågående förhör och behöver snabbt avgöra om det finns tidigare kopplingar till samma person.

Detta exempel förklarar varför svarstid är viktigt. Det gör kravet begripligt för verksamheten och hjälper IT att förstå användningssituationen.

### Mätbart kriterium

Det mätbara kriteriet gör kravet verifierbart.

Exempel:

> För standardsökningar på personnummer eller ärendenummer ska 95 procent av svaren visas inom två sekunder vid normal kontorsbelastning.

Detta är fortfarande inte en fullständig prestandaspecifikation, men det är betydligt mer användbart än “systemet ska vara snabbt”.

### Kompletterande riktlinje eller beslut

Den kompletterande dokumentationen beskriver hur kravet ska hanteras i design, test, drift eller förvaltning.

Exempel:

> Prestandatest ska genomföras med testdata som representerar minst fem års ärendevolym. Mätning ska göras för standardsökning, bred fritextsökning och sökning med behörighetsfiltrering.

Här börjar kravet bli användbart för planering, verifiering och förvaltning.

I SBE-dokumentationen kan dessa tre nivåer ligga tillsammans:

| Del | Innehåll | Syfte |
|---|---|---|
| Verksamhetsexempel | Utredaren söker under pågående förhör | Förklarar varför kravet finns |
| Mätbart kriterium | 95 procent inom två sekunder för standardsökning | Gör kravet verifierbart |
| Kompletterande beslut | Prestandatest med representativ ärendevolym | Gör kravet genomförbart och testbart |

Den här strukturen gör att dokumentationen fungerar för både verksamheten och IT. Verksamheten kan bedöma om exemplet är relevant. IT kan bedöma om kriteriet är tydligt och realistiskt. Test kan bedöma hur verifieringen ska göras.

## När exempel passar bra för kvalitetskrav

Alla kvalitetskrav behöver inte beskrivas med exempel. Men exempel passar särskilt bra när kravet behöver förankras i en konkret användningssituation.

Exempel är ofta användbara för:

- svarstid i kritiska arbetsflöden
- säkerhetsbeteende vid åtkomst till skyddade uppgifter
- loggning av känsliga händelser
- användbarhet i vanliga eller stressade arbetssituationer
- tillgänglighet i konkreta interaktioner
- felhantering vid externa beroenden
- begriplighet i systemmeddelanden
- informationsskydd vid sökning, export och visning

Exempel passar sämre som enda dokumentationsform för:

- övergripande tillgänglighetsstandarder
- tekniska krypteringskrav
- driftsättningskrav
- kapacitetsdimensionering
- detaljerad övervakning
- arkitekturprinciper
- regulatoriska krav som måste följas oavsett scenario

Det betyder inte att SBE är irrelevant för dessa områden. Det betyder att exemplen behöver kompletteras.

Ett säkerhetskrav kan till exempel behöva:

- verksamhetsexempel som visar vad som ska skyddas
- hot- eller riskanalys som visar varför skyddet behövs
- säkerhetskrav som beskriver principen
- arkitekturbeslut som beskriver lösningsinriktningen
- tester eller granskningar som verifierar efterlevnad

## Prestanda som SBE-understött kvalitetskrav

Prestanda är ett område där traditionella krav ofta blir antingen för vaga eller för tekniska.

Ett vagt krav:

> Systemet ska ha god prestanda.

Ett för tekniskt krav utan verksamhetsförankring:

> Samtliga API-anrop ska svara under 200 millisekunder.

Det första är inte verifierbart. Det andra kan vara dyrt, onödigt eller felriktat om det inte är kopplat till verkliga arbetsflöden.

I brottsutredningsstödet bör prestandakrav börja i användningssituationen.

Exempel:

> En utredare söker på ett ärendenummer under ett möte och behöver omedelbart se om ärendet finns och vilken status det har.

Ett möjligt mätbart kriterium:

> Sökning på exakt ärendenummer ska i 99 procent av fallen visa grunduppgifter inom en sekund vid normal belastning.

Ett annat exempel:

> En analytiker gör en bred sökning på flera kännetecken för att hitta möjliga kopplingar mellan ärenden.

Mätbart kriterium:

> Bred sökning med flera kriterier ska i 95 procent av fallen visa första resultatsidan inom fem sekunder vid normal belastning.

Här visar exemplen att alla sökningar inte har samma prestandakrav. Exakt ärendenummersökning och bred analytisk sökning har olika syfte, användningsmönster och rimlig väntetid.

Det är ofta bättre att dela upp prestandakrav efter användningsfall än att formulera ett enda globalt svarstidskrav.

En enkel dokumentationsstruktur kan vara:

| Funktion eller situation | Verksamhetsexempel | Mätbart kriterium | Kommentar |
|---|---|---|---|
| Exakt ärendenummersökning | Utredare söker under möte | 99 procent inom 1 sekund | Hög prioritet |
| Personbaserad standardsökning | Utredare kontrollerar tidigare ärenden | 95 procent inom 2 sekunder | Behörighetsfiltrering ingår |
| Bred analytisk sökning | Analytiker letar mönster | 95 procent inom 5 sekunder | Första resultatsidan räcker |
| Export av större urval | Behörig användare exporterar ärenden | Startbekräftelse inom 3 sekunder | Själva exporten får vara asynkron |

Notera att tabellen inte bara anger tider. Den förklarar varför olika krav gäller. Det gör den granskningsbar.

## Säkerhet och åtkomstkontroll

Säkerhetskrav är särskilt viktiga i ett brottsutredningsstöd. Systemet kan innehålla känsliga personuppgifter, uppgifter om pågående utredningar, sekretessmarkeringar, interna bedömningar och information som inte får spridas.

Samtidigt är säkerhet ett område där SBE lätt används fel.

Ett vanligt misstag är att skriva scenarier som låter verksamhetsnära men egentligen bara säger:

```gherkin
Givet att användaren är obehörig
När användaren försöker öppna ett ärende
Så ska åtkomst nekas
```

Det scenariot är inte fel, men det är ofta för tunt. Det säger inte vad obehörig betyder, vilken information som skyddas, hur användaren kom dit, vad systemet ska visa, vad som ska loggas eller om användaren ska få veta att ärendet finns.

Ett bättre SBE-arbete börjar med verksamhetsregler och exempel.

Regel:

> En användare får bara se ärenden inom sin behörighetsdomän, om inte ett särskilt åtkomstbeslut ger utökad behörighet.

Exempel:

| Exempel-ID | Situation | Användarens relation | Ärendets behörighetsdomän | Förväntat resultat |
|---|---|---|---|---|
| SEC-01 | Utredare söker på exakt ärendenummer | Tillhör samma domän | Samma domän | Ärendet visas |
| SEC-02 | Utredare söker på exakt ärendenummer | Tillhör annan domän | Annan domän | Ärendet visas inte som träff |
| SEC-03 | Utredare öppnar direktlänk | Tillhör annan domän | Annan domän | Åtkomst nekas utan känsliga detaljer |
| SEC-04 | Utredare har särskilt åtkomstbeslut | Beslut finns | Annan domän | Ärendet visas med beslutets omfattning |
| SEC-05 | Åtkomstbeslut har löpt ut | Tidigare beslut finns | Annan domän | Åtkomst nekas |

Därefter kan kompletterande säkerhetskrav beskriva:

- vad som ska loggas
- hur nekad åtkomst ska presenteras
- om existensen av ett ärende får avslöjas
- hur särskilda åtkomstbeslut beviljas och återkallas
- vilka kontroller som ska göras i gränssnitt, API och integrationer
- vilka säkerhetsgranskningar som krävs före produktionssättning

Här är SBE-exemplen inte hela säkerhetsspecifikationen. De är den del som gör säkerhetsregeln konkret och granskningsbar.

## Loggning och spårbarhet

Loggning är ett område som ofta hamnar mellan funktionella krav, generella krav och kvalitetskrav.

I kapitel 13 behandlades loggning som ett generellt kravområde. I detta kapitel betraktar vi loggning som kvalitetskrav, eftersom loggning ofta handlar om revisionsbarhet, ansvarighet och möjlighet till efterhandskontroll.

Ett vagt krav kan vara:

> Systemet ska logga viktiga händelser.

Frågan är då vad som räknas som viktigt.

I brottsutredningsstödet kan följande händelser behöva loggas:

- användare öppnar känsligt ärende
- användare söker på personnummer
- användare exporterar ärendedata
- användare ändrar ärendestatus
- användare lägger till eller tar bort känslig markering
- användare får nekad åtkomst
- integration hämtar uppgifter från externt register
- systemadministratör ändrar behörighet

Men även detta är bara början. För varje loggad händelse behöver dokumentationen förklara vad som ska loggas, varför och hur loggen ska användas.

Exempel:

| Händelse | Verksamhetsexempel | Logginnehåll | Kvalitetskriterium |
|---|---|---|---|
| Öppna känsligt ärende | Utredare läser ärende med skyddade uppgifter | användare, tidpunkt, ärende-ID, åtkomstgrund | Loggen ska kunna användas vid efterhandskontroll |
| Nekad åtkomst | Användare försöker öppna ärende utanför behörighetsdomän | användare, tidpunkt, försökstyp, nekad regel | Loggen ska inte innehålla mer känslig information än nödvändigt |
| Export | Behörig användare exporterar ärendedata | användare, tidpunkt, urval, syfte eller ärendereferens | Det ska gå att följa vilken information som lämnats ut |

Här blir kvalitetskravet tydligare än “god spårbarhet”. Det visar vad spårbarhet betyder i systemets kontext.

En viktig nyans är att loggning också kan skapa risk. För detaljerade loggar kan innehålla känslig information. För svaga loggar kan göra efterhandskontroll omöjlig. Därför bör loggningskrav ofta granskas av både verksamhet, säkerhet, juridik, arkitektur, test och drift.

SBE kan bidra med exempel på vad som ska hända. Men kravanalytikern behöver också dokumentera principer för dataminimering, åtkomst till loggar, gallring och revisionsprocesser.

## Användbarhet

Användbarhetskrav blir ofta svaga eftersom de skrivs som allmänna önskemål.

Exempel:

> Systemet ska vara enkelt att använda.

> Systemet ska ha ett intuitivt gränssnitt.

För en erfaren kravanalytiker bör sådana formuleringar vara varningssignaler. De uttrycker en önskad kvalitet, men inte vad kvaliteten betyder.

SBE kan hjälpa genom att koppla användbarhet till konkreta uppgifter.

Exempel:

> En erfaren utredare ska kunna skapa ett preliminärt ärende med grunduppgifter utan att lämna arbetsflödet.

Ett mätbart kriterium kan vara:

> Vid användningstest ska minst 8 av 10 representativa användare kunna skapa ett preliminärt ärende med obligatoriska uppgifter utan handledning.

Ett annat exempel:

> En utredare som får nekad åtkomst till ett ärende ska förstå vad som behöver göras härnäst utan att systemet avslöjar skyddade detaljer.

Möjligt kriterium:

> Meddelandet vid nekad åtkomst ska ange att åtkomst saknas, hänvisa till fastställd rutin för åtkomstbegäran och inte visa ärendets skyddade innehåll.

Här samspelar användbarhet och säkerhet. Ett alltför generiskt felmeddelande kan skapa onödiga supportärenden. Ett alltför detaljerat felmeddelande kan läcka information. Exemplet hjälper gruppen att diskutera avvägningen.

Användbarhetskrav lämpar sig ofta för en kombination av:

- användningsscenarier
- prototyper
- exempel på meddelandetexter
- observationer från användningstest
- acceptanskriterier för centrala uppgifter
- riktlinjer för språk, navigation och felhantering

SBE-dokumentationen behöver inte ersätta UX-arbete. Den kan i stället skapa en brygga mellan krav, UX, verksamhet och test.

## Tillgänglighet

Tillgänglighet handlar om att systemet ska kunna användas av personer med olika förutsättningar. Det kan omfatta tangentbordsnavigering, skärmläsare, kontraster, fokusordning, felmeddelanden, formulärstöd och begripligt språk.

Tillgänglighetskrav behöver ofta förhålla sig till standarder och regelverk. Därför bör de inte reduceras till några få exempel. Samtidigt kan exempel göra kraven mycket lättare att förstå.

Exempel:

> En handläggare som använder tangentbord ska kunna registrera grunduppgifter i ett preliminärt ärende utan att fastna i ett fält eller behöva använda mus.

Mätbart kriterium:

> Samtliga obligatoriska fält i flödet för preliminärt ärende ska kunna nås, fyllas i och sparas med tangentbord i logisk fokusordning.

Exempel:

> En användare med skärmläsare ska förstå varför ett ärende inte kan sparas när obligatoriska uppgifter saknas.

Mätbart kriterium:

> Felmeddelanden ska vara kopplade till rätt fält och kunna läsas upp av skärmläsare med både felorsak och föreslagen åtgärd.

Här gör exemplen standardkraven konkreta. De visar vad tillgänglighet betyder i systemets arbetsflöden. Men de ersätter inte en fullständig tillgänglighetsgranskning.

Dokumentationen bör därför innehålla:

- tillgänglighetsprinciper eller standarder som ska följas
- prioriterade arbetsflöden där tillgänglighet ska granskas särskilt
- konkreta exempel på interaktioner
- verifieringsmetod, till exempel manuell granskning, automatiska kontroller och användningstest

## Robusthet och felhantering

Robusthet handlar om hur systemet beter sig när något inte fungerar som planerat.

I ett brottsutredningsstöd kan systemet vara beroende av externa register, identitetslösningar, behörighetstjänster, dokumenthantering och meddelandetjänster. Dessa beroenden kan svara långsamt, vara otillgängliga eller returnera ofullständig information.

Ett vagt krav kan vara:

> Systemet ska hantera fel på ett robust sätt.

Ett bättre SBE-understött krav börjar med situationer.

Exempel:

> En utredare försöker öppna ett ärende när extern behörighetstjänst inte svarar.

Möjligt förväntat beteende:

> Systemet ska inte visa ärendet om behörighet inte kan verifieras. Användaren ska få ett meddelande som förklarar att åtkomstkontroll för tillfället inte kan genomföras. Händelsen ska loggas som tekniskt åtkomsthinder.

Ett annat exempel:

> En utredare sparar en statusändring när dokumenttjänsten inte kan ta emot uppdaterad dokumentreferens.

Möjligt förväntat beteende:

> Systemet ska inte markera statusändringen som helt genomförd om nödvändig dokumentreferens saknas. Användaren ska få besked om vad som sparats, vad som inte sparats och hur ärendet kan följas upp.

Här är det viktigt att inte bara beskriva tekniska fel. Verksamheten behöver förstå konsekvensen. IT behöver förstå transaktioner, felhantering och integration. Test behöver förstå hur felen kan simuleras. Drift behöver förstå vad som ska övervakas.

Robusthetskrav bör därför dokumenteras med:

- kritiska beroenden
- verksamhetsscenarier vid fel
- förväntat systembeteende
- data- och transaktionsprinciper
- loggning och larm
- återstart eller återförsök
- manuell hantering när systemet inte kan slutföra processen

## Datakvalitet

Datakvalitet är särskilt viktig i myndighetssystem där beslut, utredningar och rättsliga processer kan påverkas av informationens riktighet, fullständighet och aktualitet.

Ett vagt krav kan vara:

> Systemet ska ha god datakvalitet.

I SBE behöver vi fråga vad det betyder i konkreta situationer.

Exempel:

> En utredare registrerar en personkoppling till ett ärende och anger personnummer, roll och kopplingens källa.

Regler kan vara:

- Personnummer ska valideras mot fastställt format.
- Kopplingens källa ska anges när kopplingen inte kommer från ett integrerat register.
- Systemet ska skilja mellan bekräftad koppling, misstänkt koppling och administrativ koppling.
- En koppling får inte visas som bekräftad om den saknar källa.

Exempeltabell:

| Situation | Personnummer | Källa | Kopplingstyp | Förväntat resultat |
|---|---|---|---|---|
| Bekräftad koppling med källa | Giltigt | Angiven | Bekräftad | Kopplingen kan sparas |
| Bekräftad koppling utan källa | Giltigt | Saknas | Bekräftad | Systemet stoppar sparande |
| Misstänkt koppling utan källa | Giltigt | Saknas | Misstänkt | Systemet kräver kommentar |
| Ogiltigt personnummer | Ogiltigt | Angiven | Bekräftad | Systemet stoppar sparande |

Här är datakvalitet både ett funktionellt och ett kvalitativt område. Reglerna beskriver beteende, men syftet är att säkerställa kvaliteten på informationen.

Detta visar en viktig princip: vissa kvalitetskrav kan konkretiseras så långt att de nästan blir funktionella regler. Det är inte ett problem. Det viktiga är att dokumentationen visar både beteendet och kvalitetsmålet.

## Informationsskydd vid sökning och visning

I brottsutredningsstödet är sökning ett område där flera kvalitetskrav möts:

- prestanda
- åtkomstkontroll
- informationsskydd
- användbarhet
- spårbarhet
- datakvalitet

Anta att en utredare söker på ett personnummer. Systemet kan hitta ärenden som användaren får se, ärenden som användaren inte får se och ärenden där endast begränsad information får visas.

En traditionell kravtext kanske säger:

> Systemet ska filtrera sökresultat utifrån användarens behörighet.

Det är ett viktigt krav, men det räcker inte.

SBE-dokumentationen bör visa exempel:

| Exempel-ID | Sökning | Ärende hittas | Användarens behörighet | Förväntad visning |
|---|---|---|---|---|
| SOK-SEC-01 | Personnummer | Ett ärende i samma domän | Behörig | Ärendet visas med tillåtna grunduppgifter |
| SOK-SEC-02 | Personnummer | Ett ärende i annan domän | Obehörig | Ärendet visas inte |
| SOK-SEC-03 | Personnummer | Sekretessmarkerat ärende | Delvis behörig | Begränsad träff visas enligt regel |
| SOK-SEC-04 | Personnummer | Endast obehöriga ärenden | Obehörig | Ingen träff visas eller neutralt meddelande enligt beslutad policy |
| SOK-SEC-05 | Personnummer | Flera ärenden med blandad åtkomst | Blandad | Endast tillåtna träffar visas |

Därefter behöver kvalitetskrav komplettera:

- svarstid för sökning med behörighetsfiltrering
- loggning av sökning på känsliga sökbegrepp
- policy för om obehöriga träffars existens får avslöjas
- meddelandetexter för tomma resultat
- testdata som täcker blandade åtkomstfall
- granskning av informationsläckage via antal träffar, sortering eller felmeddelanden

Detta är ett bra exempel på varför kvalitetskrav inte bör ligga isolerade i ett separat dokument som ingen läser. De behöver kopplas till de funktionella flöden där de får betydelse.

## Dokumentationsmönster för kvalitetskrav

Ett praktiskt dokumentationsmönster för kvalitetskrav kan se ut så här:

| Del | Fråga | Exempel |
|---|---|---|
| Namn | Vad kallar vi kvalitetskravet? | Svarstid för standardsökning |
| Syfte | Varför finns kravet? | Utredaren behöver kunna agera i möten och förhör |
| Berörda flöden | Var märks kravet? | Sökning, ärendeöversikt, behörighetsfiltrering |
| Verksamhetsexempel | Vilka konkreta situationer visar behovet? | Utredare söker ärende under pågående möte |
| Mätbart kriterium | Hur vet vi att kravet är uppfyllt? | 95 procent inom två sekunder |
| Verifiering | Hur ska det kontrolleras? | Prestandatest med representativ datamängd |
| Ägarskap | Vem kan besluta om kravet? | Produktägare med arkitekt och drift |
| Kommentar | Vad behöver förtydligas? | Gäller standardsökning, inte analytisk bredsökning |

Det här mönstret är ofta mer användbart än att försöka skriva alla kvalitetskrav som Given-When-Then.

Given-When-Then kan passa för vissa observerbara beteenden:

```gherkin
Scenario: Nekad åtkomst när behörighetstjänsten inte kan verifiera användaren
  Givet att behörighetstjänsten inte svarar
  Och utredaren försöker öppna ett sekretessmarkerat ärende
  När systemet inte kan verifiera åtkomst
  Så ska ärendet inte visas
  Och användaren ska informeras om att åtkomstkontroll tillfälligt inte kan genomföras
  Och händelsen ska loggas som tekniskt åtkomsthinder
```

Men för prestanda, tillgänglighetsstandarder, övervakning eller arkitekturprinciper är en tabell, riktlinje eller mätbar kravpost ofta bättre.

SBE handlar inte om att alltid använda samma format. Det handlar om att använda exempel för att skapa gemensam förståelse och testbarhet.

## Hur kvalitetskrav kopplas till funktionella specifikationer

Kvalitetskrav bör inte bara finnas i ett separat avsnitt längst bak. De behöver kopplas till de funktionella områden där de påverkar beteende, design och verifiering.

Ett sätt är att använda referenser.

I specifikationen för sökning kan det stå:

- Funktionellt regelområde: Sökning och behörighetsfiltrering
- Relaterade kvalitetskrav:
  - KVAL-PREST-01: Svarstid för standardsökning
  - KVAL-SEC-02: Informationsskydd vid obehöriga träffar
  - KVAL-LOG-01: Loggning av sökning på känsliga sökbegrepp
  - KVAL-UX-03: Begripligt meddelande vid inga tillåtna träffar

I kvalitetskravsavsnittet beskrivs sedan varje kvalitetskrav mer generellt.

Detta ger två fördelar.

För det första kan verksamheten läsa den funktionella specifikationen och se vilka kvalitetsaspekter som hör till området.

För det andra kan IT och test hitta samlade kvalitetskriterier utan att behöva leta i varje scenario.

Målet är inte maximal spårbarhetsadministration. Målet är praktisk spårbarhet: tillräcklig koppling för att krav, test, implementation och förvaltning inte ska glida isär.

## Kvalitetskrav och automation

Vissa kvalitetskrav kan automatiseras. Andra kan delvis automatiseras. Några behöver manuell granskning eller särskild testmiljö.

Exempel på krav som ofta kan automatiseras helt eller delvis:

- vissa åtkomstregler
- vissa loggningsregler
- fältvalideringar
- API-beteenden vid fel
- vissa tillgänglighetskontroller
- vissa prestandamätningar i pipeline eller testmiljö

Exempel på krav som ofta kräver manuell eller särskild verifiering:

- faktisk användbarhet i komplexa arbetsflöden
- tillgänglighet med riktiga hjälpmedel och användare
- säkerhetsgranskning och penetrationstest
- prestanda under realistisk produktionsliknande belastning
- organisatorisk efterlevnad av logggranskning
- juridisk bedömning av informationsvisning

I SBE-dokumentationen bör automatiseringsstatus vara ärlig.

Det är bättre att skriva:

> Detta exempel används för gemensam förståelse och manuell granskning. Det är inte automatiserat.

än att skapa en falsk känsla av täckning.

För kvalitetskrav kan automationsstatus exempelvis vara:

| Status | Betydelse |
|---|---|
| Ej automatiserat | Kravet granskas manuellt eller genom separat process |
| Delvis automatiserat | Vissa kontroller är automatiserade men full verifiering kräver annat |
| Automatiserat i testmiljö | Kravet kontrolleras automatiskt i en särskild miljö |
| Övervakas i drift | Kravet följs upp genom loggar, mätvärden eller larm |
| Kräver periodisk granskning | Kravet verifieras återkommande genom revision eller kontroll |

Detta hjälper organisationen att förstå vad SBE-specifikationen faktiskt garanterar och vad som fortfarande kräver annan uppföljning.

## Vanliga misstag

- **Misstag: Att behandla alla kvalitetskrav som om de vore funktionella scenarier.**
  - Varför det händer: Teamet har börjat använda Gherkin eller exempelmallar och vill få in allt i samma format.
  - Hur man undviker det: Använd exempel när de skapar förståelse, men komplettera med mätbara kriterier, riktlinjer och beslut där det behövs.

- **Misstag: Att skriva kvalitetskrav som vaga ambitioner.**
  - Varför det händer: Ord som snabbt, säkert, användarvänligt och robust känns självklara.
  - Hur man undviker det: Fråga alltid i vilken situation kravet märks och hur man vet att det är uppfyllt.

- **Misstag: Att låta IT ensamt formulera kvalitetskrav.**
  - Varför det händer: Kvalitetskrav uppfattas som tekniska.
  - Hur man undviker det: Börja med verksamhetsexempel och risker, och låt sedan IT, test, arkitektur, säkerhet och drift komplettera med kriterier och verifiering.

- **Misstag: Att isolera kvalitetskraven från de funktionella specifikationerna.**
  - Varför det händer: Kravdokumentation delas ofta upp i funktionella och icke-funktionella avsnitt.
  - Hur man undviker det: Behåll samlade kvalitetskrav, men länka dem till berörda regelområden, scenarier och flöden.

- **Misstag: Att automatisera kvalitetskrav utan att förstå vad som behöver verifieras.**
  - Varför det händer: Automation uppfattas som en kvalitetsgaranti i sig.
  - Hur man undviker det: Dokumentera först syfte, exempel, kriterium och verifieringsmetod. Automatisera bara det som är stabilt, observerbart och värdefullt.

- **Misstag: Att formulera mätvärden utan kontext.**
  - Varför det händer: Mätbara krav känns professionella.
  - Hur man undviker det: Koppla mätvärdet till arbetsflöde, belastning, datamängd, användarroll och prioritet.

## Övningar

### Övning 1: Gör ett vagt kvalitetskrav konkret

Utgå från kravet:

> Systemet ska vara snabbt vid sökning.

Gör om kravet till en SBE-understödd dokumentation med:

- ett verksamhetsexempel
- ett eller flera mätbara kriterier
- berörda flöden
- verifieringsmetod
- eventuella öppna frågor

Använd brottsutredningsstödet som kontext.

### Övning 2: Skilj mellan exempel och kriterium

Välj ett av följande områden:

- säkerhet
- loggning
- användbarhet
- robusthet
- tillgänglighet

Formulera först ett konkret exempel. Formulera sedan ett mätbart eller granskningsbart kriterium. Beskriv vad exemplet bidrar med och vad kriteriet bidrar med.

### Övning 3: Koppla kvalitetskrav till ett funktionellt område

Utgå från funktionellt område “sökning efter ärende”. Identifiera minst fyra relevanta kvalitetskrav och koppla dem till området.

För varje krav, ange:

- kvalitetsområde
- varför kravet behövs
- ett exempel
- hur kravet kan verifieras
- om kravet kan automatiseras helt, delvis eller inte alls

### Fördjupning

Gör en enkel granskningsworkshop för ett kvalitetskrav. Låt en person representera verksamhet, en IT, en test, en säkerhet och en drift eller förvaltning. Granska om kravet är begripligt, mätbart, realistiskt och kopplat till rätt funktionella flöden.

## Snabb sammanfattning

- Kvalitetskrav beskriver egenskaper som prestanda, säkerhet, spårbarhet, användbarhet, tillgänglighet och robusthet.
- SBE kan hjälpa kvalitetskrav genom att göra dem konkreta med verksamhetsexempel.
- Exempel räcker ofta inte ensamma för kvalitetskrav; de behöver kompletteras med mätbara kriterier och verifieringsmetod.
- Alla kvalitetskrav bör inte tvingas in i Gherkin eller automatiserade scenarier.
- Dokumentation av kvalitetskrav bör fungera både för verksamheten och IT.
- Kvalitetskrav behöver kopplas till de funktionella flöden där de får praktisk betydelse.
- Automationsstatus för kvalitetskrav bör vara tydlig och ärlig.

## Quiz och reflektionsfrågor

1. Varför räcker det sällan att skriva “systemet ska vara snabbt”?
2. Vad är skillnaden mellan ett verksamhetsexempel och ett mätbart kriterium?
3. När passar Gherkin för kvalitetskrav, och när passar andra dokumentationsformer bättre?
4. Hur kan ett säkerhetskrav konkretiseras utan att avslöja känslig information?
5. Varför bör kvalitetskrav kopplas till funktionella regelområden?
6. Vilka kvalitetskrav är särskilt viktiga i ett brottsutredningsstöd?
7. Hur kan automation skapa falsk trygghet vid kvalitetskrav?

## Koppling till bokens röda tråd

Kvalitetskrav hanteras bäst när de får rätt dokumentationsform. Vissa kan konkretiseras med exempel, andra behöver mätbara kriterier, arkitekturbeslut eller särskilda verifieringsstrategier. Kapitlet förtydligar därför gränsen mellan SBE som konkretiseringsstöd och andra former av krav- och arkitekturdokumentation.


## Nästa steg

Det här kapitlet har visat hur SBE kan användas för att konkretisera kvalitetskrav utan att förenkla bort deras särskilda karaktär. Nästa kapitel tar ett bredare organisatoriskt perspektiv: hur SBE kan införas i en etablerad organisation där det redan finns roller, mallar, verktyg, styrning och invanda sätt att skriva krav.
