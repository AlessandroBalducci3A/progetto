import sys

def inizio():
    print("""
        Ciao, io mi chiamo Chatbot e sono qui per rispondere alle tue domande sull'istituto Romagnosi!
        Queste sono le informazioni su cui sono stato istruito:
        1. Informazioni generali sulla scuola
        2. Indirizzi di studio e materie
        3. Didattica e orario scolastico
        4. Stage, PCTO e collegamenti col mondo del lavoro
        5. Dopo il diploma
        6. Vita scolastica e ambiente
        7. Servizi e risorse
        8. Iscrizioni e orientamento
    """)

def seleziona():
    while True:
        risposta = input("Inserisci l'argomento selezionando il numero (1-8): ")
        if risposta.isdigit():
            risposta = int(risposta)
            if 1 <= risposta <= 8:
                break
            else:
                print("❌ Il numero inserito non è valido.")
        else:
            print("⚠️ Per favore inserisci un numero valido (1-8).")
    return risposta

def chatbot(scelta):
    argomenti = {
    1: [
        {"risposta": "L'Istituto Romagnosi è una scuola che offre formazione in vari indirizzi, con una lunga tradizione accademica e un ottimo supporto agli studenti.",
         "parole_chiave": ["scuola", "informazioni", "istituto", "tradizione", "supporto"]},
        {"risposta": "Fondata diversi anni fa, l'Istituto Romagnosi punta a combinare l'eccellenza didattica con attività culturali e sportive per gli studenti.",
         "parole_chiave": ["fondazione", "storia", "cultura", "sport", "attività"]},
        {"risposta": "L'istituto offre un ambiente accogliente dove studenti e insegnanti collaborano per raggiungere obiettivi educativi di alto livello.",
         "parole_chiave": ["ambiente", "collaborazione", "insegnanti", "studenti", "obiettivi"]}
    ],
    2: [
        {"risposta": "Gli indirizzi di studio includono: Liceo Scientifico, Liceo Classico, Istituto Tecnico e Professionale, ognuno con materie specifiche.",
         "parole_chiave": ["indirizzi", "liceo", "tecnico", "professionale", "materie"]},
        {"risposta": "Ogni indirizzo scolastico prevede percorsi differenziati: scientifico con matematica e fisica, classico con latino e greco, tecnico con materie pratiche.",
         "parole_chiave": ["percorsi", "scientifico", "classico", "pratiche", "teoriche"]},
        {"risposta": "L'Istituto offre anche corsi opzionali e attività extracurricolari per approfondire le materie principali di ogni indirizzo.",
         "parole_chiave": ["corsi", "opzionali", "attività", "approfondimento", "materie"]}
    ],
    3: [
        {"risposta": "La didattica prevede un orario scolastico che va dalle 8:00 alle 14:00, con pause e intervalli tra le lezioni.",
         "parole_chiave": ["orario", "lezioni", "pause", "giornata", "scolastico"]},
        {"risposta": "Ogni anno scolastico è diviso in due semestri, con verifiche periodiche, progetti e momenti di valutazione continua.",
         "parole_chiave": ["anno", "semestre", "verifiche", "progetti", "valutazione"]},
        {"risposta": "Le lezioni seguono un calendario settimanale strutturato, integrando laboratori, attività pratiche e lezioni teoriche.",
         "parole_chiave": ["calendario", "settimanale", "laboratori", "pratica", "teoria"]}
    ],
    4: [
        {"risposta": "L'Istituto Romagnosi offre vari progetti PCTO e stage in collaborazione con aziende locali e internazionali.",
         "parole_chiave": ["stage", "PCTO", "aziende", "collaborazione", "esperienza"]},
        {"risposta": "Gli studenti hanno la possibilità di svolgere tirocini che permettono di acquisire competenze pratiche e conoscenze del mondo del lavoro.",
         "parole_chiave": ["tirocini", "pratico", "competenze", "lavoro", "opportunità"]},
        {"risposta": "Le esperienze professionali guidate aiutano gli studenti a comprendere il settore lavorativo di interesse e sviluppare soft skills importanti.",
         "parole_chiave": ["esperienze", "professionali", "soft skills", "settore", "guidate"]}
    ],
    5: [
        {"risposta": "Dopo il diploma, gli studenti possono proseguire gli studi all'università, scegliere un percorso di formazione professionale o entrare nel mondo del lavoro.",
         "parole_chiave": ["diploma", "università", "lavoro", "formazione", "post-diploma"]},
        {"risposta": "L'Istituto supporta gli studenti nell'orientamento post-diploma, aiutandoli a individuare le opzioni più adatte alle proprie aspirazioni.",
         "parole_chiave": ["orientamento", "scelte", "aspirazioni", "supporto", "percorsi"]},
        {"risposta": "Alcuni studenti scelgono programmi internazionali o stage per acquisire esperienze pratiche prima di proseguire gli studi.",
         "parole_chiave": ["programmi", "internazionali", "stage", "esperienze", "studio"]}
    ],
    6: [
        {"risposta": "La vita scolastica è dinamica, con eventi culturali, sportivi e attività extracurriculari che coinvolgono tutti gli studenti.",
         "parole_chiave": ["vita scolastica", "eventi", "attività", "culturali", "sportive"]},
        {"risposta": "L'ambiente scolastico è accogliente e stimolante, favorendo la collaborazione e lo sviluppo personale degli studenti.",
         "parole_chiave": ["ambiente", "accogliente", "stimolante", "collaborazione", "personale"]},
        {"risposta": "Oltre alle lezioni, la scuola propone club, laboratori creativi e progetti sociali per arricchire l'esperienza scolastica.",
         "parole_chiave": ["club", "laboratori", "progetti", "sociali", "arricchimento"]}
    ],
    7: [
        {"risposta": "I servizi includono una biblioteca ben fornita, aule informatiche moderne e spazi dedicati allo studio.",
         "parole_chiave": ["servizi", "biblioteca", "aule", "informatiche", "studio"]},
        {"risposta": "Gli studenti possono contare su supporto psicopedagogico e orientamento personalizzato durante tutto l'anno scolastico.",
         "parole_chiave": ["supporto", "psicopedagogico", "orientamento", "personalizzato", "studenti"]},
        {"risposta": "Sono disponibili laboratori specializzati, assistenza tecnica e risorse digitali per favorire l'apprendimento innovativo.",
         "parole_chiave": ["laboratori", "assistenza", "risorse", "digitali", "innovativo"]}
    ],
    8: [
        {"risposta": "Le iscrizioni avvengono online tramite il portale del Ministero dell'Istruzione, con istruzioni dettagliate per ogni step.",
         "parole_chiave": ["iscrizioni", "online", "portale", "ministero", "procedura"]},
        {"risposta": "La scuola organizza eventi di orientamento per far conoscere indirizzi di studio, laboratori e attività agli studenti interessati.",
         "parole_chiave": ["orientamento", "eventi", "laboratori", "attività", "indirizzi"]},
        {"risposta": "È possibile ricevere supporto individuale per completare l'iscrizione e chiarire dubbi su procedure e documentazione richiesta.",
         "parole_chiave": ["supporto", "individuale", "documentazione", "procedure", "dubbi"]}
    ]
    }

    print(f"\nHai scelto l'argomento {scelta}. Fai una domanda sull'argomento scelto!")
    while True:
        domanda = input("\nFai una domanda: ").lower()
        risposta_trovata = False

        # Controlla tutte le risposte per l'argomento scelto
        for voce in argomenti[scelta]:
            if any(parola in domanda for parola in voce["parole_chiave"]):
                print(f"\nChatbot: {voce['risposta']}")
                risposta_trovata = True
                break

        if not risposta_trovata:
            print("\nChatbot: Mi dispiace, non ho capito la domanda. Prova con una domanda diversa.")
        continua == input("\nVuoi selezionare un'altra modalità? (si/no): ").lower()
        if continua != 'si':
            comanda()
        continua = input("\nVuoi fare un'altra domanda? (si/no): ").lower()
        if continua != 'si':
            sys.exit()
        

        else:
            cambio_argomento = input("\nChatbot: Vuoi cambiare argomento? (si/no) ").lower()
            if cambio_argomento == "si":
                scelta = seleziona()
                