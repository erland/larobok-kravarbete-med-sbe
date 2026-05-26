# Kapitel 9: Exempelworkshops och gemensam förfining

## Varför detta kapitel finns

I de tidigare kapitlen har vi byggt upp hur SBE-dokumentation kan struktureras så att den fungerar för både verksamhet och IT. Vi har sett hur funktionella krav kan formuleras som regler, exempel och scenarier, och hur dokumentationen behöver vara både begriplig och användbar.

Men SBE uppstår inte i dokumentet. SBE uppstår i samtalet.

Det är lätt att tro att Specification by Example främst handlar om att skriva bättre exempel. I praktiken handlar det minst lika mycket om att skapa rätt samtal mellan rätt personer vid rätt tidpunkt. En kravanalytiker som försöker skriva alla exempel själv riskerar att bara byta format på kraven. Resultatet kan se mer modernt ut, men fortfarande bära på samma gamla problem: antaganden, luckor, olika tolkningar och sena upptäckter.

Exempelworkshoppen är därför ett av de viktigaste arbetsmönstren i ett SBE-arbetssätt. Den gör kravarbete mer undersökande, mer konkret och mer gemensamt. I stället för att fråga “vad ska systemet göra?” frågar vi “kan vi beskriva några konkreta fall där detta händer?” och “vad ska gälla i varje fall?”

I det genomgående caset om brottsutredningsstödet blir detta särskilt tydligt. Utredare, förundersökningsledare, testare, utvecklare och arkitekt kan alla förstå ord som “visa relevanta ärenden”, “begränsa åtkomst” eller “markera känslig uppgift”. Men de kan lägga olika betydelse i orden. En exempelworkshop synliggör dessa skillnader innan de blir dyra.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- planera och facilitera en exempelworkshop för funktionella krav i ett SBE-arbetssätt
- välja rätt deltagare och förbereda rätt underlag
- använda konkreta exempel för att upptäcka regler, undantag, öppna frågor och gränsfall
- dokumentera resultatet så att det blir användbart för både verksamhet och IT
- skilja mellan workshopresultat, färdig specifikation och sådant som behöver förfinas vidare
- undvika vanliga fallgropar där workshopen blir antingen för abstrakt, för teknisk eller för lösningsstyrd

## Innan vi börjar

Det här kapitlet bygger på tre tidigare idéer.

För det första: SBE handlar om att skapa gemensam förståelse genom exempel. Exemplet är inte bara en illustration efter att kravet redan är färdigt. Det är ett arbetsredskap för att upptäcka vad kravet egentligen betyder.

För det andra: dokumentationen behöver fungera för både verksamhet och IT. Workshopen måste därför producera material som kan förstås av verksamheten och samtidigt vara tillräckligt precist för utveckling och test.

För det tredje: kravanalytikerns roll förändras. I en exempelworkshop är kravanalytikern inte bara den som samlar in krav. Kravanalytikern designar samtalet, håller fokus, fångar begrepp, stoppar otydlighet och hjälper gruppen att gå från åsikter till konkreta exempel.

## Vad en exempelworkshop är

En exempelworkshop är ett strukturerat arbetsmöte där flera kompetenser tillsammans utforskar ett avgränsat beteende genom konkreta exempel.

Syftet är inte att skriva all dokumentation färdigt under mötet. Syftet är att skapa gemensam förståelse och fånga tillräckligt bra råmaterial för en tydlig SBE-specifikation.

En bra exempelworkshop leder ofta till:

- regler som gruppen är överens om
- konkreta exempel som visar hur reglerna fungerar
- undantag och gränsfall som annars hade missats
- begrepp som behöver definieras tydligare
- öppna frågor som behöver beslut
- antaganden som behöver bekräftas
- testidéer som kan användas senare
- kompletterande kravtext där exempel inte räcker

Det är viktigt att inte mäta workshoppen i antal producerade rader. En workshop som upptäcker tre viktiga tolkningsskillnader kan vara mer värdefull än en workshop som producerar tjugo scenarier utan att någon egentligen är överens.

## När en exempelworkshop passar

Alla krav behöver inte en workshop. En enkel textändring, en tydlig teknisk justering eller ett krav som redan är väl förstått kan ofta hanteras enklare. Exempelworkshoppen är mest värdefull när beteendet är viktigt, regelstyrt eller tolkningskänsligt.

Den passar särskilt bra när:

- flera roller har olika perspektiv på samma funktion
- kravet innehåller verksamhetsregler
- det finns många undantag eller specialfall
- begreppen används olika i organisationen
- tidigare krav har lett till missförstånd
- funktionaliteten är viktig för juridik, säkerhet, spårbarhet eller operativ effektivitet
- teamet behöver besluta vilken nivå av automatisering eller testbarhet som är rimlig
- dokumentationen behöver kunna leva vidare efter införandet

I brottsutredningsstödet kan ett exempel vara funktionen “visa ärenden som utredaren får arbeta med”. Den låter enkel, men kan bero på behörighetsroll, organisatorisk tillhörighet, ärendestatus, sekretessmarkering, jäv, tillfällig delegation och åtkomstloggning. Det är en stark kandidat för en exempelworkshop.

Däremot kan en mindre ändring som “visa versionsnummer i sidfoten” sannolikt dokumenteras utan workshop.

## När en exempelworkshop inte är rätt första steg

