# Projektstatus

## Bok

Titel: Kravarbete med SBE  
Språk: Svenska  
Författare: Erland Lindmark  
Version: 0.3
Omslagsbild: Godkänd och inlagd i `assets/cover/cover.png`

## Nuvarande fas

- Start/intervju: Klart
- Bokspecifikation: Utkast klart
- Kapitelplan: Utkast godkänt
- Kapitelgenerering: Klart
- Granskning: Helhetsgranskning och redaktionell åtgärdsrunda genomförd
- Export: Förberedd efter redaktionell åtgärdsrunda, EPUB/PDF ej genomförd

## Kapitelstatus

| Kapitel | Titel | Status | Kommentar |
|---|---|---|---|
| 0 | Inledning | Redigerat | Obligatorisk inledning finns och kan förfinas senare |
| 1 | Varför traditionellt kravarbete inte alltid räcker | Redigerat | Skrivet första ämneskapitel |
| 2 | Vad SBE är — och inte är | Redigerat | Skrivet centralt begreppskapitel |
| 3 | Kravanalytikerns förändrade roll | Redigerat | Skrivet roll- och arbetssättskapitel |
| 4 | Caset: ett brottsutredningsstöd i myndighetsmiljö | Redigerat | Skrivet case- och kontextkapitel |
| 5 | Att hitta funktionella krav som lämpar sig för SBE | Redigerat | Skrivet kapitel om urval av funktionella krav för SBE |
| 6 | Från traditionella krav till exempelbaserad specifikation | Redigerat | Skrivet kapitel om omvandling från traditionella krav till exempelbaserad specifikation |
| 7 | Regler, exempel och scenarier i praktiken | Redigerat | Skrivet praktiskt fördjupningskapitel om regler, exempel, scenarier och dokumentationsnivå |
| 8 | Dokumentation som fungerar för både verksamhet och IT | Redigerat | Skrivet centralt dokumentationskapitel om lager, struktur, spårbarhet och dokumentation för både verksamhet och IT |
| 9 | Exempelworkshops och gemensam förfining | Redigerat | Skrivet kapitel om exempelworkshops, facilitering, förfining, öppna frågor och dokumentation efter workshop |
| 10 | Gherkin, Cucumber och Concordion | Redigerat | Skrivet kapitel om Gherkin, Cucumber, Concordion, formatval, automation och levande dokumentation |
| 11 | Samspel mellan krav, test och utveckling | Redigerat | Skrivet kapitel om samspel mellan krav, test och utveckling, automation, spårbarhet och rollernas bidrag |
| 12 | Kvalitetssäkring av SBE-specifikationer | Redigerat | Skrivet kapitel om kvalitetsdimensioner, granskningsflöde, exempelgranskning och beslutsmognad |
| 13 | Generella krav i ett SBE-arbetssätt | Redigerat | Skrivet kapitel om tvärgående funktionella regler, räckvidd, generella regelområden, spårbarhet och dokumentationsnivå |
| 14 | Icke-funktionella krav och kvalitetskrav | Redigerat | Skrivet kapitel om kvalitetskrav, exempel, mätbara kriterier, verifiering och relationen till funktionella flöden |
| 15 | Att införa SBE i en etablerad organisation | Redigerat | Skrivet kapitel om pilot, införandeteam, förändringsresa, verktygsmognad, förvaltning och skalning |
| 16 | Mallar, checklistor och arbetsmönster | Redigerat | Skrivet praktiskt avslutningskapitel med mallar, checklistor, arbetsmönster och beslutsstöd |

## Introducerade begrepp

