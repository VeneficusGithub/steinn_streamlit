import streamlit as st
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from github import Github
import json
import os
from dotenv import load_dotenv

load_dotenv()

def generate_pdf(sorted_scores, user_name, user_role, data_functie):
        # Generate a PDF document
    c = canvas.Canvas("result.pdf", pagesize=letter)
    
        # Teken de kop alleen op de eerste pagina
    c.drawString(100, 750, "Rangschikking van scores:")

        # Voeg de gesorteerde scores toe aan het PDF-bestand
    y_position = 670  # Startpositie voor de tekst
    for index, (category, data) in enumerate(sorted_scores):
        c.drawString(100, y_position, f"{category}: {data['gemiddelde']:.2f}")
        uitleg_text = data['uitleg']

        c.drawString(100, 730, f"Gebruiker: {user_name}")
        c.drawString(100, 710, f"Gebruikersrol: {user_role}")
        c.drawString(100, 690, f"Functie: {data_functie}")
    
            # Bepaal de juiste regelafstand voor de uitlegtekst
        line_height = 15
        max_width = 400  # Maximale breedte van de tekst
        current_y = y_position - 30  # Huidige y-positie voor de tekst
        
            # Breek de uitlegtekst op in paragrafen
        paragraphs = []
        current_paragraph = ""
        for word in uitleg_text.split():
            if c.stringWidth(current_paragraph + " " + word, "Helvetica", 12) <= max_width:
                current_paragraph += " " + word
            else:
                paragraphs.append(current_paragraph.strip())
                current_paragraph = word
        if current_paragraph:
            paragraphs.append(current_paragraph.strip())

         # Tekenen van de uitlegtekst op meerdere regels
        for paragraph in paragraphs:
            if current_y < 50:  # Als er niet genoeg ruimte op de huidige pagina is, voeg een nieuwe pagina toe
                c.showPage()
                y_position = 750  # Begin de nieuwe pagina bij de bovenkant
                current_y = y_position - 30  # Huidige y-positie voor de tekst op de nieuwe pagina

            c.drawString(120, current_y, paragraph)
            current_y -= line_height  # Verplaats de y-positie voor de volgende paragraaf

        y_position = current_y - 20  # Extra ruimte tussen de scores

    c.save()
    return "result.pdf"  # Retourneer de bestandsnaam van het gegenereerde PDF-bestand

def upload_json(json_data, user_name):
    # Verbinding maken met GitHub
    token = os.getenv("GITHUB_TOKEN")
    if token is None:
        raise Exception("GitHub token niet gevonden in environment variabelen")

    # Verbinding maken met GitHub
    g = Github(token)  
    repo = g.get_repo("VeneficusGithub/steinn_streamlit")  
    
    folder_path = "resultaten"  # Mapnaam waarin de bestanden zich bevinden

    # Bestandspad voor het JSON-bestand
    timestamp = datetime.now().strftime("%Y-%m-%d")
    json_file_name = f"result_{user_name}_{timestamp}.json"
    json_file_path = f"{folder_path}/{json_file_name}"

    # Inhoud van het JSON-bestand
    json_content = json.dumps(json_data)

    # Bestand aanmaken
    try:
        repo.create_file(json_file_path, "Commit message", json_content, branch="master")
    except Exception as e:
        print("Fout bij het uploaden van het JSON-bestand naar GitHub:", e)

def main():
    st.title("Loopbaanankers van Scheinn")

    user_name = st.text_input("Voer uw naam in")