En exempelworkshop är inte magisk. Om frågan är för stor, för oklar eller för politisk kan workshopen bli frustrerande. Då behöver man ibland göra förarbete.

En workshop är sällan rätt första steg när:

- målbilden inte är definierad
- rätt beslutsfattare inte kan delta
- deltagarna inte vet vilket arbetsflöde som diskuteras
- frågan egentligen handlar om prioritering, budget eller ansvar
- juridiska eller arkitektoniska ramar saknas
- deltagarna är oense om verksamhetsprocessen på en mer grundläggande nivå
- lösningen redan är låst men konsekvenserna inte är utredda

I sådana lägen kan kravanalytikern behöva börja med processkartläggning, intressentintervjuer, domänmodellering, juridisk analys eller beslut om avgränsning. Exempelworkshoppen fungerar bäst när det finns ett avgränsat beteende att undersöka.

## Välj rätt fokus för workshopen

En vanlig fallgrop är att boka en workshop med ett för brett ämne. “Sök i brottsutredningsstödet” är för stort. “Regler för vilka ärenden som visas i utredarens arbetslista” är mycket bättre.

Ett bra workshopfokus bör vara:

- avgränsat nog att diskuteras på 60 till 120 minuter
- viktigt nog för att flera roller ska behöva förstå det
- konkret nog för att kunna beskrivas med exempel
- öppet nog för att det fortfarande finns något att upptäcka
- kopplat till ett verkligt arbetsflöde eller en verklig beslutspunkt

Ett dåligt workshopfokus blir ofta antingen för abstrakt eller för tekniskt.

För abstrakt:

- “Behörighet i systemet”
- “Sökfunktion”
- “Ärendehantering”
- “Användarvänlighet”

Mer användbart:

- “När en utredare får öppna ett ärende”
- “Vilka träffar som ska visas vid personsökning”
- “När en uppgift ska klassas som känslig i utredningsöversikten”
- “Hur systemet ska hantera flera samtidiga ärendestatusar”

För tekniskt:

- “API-regler för endpointen `/cases/search`”
- “Databasfilter för ärendelistan”
- “Indexeringsstrategi för sökresultat”

Mer användbart:

- “Vilka ärenden en utredare ska se när arbetslistan öppnas”
- “Hur sökresultat ska filtreras när en person förekommer i flera ärenden”
- “Vad användaren ska förstå när en träff är dold av behörighetsskäl”

Det tekniska perspektivet är viktigt, men i en exempelworkshop bör det tekniska normalt stödja förståelsen av beteendet, inte äga samtalet.

## Deltagare och roller

En exempelworkshop behöver tvärfunktionell närvaro. Det betyder inte att alla måste vara med varje gång. Det betyder att de perspektiv som behövs för att förstå beteendet ska finnas i rummet.

I en myndighetskontext kring brottsutredningsstöd kan en workshop ofta behöva följande roller:

- kravanalytiker eller facilitator
- verksamhetsexpert, till exempel erfaren utredare
- beslutsför person, till exempel förundersökningsledare eller produktägare
- testare eller kvalitetssäkringsrepresentant
- utvecklare
- arkitekt eller lösningsansvarig vid behov
- informationssäkerhet, juridik eller dataskydd vid behov
- förvaltning eller systemadministration vid behov

Alla behöver inte tala lika mycket. Men de behöver kunna bidra när deras perspektiv blir relevant.

### Facilitatorn

Facilitatorn äger processen, inte svaret. Ofta är det kravanalytikern som har denna roll.

Facilitatorn ska:

- hålla frågan avgränsad
- se till att exempel blir konkreta
- fånga regler, undantag och öppna frågor
- stoppa diskussioner som blir för tekniska för tidigt
- stoppa diskussioner som blir för abstrakta
- säkerställa att tyst kunskap kommer fram
- sammanfatta beslut och oklarheter
- skilja mellan överenskommet, antaget och oklart

En bra facilitator behöver kunna växla mellan detalj och helhet. När diskussionen blir vag ber facilitatorn om exempel. När exemplen blir för många söker facilitatorn efter regeln bakom exemplen.

### Verksamhetsexperten

Verksamhetsexperten bidrar med domänkunskap. I caset kan det vara en utredare som vet hur ärenden faktiskt hanteras.

Verksamhetsexperten ska inte bara svara på frågor. Personen behöver också reagera på exempel:

- “Det där händer ofta.”
- “Det där är ett specialfall.”
- “Så får vi inte göra juridiskt.”
- “Så uttrycker vi oss inte i verksamheten.”
- “Det där är inte samma sak som ett avslutat ärende.”

Kravanalytikern behöver hjälpa verksamhetsexperten att gå från erfarenhet till uttryckliga regler. Mycket av värdet i en exempelworkshop uppstår när tyst kunskap blir synlig.

### Testaren

Testaren bidrar med frågan: “Hur vet vi att detta fungerar?”

I SBE är testaren inte bara mottagare av krav. Testaren hjälper gruppen att hitta luckor, gränsvärden, negativa fall och motsägande exempel.

Testaren kan fråga:

- Vad händer om förutsättningen nästan är uppfylld?
- Finns det fall där användaren inte ska få resultat?
- Hur ska systemet bete sig när data saknas?
- Hur vet vi att behörighetsregeln inte läcker information?
- Vilka exempel skulle visa att regeln är fel?

Det betyder inte att workshopen ska skriva färdiga testfall. Men testperspektivet gör exemplen skarpare.