| Begrepp | Kapitel | Kort definition |
|---|---|---|
| Tolkningsutrymme | 1 | När en kravformulering kräver att läsaren fyller i detaljer med egna antaganden |
| Dubbeldokumentation | 1 | När samma regel eller beteende beskrivs i flera artefakter och riskerar att glida isär |
| Gemensam förståelse | 1 | Delad praktisk förståelse mellan verksamhet, IT, test och andra intressenter om hur systemet ska bete sig |
| Dokumentationsglapp | 1 | Skillnaden mellan dokumentation som verksamheten kan förstå och dokumentation som IT kan använda |
| SBE | 2 | Specification by Example, ett arbetssätt där konkreta exempel används för att skapa gemensam förståelse och testbar specifikation |
| Levande dokumentation | 2 | Dokumentation som hålls aktuell genom att vara nära arbetssätt, exempel och ibland automatiserade kontroller |
| Gherkin | 2 | Textformat för att uttrycka beteenden med Given-When-Then, behandlas mer praktiskt i kapitel 10 |
| Cucumber | 2 | Verktygsekosystem för BDD och körning av Gherkin-scenarier, behandlas mer praktiskt i kapitel 10 |
| Concordion | 2 | Verktyg för dokumentnära körbara specifikationer, behandlas mer praktiskt i kapitel 10 |
| Förståelsefacilitator | 3 | Kravanalytikerns roll i SBE: att skapa förutsättningar för gemensam förståelse snarare än att ensam skriva krav |
| Öppen fråga | 3 | En synliggjord osäkerhet eller obesvarad fråga som behöver hanteras innan specifikationen kan stabiliseras |
| Teknisk konsekvens | 3 | IT-relevant följd av en verksamhetsregel eller ett exempel, dokumenterad separat från själva regeln |
| Systemgräns | 4 | Avgränsning mellan vad användaren gör, vad brottsutredningsstödet ansvarar för och vad andra system eller rutiner ansvarar för |
| Informationsobjekt | 4 | Verksamhetsnära objekt som används för analys, exempelvis utredningsärende, uppgift, tilldelning och åtkomstlogg |
| Verksamhetsregel | 4 | Regel uttryckt i verksamhetens språk som konkreta exempel kan pröva och förtydliga |
| Åtkomstloggning | 4 | Registrering av åtkomst eller åtkomstförsök till information, särskilt viktig vid känsliga uppgifter |
| Ärendestatus | 4 | Markering av var ett ärende befinner sig i arbetsflödet och vilka övergångar som är möjliga |

| SBE-kandidat | 5 | Ett funktionellt krav eller beteende som har tillräcklig komplexitet, risk eller tolkningsutrymme för att förfinas med regler och exempel |
| Beslutsregel | 5 | En regel där systemets beteende avgörs av villkor, exempelvis roll, relation, status eller sekretessmarkering |
| Tillståndsövergång | 5 | En förändring från en status till en annan, där regler avgör om övergången är tillåten, villkorad eller förbjuden |
| Gränsfall | 5 | En situation vid en regelgräns där systemets beteende behöver vara särskilt tydligt, exempelvis exakt vid sista giltighetstid |
| SBE-potential | 5 | Bedömning av hur mycket nytta ett krav får av att beskrivas med konkreta exempel och scenarier |

| Transformationskedja | 6 | Praktisk arbetsgång för att gå från traditionell kravtext till syfte, regler, exempel, öppna frågor och tekniska konsekvenser |
| Exempeltabell | 6 | Tabell som visar konkreta kombinationer av villkor och förväntade utfall för en regel |
| Begränsad information | 6 | Ett utfall där systemet visar viss information om ett ärende men skyddar känsliga uppgifter |
| Referensexempel | 6 | Ett konkret exempel som används för att förankra, granska och återanvända en regel i fortsatt arbete |
| Regel | 7 | En verksamhetsnära utsaga om vad som ska gälla, prövbar med konkreta exempel |
| Scenario | 7 | Beskrivning av beteende över tid eller genom en interaktion, ofta med Given-When-Then-struktur |
| Normalexempel | 7 | Exempel som visar det vanligaste förväntade beteendet |
| Undantagsexempel | 7 | Exempel som visar när en regel inte gäller eller behöver särskild hantering |
| Konfliktexempel | 7 | Exempel som prövar när två eller flera regler samspelar eller verkar krocka |
| Beslutstabell | 7 | Tabell som jämför villkor och utfall för att tydliggöra komplexa regler |
| Verksamhetsscenario | 7 | Scenario skrivet i verksamhetens språk för gemensam förståelse, inte som teknisk testimplementation |
| Verksamhetslager | 8 | Del av dokumentationen som beskriver syfte, behov och verksamhetsregler i domänens språk |
| Specifikationslager | 8 | Del av dokumentationen där regler, exempel, beslutstabeller och scenarier konkretiserar systemets beteende |
| Tekniskt lager | 8 | Del av dokumentationen där tekniska konsekvenser för design, test, integration och förvaltning dokumenteras separat från verksamhetsregeln |
| Dokumentationsmönster | 8 | Återkommande struktur för hur syfte, regler, exempel, scenarier, öppna frågor och tekniska konsekvenser dokumenteras |
| Exempel-ID | 8 | Stabil referens till ett konkret exempel som kan användas för spårbarhet, granskning och testkoppling |
| Regel-ID | 8 | Stabil referens till en regel som gör det möjligt att hänvisa till regeln utan att duplicera den |
| Begränsad sökträff | 8 | Visning där systemet visar viss icke-känslig information om ett ärende men döljer skyddade uppgifter |

