import streamlit as st

def average_TF(scores):
    # Selecteer de scores voor vraag 1, vraag 3 en vraag 5
    selected_scores = [scores[0], scores[8], scores[16], scores[24], scores[32]]
    # Bereken het gemiddelde
    average = sum(selected_scores) / len(selected_scores)
    return average

def average_AM(scores):
    selected_scores_2 = [scores[1], scores[9], scores[17], scores[25], scores[33]]
    average = sum(selected_scores_2)/ len(selected_scores_2)
    return average

def average_AU(scores):
    selected_scores_3 = [scores[2], scores[10], scores[18], scores[26], scores[34]]
    average = sum(selected_scores_3)/len(selected_scores_3)
    return average

def average_ZE(scores):
    selected_scores_4 = [scores[3], scores[11], scores[19], scores[27], scores[35]]
    average = sum(selected_scores_4)/len(selected_scores_4)
    return average

def average_OC(scores):
    selected_scores_5 = [scores[4], scores[12], scores[20], scores[28], scores[36]]
    average = sum(selected_scores_5)/len(selected_scores_5)
    return average

def average_DV(scores):
    selected_scores_6 = [scores[5], scores[13], scores[21], scores[29], scores[37]]
    average = sum(selected_scores_6)/len(selected_scores_6)
    return average

def average_UI(scores):
    selected_scores_7 = [scores[6], scores[14], scores[22], scores[30], scores[38]]
    average = sum(selected_scores_7)/len(selected_scores_7)
    return average

def average_LS(scores):
    selected_scores_4 = [scores[7], scores[15], scores[23], scores[31], scores[39]]
    average = sum(selected_scores_4)/len(selected_scores_4)
    return average

