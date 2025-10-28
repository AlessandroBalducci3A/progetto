from funzioni import inizio, seleziona, chatbot
from bot import Bot


# --- Programma principale ---
bot = Bot()

def comanda():
    print("Benvenuto! Puoi dare comandi al bot.")
    print("Comandi disponibili: saluta, parla, lavora, ricarica, stato, domanda, esci")

    while True:
        comando = input("\n👉 Inserisci un comando: ").lower()

        if comando == "saluta":
            bot.saluta()
        elif comando == "parla":
            messaggio = input("Cosa deve dire il bot? ")
            bot.parla(messaggio)
        elif comando == "lavora":
            try:
                ore = int(input("Quante ore deve lavorare? "))
                bot.lavora(ore)
            except ValueError:
                print("Inserisci un numero valido di ore.")
        elif comando == "ricarica":
            bot.ricarica()
        elif comando == "stato":
            bot.stato()
        elif comando == "esci":
            print("👋 Il bot si spegne. A presto!")
            break
        elif comando == "domanda":
            inizio()
            scelta = seleziona()
            chatbot(scelta)
        else:
            print("❌ Comando non riconosciuto. Riprova.")


comanda()


#aggiornare le parole chiave
#aggiungere css html e js
#creare un avatar
#flask
#bottone crediti
#collegare python dopo
#migliorare accesso a pagina2
#creare css per le pagine
#classe chatbot