### Utvecklaren

Utvecklaren bidrar med realiserbarhet, tekniska konsekvenser och frågor som påverkar design. I en bra workshop hjälper utvecklaren gruppen att upptäcka när ett exempel är tekniskt oklart eller när en regel har konsekvenser för data, integrationer eller systemgränser.

Utvecklaren bör inte få ta över workshopen med implementation för tidigt. Men utvecklarens frågor är ofta avgörande:

- Varifrån kommer informationen?
- Finns denna status i datamodellen?
- Är detta en realtidsregel eller en regel som kan beräknas i efterhand?
- Är detta ett verksamhetsbeslut eller ett tekniskt felhanteringsfall?
- Behöver vi visa att något är dolt, eller ska det inte synas alls?

I brottsutredningsstödet kan en sådan fråga ha stor betydelse. Om en användare saknar behörighet till ett ärende, ska sökningen visa “1 träff dold på grund av behörighet” eller ska träffen inte räknas alls? Det är inte bara teknik. Det är verksamhet, säkerhet, användbarhet och ibland juridik.

### Beslutsför roll

Många workshops producerar frågor som kräver beslut. Om ingen i rummet kan besluta blir workshopen lätt en samling antaganden.

Den beslutsföra rollen behöver inte avgöra allt direkt, men bör kunna:

- bekräfta prioritering
- välja regel när flera alternativ finns
- avgöra när en fråga ska eskaleras
- acceptera att vissa detaljer lämnas till teamet
- tydliggöra vad som är policy och vad som är lösningsval

I caset kan förundersökningsledaren eller produktägaren behöva avgöra hur arbetslistan ska prioritera ärenden när flera kriterier konkurrerar.

## Förberedelse före workshop

En bra exempelworkshop börjar före mötet. Förberedelsen behöver inte vara tung, men den behöver vara tillräcklig.

Kravanalytikern bör förbereda:

- ett tydligt syfte med workshopen
- en avgränsad fråga
- kort bakgrund
- relevanta tidigare krav eller acceptanskriterier
- kända regler och begrepp
- 2 till 4 startsexempel
- kända öppna frågor
- förslag på deltagare
- beslut om dokumentationsformat
- plats för att fånga regler, exempel, frågor och beslut

Startsexemplen är viktiga. De ska inte vara facit. De ska hjälpa gruppen att komma igång.

Ett startsexempel kan vara:

| Fall | Förutsättning | Förväntat resultat |
|---|---|---|
| Utredare tillhör samma utredningsgrupp som ärendet | Ärendet är aktivt och inte särskilt spärrat | Ärendet visas i arbetslistan |
| Utredare tillhör annan grupp | Ingen delegation finns | Ärendet visas inte |
| Utredare har tillfällig delegation | Delegationen är giltig samma dag | Ärendet visas |

Dessa exempel är inte tillräckliga som färdig specifikation. Men de hjälper gruppen att se vilka frågor som behöver diskuteras.

## Workshopens grundstruktur

En exempelworkshop kan genomföras på många sätt, men en enkel struktur fungerar ofta bra:

1. Sätt ramen.
2. Beskriv beteendet som ska utforskas.
3. Samla konkreta exempel.
4. Hitta reglerna bakom exemplen.
5. Leta efter undantag och gränsfall.
6. Fånga öppna frågor.
7. Sammanfatta beslut och nästa steg.
8. Efterbearbeta till specifikation.

Det viktiga är inte att följa en ceremoni. Det viktiga är att röra sig mellan exempel och regel på ett medvetet sätt.

## Steg 1: Sätt ramen

Börja med att klargöra vad workshopen ska och inte ska göra.

Exempel på inledning:

> I dag ska vi utforska vilka ärenden som ska visas i utredarens arbetslista när utredaren loggar in. Vi ska inte lösa hela behörighetsmodellen och inte besluta teknisk implementation. Målet är att få fram regler, exempel, undantag och öppna frågor som kan bli en SBE-specifikation.

En sådan inledning gör tre saker. Den fokuserar arbetet, skyddar gruppen från sidospår och signalerar att resultatet ska bli mer än lösa mötesanteckningar.

Det är också bra att tidigt säga hur materialet ska användas:

- Som underlag för SBE-specifikation.
- Som stöd för utveckling och test.
- Som gemensam dokumentation för verksamhet och IT.
- Som underlag för beslut där frågor fortfarande är öppna.

## Steg 2: Beskriv beteendet utan att lösa allt

Efter ramen behöver gruppen beskriva beteendet på en tillräckligt hög nivå.

Fråga till exempel:

- Vad försöker användaren åstadkomma?
- När i arbetsflödet uppstår behovet?
- Vilket beslut ska systemet hjälpa till med?
- Vad ska vara sant efter att beteendet har utförts?
- Vad är det viktigaste att inte göra fel?

För arbetslistan i brottsutredningsstödet kan gruppen säga:

> När en utredare loggar in ska systemet visa de ärenden som utredaren förväntas arbeta med, utan att visa ärenden som utredaren saknar behörighet till.

Det är en start, men inte en specifikation. Nu behöver gruppen konkretisera.

## Steg 3: Samla konkreta exempel

När beteendet är beskrivet börjar exemplen.

Facilitatorn kan fråga:

