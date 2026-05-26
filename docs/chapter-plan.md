# Kapitelplan

## Rekommenderad inriktning

- Titel: Kravarbete med SBE
- Undertitel: En praktisk handbok för kravanalytiker som vill gå från traditionella krav till levande specifikation
- Språk: Svenska
- Författare: Erland Lindmark
- Målgrupp: Erfarna kravanalytiker
- Förkunskaper: Praktisk erfarenhet av kravarbete, acceptanskriterier och textuell kravdokumentation
- Svårighetsgrad: Erfaren
- Boktyp: Praktisk lärobok/handbok
- Pedagogisk stil: Praktisk, förklarande och scenario-baserad
- Omfattning: Medelstor

## Antaganden och avgränsningar

- Boken fokuserar huvudsakligen på funktionella krav.
- Generella krav och icke-funktionella krav behandlas i egna kapitel eftersom de ofta behöver hanteras annorlunda.
- Boken använder ett genomgående case: ett brottsutredningsstöd inom en myndighet.
- Boken behandlar Gherkin, Cucumber och Concordion på en krav- och dokumentationsnära nivå.
- Boken ska fungera både som lärande text och praktiskt stöd i förändrat arbetssätt.

## Del 1: Varför SBE förändrar kravarbete

### Kapitel 0: Inledning

- Syfte: Förklara bokens mål, målgrupp, upplägg och case.
- Praktiskt exempel/scenario: Introduktion till brottsutredningsstödet.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Läsarens tidigare erfarenhet av kravarbete.

### Kapitel 1: Varför traditionellt kravarbete inte alltid räcker

- Syfte: Visa typiska problem med traditionella krav, acceptanskriterier och textuell dokumentation.
- Nya huvudbegrepp: Tolkningsutrymme, dubbeldokumentation, gemensam förståelse.
- Praktiskt exempel/scenario: Ett otydligt krav kring sökning i brottsutredningsstödet.
- Övning: Identifiera tolkningsrisker i ett traditionellt krav.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Läsarens befintliga kravpraktik.

### Kapitel 2: Vad SBE är — och inte är

- Syfte: Introducera Specification by Example och relationen till BDD, ATDD och acceptanskriterier.
- Nya huvudbegrepp: SBE, levande dokumentation, exempel, regel, scenario.
- Praktiskt exempel/scenario: Från abstrakt regel till konkret exempel.
- Övning: Skilj mellan kravtext, regel och exempel.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 1.

### Kapitel 3: Kravanalytikerns förändrade roll

- Syfte: Visa hur kravanalytikern går från kravskrivare till facilitator av gemensam förståelse.
- Nya huvudbegrepp: Facilitering, trepartssamtal, gemensamt språk.
- Praktiskt exempel/scenario: Workshop med utredare, utvecklare och testare.
- Övning: Planera frågor inför en exempelworkshop.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 2.

## Del 2: Det genomgående caset

### Kapitel 4: Caset — ett brottsutredningsstöd i myndighetsmiljö

- Syfte: Presentera kontext, aktörer, mål, informationsobjekt och centrala begränsningar.
- Nya huvudbegrepp: Utredningsärende, aktör, arbetsflöde, spårbarhet.
- Praktiskt exempel/scenario: Registrering, sökning och hantering av utredningsinformation.
- Övning: Identifiera aktörer och informationsbehov.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 1–3.

### Kapitel 5: Att hitta funktionella krav som lämpar sig för SBE

- Syfte: Visa vilka krav som tjänar mest på att beskrivas med exempel.
- Nya huvudbegrepp: Beslutsregel, tillståndsövergång, gränsfall.
- Praktiskt exempel/scenario: Regler för att visa, dölja eller filtrera utredningsinformation.
- Övning: Välj ut kravkandidater för SBE.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 4.

### Kapitel 6: Från traditionella krav till exempelbaserad specifikation

- Syfte: Omvandla textuella krav och acceptanskriterier till regler, exempel och scenarier.
- Nya huvudbegrepp: Exempelbaserad specifikation, kompletterande förklaring.
- Praktiskt exempel/scenario: Omformulering av krav för sökning och behörighet.
- Övning: Gör om ett traditionellt krav till en exempelbaserad specifikation.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 5.

### Kapitel 7: Regler, exempel och scenarier i praktiken

- Syfte: Fördjupa hur bra exempel formuleras och hur triviala eller överdrivet tekniska exempel undviks.
- Nya huvudbegrepp: Representativt exempel, gränsexempel, scenarioomfång.
- Praktiskt exempel/scenario: Undantag och gränsfall vid ärendesökning.
- Övning: Komplettera en specifikation med saknade gränsfall.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 6.