# Controleer of de naam is ingevuld en toon een bericht
    if user_name:
        st.write(f"Hallo, {user_name}! Welkom bij Loopbaanankers van Scheinn vragenlijst.")
    else:
        st.write("Voer alstublieft uw naam in het bovenstaande veld in.")

    user_role = st.selectbox("Functie:", ["Trainee", "Consultant", "Interne Team"])
    data_functie = st.selectbox("Met welke functie associeer je jezelf het meest:", ["Data Analist", "Data Engineer", "Data Scientist", "Interne Team"])

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
"2. Ik heb de meeste voldoening van mijn werk wanneer ik de inspanningen van anderen heb kunnen verenigen en managen",
"3. Ik droom ervan een loopbaan te hebben waarin ik vrij ben een taak op mijn eigen manier en volgens mijn eigen schema uit te voeren",
"4. Ik vind zekerheid en stabiliteit belangrijker dan vrijheid en autonomie",
"5. Ik ben altijd op zoek naar ideeën waardoor ik mijn eigen bedrijf zou kunnen beginnen",
"6. Alleen als ik het gevoel heb een daadwerkelijke bijdrage geleverd te hebben aan het maatschappelijk welzijn, voel ik mij geslaagd in mijn loopbaan",
"7. Ik droom van een loopbaan waarin ik problemen kan oplossen of zeer uitdagende situaties het hoofd kan bieden",
"8. Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een baan te accepteren die het mij onmogelijk maakt persoonlijke en gezinszaken na te streven",
"9. Ik voel me alleen geslaagd in mijn loopbaan als ik mijn technische of functionele vaardigheden tot een zeer hoog competentieniveau kan ontwikkelen",
"10. Ik droom ervan aan het hoofd te staan van een complexe organisatie en beslissingen te nemen die veel mensen beïnvloeden",
"11. Ik heb de meeste voldoening van mijn werk wanneer ik volledig vrij ben in het bepalen van mijn eigen taken, schema’s en procedures",
"12. Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een taak te accepteren die mijn zekerheid in de organisatie in gevaar zou brengen",
"13. Ik vind het opbouwen van mijn eigen bedrijf belangrijker dan het bereiken van een hoge managementpositie in de organisatie van iemand anders",
"14. Ik heb de meeste voldoening van mijn werk wanneer ik mijn talenten in dienst van anderen heb kunnen gebruiken",
"15. Ik voel me alleen geslaagd in mijn loopbaan als ik te maken heb met zeer moeilijke uitdagingen en deze het hoofd kan bieden",
"16. Ik droom van een loopbaan waarin ik mijn persoonlijke, gezins-, en arbeidsbehoeften kan verenigen.",
"17. Ik vind het aantrekkelijker een hogere functionele manager op mijn competentieterrein te worden dan een algemeen manager",
"18.	Ik voel me alleen geslaagd in mijn loopbaan als ik algemeen manager in een organisatie word",
"19.	Ik voel me alleen geslaagd in mijn loopbaan als ik volledige autonomie en vrijheid verwerf",
"20.	Ik zoek een baan in een organisatie die mij een gevoel van zekerheid en stabiliteit geeft",
"21.	Ik heb de meeste voldoening van mijn werk wanneer ik iets heb kunnen opbouwen wat volledig het resultaat is van mijn eigen ideeën en inspanningen",
"22.	Ik vind het belangrijker mijn vaardigheden te gebruiken om de wereld aantrekkelijker te maken om in te wonen en te werken dan een hoge managementpositie te bereiken",
"23.	Ik heb de meeste voldoening van mijn werk wanneer ik ogenschijnlijk onoplosbare problemen heb opgelost of ogenschijnlijk onmogelijke tegenslagen heb overwonnen",
"24.	Ik voel me alleen geslaagd in mijn leven als ik mijn persoonlijke-, gezins- en loopbaaneisen met elkaar in evenwicht kan brengen",
"25.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een taakroulatie te accepteren waardoor ik mijn competentieterrein zou moeten verlaten",
"26.	Ik vind het aantrekkelijker algemeen manager te worden dan een hogere functionele manager op mijn huidige competentieterrein",
"27.	Een taak op mijn eigen manier doen, vrij van regels en beperkingen, vind ik belangrijker dan zekerheid",
"28.	Ik heb de meeste voldoening van mijn werk wanneer ik weet dat ik volledige financiële zekerheid heb en zeker ben van mijn baan",
"29.	Ik voel me alleen geslaagd in mijn loopbaan als het me gelukt is iets te creëren of op te bouwen wat volledig mijn eigen product of idee is",
"30.	Ik droom van een loopbaan die daadwerkelijk een bijdrage levert aan de mensheid en de maatschappij",
"31.	Ik zoek naar kansen op het werk die in sterke mate een uitdaging vormen voor mijn probleemoplossende en/of prestatiegerichte vaardigheden",
"32.	Ik vind het belangrijker de eisen van mijn persoonlijke en beroepsleven met elkaar in evenwicht te brengen dan een hoge managementpositie te bereiken",
"33.	Ik heb de meeste voldoening van mijn werk wanneer ik mijn speciale vaardigheden en talenten kan gebruiken",
"34.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een baan te accepteren waardoor ik van het algemeen managementspoor zou afdwalen",
"35.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een baan te accepteren waardoor mijn autonomie en vrijheid zouden verminderen",
"36.	Ik droom van een loopbaan waarin ik een gevoel van zekerheid en stabiliteit ervaar",
"37.	Ik droom ervan mijn eigen bedrijf te beginnen en op te bouwen",
"38.	Ik zou nog eerder weggaan bij het bedrijf waar ik werk dan een taak te accepteren waardoor ik anderen minder goed van dienst zou kunnen zijn",
"39.	Ik vind het belangrijker aan vrijwel onoplosbare problemen te werken dan een hoge managementpositie te bereiken",
"40.	Ik heb altijd gezocht naar werk dat zo min mogelijk invloed heeft op mijn persoonlijke of gezinszaken"
]
    
    
    # Dictionary om scores bij te houden
    question_scores = {question: 0 for question in questions}

    # bonus_counter = 0