- Kan vi ta ett vanligt fall?
- Kan vi ta ett fall där användaren inte ska få åtkomst?
- Kan vi ta ett gränsfall?
- Kan vi ta ett fall som brukar skapa missförstånd?
- Kan vi ta ett fall där två regler krockar?

Ett användbart sätt är att skriva exemplen i enkel tabellform innan man väljer mer formellt format.

| Exempel | Situation | Förväntat resultat |
|---|---|---|
| E1 | Utredaren är tilldelad ärendet och ärendet är aktivt | Ärendet visas i arbetslistan |
| E2 | Utredaren tillhör samma grupp men är inte tilldelad ärendet | Ärendet visas inte om gruppåtkomst saknas |
| E3 | Utredaren har giltig delegation från ansvarig grupp | Ärendet visas med markering om delegation |
| E4 | Delegationen gick ut i går | Ärendet visas inte |
| E5 | Ärendet är spärrat på grund av särskild sekretess | Ärendet visas inte, även om utredaren är tilldelad |
| E6 | Utredaren är förundersökningsledare för ärendet | Ärendet visas även om utredaren inte är handläggare |

Tabellen visar snabbt att “visa ärenden” inte är en enda regel. Den består av flera regler som behöver prioriteras.

## Steg 4: Hitta reglerna bakom exemplen

När exemplen finns på bordet är nästa fråga: vilka regler verkar styra dem?

Utifrån exemplen ovan kan gruppen börja formulera regler:

- En utredare ska se aktiva ärenden där utredaren är tilldelad som handläggare.
- En utredare ska se ärenden där utredaren har giltig delegation.
- En förundersökningsledare ska se ärenden där personen är ansvarig beslutsfattare.
- Särskild sekretess ska begränsa visning även om andra åtkomstregler är uppfyllda.
- Utgången delegation ska inte ge åtkomst.
- Ärenden som inte visas på grund av behörighet ska inte exponera känslig information.

Nu blir det möjligt att diskutera ordning och prioritet. Om en användare både är tilldelad och ärendet är spärrat, vilken regel vinner? I många verksamheter är detta den typ av fråga som annars upptäcks sent.

## Steg 5: Leta efter undantag och gränsfall

När gruppen har de första reglerna ska facilitatorn inte avsluta för snabbt. Bra SBE-workshops stannar upp och letar efter undantag.

Frågor som ofta fungerar:

- Finns det fall där regeln inte ska gälla?
- Vad händer när information saknas?
- Vad händer om två roller gäller samtidigt?
- Vad händer om status ändras under dagen?
- Finns det tidsgränser?
- Finns det manuella beslut som överstyr regeln?
- Vad får användaren veta när något inte visas?
- Behöver systemet logga att något kontrollerades?
- Finns det skillnad mellan att se att ett ärende finns och att öppna ärendet?

För brottsutredningsstödet kan gränsfallen vara mer verksamhetskritiska än normalfallen. Till exempel:

| Gränsfall | Fråga |
|---|---|
| Utredaren byter organisatorisk placering under dagen | Ska arbetslistan uppdateras direkt eller nästa inloggning? |
| Ärendet spärras efter att utredaren redan öppnat det | Ska åtkomsten brytas direkt? |
| Delegationen saknar slutdatum | Är den giltig eller ogiltig? |
| Ärendet förekommer i sökindex men användaren saknar åtkomst | Ska träffen döljas helt? |
| Användaren har roll i ärendet men är registrerad som jävig | Ska jäv alltid överstyra rollbaserad åtkomst? |

Det är ofta här SBE visar sitt värde. Traditionell kravtext har en tendens att beskriva normalfallet. Exempelworkshoppen gör det lättare att hitta det som faktiskt skapar risk.

## Steg 6: Fånga öppna frågor utan att tappa tempo

Alla frågor ska inte lösas i workshopen. Om gruppen försöker lösa allt direkt kan workshopen stanna.

Facilitatorn bör därför ha en tydlig plats för öppna frågor. Frågor ska fångas med ägare och nästa steg.

Exempel:

| Öppen fråga | Varför den är viktig | Ägare | Nästa steg |
|---|---|---|---|
| Ska dold träff räknas i antal sökresultat? | Påverkar både användbarhet och informationssäkerhet | Produktägare och säkerhetsansvarig | Beslut före nästa förfining |
| Hur snabbt ska spärrad åtkomst slå igenom? | Påverkar arkitektur och risk | Arkitekt | Ta fram alternativ |
| Är delegation utan slutdatum tillåten? | Påverkar regel och datavalidering | Verksamhetsexpert | Kontrollera riktlinje |
| Ska jäv blockera även förundersökningsledare? | Påverkar juridik och ansvar | Jurist | Utred regelverk |

Det viktiga är att inte gömma osäkerhet. En SBE-specifikation ska inte låtsas vara färdig när centrala frågor saknar beslut.

## Steg 7: Sammanfatta beslut och nästa steg

Avsluta workshopen med en kort sammanfattning. Det är lätt att gruppen tror att alla hört samma sak, men sammanfattningen avslöjar ofta kvarvarande skillnader.

Sammanfatta:

- vilka regler gruppen verkar vara överens om
- vilka exempel som ska tas vidare
- vilka frågor som är öppna
- vilka beslut som behövs
- vem som gör efterbearbetningen
- när gruppen ska granska specifikationen

Exempel på avslut:

