import random

class Pokemon:
    def __init__(self, nom, type_pokemon):
        self.__nom = nom
        self.__type = type_pokemon
        self.__points_de_vie = 100
        self.__niveau = 1
        self.__puissance_attaque = 0
        self.__defense = 0

    def get_nom(self):
        return self.__nom

    def get_points_de_vie(self):
        return self.__points_de_vie

    def get_type(self):
        return self.__type

    def get_niveau(self):
        return self.__niveau

    def get_puissance_attaque(self):
        return self.__puissance_attaque

    def get_defense(self):
        return self.__defense

    def set_nom(self, nom):
        self.__nom = nom

    def set_points_de_vie(self, points_de_vie):
        self.__points_de_vie = points_de_vie

    def set_type(self, type_pokemon):
        self.__type = type_pokemon

    def set_niveau(self, niveau):
        self.__niveau = niveau

    def set_puissance_attaque(self, puissance_attaque):
        self.__puissance_attaque = puissance_attaque

    def set_defense(self, defense):
        self.__defense = defense

    def afficher_infos(self):
        print("Nom:", self.__nom)
        print("Points de vie:", self.__points_de_vie)
        print("Type:", self.__type)
        print("Niveau:", self.__niveau)
        print("Puissance d'attaque:", self.__puissance_attaque)
        print("Défense:", self.__defense)


class PokemonNormal(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "normal")
        self.set_points_de_vie(90)
        self.set_puissance_attaque(20)
        self.set_defense(10)


class PokemonFeu(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "feu")
        self.set_points_de_vie(70)
        self.set_puissance_attaque(25)
        self.set_defense(5)


class PokemonEau(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "eau")
        self.set_points_de_vie(90)
        self.set_puissance_attaque(15)
        self.set_defense(15)


class PokemonTerre(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "terre")
        self.set_points_de_vie(70)
        self.set_puissance_attaque(5)
        self.set_defense(20)


class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2

    def verifier_pokemon_en_vie(self):
        if self.__pokemon1.get_points_de_vie() <= 0:
            return self.__pokemon2
        elif self.__pokemon2.get_points_de_vie() <= 0:
            return self.__pokemon1
        else:
            return None

    def choisir_aleatoire_attaque(self):
        return random.randint(0, 1)

    def calculer_degats(self, attaquant, defenseur):
        if attaquant.get_type() == "normal":
            multiplicateur = 1
        elif attaquant.get_type() == "feu":
            if defenseur.get_type() == "eau":
                multiplicateur = 0.5
            elif defenseur.get_type() == "terre":
                multiplicateur = 2
            else:
                multiplicateur = 1
        elif attaquant.get_type() == "eau":
            if defenseur.get_type() == "feu":
                multiplicateur = 2
            elif defenseur.get_type() == "terre":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        elif attaquant.get_type() == "terre":
            if defenseur.get_type() == "eau":
                multiplicateur = 2
            elif defenseur.get_type() == "feu":
                multiplicateur = 0.5
            else:
                multiplicateur = 1

        degats = attaquant.get_puissance_attaque() * multiplicateur
        return degats
    
# créer deux Pokémons
pikachu = PokemonEau("Pikachu")
bulbasaur = PokemonTerre("Bulbasaur")

# afficher les informations des Pokémons
pikachu.afficher_infos()
bulbasaur.afficher_infos()

# créer un combat entre les deux Pokémons
combat = Combat(pikachu, bulbasaur)

# tant que les deux Pokémons sont en vie, les faire combattre
while not combat.verifier_pokemon_en_vie():
    attaquant = combat.choisir_aleatoire_attaque()
    if attaquant == 0:
        degats = combat.calculer_degats(pikachu, bulbasaur)
        bulbasaur.set_points_de_vie(bulbasaur.get_points_de_vie() - degats)
    else:
        degats = combat.calculer_degats(bulbasaur, pikachu)
        pikachu.set_points_de_vie(pikachu.get_points_de_vie() - degats)

# afficher le gagnant
gagnant = combat.verifier_pokemon_en_vie()
print("Le gagnant est", gagnant.get_nom())