# Functie om 4 punten toe te voegen aan de score van een vraag
    def add_points(question):
        question_scores[question] += 4


    def show_question(question, index):
        st.write(f"{question}:")
        score = question_scores[question]
        col1, col2 = st.columns([4, 1])
        question_scores[question] = col1.slider("", 0, 6, value=score, step=1, key=f"slider_{index}")
        checked = col2.checkbox("Bonus", key=f"checkbox_{index}")
        if checked:
            add_points(question)

# Toon alle vragen en bijbehorende sliders en selectievakjes
    for index, question in enumerate(questions):
        show_question(question, index)
    st.write("**Zoek nu de onderwerpen die je het hoogst gewaardeerd hebt. Kies de DRIE onderwerpen die het meest op jou van toepassing zijn en selecteer bij deze vraag de 'Bonus'-knop.**")
# Categorien met bijbehorende vraagindices
    category_indices = {
        "Technisch Functioneel": [0, 8, 16, 24, 32],  # Voorbeeld: indices van de eerste vier vragen
        "Algemeen Management": [1,9, 17, 25, 33],  # Voorbeeld: indices van de volgende vier vragen
        "Autonomie/onafhankelijkheid": [2, 10, 18, 26, 34],
        "Zekerheid/stabiliteit": [3, 11, 19, 27, 35],
        "Ondernemingsgerichte creativiteit": [4, 12, 20, 28, 36],
        "Gevoel van dienstverlening, toewijding aan de zaak": [5, 13, 21, 29, 37],
        "Zuivere uitdaging": [6, 14, 22, 30, 38],
        "Levensstijl": [7, 15, 23, 31, 39]
    # Voeg hier de overige categorieën toe met bijbehorende indices
}

    def average_scores(scores, questions):
        category_averages = {}
        for category, indices in category_indices.items():
            category_scores = [scores[questions[i]] for i in indices]
            if category_scores:  # Controleer of de lijst niet leeg is
                category_averages[category] = sum(category_scores) / len(category_scores)
            else:
                category_averages[category] = 0  # Als de lijst leeg is, zet het gemiddelde op 0
        return category_averages