> Vi har identifierat fyra huvudregler för arbetslistan: tilldelning, delegation, ansvarig beslutsfattare och särskild sekretess. Vi är överens om att särskild sekretess överstyr övriga regler. Vi har öppna frågor om dolda sökträffar, omedelbar åtkomstbrytning och delegation utan slutdatum. Kravanalytikern tar fram en första SBE-specifikation till torsdag. Produktägare, testare och utvecklare granskar exemplen före nästa förfining.

Detta är enkelt, men kraftfullt. Det gör workshopen till en del av ett arbetsflöde, inte bara ett möte.

## Efterbearbetning: från workshopmaterial till specifikation

Efter workshopen behöver materialet städas. Råa workshopanteckningar är sällan bra dokumentation. De kan vara röriga, dubblerade och innehålla både beslut, gissningar och sidokommentarer.

Efterbearbetningen bör göra fyra saker:

1. Strukturera materialet.
2. Skilja beslut från öppna frågor.
3. Formulera regler och exempel tydligt.
4. Kontrollera att dokumentationen fungerar för både verksamhet och IT.

En möjlig struktur är:

- Syfte och omfattning.
- Begrepp som används.
- Regler.
- Exempel.
- Scenarier eller tabeller.
- Öppna frågor.
- Avgränsningar.
- Koppling till test och implementation.

För arbetslistan kan den färdiga specifikationsdelen börja så här:

> Denna specifikation beskriver vilka ärenden som ska visas i en utredares arbetslista när utredaren loggar in i brottsutredningsstödet. Syftet är att arbetslistan ska visa ärenden som användaren har ett aktivt ansvar för eller giltig delegation till, utan att exponera ärenden som begränsas av särskild sekretess eller annan åtkomstspärr.

Sedan kan reglerna formuleras:

| Regel | Beskrivning |
|---|---|
| R1 | Ett aktivt ärende visas om utredaren är tilldelad som handläggare |
| R2 | Ett ärende visas om utredaren har en giltig delegation för ärendet |
| R3 | Ett ärende visas om användaren är registrerad som ansvarig förundersökningsledare |
| R4 | Särskild sekretess överstyr R1, R2 och R3 om inte särskilt beslut om åtkomst finns |
| R5 | Utgången delegation ger inte åtkomst |
| R6 | Systemet ska inte exponera ärendets identitet i arbetslistan när användaren saknar åtkomst |

Därefter kan exemplen kopplas till reglerna.

| Exempel | Regler | Förutsättning | Förväntat resultat |
|---|---|---|---|
| E1 | R1 | Utredaren är tilldelad ett aktivt ärende utan spärr | Ärendet visas |
| E2 | R2 | Utredaren har giltig delegation till aktivt ärende | Ärendet visas |
| E3 | R5 | Utredaren hade delegation som löpte ut föregående dag | Ärendet visas inte |
| E4 | R4 | Utredaren är tilldelad ärendet men ärendet har särskild sekretess | Ärendet visas inte utan särskilt åtkomstbeslut |
| E5 | R3 | Användaren är ansvarig förundersökningsledare | Ärendet visas |
| E6 | R6 | Användaren saknar åtkomst till ärende som matchar annat filter | Ärendet exponeras inte i arbetslistan |

Detta är mer användbart än en lista med acceptanskriterier eftersom det visar relationen mellan regel och exempel. Det gör också granskningen enklare. Verksamheten kan kontrollera om exemplen är rimliga. IT kan se vilka regler som behöver implementeras och testas.

## Workshopformat: exempel mapping

Ett vanligt och användbart arbetssätt i SBE är att använda en enkel uppdelning mellan regler, exempel, frågor och eventuellt berättelse eller story. Detta kallas ofta example mapping.

Poängen är inte tavlans färger eller formatet i sig. Poängen är att separera olika typer av information:

- Regler beskriver vad som ska gälla.
- Exempel visar konkreta fall där reglerna tillämpas.
- Frågor visar vad gruppen ännu inte vet.
- Story eller funktion beskriver vilket beteende som utforskas.

I ett digitalt eller fysiskt rum kan man arbeta med fyra ytor:

| Yta | Innehåll |
|---|---|
| Funktion eller story | Det beteende gruppen utforskar |
| Regler | Påståenden om vad som ska gälla |
| Exempel | Konkreta fall som visar reglerna |
| Frågor | Oklarheter, beslut och antaganden |

För brottsutredningsstödet kan ytorna fyllas så här:

| Typ | Innehåll |
|---|---|
| Funktion | Visa utredarens arbetslista |
| Regel | Särskild sekretess överstyr normal tilldelning |
| Exempel | Utredare är tilldelad men ärendet är sekretesspärrat |
| Fråga | Vem kan fatta särskilt åtkomstbeslut? |

Det här formatet är särskilt bra när gruppen annars blandar allt i samma diskussion. Det gör det synligt om man har många exempel men få regler, eller många regler men nästan inga konkreta exempel.

## Workshopformat: beslutstabell

Ibland är en beslutstabell bättre än scenarier. Det gäller särskilt när flera villkor kombineras och ger olika resultat.

Arbetslistan kan till exempel beskrivas med villkor:

| Tilldelad | Giltig delegation | Ansvarig FL | Särskild sekretess | Förväntat resultat |
|---|---|---|---|---|
| Ja | Nej | Nej | Nej | Visa ärende |
| Nej | Ja | Nej | Nej | Visa ärende |
| Nej | Nej | Ja | Nej | Visa ärende |
| Ja | Nej | Nej | Ja | Visa inte utan särskilt beslut |
| Nej | Nej | Nej | Nej | Visa inte |
| Nej | Ja | Nej | Ja | Visa inte utan särskilt beslut |

