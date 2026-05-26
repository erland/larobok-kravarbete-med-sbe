# Kapitel 12: Kvalitetssäkring av SBE-specifikationer

## Varför detta kapitel finns

När en organisation börjar arbeta med SBE brukar de första förbättringarna komma snabbt. Kraven blir mer konkreta. Verksamheten känner igen sig i exemplen. Testare och utvecklare får något mer prövbart än allmänna formuleringar. Diskussionerna flyttas från abstrakta tolkningar till konkreta situationer.

Efter ett tag uppstår en ny fråga: hur vet vi att våra SBE-specifikationer faktiskt är bra?

Det räcker inte att en specifikation innehåller exempel. Den kan ändå vara svår att förstå, sakna viktiga fall, blanda verksamhetsregler med tekniska detaljer eller vara så omfattande att ingen orkar underhålla den. En SBE-specifikation kan också se tydlig ut men ändå dölja öppna frågor, antaganden och beslut som inte är förankrade.

Det här kapitlet handlar om kvalitetssäkring av SBE-specifikationer. Fokus ligger inte på formell granskning för sakens skull, utan på praktisk kvalitet: att specifikationen ska fungera som gemensam sanning för verksamhet, krav, test och utveckling över tid.

I caset med brottsutredningsstödet blir detta särskilt viktigt. Regler om åtkomst, sekretess, statusövergångar, loggning och informationsvisning får inte bara vara ungefär rätt. De behöver vara tillräckligt tydliga för att verksamheten ska kunna bekräfta dem, tillräckligt konkreta för att IT ska kunna bygga dem och tillräckligt stabila för att test och förvaltning ska kunna lita på dem.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- bedöma kvaliteten i en SBE-specifikation utifrån begriplighet, precision, täckning och underhållbarhet
- skilja mellan en specifikation som ser komplett ut och en specifikation som faktiskt är granskningsbar
- identifiera vanliga kvalitetsbrister i regler, exempel, scenarier och beslutstabeller
- använda en praktisk granskningsmodell för SBE-dokumentation
- avgöra när fler exempel behövs och när fler exempel bara skapar brus
- kvalitetssäkra att dokumentationen fungerar både för verksamhet och IT
- hantera öppna frågor, antaganden och beslutsbehov som en del av kvalitetsarbetet

## Innan vi börjar

De tidigare kapitlen har byggt upp flera delar som behövs för kvalitetssäkring:

- Kapitel 6 visade hur traditionell kravtext kan omvandlas till exempelbaserad specifikation.
- Kapitel 7 fördjupade skillnaden mellan regler, exempel, scenarier och beslutstabeller.
- Kapitel 8 visade hur dokumentationen kan struktureras så att den fungerar för både verksamhet och IT.
- Kapitel 9 beskrev hur exempel tas fram och förfinas i workshops.
- Kapitel 10 och 11 visade hur exempel kan kopplas till test, utveckling och eventuell automation.

Det här kapitlet binder ihop dessa delar. Vi går från frågan “hur skriver vi specifikationen?” till frågan “hur vet vi att den håller tillräcklig kvalitet?”.

## Vad betyder kvalitet i en SBE-specifikation?

Kvalitet i SBE handlar inte om att specifikationen är lång, formellt korrekt eller skriven i ett visst verktyg. Det handlar om att den kan användas för rätt saker av rätt personer.

En bra SBE-specifikation ska kunna svara på frågor som:

- Förstår verksamheten vilket beteende som beskrivs?
- Kan verksamheten avgöra om exemplen är rimliga?
- Kan utvecklare se vad systemet ska göra och var osäkerhet finns?
- Kan testare härleda relevanta testfall utan att uppfinna egna regler?
- Kan nya personer förstå varför ett beteende finns?
- Kan specifikationen ändras utan att allt måste skrivas om?
- Är det tydligt vilka frågor som fortfarande är öppna?

Det betyder att kvalitet är flerdimensionell. En specifikation kan vara tekniskt testbar men obegriplig för verksamheten. Den kan vara lättläst men för oprecis för utveckling. Den kan vara komplett i ett enskilt flöde men missa viktiga undantag. Den kan vara korrekt i dag men svår att underhålla när reglerna förändras.

I SBE behöver vi därför granska flera kvalitetsdimensioner samtidigt.

## En praktisk kvalitetsmodell

Ett användbart sätt att granska SBE-specifikationer är att använda sex kvalitetsdimensioner:

| Dimension | Fråga | Typisk risk |
|---|---|---|
| Begriplighet | Kan rätt personer förstå specifikationen? | Verksamheten tappar bort sig i tekniska detaljer |
| Precision | Är beteendet tillräckligt entydigt? | Olika roller gör olika tolkningar |
| Täckning | Finns tillräckliga exempel för viktiga fall? | Undantag och gränsfall missas |
| Spårbarhet | Går det att se varför regeln finns och vad den påverkar? | Dokumentationen blir svår att förvalta |
| Underhållbarhet | Går specifikationen att ändra utan onödig friktion? | Dubbeldokumentation och spridda regler |
| Beslutsmognad | Är det tydligt vad som är beslutat, antaget eller öppet? | Teamet bygger på outtalade antaganden |

Den här modellen kan användas vid granskning av en hel specifikation, ett funktionsområde eller ett enskilt regelpaket.

I brottsutredningsstödet kan samma modell användas för att granska exempelvis sökbehörighet, statusövergångar eller visning av begränsad information.

## Begriplighet: kan verksamheten bekräfta specifikationen?

En SBE-specifikation måste vara begriplig för verksamheten. Det betyder inte att varje teknisk detalj ska döljas, men det betyder att kärnan i beteendet ska kunna granskas av de personer som kan verksamhetsreglerna.

En specifikation är begriplig när verksamheten kan säga:

- “Ja, det här är rätt beteende.”
- “Nej, det här exemplet stämmer inte.”
- “Här saknas ett undantag.”
- “Den här regeln gäller bara i vissa ärendetyper.”
- “Det här ordet betyder inte samma sak för oss.”

