class Personne:
    def __init__(self, nom, prénom, telephone=None, email=None,adresse=None):
        self.nom = nom
        self.prénom = prénom
        self.telephone = telephone
        self.email = email
        #self._adresse=None # 5 i added the addrese parametre so it become like below
        self._adresse = adresse

    def __str__(self):
        region = self._adresse.split(",")[-1] if self._adresse else "Non spécifiée"
        return f"Nom: {self.nom}, Prénom: {self.prénom}, Téléphone: {self.telephone}, Email: {self.email}, Région: {region}" #Adresse: {self._adresse}

'''
personne1 = Personne("Doe", "John")
print(personne1)

personne2 = Personne("Smith", "Alice", "987654321", "alice@example.com")
print(personne2)  '''

#4
"""
personne1 = Personne("Doe", "John", "123456789", "john@example.com")
personne1._adresse = "123, rue de Paris, 75001, Île-de-France"  # Exemple d'attribution d'adresse
print(personne1)
"""


#6
personne1 = Personne("Doe", "John", "123456789", "john@example.com", "123, rue de Paris, 75001, Île-de-France")
print(personne1)

personne2 = Personne("Smith", "Alice", "987654321", "alice@example.com")
print(personne2)