En beslutstabell hjälper gruppen att se kombinationer. Den avslöjar också om vissa kombinationer saknas.

Men beslutstabeller har en risk: de kan bli mekaniska och svåra att läsa om de växer för mycket. Därför bör de ofta kompletteras med korta förklaringar och några namngivna exempel.

## Workshopformat: tidslinje eller flöde

Vissa krav handlar inte främst om en regelmatris utan om ordning över tid. Då kan workshopen behöva följa ett flöde.

Exempel:

- Ett ärende skapas.
- Utredare tilldelas.
- Uppgift klassas som känslig.
- Förundersökningsledare fattar beslut.
- Delegation ges.
- Delegation löper ut.
- Ärendet avslutas.
- Arkivering påbörjas.

Vid sådana krav kan facilitatorn fråga:

- Vad kan hända först?
- Vad får inte hända före ett beslut?
- Vilka statusar finns?
- Vad ska systemet göra vid övergång mellan statusar?
- Vilka roller får initiera övergången?
- Vilka händelser ska loggas?

Detta kan senare bli en kombination av tillståndsregler, exempel och scenarier.

## Frågeteknik för att få fram bra exempel

Kvaliteten på exemplen beror ofta på kvaliteten på frågorna. Erfarna kravanalytiker kan vinna mycket på att byta några klassiska kravfrågor mot mer exempelorienterade frågor.

I stället för:

> Vilka krav har ni på arbetslistan?

Fråga:

> Kan vi ta tre konkreta situationer där arbetslistan måste visa rätt ärenden?

I stället för:

> Ska användaren kunna söka på personnummer?

Fråga:

> Kan vi ta ett exempel där sökning på personnummer ska ge träff, och ett exempel där den inte ska göra det?

I stället för:

> Vilka behörighetsregler gäller?

Fråga:

> Kan vi ta ett fall där användaren ska få se ärendet trots att den inte är handläggare, och ett fall där användaren inte ska få se ärendet trots att den är kopplad till ärendet?

Andra användbara frågor:

- Vad är det vanligaste fallet?
- Vad är det mest riskfyllda fallet?
- Vad brukar nya användare missförstå?
- Vad brukar systemet behöva göra annorlunda än en människa?
- Vad skulle vara ett felaktigt resultat?
- Vilket exempel skulle få er att säga “nej, så får systemet absolut inte göra”?
- Finns det ett fall där verksamheten och IT brukar tolka regeln olika?
- Om vi automatiserade ett test för detta, vilket exempel skulle ge mest värde?

Frågorna leder bort från abstrakta kravformuleringar och in i beteende.

## Dokumentera under workshopen

Under workshopen behöver någon dokumentera synligt. Helst ska gruppen kunna se materialet växa fram. Det minskar risken för att kravanalytikern efteråt råkar tolka om samtalet.

Synlig dokumentation kan göras i en digital whiteboard, i ett dokument, i ett ärendehanteringsverktyg eller i ett enklare tabellformat. Verktyget är mindre viktigt än tydligheten.

Dokumentationen under mötet bör inte vara för polerad. Den ska fånga:

- regler
- exempel
- undantag
- frågor
- beslut
- begrepp
- antaganden
- parkerade sidospår

Det är bra att märka materialet direkt:

- “Beslut”
- “Antagande”
- “Öppen fråga”
- “Exempel”
- “Begrepp”
- “Utanför scope”

Det hjälper efterbearbetningen.

## Från workshop till backlog

I många organisationer behöver workshopresultatet kopplas till backlogg, ärenden eller kravobjekt. Här är det viktigt att inte förlora SBE-tanken.

Ett vanligt misstag är att varje exempel blir ett separat backloggobjekt. Då splittras helheten. Ett annat misstag är att allt klumpas ihop i en stor kravtext. Då försvinner precisionen.

Ett mer hållbart mönster är:

- Backloggobjektet beskriver vilket beteende eller vilken förmåga som ska utvecklas.
- SBE-specifikationen beskriver regler och exempel.
- Öppna frågor spåras som beslutspunkter eller utredningsuppgifter.
- Testidéer kopplas till specifikationen, men skrivs inte alltid som separata krav.
- Förändringar i regler uppdateras i den levande dokumentationen.

För arbetslistan kan backloggobjektet vara:

> Som utredare vill jag se de ärenden som jag ansvarar för eller har giltig delegation till, så att jag snabbt kan fortsätta mitt arbete utan att exponeras för ärenden jag saknar behörighet till.

SBE-specifikationen innehåller sedan reglerna och exemplen. Backloggtexten ensam är inte tillräcklig.

## Facilitering i myndighetsmiljö

Myndighetsmiljöer kan innebära särskilda utmaningar för exempelworkshops. Det kan finnas starka formella processer, många intressenter, juridiska begränsningar och hög känslighet kring information.

Det påverkar faciliteringen.

För det första behöver avgränsningen vara tydlig. Om workshopen blandar verksamhetsprocess, juridik, teknik, informationssäkerhet och organisatoriskt ansvar utan struktur blir den snabbt tung.

För det andra behöver man vara noga med exempeldata. Fiktiva exempel ska vara realistiska men inte innehålla verkliga personuppgifter eller känsliga uppgifter.

