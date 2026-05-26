# Canon-terminologi

## Grundprincip

Boken ska använda svenska termer när de är tydliga, men introducera vedertagna engelska begrepp första gången när de är etablerade i branschen.

## Centrala termer

| Term | Rekommenderad användning | Kommentar |
|---|---|---|
| SBE | Använd SBE efter första introduktion | Första gången: Specification by Example, SBE |
| Specification by Example | Använd vid första introduktion och vid förtydliganden | Engelsk term behålls eftersom den är vedertagen |
| Exempel | Konkret fall som visar hur en regel ska fungera | Ska inte blandas ihop med testfall för tidigt |
| Regel | Verksamhetsregel eller funktionsregel som exemplen konkretiserar | Regeln ska vara begriplig för verksamheten |
| Scenario | Sammanhängande beskrivning av en situation, ofta med förutsättning, händelse och resultat | Kan vara i Gherkin-format eller mer fri text |
| Levande dokumentation | Dokumentation som hålls aktuell och används aktivt | Inte synonymt med automatiserad testsvit |
| BDD | Behavior-Driven Development, använd som närliggande arbetssätt till SBE | Förklara att BDD inte är synonymt med SBE |
| ATDD | Acceptance Test-Driven Development, använd när fokus ligger på acceptanstester före implementation | Förklara relationen till SBE utan att göra boken testautomationscentrerad |
| Öppen fråga | Något som specifikationen ännu inte har besvarat | Ska behandlas som en värdefull analysartefakt |
| Acceptanskriterium | Villkor för att en funktion eller ändring ska accepteras | Jämförs med exempel, men ska inte göras till synonym |
| Gherkin | Format med Given, When, Then | Förklara på svenska men behåll nyckelorden |
| Cucumber | Verktyg för BDD/Gherkin | Behandlas på kravanalytikernivå |
| Concordion | Verktyg för dokumentnära körbara specifikationer | Behandlas som alternativ till mer scenariofilorienterade format |
| Funktionellt krav | Krav på vad systemet ska göra | Huvudfokus i boken |
| Generellt krav | Tvärgående krav eller återkommande regel | Behandlas separat |
| Icke-funktionellt krav | Kvalitetskrav på hur väl systemet ska fungera | Behandlas separat |
| Tolkningsutrymme | Använd för osäkerhet som uppstår när läsaren måste fylla i egna antaganden | Introduceras i kapitel 1 |
| Dubbeldokumentation | Använd när samma regel beskrivs i flera artefakter | Koppla till risk för flera versioner av sanningen |
| Gemensam förståelse | Använd för delad praktisk förståelse mellan verksamhet, IT, test och andra intressenter | Viktigare än enbart formellt godkänd dokumentation |
| Dokumentationsglapp | Använd för skillnaden mellan dokumentation som verksamheten kan förstå och dokumentation som IT kan använda | Återkommer i kapitel om dokumentationsstruktur |
| Förståelsefacilitator | Använd för kravanalytikerns SBE-roll | Rollen handlar om att möjliggöra gemensam förståelse, inte att ensam äga sanningen |
| Teknisk konsekvens | Använd för IT-relevanta följder av en regel eller ett exempel | Ska inte blandas ihop med verksamhetsregeln |
| Beslut | Använd för val som gruppen har gjort och som påverkar specifikationen | Skilj från regel och öppen fråga |
| Systemgräns | Använd för att avgränsa vad användaren gör, vad brottsutredningsstödet ansvarar för och vad andra system ansvarar för | Introduceras i kapitel 4 |
| Informationsobjekt | Använd för verksamhetsnära objekt i analysen | Ska inte likställas med databasmodell |
| Verksamhetsregel | Använd för regler uttryckta i verksamhetens språk | Skilj från teknisk konsekvens och testfall |
| Åtkomstloggning | Använd för systemets registrering av åtkomst och åtkomstförsök | Kan vara både funktionellt beteende och del av kvalitets-/säkerhetskrav |
| Ärendestatus | Använd för status i utredningsärendets arbetsflöde | Statusövergångar används som återkommande SBE-exempel |

| SBE-kandidat | Använd för krav eller beteenden som bör förfinas med regler och exempel | Introduceras i kapitel 5 |
| Beslutsregel | Använd för regler där systemet behöver välja beteende utifrån villkor | Skilj från generell regel och teknisk validering |
| Tillståndsövergång | Använd för byte mellan statusar i ett arbetsflöde | Bra kandidat för tabeller och exempel |
| Gränsfall | Använd för situationer vid en regelgräns | Exempelvis exakt vid sista giltighetstid |
| SBE-potential | Använd för bedömning av hur mycket nytta ett krav har av exempelbaserad förfining | Används i urval och prioritering |