Om verksamheten bara kan läsa rubriken men inte exemplen har specifikationen inte lyckats. Om IT behöver översätta varje rad muntligt under granskningen är dokumentationen inte tillräckligt verksamhetsnära.

### Exempel från caset

Anta att specifikationen innehåller följande regel:

> Systemet ska exkludera sökträffar där användarens behörighetskontext inte matchar ärendets åtkomstprofil.

För IT kan formuleringen kännas rimlig. Den antyder att det finns en behörighetskontext och en åtkomstprofil. Men för en utredare eller förundersökningsledare kan den vara svår att bekräfta. Den säger inte vilka situationer som avses.

En mer verksamhetsnära regel kan vara:

> En utredare får se ett ärende i sökresultatet om utredaren tillhör ärendets ansvariga enhet eller är tilldelad ärendet. Om ärendet är särskilt sekretessmarkerat krävs dessutom ett särskilt åtkomstbeslut.

Den senare formuleringen är fortfarande inte fullständig, men den går att diskutera. Verksamheten kan reagera på orden “tillhör”, “tilldelad”, “särskilt sekretessmarkerat” och “särskilt åtkomstbeslut”. Det är bra. De orden är verksamhetens begrepp och kan konkretiseras med exempel.

### Granskningsfrågor för begriplighet

Vid granskning kan kravanalytikern ställa frågor som:

- Kan en verksamhetsexpert läsa regeln utan att behöva förstå teknisk arkitektur?
- Använder specifikationen verksamhetens ord på ett konsekvent sätt?
- Är tekniska konsekvenser separerade från verksamhetsregeln?
- Finns exempel som gör regeln igenkännbar i arbetssituationen?
- Är otydliga begrepp markerade och definierade?

Begriplighet betyder inte förenkling till den grad att precision försvinner. Det betyder att specifikationen börjar i verksamhetens verklighet och därefter gör beteendet tillräckligt konkret för IT.

## Precision: kan olika roller tolka beteendet på samma sätt?

Precision handlar om att minska tolkningsutrymmet. En specifikation kan vara begriplig men ändå oprecis. Alla förstår ungefär vad den säger, men olika personer kan fortfarande dra olika slutsatser.

Traditionella acceptanskriterier kan ofta hamna här:

> Användaren ska endast se ärenden som användaren har behörighet till.

Det är begripligt. Men det är inte tillräckligt precist. Vad betyder behörighet? Räcker organisatorisk enhet? Vad händer vid delegation? Vad händer vid särskild sekretess? Vad händer om användaren tidigare haft behörighet men inte längre har det? Ska träffen döljas helt eller visas begränsat?

SBE ökar precisionen genom exempel.

| Exempel-ID | Utredarens relation | Ärendets markering | Särskilt beslut | Förväntat resultat |
|---|---|---|---|---|
| SOK-KV-01 | Samma ansvariga enhet | Ingen särskild sekretess | Nej | Ärendet visas |
| SOK-KV-02 | Tilldelad ärendet | Ingen särskild sekretess | Nej | Ärendet visas |
| SOK-KV-03 | Ingen relation | Ingen särskild sekretess | Nej | Ärendet visas inte |
| SOK-KV-04 | Tilldelad ärendet | Särskild sekretess | Nej | Ärendet visas inte |
| SOK-KV-05 | Tilldelad ärendet | Särskild sekretess | Ja | Ärendet visas |

Tabellen gör inte bara regeln mer testbar. Den gör den mer granskningsbar. En verksamhetsexpert kan peka på ett exempel och säga: “Det där stämmer inte. Tilldelning ska inte räcka vid särskild sekretess.” Eller: “Särskilt beslut krävs bara för vissa ärendekategorier.”

Det är precis den typen av reaktion vi vill få fram tidigt.

### Precision utan överdetaljering

Det finns en risk att precision misstolkas som maximal detaljering. Då börjar specifikationen beskriva skärmfält, API-anrop, databasvärden och tekniska felkoder långt innan det behövs.

En SBE-specifikation ska vara precis om beteendet, men inte nödvändigtvis detaljerad om lösningen.

I caset betyder det till exempel:

- Specificera när ärendet ska visas, döljas eller visas begränsat.
- Specificera vilka verksamhetsvillkor som styr utfallet.
- Specificera vilka öppna frågor som återstår.
- Undvik att i huvudregeln beskriva exakt SQL-logik, tjänsteanrop eller cachemekanismer.
- Lägg tekniska konsekvenser i ett separat tekniskt lager när de behövs.

Precision handlar alltså om att rätt sak är tydlig på rätt nivå.

## Täckning: har vi rätt exempel, inte bara många exempel?

Täckning handlar om att exemplen tillsammans belyser det beteende som behöver förstås. Det är lätt att tro att fler exempel alltid är bättre. Så är det inte. Målet är inte att samla så många exempel som möjligt, utan att ha exempel som täcker viktiga variationer.

En bra uppsättning exempel brukar innehålla:

- normalfall
- viktiga undantag
- gränsfall
- konflikter mellan regler
- riskfyllda situationer
- tidigare missförstånd
- beslutade men ovanliga fall

För sökbehörighet räcker det sällan med ett exempel där allt går rätt. De viktiga frågorna uppstår i undantagen.

### Exempel på täckningsanalys

Anta att specifikationen för sökresultat har dessa exempel:

| Exempel-ID | Situation | Förväntat resultat |
|---|---|---|
| SOK-KV-01 | Utredare söker ärende i egen enhet | Ärendet visas |
| SOK-KV-02 | Utredare söker tilldelat ärende | Ärendet visas |
| SOK-KV-03 | Utredare söker ärende utan relation | Ärendet visas inte |

Det är en början, men täckningen är svag om brottsutredningsstödet också har sekretessmarkeringar, delegationer, spärrar och rollbaserade undantag.

En granskare kan då fråga:

- Finns exempel för särskild sekretess?
- Finns exempel för utgången delegation?
- Finns exempel för spärr på grund av jäv?
- Finns exempel för förundersökningsledare?
- Finns exempel för begränsad sökträff?
- Finns exempel där flera regler samspelar?

Täckning handlar alltså inte om antalet rader, utan om vilka variationer raderna representerar.

