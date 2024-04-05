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
    st.header("Gemiddelde Scores")
    average = average_TF(answers)
    st.write(f"Gemiddelde TF: {average:.2f}")
    average2 = average_AM(answers)
    st.write(f"Gemiddelde AM: {average2:.2f}")
    average3 = average_AU(answers)
    st.write(f"Gemiddelde AU: {average3:.2f}")
    average4 = average_ZE(answers)
    st.write(f"Gemiddelde ZE: {average4:.2f}")
    average5 = average_OC(answers)
    st.write(f"Gemiddelde OC: {average5:.2f}")
    average6 = average_DV(answers)
    st.write(f"Gemiddelde DV: {average6:.2f}")
    average7 = average_UI(answers)
    st.write(f"Gemiddelde UI: {average7:.2f}")
    average8 = average_LS(answers)
    st.write(f"Gemiddelde LS: {average8:.2f}")


if __name__ == "__main__":
    main()