| Transformationskedja | Använd för den praktiska arbetsgången från traditionell kravtext till exempelbaserad specifikation | Introduceras i kapitel 6 |
| Exempeltabell | Använd för tabeller som konkretiserar regler genom kombinationer av villkor och utfall | Skilj från testmatris om fokus ännu är analys |
| Begränsad information | Använd för ett skyddat utfall där systemet visar vissa ärendeuppgifter men döljer känsliga detaljer | Definiera alltid vilka fält som ingår när begreppet används konkret |
| Referensexempel | Använd för konkreta exempel som återanvänds som ankare i fortsatt analys, test och dokumentation | Ska inte nödvändigtvis betyda automatiserat test |

| Regel | Använd för verksamhetsnära utsaga om vad som ska gälla | Ska kunna prövas med exempel och inte blandas ihop med teknisk implementation |
| Scenario | Använd när beteende behöver beskrivas över tid eller genom interaktion | Skilj från exempeltabell och tekniskt testscenario |
| Normalexempel | Använd för det vanligaste förväntade beteendet | Bör inte vara det enda exemplet vid komplexa regler |
| Undantagsexempel | Använd för fall där regeln inte gäller eller behöver särskild hantering | Viktigt för att hitta dolda antaganden |
| Konfliktexempel | Använd för exempel där flera regler samspelar eller verkar krocka | Särskilt relevant för behörighet, sekretess och ansvar |
| Beslutstabell | Använd för tabell som visar villkor och utfall för komplexa regler | Använd när jämförelse av kombinationer är viktigare än händelseförlopp |
| Verksamhetsscenario | Använd för scenario som verksamhet och IT kan läsa tillsammans | Håll tekniska anrop och implementation utanför huvudspecifikationen |

| Verksamhetslager | Dokumentationslager för syfte, behov och regler i verksamhetens språk | Ska kunna granskas utan teknisk lösningskunskap |
| Specifikationslager | Dokumentationslager där regler konkretiseras med exempel, scenarier och beslutstabeller | SBE-dokumentationens kärna |
| Tekniskt lager | Dokumentationslager för tekniska konsekvenser | Ska kopplas till regler men hållas separat från verksamhetsregeln |
| Dokumentationsmönster | Återkommande struktur för en typ av specifikation | Används för igenkänning och underhållbarhet |
| Regel-ID | Stabil referens till en regel | Används för spårbarhet utan dubbeldokumentation |
| Exempel-ID | Stabil referens till ett exempel | Används för spårbarhet, granskning och testkoppling |
| Begränsad sökträff | Sökresultat som visar endast tillåten, icke-känslig information | Används i caset om sekretess och åtkomst |

| Exempelworkshop | Använd för strukturerat arbetsmöte där flera roller utforskar ett avgränsat beteende genom konkreta exempel | Introduceras i kapitel 9 |
| Facilitator | Använd för den som leder workshopprocessen och säkrar fokus, deltagande och dokumentation | Ofta kravanalytikern i bokens exempel |
| Example mapping | Använd för workshopmönster där funktion, regler, exempel och frågor separeras | Engelsk term kan behållas som etablerat begrepp |
| Workshopmaterial | Använd för råmaterial från workshop innan det har efterbearbetats till specifikation | Skilj från färdig SBE-specifikation |
| Beslutsför roll | Använd för person eller funktion som kan bekräfta regler eller äga beslut | Viktigt i myndighetscaset |
| Workshopavgränsning | Använd för tydlig scope-definition för en exempelworkshop | Hjälper gruppen undvika för breda möten |


| Automatiserbart scenario | Använd för scenario som kan kopplas till körbar kontroll utan att förlora verksamhetsnivån | Introduceras i kapitel 10 |
| Step definition | Använd för Cucumber-kod som binder Gherkin-steg till teknisk körning | Förklara som tekniskt lager, inte kravdokumentation |
| Scenario Outline | Använd för Gherkin-scenario med flera exempelrader | Behåll engelsk term eftersom den är verktygsnära |
| Verktygsnära specifikation | Använd för specifikation uttryckt i format som stödjer automation | Exempel: Gherkin/Cucumber eller Concordion |
| Automationsstatus | Använd för status på om ett scenario/exempel är ej automatiserat, planerat, automatiserat eller pensionerat | Kopplas till dokumentationsstruktur |
| Syntetiska data | Använd för fiktiva men realistiska data i exempel | Viktigt i myndighets- och brottsutredningscaset |