### Täckningsmatris för analys

En enkel täckningsmatris kan hjälpa utan att bli tung administration.

| Regelområde | Normalfall | Undantag | Gränsfall | Konfliktfall | Öppna frågor |
|---|---|---|---|---|---|
| Sökbehörighet | Finns | Finns delvis | Saknas | Saknas | Finns |
| Särskild sekretess | Finns | Finns | Saknas | Finns delvis | Finns |
| Delegation | Finns | Saknas | Saknas | Saknas | Finns |
| Jäv/spärr | Saknas | Saknas | Saknas | Saknas | Finns |
| Begränsad sökträff | Finns delvis | Saknas | Saknas | Finns delvis | Finns |

Matrisen visar inte hela sanningen, men den hjälper gruppen att se var specifikationen behöver förfinas.

## Spårbarhet: går det att förstå sammanhanget?

Spårbarhet i SBE ska inte bli ett administrativt självändamål. Syftet är att kunna förstå varför en regel finns, vilka exempel som konkretiserar den och vad som påverkas om den ändras.

En lättviktig spårbarhet kan räcka långt:

| Artefakt | Exempel |
|---|---|
| Regel-ID | REG-SOK-01 |
| Regel | En utredare får se ett ärende om utredaren tillhör ansvarig enhet eller är tilldelad ärendet |
| Exempel | SOK-KV-01, SOK-KV-02, SOK-KV-03 |
| Öppna frågor | OQ-SOK-04: Ska dold träff räknas i antal sökresultat? |
| Testkoppling | Manuell granskning, automatiserade regressionstest för stabila exempel |
| Relaterade krav | Behörighet, sökresultat, åtkomstloggning |

Det viktiga är inte att varje relation finns i ett avancerat verktyg. Det viktiga är att sambanden är möjliga att följa.

### Spårbarhet utan dubbeldokumentation

En vanlig fallgrop är att försöka skapa spårbarhet genom att kopiera samma regel till flera dokument:

- i kravspecifikationen
- i acceptanskriterier
- i testfall
- i teknisk design
- i förvaltningsdokumentation

Det kan kännas tryggt i början, men skapar snabbt flera versioner av sanningen.

SBE bör i stället sträva efter stabila referenser:

- Regeln skrivs på ett ställe.
- Exemplen konkretiserar regeln.
- Testfall och automatisering refererar till exempel-ID eller regel-ID.
- Teknisk dokumentation beskriver implementationens konsekvenser, inte en ny version av regeln.
- Öppna frågor och beslut kopplas till regeln utan att regeln dupliceras.

När en regel ändras ska gruppen veta var sanningen finns.

## Underhållbarhet: går specifikationen att leva med?

En SBE-specifikation är bara levande dokumentation om den faktiskt hålls levande. Därför behöver den vara underhållbar.

Underhållbarhet påverkas av flera saker:

- hur tydligt specifikationen är strukturerad
- om regler och exempel är separerade på rätt sätt
- om samma sak skrivs på flera ställen
- om exempel är namngivna och begripliga
- om gamla exempel rensas bort när regler ändras
- om öppna frågor och beslut hanteras aktivt
- om automatiserade tester är kopplade på ett hållbart sätt

En specifikation som är perfekt första dagen men svår att ändra blir snabbt en belastning.

### Tecken på svag underhållbarhet

Följande signaler bör tas på allvar:

- Det är oklart vilken regel som ett exempel hör till.
- Flera exempel skiljer sig bara i irrelevanta detaljer.
- Samma regel uttrycks med olika ord på olika ställen.
- Verksamheten vågar inte ändra i dokumentationen eftersom den känns teknisk.
- Utvecklare ändrar automatiserade tester utan att specifikationen uppdateras.
- Öppna frågor ligger kvar utan ansvarig eller beslut.
- Dokumentationen innehåller gamla exempel som inte längre gäller.
- Nya teammedlemmar behöver muntlig genomgång för att förstå vad som är beslutat.

Underhållbarhet är inte bara ett dokumentationsproblem. Det är ett arbetssättsproblem. Om teamet inte har en vana att uppdatera specifikationen när regler ändras kommer dokumentationen att tappa sin roll som gemensam sanning.

### Praktisk regel

En enkel tumregel är:

> Om specifikationen inte används när teamet ändrar systemet, är den inte längre levande dokumentation.

Det betyder att kvalitetssäkring inte bara sker i en granskning. Den sker varje gång teamet använder specifikationen för att fatta beslut, utveckla, testa eller förvalta.

## Beslutsmognad: vet vi vad som är beslutat?

En SBE-specifikation kan vara välskriven men ändå farlig om den blandar ihop beslut, antaganden och öppna frågor.

I kravarbete är detta en klassisk risk. Någon skriver ett exempel för att illustrera ett möjligt beteende. En utvecklare tolkar det som beslutat. En testare bygger testfall på det. Verksamheten trodde att frågan fortfarande var öppen.

Därför behöver specifikationen visa beslutsmognad.

| Status | Betydelse | Hantering |
|---|---|---|
| Beslutat | Gruppen har enats om beteendet | Kan användas för implementation och test |
| Antaget | Används tillfälligt för att komma vidare | Ska markeras och bekräftas |
| Öppen fråga | Beteendet är ännu inte beslutat | Ska ha ägare eller nästa steg |
| Parkerat | Frågan är känd men hanteras senare | Ska inte driva implementation |
| Ersatt | Tidigare beslut gäller inte längre | Ska arkiveras eller markeras tydligt |

I brottsutredningsstödet kan frågan om dold sökträff vara ett exempel:

> Ska systemet visa att det finns en träff som användaren inte får se, eller ska träffen döljas helt?

Detta är inte bara en användargränssnittsfråga. Det påverkar säkerhet, juridik, användbarhet, loggning och förtroende. Om teamet skriver exempel utan att markera frågan som öppen kan en lösning byggas på ett ogrundat antagande.

## Granskning på flera nivåer

Alla SBE-specifikationer behöver inte granskas på samma sätt. Det är ofta bättre att granska på flera nivåer.