def main():
    st.title("Loopbaanankers van Scheinn")

    # Vragenlijst
    st.header("Vragenlijst")
    st.write("0 = is nooit van toepassing")
    st.write("1 = is zo nu en dan van toepassing")
    st.write("2 = is soms van toepassing")
    st.write("3 = is regelmatig van toepassing")
    st.write("4 = is vaak van toepassing")
    st.write("5 = is bijna altijd van toepassing")
    st.write("6 = is altijd van toepassing")
    questions = [
"1. Ik droom ervan zo goed te zijn in wat ik doe dat er voortdurend om mijn deskundige advies wordt gevraagd",
"2. Ik heb de meeste voldoening van mijn werk wanneer ik de inspanningen van anderen heb kunnen verenigen en managen.",
"3. Ik droom ervan een loopbaan te hebben waarin ik vrij ben een taak op mijn eigen manier en volgens mijn eigen schema uit te voeren.",
"4. Ik vind zekerheid en stabiliteit belangrijker dan vrijheid en autonomie.",
"5. Ik ben altijd op zoek naar ideeën waardoor ik mijn eigen bedrijf zou kunnen beginnen.",
"6. Alleen als ik het gevoel heb een daadwerkelijke bijdrage geleverd te hebben aan het maatschappelijk welzijn, voel ik mij geslaagd in mijn loopbaan. ",
"7. Ik droom van een loopbaan waarin ik problemen kan oplossen of zeer uitdagende situaties het hoofd kan bieden. ",
"8. Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een baan te accepteren die het mij onmogelijk maakt persoonlijke en gezinszaken na te streven.",
"9. Ik voel me alleen geslaagd in mijn loopbaan als ik mijn technische of functionele vaardigheden tot een zeer hoog competentieniveau kan ontwikkelen. ",
"10. Ik droom ervan aan het hoofd te staan van een complexe organisatie en beslissingen te nemen die veel mensen beïnvloeden. ",
"11. Ik heb de meeste voldoening van mijn werk wanneer ik volledig vrij ben in het bepalen van mijn eigen taken, schema’s en procedures. ",
"12. Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een taak te accepteren die mijn zekerheid in de organisatie in gevaar zou brengen.",
"13. Ik vind het opbouwen van mijn eigen bedrijf belangrijker dan het bereiken van een hoge managementpositie in de organisatie van iemand anders.",
"14. Ik heb de meeste voldoening van mijn werk wanneer ik mijn talenten in dienst van anderen heb kunnen gebruiken.",
"15. Ik voel me alleen geslaagd in mijn loopbaan als ik te maken heb met zeer moeilijke uitdagingen en deze het hoofd kan bieden.",
"16. Ik droom van een loopbaan waarin ik mijn persoonlijke, gezins-, en arbeidsbehoeften kan verenigen.",
"17. Ik vind het aantrekkelijker een hogere functionele manager op mijn competentieterrein te worden dan een algemeen manager. ",
"18.	Ik voel me alleen geslaagd in mijn loopbaan als ik algemeen manager in een organisatie word.",
"19.	Ik voel me alleen geslaagd in mijn loopbaan als ik volledige autonomie en vrijheid verwerf.",
"20.	Ik zoek een baan in een organisatie die mij een gevoel van zekerheid en stabiliteit geeft.",
"21.	Ik heb de meeste voldoening van mijn werk wanneer ik iets heb kunnen opbouwen wat volledig het resultaat is van mijn eigen ideeën en inspanningen.",
"22.	Ik vind het belangrijker mijn vaardigheden te gebruiken om de wereld aantrekkelijker te maken om in te wonen en te werken dan een hoge managementpositie te bereiken.",
"23.	Ik heb de meeste voldoening van mijn werk wanneer ik ogenschijnlijk onoplosbare problemen heb opgelost of ogenschijnlijk onmogelijke tegenslagen heb overwonnen.",
"24.	Ik voel me alleen geslaagd in mijn leven als ik mijn persoonlijke-, gezins- en loopbaaneisen met elkaar in evenwicht kan brengen.",
"25.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een taakroulatie te accepteren waardoor ik mijn competentieterrein zou moeten verlaten.",
"26.	Ik vind het aantrekkelijker algemeen manager te worden dan een hogere functionele manager op mijn huidige competentieterrein.",
"27.	Een taak op mijn eigen manier doen, vrij van regels en beperkingen, vind ik belangrijker dan zekerheid.",
"28.	Ik heb de meeste voldoening van mijn werk wanneer ik weet dat ik volledige financiële zekerheid heb en zeker ben van mijn baan.",
"29.	Ik voel me alleen geslaagd in mijn loopbaan als het me gelukt is iets te creëren of op te bouwen wat volledig mijn eigen product of idee is.",
"30.	Ik droom van een loopbaan die daadwerkelijk een bijdrage levert aan de mensheid en de maatschappij.",
"31.	Ik zoek naar kansen op het werk die in sterke mate een uitdaging vormen voor mijn probleemoplossende en/of prestatiegerichte vaardigheden.",
"32.	Ik vind het belangrijker de eisen van mijn persoonlijke en beroepsleven met elkaar in evenwicht te brengen dan een hoge managementpositie te bereiken.",
"33.	Ik heb de meeste voldoening van mijn werk wanneer ik mijn speciale vaardigheden en talenten kan gebruiken.",
"34.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een baan te accepteren waardoor ik van het algemeen managementspoor zou afdwalen.",
"35.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een baan te accepteren waardoor mijn autonomie en vrijheid zouden verminderen.",
"36.	Ik droom van een loopbaan waarin ik een gevoel van zekerheid en stabiliteit ervaar.",
"37.	Ik droom ervan mijn eigen bedrijf te beginnen en op te bouwen.",
"38.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een taak te accepteren waardoor ik anderen minder goed van dienst zou kunnen zijn.",
"39.	Ik vind het belangrijker aan vrijwel onoplosbare problemen te werken dan een hoge managementpositie te bereiken.",
"40.	Ik heb altijd gezocht naar werk dat zo min mogelijk invloed heeft op mijn persoonlijke of gezinszaken."
]
    answers = []
    for question in questions:
        answer = st.slider(question, 0, 6, step=1)
        answers.append(answer)


    # Bereken en toon uitslag
    st.header("Scores")
    average = average_TF(answers)
    st.write(f"Technisch Functioneel: {average:.2f}")
    average2 = average_AM(answers)
    st.write(f"Algemeen Management: {average2:.2f}")
    average3 = average_AU(answers)
    st.write(f"Autonomie/onafhankelijkheid: {average3:.2f}")
    average4 = average_ZE(answers)
    st.write(f"Zekerheid/stabiliteit: {average4:.2f}")
    average5 = average_OC(answers)
    st.write(f"Ondernemingsgerichte creativiteit: {average5:.2f}")
    average6 = average_DV(answers)
    st.write(f"Gevoel van dienstverlening, toewijding aan de zaak: {average6:.2f}")
    average7 = average_UI(answers)
    st.write(f"Zuivere uitdaging: {average7:.2f}")
    average8 = average_LS(answers)
    st.write(f"Levensstijl: {average8:.2f}")

    st.header("Rangschikking")
    scores = {
        "Technisch Functioneel": {"gemiddelde": average, 
                                "uitleg": "Als je loopbaanankercompetentie op een technisch of functioneel terrein is, wil je niet de mogelijkheid opgeven je vaardigheden op dat terrein toe te passen en die vaardigheden steeds verder te ontwikkelen naar een steeds hoger niveau. Je ontleent je gevoel van identiteit aan het uitoefenen van je vaardigheden en je bent het gelukkigst wanneer je door je werk op deze terreinen uitgedaagd wordt. Je bent misschien bereid anderen op jouw technische of functionele terrein te managen, maar je bent niet geïnteresseerd in management om het management en je bent geneigd het algemeen management te mijden omdat je dan je eigen competentieterrein zou moeten verlaten. Je vragenlijstscore op dit terrein staat in de eerste kolom van het scoreblad onder TF."},
        "Algemeen Management": {"gemiddelde": average2,
                                "uitleg": "Als je loopbaananker algemeen-managementcompetentie is, wil je niet de mogelijkheid opgeven tot een zo hoog mogelijk niveau in een organisatie op te klimmen waardoor je de inspanningen voor anderen in verschillende functies kunt verenigen en verantwoordelijk kunt zijn voor de prestaties van een bepaalde afdeling van de organisatie. Je wilt verantwoordelijk en bespreekbaar zijn voor het eindresultaat en je identificeert je eigen werk met het succes van de organisatie waarvoor je werkt. Als je je op dit moment op een technisch of functioneel terrein bevindt, zie je dat als een noodzakelijke leerervaring; je ambieert echter zo snel mogelijk een generalistenbaan. Een hoog managementniveau in een functie interesseert je niet. Je vragenlijstscore op dit terrein staat in de tweede kolom van het scoreblad onder AM."},
        "Autonomie/onafhankelijkheid": {"gemiddelde": average3,
                                "uitleg": "Als je loopbaananker autonomie/onafhankelijkheid is, wil je de mogelijkheid je eigen werk op je eigen manier te definiëren niet opgeven. Als je in een organisatie werkzaam bent, wil je een baan hebben die flexibel is met betrekking tot wanneer en hoe je werkt. Als je regels en beperkingen in een organisatie absoluut niet kunt verdragen, kies je een beroep waarin je de door jou gezochte vrijheid wel hebt, zoals lesgeven en advieswerk. Je wijst kansen op promotie of verbetering af om je autonomie te bewaren. Je kunt er zelfs naar streven een eigen bedrijf te beginnen om zo een gevoel van autonomie te bereiken; deze drijfveer is echter niet dezelfde als de ondernemingsgerichte creativiteit die later beschreven wordt. Je vragenlijstscore op dit terrein staat in de derde kolom van het scoreblad onder AU."},
        "Zekerheid/stabiliteit": {"gemiddelde": average4,
                                "uitleg": "Als je loopbaananker zekerheid/stabiliteit is, wil je de zekerheid die een baan je geeft of de vaste aanstelling in een baan of organisatie niet opgeven. Je belangrijkste zorg is het gevoel te hebben dat je succes hebt zodat je je kunt ontspannen. Het anker uit zich in de zorg voor financiële zekerheid (zoals pensioenschema’s en plannen voor vervroegde uittreding) of de zekerheid op een baan. Een dergelijke stabiliteit kan inhouden dat je je loyaliteit en bereidheid om alles wat de werkgever van je vraagt te doen, verhandelt voor een belofte op een vaste aanstelling. Je houdt je niet zo bezig met de inhoud van je werk en de positie die je in de organisatie bereikt, hoewel je als je talentvol bent een hoog niveau kunt bereiken. Iedereen heeft een bepaalde behoefte aan zekerheid en stabiliteit (net zoals iedereen een bepaalde behoefte heeft aan autonomie), in het bijzonder in een periode waarin er sprake is van zware financiële lasten of wanneer men tegen zijn pensionering aanloopt. Op deze manier verankerde mensen zijn echter altijd met deze zaken bezig en bouwen hun hele zelfbeeld op rond het managen van zekerheid en stabiliteit. Je vragenlijstscore op dit terrein staat in de vierde kolom van het scoreblad onder ZE."},
        "Ondernemingsgerichte creativiteit": {"gemiddelde": average5,
                                "uitleg": "Als je loopbaananker ondernemingsgerichte creativiteit is, wil je niet de mogelijkheid opgeven een eigen organisatie of onderneming te creëren, die stoelt op je eigen talenten en je bereidheid risico’s te nemen en hindernissen te overwinnen. Je wilt de wereld bewijzen dat je een onderneming kunt creëren die het resultaat is van je eigen inspanningen. Misschien werk je voor anderen in een organisatie waarbij je leert en inschat wat je kansen voor de toekomst zijn, maar zodra je jezelf daartoe in staat acht, ga je op eigen kracht verder. Als bewijs van je talenten wil je dat je onderneming financieel succesvol is. Je vragenlijstscore op dit terrein staat in de vijfde kolom van het scoreblad onder OC."},
        "Gevoel van dienstverlening, toewijding aan de zaak": {"gemiddelde": average6,
                                "uitleg": "Als je loopbaananker dienstverlening/toewijding aan een zaak is, wil je niet de mogelijkheid opgeven werk na te streven dat iets van waarde oplevert, zoals de wereld leefbaarder maken, milieuproblemen oplossen, harmonie tussen mensen bevorderen, anderen helpen, de veiligheid van mensen verbeteren, ziekten genezen door nieuwe producten, enzovoort. Je streeft dergelijke mogelijkheden zelfs na als dat betekent dat er organisaties veranderd moeten worden, en je accepteert geen overplaatsingen of promoties waardoor je het werk dat aan deze waarden voldoet niet meer zou kunnen doen. Je vragenlijstscore op dit terrein staat in de zesde kolom van het scoreblad onder DV."},
        "Zuivere uitdaging": {"gemiddelde": average7,
                                "uitleg": "Als je loopbaananker zuivere uitdaging is, wil je niet de mogelijkheid opgeven aan oplossingen voor ogenschijnlijk onoplosbare problemen te werken, sterke tegenstanders te verslaan of moeilijke hindernissen te overwinnen. Voor jou is het feit dat je hierin het onmogelijke kunt doen de enige reden van betekenis een baan of loopbaan te volgen. Sommige mensen vinden een dergelijke zuivere uitdaging in intellectueel werk, zoals de ingenieur die alleen geïnteresseerd is in hopeloos moeilijke ontwerpen; sommigen vinden de uitdaging in complexe situaties met vele facetten, zoals de strategie-adviseur die alleen geïnteresseerd is in cliënten die op het punt staan failliet te gaan en alle andere hulpmiddelen al geprobeerd hebben; sommigen vinden het in interpersoonlijke concurrentie, zoals de beroepssporter of de verkoper die iedere verkoop definieert als een plus of een min. Nieuwe kansen, variatie en moeilijkheid worden doelen op zich, en als iets gemakkelijk is, wordt het onmiddellijk saai. Je vragenlijstscore op dit terrein staat in de zevende kolom van het scoreblad UI."},
        "Levensstijl": {"gemiddelde": average8,
                                "uitleg": "Als je loopbaananker levensstijl is, wil je niet een situatie opgeven waarin je je persoonlijke behoeften, de behoeften van je gezin en de eisen die je loopbaan stelt met elkaar in evenwicht kunt brengen en verenigen. Je wilt dat alle belangrijke onderdelen van je leven samenwerken in de richting van een geïntegreerd geheel, en je hebt daarom een loopbaansituatie nodig die flexibel genoeg is om een dergelijke integratie tot stand te brengen. Misschien moet je sommige aspecten van de loopbaan opofferen (bijvoorbeeld een verhuizing naar een andere plaats die een promotie zou inhouden, maar je hele leefsituatie op haar kop zou zetten), en je definieert succes niet alleen op grond van succes in je loopbaan. Je vindt dat je identiteit meer te maken heeft met hoe je je leven in zijn geheel leeft, waar je je vestigt, hoe je met je gezinssituatie omgaat, en hoe je jezelf ontwikkelt dan met een bepaalde baan of organisatie. Je vragenlijstscore op dit terrein staat in de achtste kolom van het scoreblad onder LS."}
    }

    # Sorteer de gemiddelde scores van hoog naar laag
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]["gemiddelde"], reverse=True)

    # Toon de gerangschikte gemiddelde scores
    for category, data in sorted_scores:
        st.write(f"{category}: {data['gemiddelde']:.2f}")
        st.write(f"Uitleg: {data['uitleg']}")

if __name__ == "__main__":
    main()