## Stilregler

- Skriv `SBE` efter första förklaring.
- Skriv `Specification by Example` när begreppet behöver förtydligas.
- Använd `verksamhet` och `IT` konsekvent när båda perspektiven diskuteras.
- Använd `brottsutredningsstöd` som namn på det generiska systemcaset.
- Undvik att kalla alla exempel för testfall. Förklara först när ett exempel blir testbart eller automatiserbart.
| Kravexempel | Använd för verksamhetsnära exempel som konkretiserar en regel | Ska inte göras synonymt med testfall |
| Testfall | Använd för verifieringsbeskrivning med steg, data och förväntade observationer | Skilj från kravexempel |
| Automatiserat test | Använd för körbar kontroll av beteende | Kan länkas till exempel men ersätter inte verksamhetsdokumentation |
| Teknisk implementation | Använd för lösningen som realiserar beteendet i systemet | Ska inte beskrivas som krav om det inte är ett beslutat krav |
| Regressionsvärde | Använd för nyttan av att kunna köra kontrollen upprepade gånger | Hjälper vid beslut om automation |
| Praktisk spårbarhet | Använd för lättviktig koppling mellan regel, exempel, test, implementation och beslut | Ska vara stödjande, inte administrativt tung |
| Avvikelsehantering | Använd när system, test och specifikation inte stämmer överens | Kräver analys innan dokumentation eller test ändras |



## Termer etablerade i kapitel 12

| Term | Rekommenderad användning | Kommentar |
|---|---|---|
| Kvalitetsdimension | Använd för de perspektiv som används för att granska SBE-specifikationer | I kapitel 12 används begriplighet, precision, täckning, spårbarhet, underhållbarhet och beslutsmognad |
| Begriplighet | Använd för att beskriva om verksamhet och andra läsare kan förstå och bekräfta specifikationen | Ska inte förväxlas med förenkling eller låg detaljnivå |
| Precision | Använd för att beskriva hur entydigt beteendet är beskrivet | Precision ska gälla beteende, inte nödvändigtvis teknisk implementation |
| Täckning | Använd för hur väl exempel belyser viktiga variationer | Fler exempel är inte automatiskt bättre täckning |
| Granskningsbarhet | Använd för att beskriva om regler, exempel och frågor kan bedömas av rätt roller | Koppla till verksamhetsgranskning, IT-granskning och gemensam kvalitetsgranskning |
| Beslutsmognad | Använd för tydlighet kring vad som är beslutat, antaget, öppet, parkerat eller ersatt | Viktigt innan implementation och automation |
| Automationskandidat | Använd för exempel som kan vara lämpligt att automatisera | Ska bedömas utifrån stabilitet, observerbarhet, testdata och värde |
| Kvalitetsgranskning | Använd för praktisk granskning av SBE-specifikationens användbarhet | Ska leda till konkreta åtgärder, inte bara formellt godkännande |


## Termer etablerade i kapitel 13

| Term | Rekommenderad användning | Kommentar |
|---|---|---|
| Generellt krav | Använd för krav som gäller över flera funktioner, flöden, informationsobjekt eller roller | Ska inte automatiskt behandlas som icke-funktionellt krav |
| Tvärgående verksamhetsregel | Använd för verksamhetsregler med bred räckvidd | Dokumentera centralt och visa effekten i viktiga flöden |
| Räckvidd | Använd för att beskriva var en regel gäller, var den inte gäller och vilka undantag som finns | Räckvidd är avgörande för generella krav |
| Regelområde | Använd för en samlad grupp av relaterade generella regler, exempel, undantag och scenarier | Exempel: åtkomst och behörighetsdomän, ärendestatus, loggning |
| Standardbeteende | Använd för återkommande systembeteende som ska vara konsekvent i flera delar av lösningen | Exempel: visning av tomma fält |
| Behörighetsdomän | Använd för avgränsning som styr vilka ärenden eller uppgifter en användare får se eller hantera | Central term i caset om brottsutredningsstödet |
| Statusövergång | Använd för förändring från en ärendestatus till en annan enligt definierade regler och villkor | Lämpar sig ofta för beslutstabell |
| Regelägare | Använd för roll eller funktion som kan fatta beslut om en generell regel | Viktigt för ändringshantering och spårbarhet |
| Dokumentationsnivå | Använd för hur omfattande en regel behöver beskrivas utifrån risk, påverkan och stabilitet | Hjälper kravanalytikern att undvika både över- och underdokumentation |