### Snabbgranskning

En snabbgranskning kan göras av kravanalytiker, testare och utvecklare innan en workshop eller inför refinement.

Syfte:

- hitta uppenbara oklarheter
- se om exempel saknar förväntat resultat
- fånga dubbla regler
- identifiera öppna frågor
- förbereda diskussion med verksamheten

Frågor:

- Förstår vi vad regeln försöker säga?
- Finns minst ett konkret exempel?
- Finns det uppenbara undantag som saknas?
- Är något formulerat tekniskt utan att behöva vara det?
- Finns öppna frågor markerade?

### Verksamhetsgranskning

Verksamhetsgranskningen fokuserar på om beteendet är rätt, begripligt och fullständigt nog ur verksamhetens perspektiv.

Deltagare kan vara:

- utredare
- förundersökningsledare
- verksamhetsspecialist
- produktägare
- kravanalytiker
- testare som lyssnar efter testbarhet

Frågor:

- Stämmer regeln med hur arbetet ska fungera?
- Känner ni igen exemplen?
- Finns viktiga undantag?
- Används rätt begrepp?
- Är något beskrivet som beslutat fast det egentligen är oklart?

### IT-granskning

IT-granskningen fokuserar på realiserbarhet, testbarhet, tekniska konsekvenser och beroenden.

Deltagare kan vara:

- utvecklare
- testare
- arkitekt
- säkerhetsrepresentant
- systemförvaltare
- kravanalytiker

Frågor:

- Är beteendet observerbart?
- Går exemplen att testa?
- Kräver regeln tekniska beslut som saknas?
- Finns beroenden till andra system?
- Finns risk att automation blir för skör?
- Är tekniska konsekvenser dokumenterade separat från verksamhetsregeln?

### Gemensam kvalitetsgranskning

För viktiga eller riskfyllda områden bör verksamhet och IT granska tillsammans. Det är särskilt viktigt när regler påverkar säkerhet, juridik, spårbarhet eller kritiska arbetsflöden.

I caset kan detta gälla:

- åtkomst till sekretessmarkerade ärenden
- loggning av åtkomstförsök
- statusövergångar som påverkar beslut
- visning av begränsad information
- spärrar vid jäv eller särskilda skyddsbehov

Målet är inte att alla ska förstå allt på samma tekniska djup. Målet är att alla ska förstå sin del av sanningen och hur den hänger ihop med helheten.

## Kvalitetssäkring av regler

Regler är ryggraden i många SBE-specifikationer. Om regeln är otydlig blir exemplen ofta antingen spretiga eller missvisande.

En bra regel är:

- uttryckt i verksamhetens språk
- avgränsad till ett beteende eller en princip
- konkretiserbar med exempel
- fri från onödig teknisk implementation
- kopplad till öppna frågor om den inte är färdig
- tillräckligt stabil för att användas i vidare arbete

### Svag regel

> Systemet ska hantera behörighet korrekt.

Problemet är inte att regeln är falsk. Problemet är att den inte säger något granskningsbart. Ingen kan veta vad “korrekt” betyder utan att lägga till egna antaganden.

### Bättre regel

> En utredare får se ett ärende i sökresultatet om utredaren tillhör ärendets ansvariga enhet eller är tilldelad ärendet, så länge ärendet inte är särskilt sekretessmarkerat.

Den regeln går att diskutera och exemplifiera. Den är fortfarande inte komplett, men den har en tydlig form.

### Ännu bättre med kompletterande regler

För komplexa områden är det ofta bättre med flera små regler än en lång regel.

- En utredare får se ett ärende i sökresultatet om utredaren tillhör ärendets ansvariga enhet.
- En utredare får se ett ärende i sökresultatet om utredaren är tilldelad ärendet.
- Särskild sekretess överstyr tilldelning om det saknas särskilt åtkomstbeslut.
- Ett ärende som inte visas i sökresultatet ska inte avslöjas genom antal träffar om detta strider mot sekretessregeln.

Den sista regeln visar dessutom en ny fråga: ska antal träffar påverkas av dolda ärenden? Det är en bra signal att specifikationen behöver granskning.

## Kvalitetssäkring av exempel

Exempel är SBE-specifikationens konkreta ankare. De visar hur reglerna ska fungera i praktiken. Men alla exempel är inte bra exempel.

Ett bra exempel är:

- konkret
- relevant
- begripligt
- kopplat till en regel
- tydligt i förutsättningar och förväntat resultat
- fritt från irrelevant variation
- möjligt att använda i dialog med verksamhet och IT

### Exempel med för mycket brus

| Exempel-ID | Användare | Klockslag | Webbläsare | Skärmstorlek | Ärende | Relation | Förväntat resultat |
|---|---|---|---|---|---|---|---|
| SOK-KV-06 | Anna | 09:14 | Edge | 1920x1080 | Ärende 1001 | Samma enhet | Ärendet visas |

Om klockslag, webbläsare och skärmstorlek inte påverkar regeln ska de inte finnas i exemplet. De får läsaren att undra om de är viktiga.

### Exempel med relevant information

| Exempel-ID | Relation till ärende | Sekretessmarkering | Särskilt beslut | Förväntat resultat |
|---|---|---|---|---|
| SOK-KV-06 | Samma ansvariga enhet | Nej | Nej | Ärendet visas |
| SOK-KV-07 | Samma ansvariga enhet | Ja | Nej | Ärendet visas inte |
| SOK-KV-08 | Samma ansvariga enhet | Ja | Ja | Ärendet visas |

Här är variationen relevant. Varje kolumn hjälper läsaren att förstå regeln.

### Granskningsfrågor för exempel

- Vilken regel konkretiserar exemplet?
- Är alla villkor i exemplet relevanta för utfallet?
- Är förväntat resultat observerbart?
- Finns både normalfall och viktiga undantag?
- Finns gränsfall där regelns betydelse ändras?
- Finns exempel som bara upprepar samma sak?
- Är exemplet begripligt utan muntlig förklaring?

Bra exempel minskar behovet av muntlig komplettering. Om gruppen alltid behöver säga “det som egentligen menas är…” bör exemplet skrivas om.