För det tredje behöver beslut och antaganden dokumenteras tydligt. I en myndighetskontext är det extra viktigt att kunna se varför en regel gäller och vem som har bekräftat den.

För det fjärde behöver gruppen skilja mellan verksamhetsregel och systemregel. Ibland är systemet bara ett stöd för en regel som finns i lag, föreskrift, riktlinje eller lokal process. Ibland skapar systemet ett nytt beteende genom sin design.

Exempel:

| Påstående | Typ | Kommentar |
|---|---|---|
| En användare utan åtkomst ska inte kunna öppna ett sekretessmarkerat ärende | Verksamhets- och säkerhetsregel | Behöver förankras i regelverk och säkerhetsprincip |
| Systemet ska visa en gul ikon för ärenden med delegation | Systemregel eller lösningsval | Kan ändras utan att verksamhetsregeln ändras |
| Delegation ska ha startdatum och slutdatum | Verksamhetsregel och datakrav | Påverkar både process och system |
| Systemet ska uppdatera arbetslistan var femte minut | Lösnings- och kvalitetsbeslut | Kan bero på prestanda och arkitektur |

Den här sorteringen hjälper gruppen att inte låsa fel sak.

## Hantera konflikter och olika tolkningar

Exempelworkshops gör oenighet synlig. Det är bra, men kan också vara obekvämt.

Typiska konflikter är:

- Verksamheten vill ha flexibilitet, IT behöver entydiga regler.
- Säkerhet vill minimera exponering, användare vill förstå varför något saknas.
- Test vill ha tydliga förväntade resultat, verksamheten vill behålla bedömningsutrymme.
- Produktägare vill hålla scope, specialister vill fånga alla undantag.
- Arkitektur vill ha generella mönster, verksamheten vill lösa ett akut problem.

Facilitatorn ska inte låtsas att konflikterna inte finns. Men facilitatorn ska hjälpa gruppen att formulera konflikten som beslut.

Exempel:

> Vi har två möjliga regler. Antingen döljer vi helt att det finns ett ärende som användaren saknar åtkomst till, eller så visar vi att det finns dold information. Det är ett beslut mellan informationssäkerhet och användarstöd. Vi behöver ägare och beslutskriterier.

Genom att formulera konflikten som val med konsekvenser blir diskussionen mer produktiv.

## Få rätt detaljnivå

En workshop kan fastna på fel detaljnivå.

För grov nivå:

> Användaren ska bara se relevanta ärenden.

Det är inte tillräckligt. Vad betyder relevant?

För detaljerad nivå:

> När användaren klickar på knappen ska frontend anropa endpoint X, backend ska filtrera på tabell Y, och resultatet ska serialiseras i format Z.

Det kan vara viktigt senare, men det är inte verksamhetsbeteendet.

Rätt nivå för SBE ligger ofta här:

> Ett ärende visas i arbetslistan när användaren är tilldelad ärendet, ärendet är aktivt och ingen åtkomstspärr gäller.

Sedan konkretiseras detta med exempel.

Ett enkelt test för detaljnivå är att fråga:

- Kan verksamheten förstå och bekräfta detta?
- Kan IT använda det för design och test?
- Beskriver det beteende snarare än implementation?
- Är det tillräckligt konkret för att minska tolkningsutrymme?
- Kan det underhållas när systemet förändras?

Om svaret är ja ligger specifikationen ofta på rätt nivå.

## Vad som ska vara klart efter workshopen

Efter en bra exempelworkshop behöver inte allt vara färdigt. Men det bör vara tydligt vad som är klart och vad som återstår.

Miniminivå efter en workshop:

- Avgränsat beteende är tydligt.
- Centrala regler är identifierade.
- Flera konkreta exempel finns.
- Viktiga undantag är fångade.
- Öppna frågor har ägare.
- Nästa steg är bestämt.

Mognare nivå efter efterbearbetning:

- Reglerna är formulerade i dokumentationsstruktur.
- Exemplen är rensade och namngivna.
- Begrepp är definierade.
- Scenarier eller beslutstabeller är valda där de passar.
- Öppna frågor är separerade från färdig specifikation.
- Specifikationen har granskats av minst verksamhet, test och utveckling.

Det är bättre att ha en tydlig ofärdig specifikation än en otydlig “klar” specifikation.

## Vanliga misstag

- **Misstag: Workshopen börjar med dokumentformatet.**
  - Varför det händer: Teamet vill snabbt komma till Gherkin, mallar eller verktyg.
  - Hur man undviker det: Börja med beteende, regler och exempel. Välj format när förståelsen finns.

- **Misstag: Kravanalytikern skriver exemplen själv efter intervjuer.**
  - Varför det händer: Det känns effektivare och mindre krävande än gemensamma workshops.
  - Hur man undviker det: Använd intervjuer som förberedelse, men låt viktiga exempel granskas gemensamt.

- **Misstag: För många deltagare bjuds in utan tydlig roll.**
  - Varför det händer: Man vill vara inkluderande eller undvika att missa någon.
  - Hur man undviker det: Bjud in perspektiv, inte publik. Dela hellre upp arbetet i flera fokuserade workshops.

- **Misstag: Gruppen diskuterar lösning för tidigt.**
  - Varför det händer: Utvecklare och arkitekter ser snabbt tekniska konsekvenser.
  - Hur man undviker det: Parkera implementation tills beteendet är tydligt, men fånga tekniska risker som frågor.