## Termer etablerade i kapitel 14

| Term | Rekommenderad användning | Kommentar |
|---|---|---|
| Kvalitetskrav | Använd för krav som beskriver systemets egenskaper, exempelvis prestanda, säkerhet, spårbarhet, användbarhet, tillgänglighet och robusthet | Kan ibland konkretiseras med exempel men behöver ofta mätbara kriterier |
| Verksamhetsexempel | Använd för konkret situation som visar varför ett kvalitetskrav behövs | Ska vara begripligt för verksamheten och kopplat till ett faktiskt arbetsflöde |
| Mätbart kriterium | Använd för kriterier som gör kvalitetskrav verifierbara | Exempel: svarstid, belastning, andel lyckade användaruppgifter eller granskningsbart utfall |
| Verifieringsmetod | Använd för att beskriva hur kvalitetskravet kontrolleras | Kan vara test, mätning, granskning, revision eller driftövervakning |
| Informationsskydd | Använd för skydd mot att känslig information visas, avslöjas eller kan härledas av obehöriga | Särskilt viktigt vid sökning, visning, export och felmeddelanden |
| Robusthet | Använd för systemets förmåga att hantera fel, avbrott och externa beroenden | Ska beskrivas med verksamhetskonsekvens, inte bara tekniskt fel |
| Datakvalitet | Använd för informationens riktighet, fullständighet, aktualitet och användbarhet | Kan konkretiseras med regler och exempeltabeller |
| Automationsstatus | Använd för att visa hur ett krav eller exempel verifieras över tid | Var tydlig med ej automatiserat, delvis automatiserat, automatiserat, övervakat eller periodiskt granskat |
| Införande | Använd för den praktiska förändringsresan där SBE blir del av ordinarie arbete | Ska inte beskrivas som enbart utbildning, mall eller verktygsutrullning |
| Pilotområde | Använd för ett avgränsat område där SBE prövas och följs upp | Ska vara viktigt, regelintensivt och hanterbart |
| Införandeteam | Använd för liten grupp som driver och lär av införandet | Behöver krav, verksamhet, test, utveckling och produkt-/beslutsmandat |
| Införanderytm | Använd för återkommande sekvens av identifiering, workshop, dokumentation, granskning och uppdatering | Ska hållas lätt nog för vardagligt arbete |
| Dokumentationsägarskap | Använd för ansvar efter leverans | Betona att levande dokumentation kräver ägare och ändringsrytm |
| Införandemognad | Använd för organisationens beredskap att skala SBE | Skala principer före detaljerade mallar |
| Artefakt | Använd för dokumentations- eller arbetsprodukt | Exempel: kravspecifikation, SBE-specifikation, testfall, beslut, öppna frågor |



## Kapitel 16: mallar, checklistor och arbetsmönster

| Begrepp | Användning | Kommentar |
|---|---|---|
| Mall | Använd för återanvändbar struktur som stödjer dokumentation och granskning | Ska inte framställas som ersättning för analys eller samtal |
| Checklista | Använd för praktisk kontroll av kvalitet, formatval eller införandeberedskap | Ska vara beslutsstöd, inte byråkratisk grind |
| Arbetsmönster | Använd för återkommande sekvens av aktiviteter | Exempel: från traditionellt krav till SBE, granskningsmöte eller införanderytm |
| Dokumentationspaket | Använd för samlad dokumentation per funktionellt område | Innehåller syfte, regler, exempel, frågor, kopplingar och ägarskap |
| Beslutsstöd | Använd för att välja format, automationsnivå eller införandeväg | Ska väga läsare, nytta, risk och underhåll |
| Automationskandidat | Använd för exempel eller regel som kan automatiseras men där beslut ännu inte är taget | Automatisering ska styras av nytta och stabilitet |
| Granskningsmöte | Använd för möte där specifikationen prövas av både verksamhet och IT | Fokus på användbarhet, inte bara textkvalitet |

## Redaktionella kontinuitetsregler efter helhetsgranskning

- Använd konsekvent `SBE` som kortform efter första introduktionen av `Specification by Example`.
- Skilj konsekvent mellan SBE som arbetssätt, Gherkin som format och Cucumber/Concordion som verktygsstöd.
- Beskriv brottsutredningsstödet som ett genomgående pedagogiskt case, inte som ett komplett systemförslag.
- När dokumentation diskuteras ska både verksamhetens läsbarhet och IT:s behov av precision nämnas när det är relevant.