## Kvalitetssäkring av scenarier

Scenarier är användbara när beteendet sker över tid eller genom interaktion. De kan skrivas i Gherkin eller i friare verksamhetsspråk.

Ett bra scenario har:

- en tydlig startpunkt
- en relevant händelse eller handling
- ett observerbart resultat
- en avgränsad poäng
- få irrelevanta sidospår
- begrepp som redan är definierade eller förklarade

### Scenario som försöker göra för mycket

```gherkin
Scenario: Utredare söker efter ärende och får rätt resultat
  Given att utredaren är inloggad
  And att utredaren har rätt behörighet
  And att ärendet finns
  And att ärendet har rätt status
  And att ärendet inte är spärrat
  And att användaren söker
  Then visas rätt resultat
  And sökningen loggas
  And användaren kan öppna ärendet
  And systemet visar rätt flikar
```

Det här scenariot är svårt att granska. Det blandar sökresultat, loggning, öppning av ärende och gränssnittsdetaljer. Det använder dessutom uttryck som “rätt behörighet” och “rätt resultat”, vilket återinför tolkningsutrymme.

### Scenario med tydligare poäng

```gherkin
Scenario: Tilldelat ärende utan särskild sekretess visas i sökresultatet
  Given att utredaren är tilldelad ärendet
  And att ärendet inte är särskilt sekretessmarkerat
  When utredaren söker på ärendets diarienummer
  Then visas ärendet i sökresultatet
```

Detta scenario är smalare. Det betyder inte att loggning och öppning av ärende är oviktigt. Det betyder att de bör beskrivas där de hör hemma.

### Granskningsfrågor för scenarier

- Har scenariot ett tydligt syfte?
- Testar eller beskriver det en sak åt gången?
- Är förutsättningarna tillräckligt konkreta?
- Är resultatet observerbart?
- Finns ord som “rätt”, “korrekt”, “relevant” eller “giltig” utan definition?
- Är scenariot på verksamhetsnivå eller har det glidit in i teknisk implementation?
- Skulle verksamheten kunna säga om scenariot är sant eller falskt?

Scenarier bör inte bli små romaner. De ska vara tillräckligt konkreta för att skapa samsyn och tillräckligt avgränsade för att kunna underhållas.

## Kvalitetssäkring av beslutstabeller

Beslutstabeller är kraftfulla när många villkor påverkar ett utfall. De passar särskilt bra för behörighet, validering, klassificering och statusövergångar.

Men beslutstabeller kan snabbt bli svåra att läsa.

En bra beslutstabell har:

- tydliga kolumner
- begripliga värden
- en tydlig förväntad effekt
- inga onödiga villkor
- konsekvent användning av ja, nej, saknas eller ej relevant
- uppdelning i flera tabeller om den blir för stor

### Beslutstabell för sökvisning

| Exempel-ID | Samma enhet | Tilldelad | Särskild sekretess | Särskilt beslut | Förväntat resultat |
|---|---|---|---|---|---|
| SOK-KV-09 | Ja | Nej | Nej | Nej | Visas |
| SOK-KV-10 | Nej | Ja | Nej | Nej | Visas |
| SOK-KV-11 | Nej | Nej | Nej | Nej | Visas inte |
| SOK-KV-12 | Ja | Nej | Ja | Nej | Visas inte |
| SOK-KV-13 | Ja | Nej | Ja | Ja | Visas |

Den här tabellen är hanterbar. Om vi lägger till jäv, delegation, ärendestatus, informationsklass, tidsgräns, roll och organisatorisk nivå i samma tabell kan den bli för svår att använda.

Då bör vi dela upp den:

- en tabell för grundläggande åtkomst
- en tabell för sekretessöverstyrning
- en tabell för delegation
- en tabell för jäv eller spärr
- en tabell för begränsad information

### Granskningsfrågor för beslutstabeller

- Är varje kolumn relevant för utfallet?
- Finns kombinationer som saknas?
- Finns kombinationer som är omöjliga och bör markeras?
- Är värdena konsekventa?
- Är tabellen läsbar för verksamheten?
- Bör tabellen delas upp?
- Finns exempel-ID som gör tabellen lätt att referera till?

En beslutstabell ska hjälpa läsaren att se variation. Om tabellen kräver lång muntlig förklaring har den blivit för tung eller för teknisk.

## Dokumentation som kvalitetsrisk

I SBE är dokumentationsstrukturen en del av kvaliteten. Även bra regler och exempel kan förlora värde om de ligger på fel plats, blandas ihop med lösningsdetaljer eller saknar sammanhang.

Kapitel 8 beskrev lager som kan användas:

- verksamhetslager
- specifikationslager
- tekniskt lager
- test- och automationskoppling
- beslut och öppna frågor

Kvalitetssäkring bör kontrollera att varje typ av information ligger på rätt plats.

### Exempel på blandad dokumentation

> När en utredare söker ska systemet anropa behörighetstjänsten, filtrera resultat utifrån ACL-tabellen och visa endast ärenden där användaren har rätt roll enligt rolltabellen. Utredaren ska se tilldelade ärenden och ärenden i sin enhet.

Här blandas verksamhetsregel och teknisk lösning. Det kan vara relevant att behörighetstjänsten finns, men den bör inte stå inne i verksamhetsregeln om den inte är en del av det beteende verksamheten ska bekräfta.

### Bättre uppdelning

Verksamhetsregel:

> En utredare får se ärenden i sökresultatet om utredaren tillhör ärendets ansvariga enhet eller är tilldelad ärendet.

Exempel:

| Exempel-ID | Relation | Förväntat resultat |
|---|---|---|
| SOK-KV-14 | Samma ansvariga enhet | Ärendet visas |
| SOK-KV-15 | Tilldelad ärendet | Ärendet visas |
| SOK-KV-16 | Ingen relation | Ärendet visas inte |

Teknisk konsekvens:

> Sökfunktionen behöver kontrollera relationen mellan användare och ärende via behörighetsinformationen innan resultatet returneras till användaren.

Öppen fråga:

> Ska sökningen logga även ärenden som filtreras bort på grund av saknad behörighet?

