# Kvalitetschecklista

## Språk och målgrupp

- All boktext är på svenska.
- Vedertagna engelska begrepp används bara där de tillför tydlighet.
- Texten utgår från att läsaren är erfaren kravanalytiker.
- Grundläggande kravarbete förklaras inte i onödan.
- Tonen är professionell, praktisk och pedagogisk.

## Pedagogik

- Varje kapitel har tydliga lärandemål.
- Varje kapitel använder brottsutredningsstödet när det passar.
- Nya SBE-begrepp introduceras i rätt ordning.
- Varje kapitel innehåller exempel, vanliga misstag och övningar eller reflektionsfrågor.
- Kapitlen hjälper läsaren att förändra arbetssätt, inte bara lära sig termer.

## Progression

- Begrepp används inte som kända innan de förklarats.
- Funktionella krav behandlas före generella och icke-funktionella krav.
- Gherkin, Cucumber och Concordion introduceras först efter regler, exempel, scenarier och dokumentationsstruktur.
- Organisation och införande kommer efter att arbetssättet är etablerat.

## Dokumentation

- Dokumentationsråd fungerar för både verksamhet och IT.
- Skillnaden mellan kravtext, regel, exempel, scenario och testfall är tydlig.
- Levande dokumentation beskrivs utan att reducera SBE till testautomation.
- Verktygsval kopplas till syfte och sammanhang.

## Export

- Kapitel använder endast H1–H3.
- Listor har tomrad före och efter.
- Tabeller har header, separatorrad och lika många celler per rad.
- Inga H4-rubriker förekommer.
- Alla bildreferenser pekar på existerande filer.
- `docs/export-metadata.yaml` är uppdaterad.


## Helhetsgranskning 2026-05-26

- Kapitel 0–16 finns och följer beslutad kapitelordning.
- Bokens röda tråd är kontrollerad: från problem med traditionellt kravarbete, via SBE-dokumentation och workshoparbete, till testkoppling, kvalitetskrav och organisatoriskt införande.
- Det genomgående caset med brottsutredningsstöd används återkommande och fungerar som sammanhållande exempel.
- Dokumentationsperspektivet för både verksamhet och IT är särskilt förstärkt genom kapitel 8, 10, 11, 12 och 16.
- Omslagsbild finns på `assets/cover/cover.png` och refereras i metadata.
- Lokal markdownvalidering via `scripts/export-book.py markdown` är kontrollerad efter justering av valideringslogiken.
- EPUB/PDF är ännu inte genererade i denna granskning.

## Redaktionell åtgärdsrunda 2026-05-26

- Kapiteltexterna har justerats efter helhetsgranskningen, inte bara granskningsdokumenten.
- Varje kapitel har fått tydligare koppling till bokens röda tråd där det stärker progressionen.
- Övergången mellan dokumentation, testkoppling och organisatoriskt införande har förtydligats.
- Skillnaden mellan SBE, Gherkin/Cucumber/Concordion och generell testautomation har förtydligats i manusflödet.
- Projektet är redo för exportgenerering för läsgranskning.