| Exempelworkshop | 9 | Strukturerat arbetsmöte där flera roller utforskar ett avgränsat beteende genom konkreta exempel |
| Facilitator | 9 | Person som leder workshopprocessen, håller fokus och hjälper gruppen att växla mellan regler, exempel och frågor |
| Example mapping | 9 | Workshopmönster där funktion, regler, exempel och frågor separeras för att skapa gemensam förståelse |
| Workshopmaterial | 9 | Råmaterial från workshop som behöver efterbearbetas innan det blir färdig SBE-specifikation |
| Beslutsför roll | 9 | Deltagare eller intressent som kan bekräfta regler, välja mellan alternativ eller äga vidare beslut |
| Workshopavgränsning | 9 | Tydlig begränsning av vilket beteende workshopen ska utforska och vad som ligger utanför scope |

| Automatiserbart scenario | 10 | Scenario som är formulerat så att det kan kopplas till körbar kontroll utan att förlora verksamhetsnivån |
| Step definition | 10 | Kod som kopplar en Gherkin-rad till teknisk körning i Cucumber |
| Scenario Outline | 10 | Gherkin-struktur där samma scenario körs med flera exempelrader |
| Verktygsnära specifikation | 10 | Specifikation som uttrycks i ett format som kan stödja automation, exempelvis Gherkin eller Concordion |
| Automationsstatus | 10 | Markering av om ett exempel eller scenario är ej automatiserat, planerat, automatiserat eller pensionerat |
| Syntetiska data | 10 | Fiktiva men realistiska data som används i exempel utan att exponera verklig känslig information |

| Kravexempel | 11 | Verksamhetsnära exempel som konkretiserar en regel och skapar gemensam förståelse |
| Testfall | 11 | Beskrivning av hur ett beteende verifieras, ofta med testdata, steg och förväntade observationer |
| Automatiserat test | 11 | Körbar kontroll som verifierar ett beteende upprepbart |
| Teknisk implementation | 11 | Den lösning i systemet som realiserar ett beslutat beteende |
| Regressionsvärde | 11 | Nyttan av att kunna kontrollera att ett beteende fortsätter fungera efter ändringar |
| Praktisk spårbarhet | 11 | Lättviktig koppling mellan regel, exempel, test, implementation och beslut |
| Avvikelsehantering | 11 | Arbetssätt för att analysera skillnader mellan specifikation, test och system innan något ändras |