Den här uppdelningen gör dokumentationen mer granskningsbar. Verksamheten kan bekräfta regeln. IT kan diskutera teknisk konsekvens. Juridik eller säkerhet kan hantera den öppna frågan.

## Vanliga kvalitetsbrister

SBE-specifikationer får ofta återkommande brister. Att känna igen dem gör granskningen snabbare.

### Brist 1: Exempel utan regel

Exempel utan regel kan vara användbara i en tidig workshop, men de blir svåra att underhålla om de inte kopplas till en regel.

Problem:

- Det är oklart varför exemplet finns.
- Flera exempel kan motsäga varandra.
- Testare och utvecklare får svårt att avgöra vad som är princip och vad som är enstaka fall.

Åtgärd:

- Formulera regeln som exemplen konkretiserar.
- Koppla exempel-ID till regel-ID.
- Markera eventuella undantag.

### Brist 2: Regel utan exempel

En regel utan exempel kan fortfarande vara för abstrakt.

Problem:

- Gruppen tror att regeln är förstådd.
- Undantag upptäcks sent.
- Testare behöver skapa egna tolkningar.

Åtgärd:

- Ta fram minst ett normalexempel.
- Lägg till viktiga undantag.
- Fråga verksamheten när regeln inte gäller.

### Brist 3: Exempel som är för tekniska

Tekniska exempel kan behövas, men de bör inte ersätta verksamhetsexempel.

Problem:

- Verksamheten kan inte granska beteendet.
- Specifikationen blir beroende av lösningsdesign.
- Teamet riskerar att låsa implementation för tidigt.

Åtgärd:

- Skriv om huvudexemplet i verksamhetsspråk.
- Lägg tekniska detaljer i tekniskt lager.
- Behåll tekniska tester som koppling, inte som enda specifikation.

### Brist 4: För många nästan likadana exempel

När exemplen blir många men inte tillför ny förståelse minskar läsbarheten.

Problem:

- Viktiga fall drunknar i variation.
- Specifikationen blir svår att granska.
- Automation kan bli långsam och skör.

Åtgärd:

- Behåll referensexempel.
- Sammanfoga liknande variationer.
- Använd beslutstabell när många kombinationer behöver visas.
- Markera vilka exempel som är regressionsexempel och vilka som bara var analysstöd.

### Brist 5: Öppna frågor göms i texten

Öppna frågor som skrivs in i brödtext utan ansvar eller status försvinner lätt.

Problem:

- Teamet tror att frågan är löst.
- Beslut skjuts upp men påverkar implementation.
- Risker blir osynliga.

Åtgärd:

- Lägg öppna frågor i egen lista eller tabell.
- Ge varje öppen fråga ägare eller nästa steg.
- Markera om exempel bygger på antagande.

### Brist 6: Dokumentationen följer verktyget i stället för läsaren

När ett verktyg styr strukturen för hårt kan dokumentationen bli sämre för verksamheten.

Problem:

- Allt tvingas in i Gherkin även när beslutstabell vore tydligare.
- Långa scenarier ersätter pedagogisk förklaring.
- Läsaren måste förstå verktygets format för att förstå regeln.

Åtgärd:

- Välj format utifrån beteendets karaktär.
- Använd Gherkin när det passar interaktion och observerbart beteende.
- Använd tabell eller Concordion-liknande dokumentation när många villkor behöver överblick.
- Separera analysdokumentation från automationskod där det behövs.

## Granskningsflöde för ett regelområde

Här är ett praktiskt granskningsflöde för ett regelområde i brottsutredningsstödet.

### Steg 1: Avgränsa regelområdet

Välj ett område, till exempel “sökbehörighet för utredningsärenden”.

Skriv syftet kort:

> Regelområdet beskriver när en utredare får se, inte se eller se begränsad information om ett ärende i sökresultatet.

Avgränsa bort sådant som hör till andra områden:

- inloggning
- användaradministration
- teknisk autentisering
- fullständig loggningsspecifikation
- användargränssnittets visuella design

### Steg 2: Identifiera regler

Lista reglerna i verksamhetsspråk.

| Regel-ID | Regel | Status |
|---|---|---|
| REG-SOK-01 | En utredare får se ärenden i sin ansvariga enhet | Beslutat |
| REG-SOK-02 | En utredare får se ärenden som utredaren är tilldelad | Beslutat |
| REG-SOK-03 | Särskild sekretess överstyr enhet och tilldelning om särskilt beslut saknas | Antaget |
| REG-SOK-04 | Jäv eller spärr blockerar visning även vid tilldelning | Öppen fråga |

Redan här ser vi kvalitet. Det är tydligt vad som är beslutat och vad som inte är det.

### Steg 3: Koppla exempel till regler

| Exempel-ID | Regel-ID | Situation | Förväntat resultat |
|---|---|---|---|
| SOK-KV-17 | REG-SOK-01 | Utredaren tillhör ansvarig enhet | Ärendet visas |
| SOK-KV-18 | REG-SOK-02 | Utredaren är tilldelad ärendet | Ärendet visas |
| SOK-KV-19 | REG-SOK-03 | Tilldelad men särskild sekretess saknar beslut | Ärendet visas inte |
| SOK-KV-20 | REG-SOK-03 | Tilldelad och särskilt beslut finns | Ärendet visas |
| SOK-KV-21 | REG-SOK-04 | Tilldelad men jäv/spärr finns | Öppen fråga |

Exempel SOK-KV-21 ska inte behandlas som beslutat. Det ska markeras som analysfall eller öppen fråga.

### Steg 4: Granska täckning

Fråga:

- Har vi normalfall?
- Har vi undantag?
- Har vi konfliktfall?
- Finns gränsfall?
- Saknas aktörer?
- Saknas statusar eller ärendetyper?

Om viktiga fall saknas lägger gruppen till exempel. Om många exempel bara upprepar samma regel tar gruppen bort eller sammanfattar.

### Steg 5: Granska läsbarhet

Låt en verksamhetsperson läsa specifikationen utan muntlig förklaring.

Fråga:

