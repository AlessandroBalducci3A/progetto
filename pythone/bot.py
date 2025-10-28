class Bot:
    def __init__(self, nome="Romy", cognome="GD"):
        self.nome = nome
        self.cognome = cognome
        self.energia = 100

    def saluta(self):
        print(f"ciao sono {self.nome} {self.cognome}")

    def parla(self, messaggio):
        print(f"{self.nome}: {messaggio}")
    
    def lavora(self, ore):
        if self.energia <= 0:
            print(f"{self.nome} è troppo stanco per lavorare! 😴")
        else:
            self.energia -= ore * 10
            if self.energia < 0:
                self.energia = 0
            print(f"{self.nome} ha lavorato per {ore} ore. Energia rimasta: {self.energia}%")

    def ricarica(self):
        print(f"{self.nome} si sta ricaricando 🔋...")
        self.energia = 100
        print(f"{self.nome} è di nuovo al massimo dell’energia! 💪")

    def stato(self):
        print(f"Nome: {self.nome} {self.cognome} | Energia: {self.energia}%")
    
    def domanda(self):
        print("inserisci la domanda: ")