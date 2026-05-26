# Kravarbete med SBE

**En praktisk handbok för kravanalytiker som vill gå från traditionella krav till levande specifikation**

Författare: Erland Lindmark  
Språk: svenska  
Version: 0.1  
Datum: 2026-05-26

Detta är ett startprojekt för en praktisk lärobok/handbok om kravarbete och dokumentation med SBE, med ett genomgående case om framtagning av ett brottsutredningsstöd inom en myndighet.

## Projektstruktur

- `chapters/` innehåller inledning och kapitelmanus.
- `docs/` innehåller bokspecifikation, kapitelplan, canon, terminologi, status och exportmetadata.
- `assets/cover/` är plats för omslagsbild.
- `assets/image-prompts/` innehåller bildpromptar, inklusive omslagsprompt.
- `styles/` innehåller CSS för EPUB och PDF.
- `scripts/` innehåller lokal exportpipeline.
- `exports/` är målplats för genererade EPUB/PDF/DOCX/Markdown-filer.

## Nästa rekommenderade steg

1. Skriv eller generera `chapters/00-inledning.md`.
2. Skriv kapitel 1.
3. Uppdatera `docs/project-status.md` efter varje kapitel.
4. Bygg lokalt med `scripts/export-book.sh` när manus är tillräckligt färdigt.

## Export lokalt

Projektet är förberett för lokal export med Pandoc:

```bash
bash scripts/export-book.sh epub
bash scripts/export-book.sh pdf
bash scripts/export-book.sh all
```

Scriptet validerar metadata, kapitelordning, rubriknivåer, tabeller, kodblock och bildreferenser före export.
