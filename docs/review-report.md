# Helhetsgranskning

## Datum

2026-05-26

## Sammanfattning

Helhetsgranskningen har genomförts efter att samtliga planerade kapitel och omslaget lagts in i projektet. Boken bedöms vara komplett på manusnivå och redo för export till EPUB/PDF för läsgranskning.

## Granskat

- Kapitelordning i `book.yaml` och `docs/export-metadata.yaml`.
- Att `chapters/00-inledning.md` finns först i kapitelordningen.
- Att kapitel 1–16 finns och motsvarar beslutad kapitelplan.
- Att titel, undertitel, författare, språk, version och omslagsreferens finns i metadata.
- Att omslagsbilden finns som `assets/cover/cover.png`.
- Att bokens nivå och ton riktar sig till erfarna kravanalytiker.
- Att det genomgående caset med brottsutredningsstöd återkommer i boken.
- Att funktionella krav behandlas före generella krav och icke-funktionella krav.
- Att Gherkin, Cucumber och Concordion behandlas efter att regler, exempel, scenarier och dokumentationsstruktur har introducerats.
- Att exportscriptets markdownvalidering fungerar för bokens text och inte feltolkar markdown- eller Gherkin-exempel inuti kodblock.

## Resultat

| Område | Bedömning | Kommentar |
|---|---|---|
| Kapitelstruktur | Godkänd | Inledning och kapitel 1–16 finns i beslutad ordning. |
| Metadata | Godkänd | Titel, undertitel, författare, språk, identifierare, version och omslag finns. |
| Progression | Godkänd | Boken går från problem och begrepp till praktisk dokumentation, testkoppling och införande. |
| Målgruppsanpassning | Godkänd | Texten utgår från erfaren kravpraktik och undviker onödig nybörjarnivå. |
| Casekontinuitet | Godkänd | Brottsutredningsstödet används återkommande som sammanhållande exempel. |
| Dokumentationsperspektiv | Godkänd | Boken behandlar dokumentation för både verksamhet och IT. |
| Exportförberedelse | Godkänd för nästa steg | Markdownvalidering för sammanslagning fungerar. EPUB/PDF återstår att generera. |

## Utförda ändringar

- Uppdaterat projektversion till `0.2`.
- Uppdaterat projektstatus till helhetsgranskad.
- Uppdaterat kvalitetschecklista med granskningsutfall.
- Lagt till denna granskningsrapport.
- Justerat `scripts/export-book.py` så att valideringen ignorerar innehåll i kodblock när den kontrollerar rubriker, tabeller och bildreferenser.

## Rekommenderat nästa steg

Skapa EPUB och PDF för läsgranskning. Efter läsgranskning bör en språkredaktionell slutputs göras innan eventuell slutversion.

## Redaktionell åtgärdsrunda 2026-05-26

Efter helhetsgranskningen har en faktisk manusredigering genomförts i kapiteltexterna. Fokus har varit att förstärka bokens röda tråd och göra övergångarna tydligare utan att skriva om kapitlen från grunden.

### Utförda manusjusteringar

- Inledningen har kompletterats med en tydligare beskrivning av den sammanhängande förändringsresan.
- Kapitel 1–3 har förstärkts med tydligare koppling mellan traditionella kravproblem, SBE och kravanalytikerns förändrade roll.
- Kapitel 4–8 har förstärkts med tydligare koppling mellan case, funktionella krav, exempelbaserad specifikation och dokumentation för både verksamhet och IT.
- Kapitel 9–12 har förstärkts med tydligare koppling mellan workshoparbete, Gherkin/Cucumber/Concordion, test, utveckling och kvalitetsgranskning.
- Kapitel 13–16 har förstärkts med tydligare övergångar kring generella krav, kvalitetskrav, organisatoriskt införande och praktiska mallar.

### Bedömning efter åtgärd

Manuset är nu mer sammanhållet inför export för läsgranskning. Nästa steg är att skapa EPUB och PDF och göra en läsgranskning av de genererade formaten.