- Vilken regel tycker du att detta beskriver?
- Vilket exempel känns mest realistiskt?
- Vilket exempel känns fel eller saknas?
- Vilka ord behöver definieras?

Låt sedan en utvecklare och testare läsa samma specifikation.

Fråga:

- Kan ni se vad systemet ska göra?
- Kan ni se vad som behöver testas?
- Kan ni se vad som är oklart?
- Finns tekniska konsekvenser som behöver dokumenteras separat?

### Steg 6: Besluta nästa åtgärd

Efter granskningen bör varje brist få en tydlig åtgärd.

| Fynd | Åtgärd | Ansvar |
|---|---|---|
| Jäv/spärr är inte beslutat | Ta upp med verksamhet och juridik | Produktägare |
| Särskild sekretess behöver tydligare definition | Förtydliga regel och lägga till exempel | Kravanalytiker |
| Automationskandidater saknar stabil data | Avvakta automation tills testdatafråga är löst | Testare |
| Teknisk konsekvens för loggning saknas | Dokumentera i tekniskt lager | Utvecklare och arkitekt |

Kvalitetssäkring blir då inte en passiv kontroll. Den leder till konkret förbättring.

## När är en specifikation tillräckligt bra?

En vanlig fråga är när man kan sluta förfina. Svaret är inte “när alla tänkbara exempel finns”. Svaret är snarare: när specifikationen är tillräckligt bra för nästa beslut.

För implementation kan det betyda:

- kärnregler är beslutade
- viktiga exempel är granskade
- kända öppna frågor är markerade
- kritiska undantag är hanterade
- testare och utvecklare kan arbeta utan att gissa
- verksamheten har bekräftat beteendet

För automation kan kraven vara högre:

- exempel är stabila
- förväntat resultat är observerbart
- testdata går att styra
- tekniska beroenden är hanterbara
- scenarier är inte för sköra
- teamet vet vem som underhåller testerna

För en tidig workshop kan kraven vara lägre:

- exemplen behöver bara vara tillräckligt tydliga för att skapa diskussion
- öppna frågor får finnas
- felaktiga exempel kan vara värdefulla om de avslöjar missförstånd

Kvalitet ska alltså bedömas utifrån användning. En specifikation som är tillräcklig för analys är inte alltid tillräcklig för implementation. En specifikation som är tillräcklig för implementation är inte alltid mogen för automation.

## Kvalitet och automation

Automation kan hjälpa till att hålla dokumentationen levande, men automation löser inte kvalitetsproblemen automatiskt.

Ett automatiserat scenario kan fortfarande vara:

- byggt på fel regel
- obegripligt för verksamheten
- för tekniskt
- för smalt
- för skört
- duplicerat i för många varianter
- svårt att koppla till verksamhetsbeslut

Innan ett exempel automatiseras bör teamet fråga:

- Är beteendet beslutat?
- Är exemplet viktigt att regressionssäkra?
- Är förväntat resultat observerbart?
- Är testdata hanterbar?
- Är scenariot stabilt nog?
- Kommer automatiseringen att öka eller minska begripligheten?

I brottsutredningsstödet kan ett stabilt exempel om tilldelat ärende i arbetslista vara en bra automationskandidat. Ett exempel som beror på en ännu obeslutad juridisk tolkning av dold sökträff bör däremot inte automatiseras som om det vore beslutat.

Automation ska förstärka kvalitet, inte dölja brister.

## Kvalitetsgranskning som workshop

För viktiga regelområden kan kvalitetssäkring göras som en särskild granskningsworkshop.

### Förslag på agenda

| Moment | Syfte | Tid |
|---|---|---|
| Påminn om regelområdet | Skapa gemensam kontext | 10 minuter |
| Gå igenom regler | Kontrollera språk och beslut | 20 minuter |
| Gå igenom exempel | Kontrollera precision och täckning | 30 minuter |
| Identifiera saknade fall | Hitta undantag och gränsfall | 20 minuter |
| Granska öppna frågor | Säkerställa ägare och nästa steg | 15 minuter |
| Besluta åtgärder | Göra förbättringar konkreta | 15 minuter |

Deltagare bör väljas efter regelområdets risk. För sökbehörighet kan det vara kravanalytiker, utredare, förundersökningsledare, testare, utvecklare, säkerhet och juridik. För en enklare statusövergång kanske färre personer räcker.

### Viktigt arbetssätt

Kravanalytikern bör inte fråga “är dokumentet godkänt?”. Det leder ofta till passiva svar.

Ställ hellre konkreta granskningsfrågor:

- Vilket exempel känns fel?
- Vilket exempel saknas?
- Vilket ord kan tolkas olika?
- Vad skulle en ny utredare missförstå?
- Vad skulle en utvecklare behöva gissa?
- Vad skulle en testare behöva hitta på själv?
- Vad vågar vi automatisera?
- Vad ska inte automatiseras ännu?

Dessa frågor skapar bättre kvalitet än en allmän godkännandeprocess.

## Kvalitetschecklista

Följande checklista kan användas vid granskning av ett regelområde.

### Begriplighet

- Regeln är skriven i verksamhetens språk.
- Centrala begrepp är definierade eller länkade till terminologi.
- Verksamheten kan läsa och bekräfta exemplen.
- Tekniska detaljer ligger inte i vägen för verksamhetsförståelsen.
- Exempel och scenarier använder igenkännbara situationer.

### Precision

- Varje regel har minst ett konkret exempel.
- Förväntat resultat är tydligt och observerbart.
- Ord som “rätt”, “korrekt”, “giltig” och “relevant” är definierade eller undviks.
- Villkor och utfall blandas inte ihop.
- Undantag anges tydligt.

### Täckning

- Normalfall finns.
- Viktiga undantag finns.
- Gränsfall finns där regler ändrar utfall.
- Konflikter mellan regler är undersökta.
- Saknade fall är markerade som öppna frågor.

### Spårbarhet

- Regler har stabila ID:n där det behövs.
- Exempel kan kopplas till regler.
- Beslut och öppna frågor är synliga.
- Testkoppling finns där den ger värde.
- Samma regel kopieras inte okontrollerat till flera platser.