- **Misstag: Workshopen producerar exempel men inga regler.**
  - Varför det händer: Gruppen fastnar i enskilda fall.
  - Hur man undviker det: Fråga regelbundet: “Vilken regel visar detta exempel?”

- **Misstag: Workshopen producerar regler men inga exempel.**
  - Varför det händer: Deltagarna är vana vid abstrakt kravspråk.
  - Hur man undviker det: Be alltid om minst ett vanligt fall, ett undantag och ett gränsfall.

- **Misstag: Öppna frågor skrivs som om de vore beslutade krav.**
  - Varför det händer: Man vill att dokumentationen ska se färdig ut.
  - Hur man undviker det: Märk frågor, antaganden och beslut tydligt.

- **Misstag: Dokumentationen efteråt blir för teknisk för verksamheten.**
  - Varför det händer: Materialet översätts direkt till testfall eller implementation.
  - Hur man undviker det: Behåll verksamhetsspråk och koppla tekniska detaljer separat.

- **Misstag: Dokumentationen efteråt blir för verksamhetsnära för IT.**
  - Varför det händer: Man vill undvika tekniska detaljer helt.
  - Hur man undviker det: Lägg till regler, förväntade resultat, datavillkor och testbara exempel.

## Övningar

### Övning 1: Planera en exempelworkshop

Utgå från funktionen “utredaren ska kunna söka efter personer som förekommer i ett ärende”.

Ta fram:

- workshopens syfte
- avgränsning
- vilka roller som ska delta
- 3 startsexempel
- 3 frågor du vill att workshopen ska besvara
- 2 risker med workshopen

Fundera särskilt på hur du undviker att workshopen blir en allmän diskussion om hela sökfunktionen.

### Övning 2: Hitta regler bakom exempel

Du har följande exempel:

| Exempel | Situation | Förväntat resultat |
|---|---|---|
| E1 | Utredare söker på personnummer i eget aktiva ärende | Personen visas |
| E2 | Utredare söker på personnummer i ärende från annan grupp | Personen visas inte |
| E3 | Utredare har delegation till annat ärende | Personen visas |
| E4 | Personen är skyddad och ärendet saknar särskilt åtkomstbeslut | Personen visas inte |
| E5 | Personen är skyddad men åtkomstbeslut finns | Personen visas med särskild markering |

Skriv de regler som exemplen antyder. Markera också minst två öppna frågor.

### Övning 3: Välj dokumentationsform

Välj ett av följande områden:

- arbetslista
- personsökning
- delegation
- spärrade ärenden
- klassning av känslig uppgift

Bestäm om du skulle börja dokumentera området med:

- fria exempel
- beslutstabell
- scenarier
- flöde eller tidslinje
- kombination av flera format

Motivera valet utifrån både verksamhetens läsbarhet och IT:s behov av precision.

### Fördjupning

Planera en workshopserie för ett större område i brottsutredningsstödet, till exempel “åtkomst och behörighet”. Dela upp området i 3 till 5 fokuserade workshops. För varje workshop, ange syfte, deltagare och förväntat resultat.

## Snabb sammanfattning

- En exempelworkshop är ett strukturerat samtal där flera roller utforskar ett avgränsat beteende genom konkreta exempel.
- Workshopen är mest värdefull när kravet innehåller regler, undantag, tolkningsrisker eller flera perspektiv.
- Kravanalytikerns roll är att facilitera gemensam förståelse, inte att själv producera alla exempel.
- Bra workshops växlar mellan exempel och regler.
- Öppna frågor ska fångas tydligt och inte maskeras som beslutade krav.
- Dokumentationen efteråt behöver städas så att den fungerar för både verksamhet och IT.
- Workshopens resultat är inte bara mötesanteckningar, utan råmaterial för levande SBE-dokumentation.

## Quiz och reflektionsfrågor

1. Varför räcker det inte att kravanalytikern själv skriver exempel efter en intervju?
2. Vilka typer av krav eller beteenden lämpar sig bäst för exempelworkshops?
3. Vilken roll har testaren i en exempelworkshop?
4. Hur kan facilitatorn upptäcka att gruppen ligger på för abstrakt nivå?
5. Varför bör öppna frågor separeras tydligt från beslutade regler?
6. När är en beslutstabell mer användbar än scenarier?
7. Vilka risker finns om workshopen blir för teknisk för tidigt?
8. Hur kan dokumentationen efter workshopen göras användbar för både verksamhet och IT?

## Koppling till bokens röda tråd

Exempelworkshopen är där bokens dokumentationsprinciper blir social praktik. Den hjälper gruppen att hitta skillnaden mellan det man tror är överenskommet och det som faktiskt är specificerat. Resultatet ska därför inte bara vara mötesanteckningar, utan förbättrade regler, exempel, öppna frågor och beslut.


## Nästa steg

I nästa kapitel går vi närmare in på mer verktygsnära format och automatiseringsmöjligheter. Vi ska titta på Gherkin, Cucumber och Concordion, och diskutera när dessa format hjälper SBE-arbetet och när de riskerar att styra samtalet för mycket.

Det är en viktig fortsättning på detta kapitel. En exempelworkshop ska inte börja i verktyget, men om gruppen har bra regler och exempel kan vissa delar senare uttryckas i ett format som också kan användas för automatiserade tester eller körbar dokumentation.