### Kapitel 8: Dokumentation som fungerar för både verksamhet och IT

- Syfte: Visa hur SBE-dokumentation struktureras så att den är läsbar för verksamheten och användbar för IT.
- Nya huvudbegrepp: Dokumentationslager, läsbarhet, spårbarhet, levande specifikation.
- Praktiskt exempel/scenario: Dokumentationsstruktur för sökfunktion, behörighetsregel och ärendeflöde.
- Övning: Strukturera en specifikation för två målgrupper.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 6–7.

## Del 3: Samarbete, test och verktygsnära format

### Kapitel 9: Exempelworkshops och gemensam förfining

- Syfte: Beskriva hur exempel tas fram tillsammans i workshops och förfiningsmöten.
- Nya huvudbegrepp: Example mapping, öppna frågor, beslutslogg.
- Praktiskt exempel/scenario: Workshop kring när en utredare får se en uppgift.
- Övning: Planera en exempelworkshop.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 8.

### Kapitel 10: Gherkin, Cucumber och Concordion

- Syfte: Förklara Gherkin-formatet och när Cucumber respektive Concordion kan passa.
- Nya huvudbegrepp: Gherkin, Given-When-Then, körbar specifikation, testautomation.
- Praktiskt exempel/scenario: Samma regel uttryckt som Gherkin-scenario och dokumentnära Concordion-specifikation.
- Övning: Välj dokumentations- och automationsformat för olika kravtyper.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 7–9.

### Kapitel 11: Samspel mellan krav, test och utveckling

- Syfte: Visa hur krav, test och implementation kopplas ihop utan att specifikationen blir för teknisk.
- Nya huvudbegrepp: Testbarhet, automatiseringsstrategi, ansvarsfördelning.
- Praktiskt exempel/scenario: Från verksamhetsexempel till testfall och implementation.
- Övning: Bedöm vilka exempel som bör automatiseras.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 10.

### Kapitel 12: Kvalitetssäkring av SBE-specifikationer

- Syfte: Ge kriterier för att granska om en specifikation håller tillräcklig kvalitet.
- Nya huvudbegrepp: Täckning, precision, underhållbarhet, rätt detaljnivå.
- Praktiskt exempel/scenario: Granskning av en specifikation för informationssökning.
- Övning: Kvalitetsgranska en SBE-specifikation.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 11.

## Del 4: Svårare kravtyper och organisatorisk omställning

### Kapitel 13: Generella krav i ett SBE-arbetssätt

- Syfte: Behandla tvärgående regler och återkommande beteenden.
- Nya huvudbegrepp: Generell regel, återanvändbar specifikation, policyregel.
- Praktiskt exempel/scenario: Gemensamma behörighetsprinciper och standardbeteenden.
- Övning: Separera funktionsspecifik regel från generell regel.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 8 och 12.

### Kapitel 14: Icke-funktionella krav och kvalitetskrav

- Syfte: Visa hur prestanda, säkerhet, loggning, spårbarhet, användbarhet och robusthet hanteras.
- Nya huvudbegrepp: Kvalitetskrav, mätbart kriterium, arkitekturbeslut.
- Praktiskt exempel/scenario: Spårbarhet och loggning i brottsutredningsstödet.
- Övning: Omvandla ett vagt kvalitetskrav till mätbara kriterier och exempel.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 13.

### Kapitel 15: Att införa SBE i en etablerad organisation

- Syfte: Visa hur en organisation går från etablerade kravmallar till ett hållbart SBE-arbetssätt.
- Nya huvudbegrepp: Pilot, governance, förändringsmotstånd, arbetssätt.
- Praktiskt exempel/scenario: Införande i ett myndighetsprogram med flera team.
- Övning: Skapa en införandeplan.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 1–14.

### Kapitel 16: Mallar, checklistor och arbetsmönster

- Syfte: Samla praktiska mallar och beslutsstöd.
- Nya huvudbegrepp: Granskningschecklista, dokumentationsmall, verktygsbeslut.
- Praktiskt exempel/scenario: Slutlig verktygslåda för brottsutredningsstödet.
- Övning: Välj mall och arbetsmönster för ett nytt kravområde.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Hela boken.

## Progressionskontroll

- Begrepp introduceras i ordningen: traditionellt kravarbete, SBE, exempel, regler, scenarier, dokumentationsstruktur, workshops, Gherkin, verktyg, testautomation, generella krav, kvalitetskrav och införande.
- Boken förutsätter kravvana men introducerar SBE-begrepp stegvis.
- Varje kapitel ska använda brottsutredningsstödet för att hålla progressionen konkret.
- Boken avslutas med praktiska mallar och checklistor som binder ihop arbetssättet.