| Kvalitetsdimension | 12 | Perspektiv som används för att bedöma om en SBE-specifikation fungerar i praktiken, exempelvis begriplighet, precision och täckning |
| Begriplighet | 12 | Att rätt läsare kan förstå och bekräfta specifikationen utan onödig översättning |
| Precision | 12 | Att beteendet är tillräckligt entydigt för att olika roller inte ska göra olika tolkningar |
| Täckning | 12 | Att exemplen belyser viktiga normalfall, undantag, gränsfall och konfliktfall |
| Beslutsmognad | 12 | Tydlighet kring vad som är beslutat, antaget, öppet, parkerat eller ersatt |
| Granskningsbarhet | 12 | Att specifikationen kan bedömas av verksamhet och IT utifrån konkreta regler, exempel och frågor |
| Generellt krav | 13 | Ett krav som gäller över flera funktioner, flöden, informationsobjekt eller roller |
| Tvärgående verksamhetsregel | 13 | En verksamhetsregel som påverkar flera funktionella områden |
| Räckvidd | 13 | Beskrivning av var en regel gäller, var den inte gäller och vilka undantag som finns |
| Regelområde | 13 | Samlad dokumentation för en grupp relaterade generella regler, exempel och scenarier |
| Standardbeteende | 13 | Ett återkommande systembeteende som ska vara konsekvent över flera delar av lösningen |
| Behörighetsdomän | 13 | Avgränsning som styr vilka ärenden eller uppgifter en användare får se eller hantera |
| Statusövergång | 13 | Förändring från en ärendestatus till en annan enligt definierade regler och villkor |
| Regelägare | 13 | Roll eller funktion som kan fatta beslut om en generell regel och dess ändringar |
| Kvalitetskrav | 14 | Krav som beskriver systemets egenskaper, exempelvis prestanda, säkerhet, spårbarhet, användbarhet, tillgänglighet och robusthet |
| Verksamhetsexempel | 14 | Konkret situation som visar varför ett kvalitetskrav behövs och vad det betyder i praktiken |
| Mätbart kriterium | 14 | Formulering som gör ett kvalitetskrav verifierbart, exempelvis svarstid, täckning eller granskningsbart utfall |
| Verifieringsmetod | 14 | Sätt att kontrollera om ett kvalitetskrav är uppfyllt, exempelvis test, granskning, mätning eller revision |
| Informationsskydd | 14 | Skydd mot att känslig information visas, avslöjas eller kan härledas av obehöriga |
| Robusthet | 14 | Systemets förmåga att hantera fel, avbrott och externa beroenden utan felaktigt eller riskabelt beteende |
| Datakvalitet | 14 | Egenskap hos information som gör den korrekt, fullständig, aktuell och användbar i sitt sammanhang |
| Automationsstatus | 14 | Markering av om ett kvalitetskrav eller exempel är ej automatiserat, delvis automatiserat, automatiserat, övervakat eller granskas periodiskt |
| Införande | 15 | Den praktiska förändringsresa där SBE stegvis blir en del av ordinarie kravarbete, dokumentation, test och förvaltning |
| Pilotområde | 15 | Avgränsat område där SBE prövas i liten skala för att skapa lärande och visa nytta innan arbetssättet skalas |
| Införandeteam | 15 | Liten grupp med relevanta roller som driver och följer upp SBE-införandet i praktiken |
| Införanderytm | 15 | Återkommande arbetssätt för att identifiera områden, hålla exempelworkshops, dokumentera, granska och uppdatera specifikationer |
| Artefakt | 15 | Dokumentations- eller arbetsprodukt som används i kravarbete, test, styrning eller förvaltning |
| Dokumentationsägarskap | 15 | Tydligt ansvar för att SBE-specifikationen hålls korrekt och levande efter leverans |
| Införandemognad | 15 | Grad av organisatorisk förmåga att använda och skala SBE utan att skapa otydlighet, dubbeldokumentation eller felaktig standardisering |
| Mall | 16 | Återanvändbar struktur som stödjer samtal, dokumentation och granskning utan att ersätta analysen |
| Checklista | 16 | Praktiskt stöd för att bedöma kvalitet, formatval, införande eller utvecklingsberedskap |
| Arbetsmönster | 16 | Återkommande sekvens av aktiviteter som kan användas i liknande kravsituationer |
| Dokumentationspaket | 16 | Samlad dokumentation för ett funktionellt område, inklusive syfte, regler, exempel, frågor, kopplingar och ägarskap |
| Beslutsstöd | 16 | Hjälp för att välja dokumentationsformat, automationsnivå eller införandeväg utifrån situation och nytta |
| Automationskandidat | 16 | Exempel eller regel som verkar lämplig för automatiserad verifiering men där beslut ännu inte är taget |

## Öppna beslut

- Slutlig omslagsdesign behöver genereras och godkännas.
- Bokens slutliga exportformat prioriteras senare: EPUB, PDF, DOCX eller alla.

## Nästa rekommenderade steg

- Granska helheten: progression, terminologi, case-kontinuitet och exportberedskap.

## Granskningsnoteringar

- Helhetsgranskning genomförd efter att samtliga kapitel 0–16 och omslag lagts in.
- Kapitelordning, metadata, omslagsreferens och lokal markdownvalidering har kontrollerats.
- Exportscriptet har justerats så att validering skiljer mellan bokens markdown och markdown-/Gherkin-exempel inuti kodblock.
- Inga inre illustrationer används enligt projektbeslut.

## Nästa rekommenderade steg

- Skapa EPUB och PDF för läsgranskning.
- Gör därefter en språkredaktionell slutputs utifrån läsgranskningen.

## Redaktionell åtgärdsrunda 2026-05-26

- Kapitel 0–16 har justerats med tydligare övergångar och kopplingar till bokens röda tråd.
- Dokumentationsperspektivet för både verksamhet och IT har förstärkts i relevanta kapitel.
- Skillnaden mellan SBE som arbetssätt och verktyg/testautomation har förtydligats.
- Gränsen mellan funktionella krav, generella krav och kvalitetskrav har gjorts tydligare i övergångarna mellan kapitlen.
- Projektversionen är uppdaterad till 0.3.

## Exportlogg

- PDF skapad med Pandoc, innehållsförteckning före inledningen och omslag som första sida.