### Underhållbarhet

- Specifikationen har tydlig struktur.
- Exemplen har relevant information och inte onödigt brus.
- Gamla eller ersatta exempel är markerade eller borttagna.
- Dokumentationen går att uppdatera utan att många artefakter måste ändras.
- Ansvar för uppdatering är tydligt.

### Beslutsmognad

- Det framgår vad som är beslutat.
- Antaganden är markerade.
- Öppna frågor har ägare eller nästa steg.
- Parkerade frågor används inte som implementeringsunderlag.
- Automationskandidater bygger på stabila beslut.

## Vanliga misstag

- **Misstag: Att granska SBE-specifikationer som om de vore traditionella kravdokument.**
  - Varför det händer: Organisationen är van vid formell kravgranskning där fokus ligger på dokumentets fullständighet och godkännande.
  - Hur du undviker det: Granska i stället om regler och exempel skapar gemensam förståelse, minskar tolkningsutrymme och fungerar för både verksamhet och IT.

- **Misstag: Att mäta kvalitet i antal exempel.**
  - Varför det händer: Exempel känns konkreta och lätta att räkna.
  - Hur du undviker det: Bedöm om exemplen täcker rätt variationer, inte om de är många.

- **Misstag: Att automatisera exempel för tidigt.**
  - Varför det händer: Automatisering uppfattas som bevis på mognad.
  - Hur du undviker det: Automatisera först när beteendet är beslutat, observerbart och stabilt nog.

- **Misstag: Att låta verktygsformatet styra kvaliteten.**
  - Varför det händer: Gherkin, Cucumber eller Concordion kan ge en känsla av struktur.
  - Hur du undviker det: Välj format efter läsbarhet, beteendets karaktär och förvaltningsbarhet.

- **Misstag: Att gömma öppna frågor för att specifikationen ska se färdig ut.**
  - Varför det händer: Öppna frågor kan uppfattas som bristande framdrift.
  - Hur du undviker det: Behandla öppna frågor som kvalitetsinformation. De visar var beslut behövs.

## Övningar

### Övning 1: Granska en regel

Utgå från följande regel:

> En utredare ska endast se relevanta ärenden i sökresultatet.

Besvara frågorna:

1. Vilka ord skapar tolkningsutrymme?
2. Vilka verksamhetsregler behöver formuleras tydligare?
3. Vilka exempel behövs för att konkretisera regeln?
4. Vilka öppna frågor bör markeras?
5. Hur skulle du skriva om regeln så att den blir mer granskningsbar?

### Övning 2: Bedöm exempeltäckning

Anta att följande exempel finns för sökbehörighet:

| Exempel-ID | Situation | Förväntat resultat |
|---|---|---|
| SOK-OV-01 | Utredare tillhör ansvarig enhet | Ärendet visas |
| SOK-OV-02 | Utredare är tilldelad ärendet | Ärendet visas |
| SOK-OV-03 | Utredare saknar relation till ärendet | Ärendet visas inte |

Identifiera minst fem saknade variationer som kan vara viktiga i ett brottsutredningsstöd. Markera vilka som är normalfall, undantag, gränsfall eller konfliktfall.

### Övning 3: Skapa granskningsfrågor

Du ska facilitera en kvalitetsgranskning av regler för särskild sekretess.

Ta fram:

1. tre frågor till verksamheten
2. tre frågor till testare
3. tre frågor till utvecklare eller arkitekt
4. två frågor till säkerhet eller juridik
5. en fråga som avgör om något exempel är moget för automation

### Fördjupning

Välj ett kravområde från ditt eget arbete. Gör en lättviktig SBE-kvalitetsgranskning med sex dimensioner:

- begriplighet
- precision
- täckning
- spårbarhet
- underhållbarhet
- beslutsmognad

Skriv ned vilka två förbättringar som skulle ge mest nytta direkt.

## Snabb sammanfattning

- Kvalitet i SBE handlar om användbarhet, inte bara form.
- En bra SBE-specifikation ska fungera för både verksamhet och IT.
- Begriplighet, precision, täckning, spårbarhet, underhållbarhet och beslutsmognad är praktiska kvalitetsdimensioner.
- Fler exempel är inte alltid bättre. Rätt exempel är bättre.
- Regler, exempel, scenarier och beslutstabeller behöver granskas på olika sätt.
- Öppna frågor är inte misslyckanden. De är synliggjord analys.
- Automation kan förstärka kvalitet, men ska inte användas för att dölja oklara beslut.
- Kvalitetssäkring bör leda till konkreta åtgärder, inte bara godkännande.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan en begriplig och en precis SBE-specifikation?
2. Varför kan många exempel göra specifikationen sämre?
3. Hur kan öppna frågor öka kvaliteten i kravdokumentationen?
4. När bör en beslutstabell delas upp i flera mindre tabeller?
5. Vilka risker finns med att automatisera exempel innan beslut är mogna?
6. Hur kan kravanalytikern granska att dokumentationen fungerar både för verksamhet och IT?
7. Vilka kvalitetsdimensioner är viktigast i ett regelområde med hög säkerhetsrisk?

## Koppling till bokens röda tråd

Kvalitetssäkring av SBE handlar inte bara om att hitta fel i texten. Den avgör om specifikationen fortfarande går att använda som gemensam sanning när verksamhetsbeslut, tekniska lösningar och teststrategi förändras. Därför knyter kapitlet ihop dokumentation, exempel, granskning och förvaltning.


## Nästa steg

Nu har vi sett hur SBE-specifikationer kan kvalitetssäkras som dokumentation, gemensam förståelse och grund för test och utveckling. Nästa kapitel går vidare till generella krav i ett SBE-arbetssätt.

Generella krav är ofta svårare att placera än funktionella krav. De gäller inte alltid ett enskilt flöde, utan återkommer över många delar av systemet. I brottsutredningsstödet kan det handla om gemensamma behörighetsprinciper, standardbeteenden, söklogik, notifieringar eller återkommande regler för informationsvisning. Därför behöver de hanteras på ett sätt som bevarar tydlighet utan att skapa onödig upprepning.