# Toon gemiddelde scores per categorie
    st.header("Gemiddelde scores per categorie")
    for category, average in average_scores(question_scores, questions).items():
        st.write(f"{category}: {average:.2f}")

    category_averages = average_scores(question_scores, questions)

    st.header("Rangschikking")
    scores = {
        "Technisch Functioneel": {"gemiddelde": category_averages["Technisch Functioneel"], 
                                "uitleg": "Als je loopbaanankercompetentie op een technisch of functioneel terrein is, wil je niet de mogelijkheid opgeven je vaardigheden op dat terrein toe te passen en die vaardigheden steeds verder te ontwikkelen naar een steeds hoger niveau. Je ontleent je gevoel van identiteit aan het uitoefenen van je vaardigheden en je bent het gelukkigst wanneer je door je werk op deze terreinen uitgedaagd wordt. Je bent misschien bereid anderen op jouw technische of functionele terrein te managen, maar je bent niet geïnteresseerd in management om het management en je bent geneigd het algemeen management te mijden omdat je dan je eigen competentieterrein zou moeten verlaten. Je vragenlijstscore op dit terrein staat in de eerste kolom van het scoreblad onder TF."},
        "Algemeen Management": {"gemiddelde": category_averages["Algemeen Management"],
                                "uitleg": "Als je loopbaananker algemeen-managementcompetentie is, wil je niet de mogelijkheid opgeven tot een zo hoog mogelijk niveau in een organisatie op te klimmen waardoor je de inspanningen voor anderen in verschillende functies kunt verenigen en verantwoordelijk kunt zijn voor de prestaties van een bepaalde afdeling van de organisatie. Je wilt verantwoordelijk en bespreekbaar zijn voor het eindresultaat en je identificeert je eigen werk met het succes van de organisatie waarvoor je werkt. Als je je op dit moment op een technisch of functioneel terrein bevindt, zie je dat als een noodzakelijke leerervaring; je ambieert echter zo snel mogelijk een generalistenbaan. Een hoog managementniveau in een functie interesseert je niet. Je vragenlijstscore op dit terrein staat in de tweede kolom van het scoreblad onder AM."},
        "Autonomie/onafhankelijkheid": {"gemiddelde": category_averages["Autonomie/onafhankelijkheid"],
                                "uitleg": "Als je loopbaananker autonomie/onafhankelijkheid is, wil je de mogelijkheid je eigen werk op je eigen manier te definiëren niet opgeven. Als je in een organisatie werkzaam bent, wil je een baan hebben die flexibel is met betrekking tot wanneer en hoe je werkt. Als je regels en beperkingen in een organisatie absoluut niet kunt verdragen, kies je een beroep waarin je de door jou gezochte vrijheid wel hebt, zoals lesgeven en advieswerk. Je wijst kansen op promotie of verbetering af om je autonomie te bewaren. Je kunt er zelfs naar streven een eigen bedrijf te beginnen om zo een gevoel van autonomie te bereiken; deze drijfveer is echter niet dezelfde als de ondernemingsgerichte creativiteit die later beschreven wordt. Je vragenlijstscore op dit terrein staat in de derde kolom van het scoreblad onder AU."},
        "Zekerheid/stabiliteit": {"gemiddelde": category_averages["Zekerheid/stabiliteit"],
                                "uitleg": "Als je loopbaananker zekerheid/stabiliteit is, wil je de zekerheid die een baan je geeft of de vaste aanstelling in een baan of organisatie niet opgeven. Je belangrijkste zorg is het gevoel te hebben dat je succes hebt zodat je je kunt ontspannen. Het anker uit zich in de zorg voor financiële zekerheid (zoals pensioenschema’s en plannen voor vervroegde uittreding) of de zekerheid op een baan. Een dergelijke stabiliteit kan inhouden dat je je loyaliteit en bereidheid om alles wat de werkgever van je vraagt te doen, verhandelt voor een belofte op een vaste aanstelling. Je houdt je niet zo bezig met de inhoud van je werk en de positie die je in de organisatie bereikt, hoewel je als je talentvol bent een hoog niveau kunt bereiken. Iedereen heeft een bepaalde behoefte aan zekerheid en stabiliteit (net zoals iedereen een bepaalde behoefte heeft aan autonomie), in het bijzonder in een periode waarin er sprake is van zware financiële lasten of wanneer men tegen zijn pensionering aanloopt. Op deze manier verankerde mensen zijn echter altijd met deze zaken bezig en bouwen hun hele zelfbeeld op rond het managen van zekerheid en stabiliteit. Je vragenlijstscore op dit terrein staat in de vierde kolom van het scoreblad onder ZE."},
        "Ondernemingsgerichte creativiteit": {"gemiddelde": category_averages["Ondernemingsgerichte creativiteit"],
                                "uitleg": "Als je loopbaananker ondernemingsgerichte creativiteit is, wil je niet de mogelijkheid opgeven een eigen organisatie of onderneming te creëren, die stoelt op je eigen talenten en je bereidheid risico’s te nemen en hindernissen te overwinnen. Je wilt de wereld bewijzen dat je een onderneming kunt creëren die het resultaat is van je eigen inspanningen. Misschien werk je voor anderen in een organisatie waarbij je leert en inschat wat je kansen voor de toekomst zijn, maar zodra je jezelf daartoe in staat acht, ga je op eigen kracht verder. Als bewijs van je talenten wil je dat je onderneming financieel succesvol is. Je vragenlijstscore op dit terrein staat in de vijfde kolom van het scoreblad onder OC."},
        "Gevoel van dienstverlening, toewijding aan de zaak": {"gemiddelde": category_averages["Gevoel van dienstverlening, toewijding aan de zaak"],
                                "uitleg": "Als je loopbaananker dienstverlening/toewijding aan een zaak is, wil je niet de mogelijkheid opgeven werk na te streven dat iets van waarde oplevert, zoals de wereld leefbaarder maken, milieuproblemen oplossen, harmonie tussen mensen bevorderen, anderen helpen, de veiligheid van mensen verbeteren, ziekten genezen door nieuwe producten, enzovoort. Je streeft dergelijke mogelijkheden zelfs na als dat betekent dat er organisaties veranderd moeten worden, en je accepteert geen overplaatsingen of promoties waardoor je het werk dat aan deze waarden voldoet niet meer zou kunnen doen. Je vragenlijstscore op dit terrein staat in de zesde kolom van het scoreblad onder DV."},
        "Zuivere uitdaging": {"gemiddelde": category_averages["Zuivere uitdaging"],
                                "uitleg": "Als je loopbaananker zuivere uitdaging is, wil je niet de mogelijkheid opgeven aan oplossingen voor ogenschijnlijk onoplosbare problemen te werken, sterke tegenstanders te verslaan of moeilijke hindernissen te overwinnen. Voor jou is het feit dat je hierin het onmogelijke kunt doen de enige reden van betekenis een baan of loopbaan te volgen. Sommige mensen vinden een dergelijke zuivere uitdaging in intellectueel werk, zoals de ingenieur die alleen geïnteresseerd is in hopeloos moeilijke ontwerpen; sommigen vinden de uitdaging in complexe situaties met vele facetten, zoals de strategie-adviseur die alleen geïnteresseerd is in cliënten die op het punt staan failliet te gaan en alle andere hulpmiddelen al geprobeerd hebben; sommigen vinden het in interpersoonlijke concurrentie, zoals de beroepssporter of de verkoper die iedere verkoop definieert als een plus of een min. Nieuwe kansen, variatie en moeilijkheid worden doelen op zich, en als iets gemakkelijk is, wordt het onmiddellijk saai. Je vragenlijstscore op dit terrein staat in de zevende kolom van het scoreblad UI."},
        "Levensstijl": {"gemiddelde": category_averages["Levensstijl"],
                                "uitleg": "Als je loopbaananker levensstijl is, wil je niet een situatie opgeven waarin je je persoonlijke behoeften, de behoeften van je gezin en de eisen die je loopbaan stelt met elkaar in evenwicht kunt brengen en verenigen. Je wilt dat alle belangrijke onderdelen van je leven samenwerken in de richting van een geïntegreerd geheel, en je hebt daarom een loopbaansituatie nodig die flexibel genoeg is om een dergelijke integratie tot stand te brengen. Misschien moet je sommige aspecten van de loopbaan opofferen (bijvoorbeeld een verhuizing naar een andere plaats die een promotie zou inhouden, maar je hele leefsituatie op haar kop zou zetten), en je definieert succes niet alleen op grond van succes in je loopbaan. Je vindt dat je identiteit meer te maken heeft met hoe je je leven in zijn geheel leeft, waar je je vestigt, hoe je met je gezinssituatie omgaat, en hoe je jezelf ontwikkelt dan met een bepaalde baan of organisatie. Je vragenlijstscore op dit terrein staat in de achtste kolom van het scoreblad onder LS."}
    }

    sorted_scores = sorted(scores.items(), key=lambda x: x[1]["gemiddelde"], reverse=True)

# Toon de gerangschikte gemiddelde scores
    for category, data in sorted_scores:
        st.write(f"{category}: {data['gemiddelde']:.2f}")
        st.write(f"Uitleg: {data['uitleg']}")

    pdf_file = generate_pdf(sorted_scores, user_name, user_role, data_functie)

# Omzetten van de gesorteerde scores naar JSON-formaat
    json_data = json.dumps({
    "Rol": user_role,  # Toevoegen van gebruikersrol
    "Data functie": data_functie,
    **{category: data["gemiddelde"] for category, data in sorted_scores}
})

# Uploaden van JSON naar GitHub
    upload_json(json_data, user_name)

# Downloadknop voor het PDF-bestand toevoegen aan de Streamlit-app
    with open(pdf_file, "rb") as f:
        data = f.read()
    st.download_button(label="Click here to download PDF", data=data, file_name="result.pdf", mime="application/pdf")
    st.success("PDF-bestand is gedownload!")


if __name__ == "__main__":
    main()


