from tkinter import *
import json
from random import randrange
import pygame
from pygame.locals import *


with open('puissance.json', encoding="utf-8") as json_pui:
    data_pui = json.load(json_pui)

with open('pokemon.json', encoding="utf-8") as json_data:
    data_poke = json.load(json_data)

    Initialisation = data_poke.get("Initialisation")

    Dracaufeu = data_poke.get("Dracaufeu")
    Tortank = data_poke.get("Tortank")
    Florizarre = data_poke.get("Florizarre")
    Papilusion = data_poke.get("Papilusion")
    Dardargnan = data_poke.get("Dardargnan")
    Roucarnage = data_poke.get("Roucarnage")
    Rattatac = data_poke.get("Rattatac")
    Rapasdepic = data_poke.get("Rapasdepic")
    Arbok = data_poke.get("Arbok")
    Raichu = data_poke.get("Raichu")
    Sablaireau = data_poke.get("Sablaireau")
    Nidoqueen = data_poke.get("Nidoqueen")
    Nidoking = data_poke.get("Nidoking")
    Melodelfe = data_poke.get("Melodelfe")
    Feunard = data_poke.get("Feunard")
    Grodoudou = data_poke.get("Grodoudou")
    Nosferalto = data_poke.get("Nosferalto")
    Rafflesia = data_poke.get("Rafflesia")
    Parasect = data_poke.get("Parasect")
    Triopikeur = data_poke.get("Triopikeur")
    Persian = data_poke.get("Persian")
    Akwakwak = data_poke.get("Akwakwak")
    Colossinge = data_poke.get("Colossinge")
    Arcanin = data_poke.get("Arcanin")
    Tartard = data_poke.get("Tartard")
    Alakazam = data_poke.get("Alakazam")
    Mackogneur = data_poke.get("Mackogneur")
    Empiflor = data_poke.get("Empiflor")
    Tentacruel = data_poke.get("Tentacruel")
    Aeromite = data_poke.get("Aeromite")
    Grolem = data_poke.get("Grolem")
    Galopa = data_poke.get("Galopa")
    Flagadoss = data_poke.get("Flagadoss")
    Magneton = data_poke.get("Magneton")
    Canarticho = data_poke.get("Canarticho")
    Dodrio = data_poke.get("Dodrio")
    Lamantine = data_poke.get("Lamantine")
    Grotadmorv = data_poke.get("Grotadmorv")
    Crustabri = data_poke.get("Crustabri")
    Ectoplasma = data_poke.get("Ectoplasma")
    Onix = data_poke.get("Onix")
    Hypnomade = data_poke.get("Hypnomade")
    Krabboss = data_poke.get("Krabboss")
    Electrode = data_poke.get("Electrode")
    Noadkoko = data_poke.get("Noadkoko")
    Ossatueur = data_poke.get("Ossatueur")
    Kicklee = data_poke.get("Kicklee")
    Tygnon = data_poke.get("Tygnon")
    Excelangue = data_poke.get("Excelangue")
    Smogogo = data_poke.get("Smogogo")
    Rhinoferos = data_poke.get("Rhinoferos")
    Leveinard = data_poke.get("Leveinard")
    Kangourex = data_poke.get("Kangourex")
    Hypocean = data_poke.get("Hypocean")
    Poissoroy = data_poke.get("Poissoroy")
    Staross = data_poke.get("Staross")
    Insecateur = data_poke.get("Insecateur")
    Lippoutou = data_poke.get("Lippoutou")
    Elektek = data_poke.get("Elektek")
    Magmar = data_poke.get("Magmar")
    Scarabrute = data_poke.get("Scarabrute")
    Tauros = data_poke.get("Tauros")
    Leviator = data_poke.get("Leviator")
    Lokhlass = data_poke.get("Lokhlass")
    Aquali = data_poke.get("Aquali")
    Voltali = data_poke.get("Voltali")
    Pyroli = data_poke.get("Pyroli")
    Porygon = data_poke.get("Porygon")
    Amonistar = data_poke.get("Amonistar")
    Kabutops = data_poke.get("Kabutops")
    Ptera = data_poke.get("Ptera")
    Ronflex = data_poke.get("Ronflex")
    Artikodin = data_poke.get("Artikodin")
    Electhor = data_poke.get("Electhor")
    Sulfura = data_poke.get("Sulfura")
    Dracolosse = data_poke.get("Dracolosse")
    Mewtwo = data_poke.get("Mewtwo")
    Mew = data_poke.get("Mew")

    Olga_Flagadoss = data_poke.get("Olga_Flagadoss")
    Olga_Lokhlass = data_poke.get("Olga_Lokhlass")
    Olga_Lippoutou = data_poke.get("Olga_Lippoutou")

    Aldo_Tygnon = data_poke.get("Aldo_Tygnon")
    Aldo_Kicklee = data_poke.get("Aldo_Kicklee")
    Aldo_Mackogneur = data_poke.get("Aldo_Mackogneur")

    Agatha_Nosferalto = data_poke.get("Agatha_Nosferalto")
    Agatha_Arbok = data_poke.get("Agatha_Arbok")
    Agatha_Ectoplasma = data_poke.get("Agatha_Ectoplasma")

    Peter_Ptera = data_poke.get("Peter_Ptera")
    Peter_Leviator = data_poke.get("Peter_Leviator")
    Peter_Dracolosse = data_poke.get("Peter_Dracolosse")

    Maitre_Arcanin = data_poke.get("Maitre_Arcanin")
    Maitre_Alakazam = data_poke.get("Maitre_Alakazam")
    Maitre_Tortank = data_poke.get("Maitre_Tortank")

    Pierre_Onix = data_poke.get("Pierre_Onix")
    Pierre_Grolem = data_poke.get("Pierre_Grolem")
    Pierre_Rhinoferos = data_poke.get("Pierre_Rhinoferos")

    Ondine_Staross = data_poke.get("Ondine_Staross")
    Ondine_Hypocean = data_poke.get("Ondine_Hypocean")
    Ondine_Tartard = data_poke.get("Ondine_Tartard")

    Bob_Raichu = data_poke.get("Bob_Raichu")
    Bob_Electrode = data_poke.get("Bob_Electrode")
    Bob_Magneton = data_poke.get("Bob_Magneton")

    Erika_Parasect = data_poke.get("Erika_Parasect")
    Erika_Rafflesia = data_poke.get("Erika_Rafflesia")
    Erika_Empiflor = data_poke.get("Erika_Empiflor")

    Koga_Grotadmorv = data_poke.get("Koga_Grotadmorv")
    Koga_Smogogo = data_poke.get("Koga_Smogogo")
    Koga_Nidoking = data_poke.get("Koga_Nidoking")

    Morgan_Noadkoko = data_poke.get("Morgan_Noadkoko")
    Morgan_Alakazam = data_poke.get("Morgan_Alakazam")
    Morgan_Aeromite = data_poke.get("Morgan_Aeromite")

    Auguste_Arcanin = data_poke.get("Auguste_Arcanin")
    Auguste_Galopa = data_poke.get("Auguste_Galopa")
    Auguste_Sulfura = data_poke.get("Auguste_Sulfura")

    Giovanni_Triopikeur = data_poke.get("Giovanni_Triopikeur")
    Giovanni_Nidoqueen = data_poke.get("Giovanni_Nidoqueen")
    Giovanni_Mewtwo = data_poke.get("Giovanni_Mewtwo")

    Red_Pikachu = data_poke.get("Red_Pikachu")
    Red_Dracaufeu = data_poke.get("Red_Dracaufeu")
    Red_Ronflex = data_poke.get("Red_Ronflex")

    



pokemon1 = Initialisation
pokemon2 = Initialisation
pokemon3 = Initialisation

pokemon_adverse1 = Arcanin
pokemon_adverse2 = Rapasdepic
pokemon_adverse3 = Nosferalto



global pokemon_actuel



max_PV_poke1 = pokemon1["PV"]
max_PV_poke2 = pokemon2["PV"]
max_PV_poke3 = pokemon3["PV"]

Attaque = "Draco-Choc"

dico_supeff = {
  "Eau" : ["Feu", "Sol", "Roche"], 
  "Feu" : ['Plante', 'Glace', 'Insect', 'Acier'],
  "Electr" : ["Eau", "Vol"],
  "Acier" : ["Glace", "Roche", "Fee"],
  "Combat" : ["Acier", "Glace", "Normal", "Roche", "Tenebr"],
  "Dragon" : ["Dragon"],
  "Glace" : ["Dragon", "Plante", "Sol", "Vol"],
  "Insect" : ["Plante", "Psy", "Tenebr"],
  "Plante" : ["Eau", "Roche", "Sol"],
  "Poison" : ["Plante", "Fee"],
  "Psy" : ["Combat", "Poison"],
  "Roche" : ["Feu", "Glace", "Insect", "Vol"],
  "Sol" : ["Acier", "Electr", "Feu", "Poison", "Roche"],
  "Spectr" : ["Psy", "Spectr"],
  "Tenebr" : ["Psy", "Spectr"],
  "Vol" : ["Combat", "Insect", "Plante"],
  "Fee" : ["Combat", "Dragon", "Tenebr"]
  }

dico_peueff = {
  "Eau" : ["Dragon", "Eau", "Plante"], 
  "Feu" : ["Dragon", "Eau", "Feu", "Roche"],
  "Electr" : ["Dragon", "Electr", "Plante"],
  "Acier" : ["Acier", "Eau", "Electr", "Feu"],
  "Combat" : ["Insect", "Poison", "Psy", "Vol", "Fee"],
  "Dragon" : ["Acier"],
  "Glace" : ["Acier", "Eau", "Feu", "Glace"],
  "Insect" : ["Acier", "Combat", "Feu", "Poison", "Spectr", "Vol", "Fee"],
  "Plante" : ["Acier", "Dragon", "Feu", "Insect", "Plante", "Poison", "Vol"],
  "Poison" : ["Poison", "Roche", "Sol", "Spectr"],
  "Psy" : ["Acier", "Psy"],
  "Roche" : ["Acier", "Combat", "Sol"],
  "Sol" : ["Eau", "Plante"],
  "Spectr" : ["Tenebr"],
  "Tenebr" : ["Combat", "Tenebr", "Fee"],
  "Vol" : ["Acier", "Electr", "Roche"],
  "Fee" : ["Acier", "Feu", "Poison"],
  "Normal" : ["Acier", "Roche"]
  }

dico_ineff = {
  "Combat" : ["Spectr"],
  "Dragon" : ["Fee"],
  "Normal" : ["Spectr"],
  "Psy" : ["Tenebr"],
  "Sol" : ["Vol"],
  "Spectr" : ["Normal"],
  "Electr": ["Sol"]
}





def selectpoke(self):
  global pokemon1
  global pokemon2
  global pokemon3
  global pokemon_actuel
  global bouton_retour2
  
  global max_PV_poke1
  global max_PV_poke2
  global max_PV_poke3

  if pokemon1 == Initialisation:
    pokemon1 = self
  elif pokemon2 == Initialisation:
    pokemon2 = self
  elif pokemon3 == Initialisation:
    pokemon3 = self
    retour_frame_home2()
    retour_frame_home()
    bouton_switchcombat = Button(frame_fenetre_home, text="Sélection du mode de jeu", command=switch_fenetre_modejeu).pack(padx=10, pady=10, side=BOTTOM)
    choix_poke.pack_forget()
    Frame2.pack_forget()

  pokemon_actuel = pokemon1
  
  global gif_mon_poke
  gif_mon_poke = PhotoImage(file=pokemon_actuel["sprite_dos"])
  gif_mon_poke = gif_mon_poke.zoom(3)
  element_gif_mon_poke = canvas_background.create_image(150, 390, image=gif_mon_poke)

  global bouton_att1
  global bouton_att2
  global bouton_att3
  global bouton_att4
  global bouton_retour
  destroy_att()
  bouton_att1 = Button(frame_attaque, text=pokemon_actuel["Att1"], command=combat1)
  bouton_att1.pack(padx=10, pady=10, side=TOP)
  bouton_att2 = Button(frame_attaque, text=pokemon_actuel["Att2"], command=combat2)
  bouton_att2.pack(padx=10, pady=10, side=TOP)
  bouton_att3 = Button(frame_attaque, text=pokemon_actuel["Att3"], command=combat3)
  bouton_att3.pack(padx=10, pady=10, side=TOP)
  bouton_att4 = Button(frame_attaque, text=pokemon_actuel["Att4"], command=combat4)
  bouton_att4.pack(padx=10, pady=10, side=TOP)
  bouton_retour = Button(frame_attaque, text="Retour", command=retour_frame_action1)
  bouton_retour.pack(padx=10, pady=10, side=TOP)

  global poke1
  global poke2
  global poke3
  destroy_poke()
  poke1 = Button(frame_changement, text=pokemon1["name"], command=change1)
  poke1.pack(padx=10, pady=10, side=TOP)
  poke2 = Button(frame_changement, text=pokemon2["name"], command=change2)
  poke2.pack(padx=10, pady=10, side=TOP)
  poke3 = Button(frame_changement, text=pokemon3["name"], command=change3)
  poke3.pack(padx=10, pady=10, side=TOP)
  bouton_retour2 = Button(frame_changement, text="Retour", command=retour_frame_action2)
  bouton_retour2.pack(padx=10, pady=10, side=TOP)

  max_PV_poke1 = pokemon1["PV"]
  max_PV_poke2 = pokemon2["PV"]
  max_PV_poke3 = pokemon3["PV"]

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

  

pokemon_actuel = pokemon1
pokemon_adverse_actuel = pokemon_adverse1

#############
#CREATION DE LA FENETRE
#############

fenetre = Tk()
fenetre.title("Pykemon")
fenetre.geometry("1200x600")
fenetre.resizable(width=False, height=False)
pygame.mixer.init()
son_precombat = pygame.mixer.Sound("sons/BattleFrontier.wav")
son_precombat.play(loops=-1, maxtime=0, fade_ms=0)
son_marathonchampions = pygame.mixer.Sound("sons/BattleGymLeader.wav")
son_conseil4 = pygame.mixer.Sound("sons/conseil4.wav")
son_maitre_league = pygame.mixer.Sound("sons/maitreligue.wav")
son_red = pygame.mixer.Sound("sons/red.wav")


#############
#FRAME HOME
#############

frame_fenetre_home = Frame(fenetre)
frame_fenetre_home.pack()

# Title
image_title = PhotoImage(file="title.png")
canvas_title = Canvas(frame_fenetre_home, width=300, height=45)
image_title = image_title.zoom(5)
element_canvas_title = canvas_title.create_image(150,32, image=image_title)
canvas_title.pack(side=TOP, pady=20)

# Frame setup team

FrameSetUp = Frame(frame_fenetre_home, borderwidth=1, relief=FLAT)
FrameSetUp.pack()

# frame 1
Frame1 = LabelFrame(FrameSetUp, text="Choose your name", borderwidth=1, relief=GROOVE)
Frame1.pack(padx=10, pady=10, side=LEFT)

# frame 2
def switch_frame_teamselection():
  frame_fenetre_home.pack_forget()
  frame_team_selection.pack()


Frame2 = LabelFrame(FrameSetUp, text="Select your Pokemon (3 max)", borderwidth=1, relief=GROOVE)
Frame2.pack(padx=10, pady=10, side=RIGHT)
var_texte = StringVar()
Entry(Frame1, textvariable=var_texte, width=20).pack(pady=10, padx=10)
choix_poke = Button(Frame2, text="Choix de votre équipe", command = switch_frame_teamselection)
choix_poke.pack()


#########
#REGLES
#########
frame_regles = Frame(fenetre)

def switch_frame_regle():
  frame_fenetre_home.pack_forget()
  frame_regles.pack()

def retour_regle():
  frame_regles.pack_forget()
  frame_fenetre_home.pack()

Button(frame_fenetre_home, text="Règles", command=switch_frame_regle).pack(padx=10, pady=10, side=BOTTOM)

texte_regles = Label(frame_regles, text="Bonjour, bienvenue dans Pykémon, \n pour jouer, vous allez devoir choisir 3 pokémons. \n Vous aurez ensuite le choix entre 3 modes de jeux. \n Pour une première partie, nous vous conseillons de prendre \n Dracaufeu, Noadkoko ainsi que Dracolosse, \n qui sont des pokémons très puissants \n et de faire le marathon des arènes, le mode de jeu le plus simple. \n Pour combattre rien de plus simple, \n il vous suffit de cliquer sur le bouton attaque de celui-ci puis de choisir l'attaque à utiliser \n Attention, toutes les attaques n'ont pas la même puissance ni la même précision. \n Pour savoir quelle attaque utiliser en priorité, il faudra les tester. \n Vous pouvez également changer de pokémon au cours d'un combat en cliquant sur le bouton \n Changement de pokemon puis en sélectionnant le pokemon que vous souhaitez envoyer au combat. \n Bonne chance jeune dresseur. \n")
texte_regles.pack()
Button(frame_regles, text="Retour", command=retour_regle).pack(padx=10, pady=10, side=BOTTOM)




#########
#SELECTION DES POKEMONS
#########

frame_team_selection = Frame(fenetre)
frame_team_selection2 = Frame(fenetre)

def switch_frame_teamselection():
  frame_fenetre_home.pack_forget()
  frame_team_selection.pack()

def switch_frame_teamselection2():
  frame_team_selection.pack_forget()
  frame_team_selection2.pack()

def retour_frame_home():
  frame_team_selection.pack_forget()
  frame_fenetre_home.pack()

def retour_frame_home2():
  frame_team_selection2.pack_forget()
  frame_team_selection.pack()

#########
#PREMIERE PAGE DE POKEMON
#########

sprite_dracaufeu = PhotoImage(file="sprite/Dracaufeu.gif")
Button(frame_team_selection, image=sprite_dracaufeu, command=lambda : selectpoke(Dracaufeu)).grid(row = 0, column = 0)
Label(frame_team_selection, text="Dracaufeu").grid(row=0, column=1)

sprite_tortank = PhotoImage(file="sprite/Tortank.gif")
Button(frame_team_selection, image=sprite_tortank, command=lambda : selectpoke(Tortank)).grid(row = 0, column = 2)
Label(frame_team_selection, text="Tortank").grid(row=0, column=3)

sprite_florizarre = PhotoImage(file="sprite/Florizarre.gif")
Button(frame_team_selection, image=sprite_florizarre, command=lambda : selectpoke(Florizarre)).grid(row = 0, column = 4)
Label(frame_team_selection, text="Florizarre").grid(row=0, column=5)

sprite_papilusion = PhotoImage(file="sprite/Papilusion.gif")
Button(frame_team_selection, image=sprite_papilusion, command= lambda : selectpoke(Papilusion)).grid(row = 0, column = 6)
Label(frame_team_selection, text="Papilusion").grid(row=0, column=7)

sprite_dardargan = PhotoImage(file="sprite/Dardargnan.gif")
Button(frame_team_selection, image=sprite_dardargan, command=lambda : selectpoke(Dardargnan)).grid(row = 0, column = 8)
Label(frame_team_selection, text="Dardargnan").grid(row=0, column=9)

sprite_roucarnage = PhotoImage(file="sprite/Roucarnage.gif")
Button(frame_team_selection, image=sprite_roucarnage, command=lambda : selectpoke(Roucarnage)).grid(row = 0, column = 10)
Label(frame_team_selection, text="Roucarnage").grid(row=0, column=11)

sprite_rattatac = PhotoImage(file="sprite/Rattatac.gif")
Button(frame_team_selection, image=sprite_rattatac, command=lambda : selectpoke(Rattatac)).grid(row = 0, column = 12)
Label(frame_team_selection, text="Rattatac").grid(row=0, column=13)

sprite_rapasdepic = PhotoImage(file="sprite/Rapasdepic.gif")
Button(frame_team_selection, image=sprite_rapasdepic, command=lambda : selectpoke(Rapasdepic)).grid(row = 1, column = 0)
Label(frame_team_selection, text="Rapasdepic").grid(row=1, column=1)

sprite_arbok = PhotoImage(file="sprite/Arbok.gif")
Button(frame_team_selection, image=sprite_arbok, command=lambda : selectpoke(Arbok)).grid(row = 1, column = 2)
Label(frame_team_selection, text="Arbok").grid(row=1, column=3)

sprite_raichu = PhotoImage(file="sprite/Raichu.gif")
Button(frame_team_selection, image=sprite_raichu, command=lambda : selectpoke(Raichu)).grid(row = 1, column = 4)
Label(frame_team_selection, text="Raichu").grid(row=1, column=5)

sprite_sablaireau= PhotoImage(file="sprite/Sablaireau.gif")
Button(frame_team_selection, image=sprite_sablaireau, command=lambda : selectpoke(Sablaireau)).grid(row = 1, column = 6)
Label(frame_team_selection, text="Sablaireau").grid(row=1, column=7)

sprite_nidoqueen= PhotoImage(file="sprite/Nidoqueen.gif")
Button(frame_team_selection, image=sprite_nidoqueen, command=lambda : selectpoke(Nidoqueen)).grid(row = 1, column = 8)
Label(frame_team_selection, text="Nidoqueen").grid(row=1, column=9)

sprite_nidoking= PhotoImage(file="sprite/Nidoking.gif")
Button(frame_team_selection, image=sprite_nidoking, command=lambda : selectpoke(Nidoking)).grid(row = 1, column = 10)
Label(frame_team_selection, text="Nidoking").grid(row=1, column=11)

sprite_melodelfe= PhotoImage(file="sprite/Melodelfe.gif")
Button(frame_team_selection, image=sprite_melodelfe, command=lambda : selectpoke(Melodelfe)).grid(row = 1, column =12)
Label(frame_team_selection, text="Melodelfe").grid(row=1, column=13)

sprite_feunard= PhotoImage(file="sprite/Feunard.gif")
Button(frame_team_selection, image=sprite_feunard, command=lambda : selectpoke(Feunard)).grid(row = 2, column = 0)
Label(frame_team_selection, text="Feunard").grid(row=2, column=1)

sprite_grodoudou= PhotoImage(file="sprite/Grodoudou.gif")
Button(frame_team_selection, image=sprite_grodoudou, command=lambda : selectpoke(Grodoudou)).grid(row = 2, column = 2)
Label(frame_team_selection, text="Grodoudou").grid(row=2, column=3)

sprite_nosferalto= PhotoImage(file="sprite/Nosferalto.gif")
Button(frame_team_selection, image=sprite_nosferalto, command=lambda : selectpoke(Nosferalto)).grid(row = 2, column = 4)
Label(frame_team_selection, text="Nosferalto").grid(row=2, column=5)

sprite_rafflesia= PhotoImage(file="sprite/Rafflesia.gif")
Button(frame_team_selection, image=sprite_rafflesia, command=lambda : selectpoke(Rafflesia)).grid(row = 2, column = 6)
Label(frame_team_selection, text="Rafflesia").grid(row=2, column=7)

sprite_parasect= PhotoImage(file="sprite/Parasect.gif")
Button(frame_team_selection, image=sprite_parasect, command=lambda : selectpoke(Parasect)).grid(row = 2, column = 8)
Label(frame_team_selection, text="Parasect").grid(row=2, column=9)

sprite_triopikeur= PhotoImage(file="sprite/Triopikeur.gif")
Button(frame_team_selection, image=sprite_triopikeur, command=lambda : selectpoke(Triopikeur)).grid(row = 2, column = 10)
Label(frame_team_selection, text="Triopikeur").grid(row=2, column=11)

sprite_persian= PhotoImage(file="sprite/Persian.gif")
Button(frame_team_selection, image=sprite_persian, command=lambda : selectpoke(Persian)).grid(row = 2, column = 12)
Label(frame_team_selection, text="Persian").grid(row=2, column=13)

sprite_akwakwak= PhotoImage(file="sprite/Akwakwak.gif")
Button(frame_team_selection, image=sprite_akwakwak, command=lambda : selectpoke(Akwakwak)).grid(row = 3, column = 0)
Label(frame_team_selection, text="Akwakwak").grid(row=3, column=1)

sprite_colossinge= PhotoImage(file="sprite/Colossinge.gif")
Button(frame_team_selection, image=sprite_colossinge, command=lambda : selectpoke(Colossinge)).grid(row = 3, column = 2)
Label(frame_team_selection, text="Colossinge").grid(row=3, column=3)

sprite_arcanin= PhotoImage(file="sprite/Arcanin.gif")
Button(frame_team_selection, image=sprite_arcanin, command=lambda : selectpoke(Arcanin)).grid(row = 3, column = 4)
Label(frame_team_selection, text="Arcanin").grid(row=3, column=5)

sprite_tartard= PhotoImage(file="sprite/Tartard.gif")
Button(frame_team_selection, image=sprite_tartard, command=lambda : selectpoke(Tartard)).grid(row = 3, column = 6)
Label(frame_team_selection, text="Tartard").grid(row=3, column=7)

sprite_alakazam= PhotoImage(file="sprite/Alakazam.gif")
Button(frame_team_selection, image=sprite_alakazam, command=lambda : selectpoke(Alakazam)).grid(row = 3, column = 8)
Label(frame_team_selection, text="Alakazam").grid(row=3, column=9)

sprite_mackogneur= PhotoImage(file="sprite/Mackogneur.gif")
Button(frame_team_selection, image=sprite_mackogneur, command=lambda : selectpoke(Mackogneur)).grid(row = 3, column = 10)
Label(frame_team_selection, text="Mackogneur").grid(row=3, column=11)

sprite_empiflor= PhotoImage(file="sprite/Empiflor.gif")
Button(frame_team_selection, image=sprite_empiflor, command=lambda : selectpoke(Empiflor)).grid(row = 3, column = 12)
Label(frame_team_selection, text="Empiflor").grid(row=3, column=13)

sprite_tentacruel= PhotoImage(file="sprite/Tentacruel.gif")
Button(frame_team_selection, image=sprite_tentacruel, command=lambda : selectpoke(Tentacruel)).grid(row = 4, column = 0)
Label(frame_team_selection, text="Tentacruel").grid(row=4, column=1)

sprite_aeromite= PhotoImage(file="sprite/Aeromite.gif")
Button(frame_team_selection, image=sprite_aeromite, command=lambda : selectpoke(Aeromite)).grid(row = 4, column = 2)
Label(frame_team_selection, text="Aeromite").grid(row=4, column=3)

sprite_grolem= PhotoImage(file="sprite/Grolem.gif")
Button(frame_team_selection, image=sprite_grolem, command=lambda : selectpoke(Grolem)).grid(row = 4, column = 4)
Label(frame_team_selection, text="Grolem").grid(row=4, column=5)

sprite_galopa= PhotoImage(file="sprite/Galopa.gif")
Button(frame_team_selection, image=sprite_galopa, command=lambda : selectpoke(Galopa)).grid(row = 4, column = 6)
Label(frame_team_selection, text="Galopa").grid(row=4, column=7)

sprite_flagadoss= PhotoImage(file="sprite/Flagadoss.gif")
Button(frame_team_selection, image=sprite_flagadoss, command=lambda : selectpoke(Flagadoss)).grid(row = 4, column = 8)
Label(frame_team_selection, text="Flagadoss").grid(row=4, column=9)

sprite_magneton= PhotoImage(file="sprite/Magneton.gif")
Button(frame_team_selection, image=sprite_magneton, command=lambda : selectpoke(Magneton)).grid(row = 4, column = 10)
Label(frame_team_selection, text="Magneton").grid(row=4, column=11)

sprite_canarticho= PhotoImage(file="sprite/Canarticho.gif")
Button(frame_team_selection, image=sprite_canarticho, command=lambda : selectpoke(Canarticho)).grid(row = 4, column = 12)
Label(frame_team_selection, text="Canarticho").grid(row=4, column=13)

sprite_dodrio= PhotoImage(file="sprite/Dodrio.gif")
Button(frame_team_selection, image=sprite_dodrio, command=lambda : selectpoke(Dodrio)).grid(row = 5, column = 0)
Label(frame_team_selection, text="Dodrio").grid(row=5, column=1)

sprite_lamantine= PhotoImage(file="sprite/Lamantine.gif")
Button(frame_team_selection, image=sprite_lamantine, command=lambda : selectpoke(Lamantine)).grid(row = 5, column = 2)
Label(frame_team_selection, text="Lamantine").grid(row=5, column=3)

sprite_grotadmorv= PhotoImage(file="sprite/Grotadmorv.gif")
Button(frame_team_selection, image=sprite_grotadmorv, command=lambda : selectpoke(Grotadmorv)).grid(row = 5, column = 4)
Label(frame_team_selection, text="Grotadmorv").grid(row=5, column=5)

sprite_crustabri= PhotoImage(file="sprite/Crustabri.gif")
Button(frame_team_selection, image=sprite_crustabri, command=lambda : selectpoke(Crustabri)).grid(row = 5, column = 6)
Label(frame_team_selection, text="Crustabri").grid(row=5, column=7)

sprite_ectoplasma= PhotoImage(file="sprite/Ectoplasma.gif")
Button(frame_team_selection, image=sprite_ectoplasma, command=lambda : selectpoke(Ectoplasma)).grid(row = 5, column = 8)
Label(frame_team_selection, text="Ectoplasma").grid(row=5, column=9)

sprite_onix= PhotoImage(file="sprite/Onix.gif")
Button(frame_team_selection, image=sprite_onix, command=lambda : selectpoke(Onix)).grid(row = 5, column = 10)
Label(frame_team_selection, text="Onix").grid(row=5, column=11)

sprite_hypnomade= PhotoImage(file="sprite/Hypnomade.gif")
Button(frame_team_selection, image=sprite_hypnomade, command=lambda : selectpoke(Hypnomade)).grid(row = 5, column = 12)
Label(frame_team_selection, text="Hypnomade").grid(row=5, column=13)

sprite_krabboss= PhotoImage(file="sprite/Krabboss.gif")
Button(frame_team_selection, image=sprite_krabboss, command=lambda : selectpoke(Krabboss)).grid(row = 6, column = 0)
Label(frame_team_selection, text="Krabboss").grid(row=6, column=1)

sprite_electrode= PhotoImage(file="sprite/Electrode.gif")
Button(frame_team_selection, image=sprite_electrode, command=lambda : selectpoke(Electrode)).grid(row = 6, column = 2)
Label(frame_team_selection, text="Electrode").grid(row=6, column=3)

sprite_noadkoko= PhotoImage(file="sprite/Noadkoko.gif")
Button(frame_team_selection, image=sprite_noadkoko, command=lambda : selectpoke(Noadkoko)).grid(row = 6, column = 4)
Label(frame_team_selection, text="Noadkoko").grid(row=6, column=5)

sprite_ossatueur= PhotoImage(file="sprite/Ossatueur.gif")
Button(frame_team_selection, image=sprite_ossatueur, command=lambda : selectpoke(Ossatueur)).grid(row = 6, column = 6)
Label(frame_team_selection, text="Ossatueur").grid(row=6, column=7)

sprite_kicklee= PhotoImage(file="sprite/Kicklee.gif")
Button(frame_team_selection, image=sprite_kicklee, command=lambda : selectpoke(Kicklee)).grid(row = 6, column = 8)
Label(frame_team_selection, text="Kicklee").grid(row=6, column=9)

sprite_tygnon= PhotoImage(file="sprite/Tygnon.gif")
Button(frame_team_selection, image=sprite_tygnon, command=lambda : selectpoke(Tygnon)).grid(row = 6, column = 10)
Label(frame_team_selection, text="Tygnon").grid(row=6, column=11)


page_suivante_teamselection = Button(frame_team_selection, text="Page suivante", command=switch_frame_teamselection2)
page_suivante_teamselection.grid(row=6, column=12)




#########
#FIN DE LA PREMIERE PAGE DE POKEMON
#########

#########
#DEUXIEME PAGE DE POKEMON
#########

sprite_excelangue= PhotoImage(file="sprite/Excelangue.gif")
Button(frame_team_selection2, image=sprite_excelangue, command=lambda : selectpoke(Excelangue)).grid(row = 0, column = 0)
Label(frame_team_selection2, text="Excelangue").grid(row=0, column=1)

sprite_smogogo= PhotoImage(file="sprite/Smogogo.gif")
Button(frame_team_selection2, image=sprite_smogogo, command=lambda : selectpoke(Smogogo)).grid(row = 0, column = 2)
Label(frame_team_selection2, text="Smogogo").grid(row=0, column=3)

sprite_rhinoferos= PhotoImage(file="sprite/Rhinoferos.gif")
Button(frame_team_selection2, image=sprite_rhinoferos, command=lambda : selectpoke(Rhinoferos)).grid(row = 0, column = 4)
Label(frame_team_selection2, text="Rhinoferos").grid(row=0, column=5)

sprite_leveinard= PhotoImage(file="sprite/Leveinard.gif")
Button(frame_team_selection2, image=sprite_leveinard, command=lambda : selectpoke(Leveinard)).grid(row = 0, column = 6)
Label(frame_team_selection2, text="Leveinard").grid(row=0, column=7)

sprite_kangourex= PhotoImage(file="sprite/Kangourex.gif")
Button(frame_team_selection2, image=sprite_kangourex, command=lambda : selectpoke(Kangourex)).grid(row = 0, column = 8)
Label(frame_team_selection2, text="Kangourex").grid(row=0, column=9)

sprite_hypocean= PhotoImage(file="sprite/Hypocean.gif")
Button(frame_team_selection2, image=sprite_hypocean, command=lambda : selectpoke(Hypocean)).grid(row = 0, column = 10)
Label(frame_team_selection2, text="Hypocean").grid(row=0, column=11)

sprite_poissoroy= PhotoImage(file="sprite/Poissoroy.gif")
Button(frame_team_selection2, image=sprite_poissoroy, command=lambda : selectpoke(Poissoroy)).grid(row = 0, column = 12)
Label(frame_team_selection2, text="Poissoroy").grid(row=0, column=13)

sprite_staross= PhotoImage(file="sprite/Staross.gif")
Button(frame_team_selection2, image=sprite_staross, command=lambda : selectpoke(Staross)).grid(row = 1, column = 0)
Label(frame_team_selection2, text="Staross").grid(row=1, column=1)

sprite_insecateur= PhotoImage(file="sprite/Insecateur.gif")
Button(frame_team_selection2, image=sprite_insecateur, command=lambda : selectpoke(Insecateur)).grid(row = 1, column = 2)
Label(frame_team_selection2, text="Insecateur").grid(row=1, column=3)

sprite_lippoutou= PhotoImage(file="sprite/Lippoutou.gif")
Button(frame_team_selection2, image=sprite_lippoutou, command=lambda : selectpoke(Lippoutou)).grid(row = 1, column = 4)
Label(frame_team_selection2, text="Lippoutou").grid(row=1, column=5)

sprite_elektek= PhotoImage(file="sprite/Elektek.gif")
Button(frame_team_selection2, image=sprite_elektek, command=lambda : selectpoke(Elektek)).grid(row = 1, column = 6)
Label(frame_team_selection2, text="Elektek").grid(row=1, column=7)

sprite_magmar= PhotoImage(file="sprite/Magmar.gif")
Button(frame_team_selection2, image=sprite_magmar, command=lambda : selectpoke(Magmar)).grid(row = 1, column = 8)
Label(frame_team_selection2, text="Magmar").grid(row=1, column=9)

sprite_scarabrute= PhotoImage(file="sprite/Scarabrute.gif")
Button(frame_team_selection2, image=sprite_scarabrute, command=lambda : selectpoke(Scarabrute)).grid(row = 1, column = 10)
Label(frame_team_selection2, text="Scarabrute").grid(row=1, column=11)

sprite_tauros= PhotoImage(file="sprite/Tauros.gif")
Button(frame_team_selection2, image=sprite_tauros, command=lambda : selectpoke(Tauros)).grid(row = 1, column = 12)
Label(frame_team_selection2, text="Tauros").grid(row=1, column=13)

sprite_leviator= PhotoImage(file="sprite/Leviator.gif")
Button(frame_team_selection2, image=sprite_leviator, command=lambda : selectpoke(Leviator)).grid(row = 2, column = 0)
Label(frame_team_selection2, text="Leviator").grid(row=2, column=1)

sprite_lokhlass= PhotoImage(file="sprite/Lokhlass.gif")
Button(frame_team_selection2, image=sprite_lokhlass, command=lambda : selectpoke(Lokhlass)).grid(row = 2, column = 2)
Label(frame_team_selection2, text="Lokhlass").grid(row=2, column=3)

sprite_aquali= PhotoImage(file="sprite/Aquali.gif")
Button(frame_team_selection2, image=sprite_aquali, command=lambda : selectpoke(Aquali)).grid(row = 2, column = 4)
Label(frame_team_selection2, text="Aquali").grid(row=2, column=5)

sprite_voltali= PhotoImage(file="sprite/Voltali.gif")
Button(frame_team_selection2, image=sprite_voltali, command=lambda : selectpoke(Voltali)).grid(row = 2, column = 6)
Label(frame_team_selection2, text="Voltali").grid(row=2, column=7)

sprite_pyroli= PhotoImage(file="sprite/Pyroli.gif")
Button(frame_team_selection2, image=sprite_pyroli, command=lambda : selectpoke(Pyroli)).grid(row = 2, column = 8)
Label(frame_team_selection2, text="Pyroli").grid(row=2, column=9)

sprite_porygon= PhotoImage(file="sprite/Porygon.gif")
Button(frame_team_selection2, image=sprite_porygon, command=lambda : selectpoke(Porygon)).grid(row = 2, column = 10)
Label(frame_team_selection2, text="Porygon").grid(row=2, column=11)

sprite_amonistar= PhotoImage(file="sprite/Amonistar.gif")
Button(frame_team_selection2, image=sprite_amonistar, command=lambda : selectpoke(Amonistar)).grid(row = 2, column = 12)
Label(frame_team_selection2, text="Amonistar").grid(row=2, column=13)

sprite_kabutops= PhotoImage(file="sprite/Kabutops.gif")
Button(frame_team_selection2, image=sprite_kabutops, command=lambda : selectpoke(Kabutops)).grid(row = 3, column = 0)
Label(frame_team_selection2, text="Kabutops").grid(row=3, column=1)

sprite_ptera= PhotoImage(file="sprite/Ptera.gif")
Button(frame_team_selection2, image=sprite_ptera, command=lambda : selectpoke(Ptera)).grid(row = 3, column = 2)
Label(frame_team_selection2, text="Ptera").grid(row=3, column=3)

sprite_ronflex= PhotoImage(file="sprite/Ronflex.gif")
Button(frame_team_selection2, image=sprite_ronflex, command=lambda : selectpoke(Ronflex)).grid(row = 3, column = 4)
Label(frame_team_selection2, text="Ronflex").grid(row=3, column=5)

sprite_artikodin= PhotoImage(file="sprite/artikodin.gif")
Button(frame_team_selection2, image=sprite_artikodin, command=lambda : selectpoke(Artikodin)).grid(row = 3, column = 6)
Label(frame_team_selection2, text="Artikodin").grid(row=3, column=7)

sprite_electhor= PhotoImage(file="sprite/Electhor.gif")
Button(frame_team_selection2, image=sprite_electhor, command=lambda : selectpoke(Electhor)).grid(row = 3, column = 8)
Label(frame_team_selection2, text="Electhor").grid(row=3, column=9)

sprite_sulfura= PhotoImage(file="sprite/Sulfura.gif")
Button(frame_team_selection2, image=sprite_sulfura, command=lambda : selectpoke(Sulfura)).grid(row = 3, column = 10)
Label(frame_team_selection2, text="Sulfura").grid(row=3, column=11)

sprite_dracolosse= PhotoImage(file="sprite/Dracolosse.gif")
Button(frame_team_selection2, image=sprite_dracolosse, command=lambda : selectpoke(Dracolosse)).grid(row = 3, column = 12)
Label(frame_team_selection2, text="Dracolosse").grid(row=3, column=13)

sprite_mewtwo= PhotoImage(file="sprite/Mewtwo.gif")
Button(frame_team_selection2, image=sprite_mewtwo, command=lambda : selectpoke(Mewtwo)).grid(row = 4, column = 0)
Label(frame_team_selection2, text="Mewtwo").grid(row=4, column=1)

sprite_mew= PhotoImage(file="sprite/Mew.gif")
Button(frame_team_selection2, image=sprite_mew, command=lambda : selectpoke(Mew)).grid(row = 4, column = 2)
Label(frame_team_selection2, text="Mew").grid(row=4, column=3)

retour_teamselection2 = Button(frame_team_selection2, text="Page précédente", command=retour_frame_home2)
retour_teamselection2.grid(row=5, column=13)

#########
#FIN DE LA DEUXIEME PAGE DE POKEMON
#########

# Visualisation des poke et de leurs caractéristiques
canvas = Canvas(frame_fenetre_home, width=500, height=150, bg='ivory')
txt = canvas.create_text(250, 75, text="Pokemon", font="Arial 16 italic", fill="pink")
canvas.pack(pady=10)


#########
#ECRAN DE FIN
#########


frame_win_champions = Frame(fenetre)
texte_win_champions = Label(frame_win_champions, text="Félicitation jeune dresseur, \n tu as vaincu les 8 champions de la régions de Kanto.")
texte_win_champions.pack()
Button(frame_win_champions, text="Retour au bureau", command=frame_win_champions.quit).pack(padx=10, pady=10, side=BOTTOM)

frame_win_ligue = Frame(fenetre)
texte_win_ligue = Label(frame_win_ligue, text="Félicitation jeune dresseur, \n tu as vaincu le conseil 4 ainsi que le Maitre de la région de Kanto.")
texte_win_ligue.pack()
Button(frame_win_ligue, text="Retour au bureau", command=frame_win_ligue.quit).pack(padx=10, pady=10, side=BOTTOM)

frame_win_red = Frame(fenetre)
texte_win_red = Label(frame_win_red, text="Félicitation jeune dresseur, \n tu as vaincu Red le dresseur légendaire.")
texte_win_red.pack()
Button(frame_win_red, text="Retour au bureau", command=frame_win_red.quit).pack(padx=10, pady=10, side=BOTTOM)




##########
#FRAME MODE DE JEU
##########

frame_fenetre_modejeu = Frame(fenetre)
image_title2 = PhotoImage(file="title2.png")
canvas_title2 = Canvas(frame_fenetre_modejeu, width=300, height=45)
image_title2 = image_title2.zoom(5)
element_canvas_title = canvas_title2.create_image(150,32, image=image_title2)
canvas_title2.pack(side=TOP, pady=20)

frame_choix_modejeu = Frame(frame_fenetre_modejeu)
frame_choix_modejeu.pack()

frame_marathonchampions = LabelFrame(frame_choix_modejeu, text="Marathon des champions", borderwidth=1, relief=GROOVE)
frame_marathonchampions.grid(row = 0, column = 0, sticky = N, padx = 10)
texte_marathonchampions = Label(frame_marathonchampions, text="Confrontez vous aux 8 champions \n d'arène de la région de Kanto")
texte_marathonchampions.pack()

frame_plateauindigo = LabelFrame(frame_choix_modejeu, text="Plateau indigo", borderwidth=1, relief=GROOVE)
frame_plateauindigo.grid(row = 0, column = 1, sticky = N, padx = 10)
texte_plateauindigo = Label(frame_plateauindigo, text="Affrontez le renommé conseil des 4 et le \n maitre de la ligue de Kanto, le plateau indigo.")
texte_plateauindigo.pack()

frame_ash = LabelFrame(frame_fenetre_modejeu, text="Dresseur légendaire", borderwidth=1, relief=GROOVE)
frame_ash.pack(pady=10)
texte_ash = Label(frame_ash, text="Combattez Red dans un combat \n pokemon au plus haut niveau.")
texte_ash.pack()


frame_ligue = Frame(fenetre)
frame_champions = Frame(fenetre)







def pop_frame_changement () :
  frame_action.grid_forget()
  frame_changement.grid(row = 0, column = 1, sticky = N, pady = 20)

def pop_frame_attaque () :
  frame_action.grid_forget()
  frame_attaque.grid(row = 0, column = 1, sticky = N, pady = 20)

def retour_frame_action1 () :
  frame_attaque.grid_forget()
  frame_action.grid(row = 0, column = 1, sticky = N, pady = 20)

def retour_frame_action2 () :
  frame_changement.grid_forget()
  frame_action.grid(row = 0, column = 1, sticky = N, pady = 20)



##########
#FONCTIONS ACTIONS COMBAT
##########

##########
#FRAME FENETRE COMBAT
##########

frame_fenetre_combat = Frame(fenetre)

##########
#CANVAS POUR L'AFFICHAGE DU COMBAT 
##########

image_background = PhotoImage(file="background.png")
image_background = image_background.zoom(2)
gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
gif_poke_adverse = gif_poke_adverse.zoom(3)
gif_mon_poke = PhotoImage(file=pokemon_actuel["sprite_dos"])
gif_mon_poke = gif_mon_poke.zoom(3)
canvas_background = Canvas(frame_fenetre_combat, width=1000, height=500)
element_canvas_background = canvas_background.create_image(500, 250, image=image_background)
element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
element_gif_mon_poke = canvas_background.create_image(150, 390, image=gif_mon_poke)
canvas_background.grid(row = 0, column = 0, sticky = NW)

def destroy_att():
  bouton_att1.destroy()
  bouton_att2.destroy()
  bouton_att3.destroy()
  bouton_att4.destroy()
  bouton_retour.destroy()


def destroy_poke():
  poke1.destroy()
  poke2.destroy()
  poke3.destroy()
  bouton_retour2.destroy()


def change1():
  ##On change tous ce qui concerne le poké sorti
  ##par tout ce qui concerne le poké entrant
  global gif_mon_poke
  global pokemon_actuel
  global bouton_att1
  global bouton_att2
  global bouton_att3
  global bouton_att4
  global bouton_retour
  pokemon_actuel = pokemon1
  gif_mon_poke = PhotoImage(file=pokemon_actuel["sprite_dos"])
  gif_mon_poke = gif_mon_poke.zoom(3)
  element_gif_mon_poke = canvas_background.create_image(150, 390, image=gif_mon_poke)
  ##On refait les attaques
  destroy_att()
  bouton_att1 = Button(frame_attaque, text=pokemon_actuel["Att1"], command=combat1)
  bouton_att1.pack(padx=10, pady=10, side=TOP)
  bouton_att2 = Button(frame_attaque, text=pokemon_actuel["Att2"], command=combat2)
  bouton_att2.pack(padx=10, pady=10, side=TOP)
  bouton_att3 = Button(frame_attaque, text=pokemon_actuel["Att3"], command=combat3)
  bouton_att3.pack(padx=10, pady=10, side=TOP)
  bouton_att4 = Button(frame_attaque, text=pokemon_actuel["Att4"], command=combat4)
  bouton_att4.pack(padx=10, pady=10, side=TOP)
  bouton_retour = Button(frame_attaque, text="Retour", command=retour_frame_action1)
  bouton_retour.pack(padx=10, pady=10, side=TOP)
  retour_frame_action2()

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)


def change2():
  ##On change tous ce qui concerne le poké sorti
  ##par tout ce qui concerne le poké entrant
  global gif_mon_poke
  global pokemon_actuel
  global bouton_att1
  global bouton_att2
  global bouton_att3
  global bouton_att4
  global bouton_retour
  pokemon_actuel = pokemon2
  gif_mon_poke = PhotoImage(file=pokemon_actuel["sprite_dos"])
  gif_mon_poke = gif_mon_poke.zoom(3)
  element_gif_mon_poke = canvas_background.create_image(150, 390, image=gif_mon_poke)
  ##On refait les attaques
  destroy_att()
  bouton_att1 = Button(frame_attaque, text=pokemon_actuel["Att1"], command=combat1)
  bouton_att1.pack(padx=10, pady=10, side=TOP)
  bouton_att2 = Button(frame_attaque, text=pokemon_actuel["Att2"], command=combat2)
  bouton_att2.pack(padx=10, pady=10, side=TOP)
  bouton_att3 = Button(frame_attaque, text=pokemon_actuel["Att3"], command=combat3)
  bouton_att3.pack(padx=10, pady=10, side=TOP)
  bouton_att4 = Button(frame_attaque, text=pokemon_actuel["Att4"], command=combat4)
  bouton_att4.pack(padx=10, pady=10, side=TOP)
  bouton_retour = Button(frame_attaque, text="Retour", command=retour_frame_action1)
  bouton_retour.pack(padx=10, pady=10, side=TOP)
  retour_frame_action2()
  ##On actualise la frame PV
  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)


def change3():
  ##On change tous ce qui concerne le poké sorti
  ##par tout ce qui concerne le poké entrant
  global gif_mon_poke
  global pokemon_actuel
  global bouton_att1
  global bouton_att2
  global bouton_att3
  global bouton_att4
  global bouton_retour
  pokemon_actuel = pokemon3
  gif_mon_poke = PhotoImage(file=pokemon_actuel["sprite_dos"])
  gif_mon_poke = gif_mon_poke.zoom(3)
  element_gif_mon_poke = canvas_background.create_image(150, 390, image=gif_mon_poke)
  ##On refait les attaques
  destroy_att()
  bouton_att1 = Button(frame_attaque, text=pokemon_actuel["Att1"], command=combat1)
  bouton_att1.pack(padx=10, pady=10, side=TOP)
  bouton_att2 = Button(frame_attaque, text=pokemon_actuel["Att2"], command=combat2)
  bouton_att2.pack(padx=10, pady=10, side=TOP)
  bouton_att3 = Button(frame_attaque, text=pokemon_actuel["Att3"], command=combat3)
  bouton_att3.pack(padx=10, pady=10, side=TOP)
  bouton_att4 = Button(frame_attaque, text=pokemon_actuel["Att4"], command=combat4)
  bouton_att4.pack(padx=10, pady=10, side=TOP)
  bouton_retour = Button(frame_attaque, text="Retour", command=retour_frame_action1)
  bouton_retour.pack(padx=10, pady=10, side=TOP)
  retour_frame_action2()
  ##On actualise la frame PV
  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

  
  
def changeadverse():
  global gif_poke_adverse
  global pokemon_adverse_actuel
  global label_poke_adverse
  if pokemon_adverse_actuel["PV"] <= 0:
    pokemon_adverse_actuel = pokemon_adverse2
    gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
    gif_poke_adverse = gif_poke_adverse.zoom(3)
    element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
    label_poke_adverse.grid_forget()
    label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)

    if pokemon_adverse_actuel["PV"] <= 0:
      pokemon_adverse_actuel = pokemon_adverse3
      gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
      gif_poke_adverse = gif_poke_adverse.zoom(3)
      element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
      label_poke_adverse.grid_forget()
      label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
      label_poke_adverse.grid(row=1, column=0, sticky=NW)



#SUPER EFFICACE

def supeff():
  global degats
  global Attaque
  typeatt = data_pui.get(Attaque)
  if typeatt["type"] == 'Eau':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Eau"] or pokemon_adverse_actuel["type2"] in dico_supeff["Eau"]:
      degats *= 2
  elif typeatt["type"] == 'Feu':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Feu"] or pokemon_adverse_actuel["type2"] in dico_supeff["Feu"]:
      degats *= 2
  elif typeatt["type"] == 'Plante':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Plante"] or pokemon_adverse_actuel["type2"] in dico_supeff["Plante"]:
      degats *= 2
  elif typeatt["type"] == 'Vol':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Vol"] or pokemon_adverse_actuel["type2"] in dico_supeff["Vol"]:
      degats *= 2
  elif typeatt["type"] == 'Combat':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Combat"] or pokemon_adverse_actuel["type2"] in dico_supeff["Combat"]:
      degats *= 2
  elif typeatt["type"] == 'Electr':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Electr"] or pokemon_adverse_actuel["type2"] in dico_supeff["Electr"]:
      degats *= 2
  elif typeatt["type"] == 'Acier':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Acier"] or pokemon_adverse_actuel["type2"] in dico_supeff["Acier"]:
      degats *= 2
  elif typeatt["type"] == 'Dragon':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Dragon"] or pokemon_adverse_actuel["type2"] in dico_supeff["Dragon"]:
      degats *= 2
  elif typeatt["type"] == 'Insect':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Insect"] or pokemon_adverse_actuel["type2"] in dico_supeff["Insect"]:
      degats *= 2
  elif typeatt["type"] == 'Psy':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Psy"] or pokemon_adverse_actuel["type2"] in dico_supeff["Psy"]:
      degats *= 2
  elif typeatt["type"] == 'Spectr':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Spectr"] or pokemon_adverse_actuel["type2"] in dico_supeff["Spectr"]:
      degats *= 2
  elif typeatt["type"] == 'Tenebr':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Tenebr"] or pokemon_adverse_actuel["type2"] in dico_supeff["Tenebr"]:
      degats *= 2
  elif typeatt["type"] == 'Glace':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Glace"] or pokemon_adverse_actuel["type2"] in dico_supeff["Glace"]:
      degats *= 2
  elif typeatt["type"] == 'Poison':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Poison"] or pokemon_adverse_actuel["type2"] in dico_supeff["Poison"]:
      degats *= 2
  elif typeatt["type"] == 'Roche':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Roche"] or pokemon_adverse_actuel["type2"] in dico_supeff["Roche"]:
      degats *= 2
  elif typeatt["type"] == 'Sol':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Sol"] or pokemon_adverse_actuel["type2"] in dico_supeff["Sol"]:
      degats *= 2
  elif typeatt["type"] == 'Fee':
    if pokemon_adverse_actuel["type1"] in dico_supeff["Fee"] or pokemon_adverse_actuel["type2"] in dico_supeff["Fee"]:
      degats *= 2

def peueff():
  global degats
  global Attaque
  typeatt = data_pui.get(Attaque)
  if typeatt["type"] == 'Eau':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Eau"] or pokemon_adverse_actuel["type2"] in dico_peueff["Eau"]:
      degats *= 0.5
  elif typeatt["type"] == 'Feu':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Feu"] or pokemon_adverse_actuel["type2"] in dico_peueff["Feu"]:
      degats *= 0.5
  elif typeatt["type"] == 'Plante':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Plante"] or pokemon_adverse_actuel["type2"] in dico_peueff["Plante"]:
      degats *= 0.5
  elif typeatt["type"] == 'Vol':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Vol"] or pokemon_adverse_actuel["type2"] in dico_peueff["Vol"]:
      degats *= 0.5
  elif typeatt["type"] == 'Combat':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Combat"] or pokemon_adverse_actuel["type2"] in dico_peueff["Combat"]:
      degats *= 0.5
  elif typeatt["type"] == 'Electr':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Electr"] or pokemon_adverse_actuel["type2"] in dico_peueff["Electr"]:
      degats *= 0.5
  elif typeatt["type"] == 'Acier':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Acier"] or pokemon_adverse_actuel["type2"] in dico_peueff["Acier"]:
      degats *= 0.5
  elif typeatt["type"] == 'Dragon':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Dragon"] or pokemon_adverse_actuel["type2"] in dico_peueff["Dragon"]:
      degats *= 0.5
  elif typeatt["type"] == 'Insect':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Insect"] or pokemon_adverse_actuel["type2"] in dico_peueff["Insect"]:
      degats *= 0.5
  elif typeatt["type"] == 'Psy':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Psy"] or pokemon_adverse_actuel["type2"] in dico_peueff["Psy"]:
      degats *= 0.5
  elif typeatt["type"] == 'Spectr':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Spectr"] or pokemon_adverse_actuel["type2"] in dico_peueff["Spectr"]:
      degats *= 0.5
  elif typeatt["type"] == 'Tenebr':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Tenebr"] or pokemon_adverse_actuel["type2"] in dico_peueff["Tenebr"]:
      degats *= 0.5
  elif typeatt["type"] == 'Glace':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Glace"] or pokemon_adverse_actuel["type2"] in dico_peueff["Glace"]:
      degats *= 0.5
  elif typeatt["type"] == 'Poison':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Poison"] or pokemon_adverse_actuel["type2"] in dico_peueff["Poison"]:
      degats *= 0.5
  elif typeatt["type"] == 'Roche':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Roche"] or pokemon_adverse_actuel["type2"] in dico_peueff["Roche"]:
      degats *= 0.5
  elif typeatt["type"] == 'Sol':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Sol"] or pokemon_adverse_actuel["type2"] in dico_peueff["Sol"]:
      degats *= 0.5
  elif typeatt["type"] == 'Fee':
    if pokemon_adverse_actuel["type1"] in dico_peueff["Fee"] or pokemon_adverse_actuel["type2"] in dico_peueff["Fee"]:
      degats *= 0.5

def supeff_adverse():
  global degats_adverse
  global Attaque_adverse
  typeatt_adverse = data_pui.get(Attaque_adverse)
  if typeatt_adverse["type"] == 'Eau':
    if pokemon_actuel["type1"] in dico_supeff["Eau"] or pokemon_actuel["type2"] in dico_supeff["Eau"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Feu':
    if pokemon_actuel["type1"] in dico_supeff["Feu"] or pokemon_actuel["type2"] in dico_supeff["Feu"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Plante':
    if pokemon_actuel["type1"] in dico_supeff["Plante"] or pokemon_actuel["type2"] in dico_supeff["Plante"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Vol':
    if pokemon_actuel["type1"] in dico_supeff["Vol"] or pokemon_actuel["type2"] in dico_supeff["Vol"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Combat':
    if pokemon_actuel["type1"] in dico_supeff["Combat"] or pokemon_actuel["type2"] in dico_supeff["Combat"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Electr':
    if pokemon_actuel["type1"] in dico_supeff["Electr"] or pokemon_actuel["type2"] in dico_supeff["Electr"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Acier':
    if pokemon_actuel["type1"] in dico_supeff["Acier"] or pokemon_actuel["type2"] in dico_supeff["Acier"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Dragon':
    if pokemon_actuel["type1"] in dico_supeff["Dragon"] or pokemon_actuel["type2"] in dico_supeff["Dragon"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Insect':
    if pokemon_actuel["type1"] in dico_supeff["Insect"] or pokemon_actuel["type2"] in dico_supeff["Insect"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Psy':
    if pokemon_actuel["type1"] in dico_supeff["Psy"] or pokemon_actuel["type2"] in dico_supeff["Psy"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Spectr':
    if pokemon_actuel["type1"] in dico_supeff["Spectr"] or pokemon_actuel["type2"] in dico_supeff["Spectr"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Tenebr':
    if pokemon_actuel["type1"] in dico_supeff["Tenebr"] or pokemon_actuel["type2"] in dico_supeff["Tenebr"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Glace':
    if pokemon_actuel["type1"] in dico_supeff["Glace"] or pokemon_actuel["type2"] in dico_supeff["Glace"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Poison':
    if pokemon_actuel["type1"] in dico_supeff["Poison"] or pokemon_actuel["type2"] in dico_supeff["Poison"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Roche':
    if pokemon_actuel["type1"] in dico_supeff["Roche"] or pokemon_actuel["type2"] in dico_supeff["Roche"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Sol':
    if pokemon_actuel["type1"] in dico_supeff["Sol"] or pokemon_actuel["type2"] in dico_supeff["Sol"]:
      degats_adverse *= 2
  elif typeatt_adverse["type"] == 'Fee':
    if pokemon_actuel["type1"] in dico_supeff["Fee"] or pokemon_actuel["type2"] in dico_supeff["Fee"]:
      degats_adverse *= 2

def peueff_adverse():
  global degats_adverse
  global Attaque_adverse
  typeatt_adverse = data_pui.get(Attaque_adverse)
  if typeatt_adverse["type"] == 'Eau':
    if pokemon_actuel["type1"] in dico_peueff["Eau"] or pokemon_actuel["type2"] in dico_peueff["Eau"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Feu':
    if pokemon_actuel["type1"] in dico_peueff["Feu"] or pokemon_actuel["type2"] in dico_peueff["Feu"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Plante':
    if pokemon_actuel["type1"] in dico_peueff["Plante"] or pokemon_actuel["type2"] in dico_peueff["Plante"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Vol':
    if pokemon_actuel["type1"] in dico_peueff["Vol"] or pokemon_actuel["type2"] in dico_peueff["Vol"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Combat':
    if pokemon_actuel["type1"] in dico_peueff["Combat"] or pokemon_actuel["type2"] in dico_peueff["Combat"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Electr':
    if pokemon_actuel["type1"] in dico_peueff["Electr"] or pokemon_actuel["type2"] in dico_peueff["Electr"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Acier':
    if pokemon_actuel["type1"] in dico_peueff["Acier"] or pokemon_actuel["type2"] in dico_peueff["Acier"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Dragon':
    if pokemon_actuel["type1"] in dico_peueff["Dragon"] or pokemon_actuel["type2"] in dico_peueff["Dragon"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Insect':
    if pokemon_actuel["type1"] in dico_peueff["Insect"] or pokemon_actuel["type2"] in dico_peueff["Insect"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Psy':
    if pokemon_actuel["type1"] in dico_peueff["Psy"] or pokemon_actuel["type2"] in dico_peueff["Psy"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Spectr':
    if pokemon_actuel["type1"] in dico_peueff["Spectr"] or pokemon_actuel["type2"] in dico_peueff["Spectr"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Tenebr':
    if pokemon_actuel["type1"] in dico_peueff["Tenebr"] or pokemon_actuel["type2"] in dico_peueff["Tenebr"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Glace':
    if pokemon_actuel["type1"] in dico_peueff["Glace"] or pokemon_actuel["type2"] in dico_peueff["Glace"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Poison':
    if pokemon_actuel["type1"] in dico_peueff["Poison"] or pokemon_actuel["type2"] in dico_peueff["Poison"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Roche':
    if pokemon_actuel["type1"] in dico_peueff["Roche"] or pokemon_actuel["type2"] in dico_peueff["Roche"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Sol':
    if pokemon_actuel["type1"] in dico_peueff["Sol"] or pokemon_actuel["type2"] in dico_peueff["Sol"]:
      degats_adverse *= 0.5
  elif typeatt_adverse["type"] == 'Fee':
    if pokemon_actuel["type1"] in dico_peueff["Fee"] or pokemon_actuel["type2"] in dico_peueff["Fee"]:
      degats_adverse *= 0.5

def ineff():
  global degats
  global Attaque
  typeatt = data_pui.get(Attaque)
  if typeatt["type"] == 'Spectr':
    if pokemon_adverse_actuel["type1"] in dico_ineff["Spectr"] or pokemon_adverse_actuel["type2"] in dico_ineff["Spectr"]:
      degats *= 0
  if typeatt["type"] == 'Dragon':
    if pokemon_adverse_actuel["type1"] in dico_ineff["Dragon"] or pokemon_adverse_actuel["type2"] in dico_ineff["Dragon"]:
      degats *= 0
  if typeatt["type"] == 'Normal':
    if pokemon_adverse_actuel["type1"] in dico_ineff["Normal"] or pokemon_adverse_actuel["type2"] in dico_ineff["Normal"]:
      degats *= 0
  if typeatt["type"] == 'Psy':
    if pokemon_adverse_actuel["type1"] in dico_ineff["Psy"] or pokemon_adverse_actuel["Psy"] in dico_ineff["Psy"]:
      degats *= 0
  if typeatt["type"] == 'Sol':
    if pokemon_adverse_actuel["type1"] in dico_ineff["Sol"] or pokemon_adverse_actuel["type2"] in dico_ineff["Sol"]:
      degats *= 0
  if typeatt["type"] == 'Combat':
    if pokemon_adverse_actuel["type1"] in dico_ineff["Combat"] or pokemon_adverse_actuel["type2"] in dico_ineff["Combat"]:
      degats *= 0
  if typeatt["type"] == 'Electr':
    if pokemon_adverse_actuel["type1"] in dico_ineff["Electr"] or pokemon_adverse_actuel["type2"] in dico_ineff["Electr"]:
      degats *= 0
  
def ineff_adverse():
  global degats_adverse
  global Attaque_adverse
  typeatt_adverse = data_pui.get(Attaque_adverse)
  if typeatt_adverse["type"] == 'Spectr':
    if pokemon_actuel["type1"] in dico_ineff["Spectr"] or pokemon_actuel["type2"] in dico_ineff["Spectr"]:
      degats_adverse *= 0
  if typeatt_adverse["type"] == 'Dragon':
    if pokemon_actuel["type1"] in dico_ineff["Dragon"] or pokemon_actuel["type2"] in dico_ineff["Dragon"]:
      degats_adverse *= 0
  if typeatt_adverse["type"] == 'Normal':
    if pokemon_actuel["type1"] in dico_ineff["Normal"] or pokemon_actuel["type2"] in dico_ineff["Normal"]:
      degats_adverse *= 0
  if typeatt_adverse["type"] == 'Psy':
    if pokemon_actuel["type1"] in dico_ineff["Psy"] or pokemon_actuel["type2"] in dico_ineff["Psy"]:
      degats_adverse *= 0
  if typeatt_adverse["type"] == 'Sol':
    if pokemon_actuel["type1"] in dico_ineff["Sol"] or pokemon_actuel["type2"] in dico_ineff["Sol"]:
      degats_adverse *= 0
  if typeatt_adverse["type"] == 'Combat':
    if pokemon_actuel["type1"] in dico_ineff["Combat"] or pokemon_actuel["type2"] in dico_ineff["Combat"]:
      degats_adverse *= 0
  if typeatt_adverse["type"] == 'Electr':
    if pokemon_actuel["type1"] in dico_ineff["Electr"] or pokemon_actuel["type2"] in dico_ineff["Electr"]:
      degats_adverse *= 0



def stab():
  global degats
  global Attaque
  typeatt = data_pui.get(Attaque)
  if typeatt["type"] == pokemon_actuel["type1"] or typeatt["type"] == pokemon_actuel["type2"]:
    degats *= 1.5

def stab_adverse():
  global degats_adverse
  global Attaque_adverse
  typeatt_adverse = data_pui.get(Attaque_adverse)
  if typeatt_adverse["type"] == pokemon_adverse_actuel["type1"] or typeatt_adverse["type"] == pokemon_adverse_actuel["type2"]:
    degats_adverse *= 1.5

def critique():
  global degats
  taux_crit = randrange(1, 101)
  if taux_crit in [1,2,3,4,5,6]:
    degats *= 1.5
    print("crit")

def critique_adverse():
  global degats_adverse
  taux_crit = randrange(1, 101)
  if taux_crit in [1,2,3,4,5,6]:
    degats_adverse *= 1.5
    print("crit adverse")




#PREMIERE ATTAQUE DE MON POKEMON
def att1_mon_poke():
  global degats
  global Attaque
  Attaque = pokemon_actuel["Att1"]
  power = data_pui.get(Attaque) # Récupère la puissance de l'attaque
  nb_1_100 = randrange(1, 101)

  if nb_1_100 in range (power["precision"]) :

    if power["catégorie"] == "phy":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statatt"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdef"] * 50)  # Calcul des dégats infligés si l'attaque est physique
    elif power["catégorie"] == "spe":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statattspe"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdefspe"] * 50)  # Calcul des dégats infligés si l'attaque est spéciale

    ineff()
    supeff()
    peueff()
    stab()
    critique()
    pokemon_adverse_actuel["PV"] -= degats
    if pokemon_adverse_actuel["PV"] > 0:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV.                     ")
      label_combat.grid(row=0, column=0, sticky=NW)
    else:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV. Il est K.O.                     ")
      label_combat.grid(row=0, column=0, sticky=NW)
    
  else:
    label_combat = Label(frame_info_combat, text=(pokemon_actuel["name"] + " tente d'utiliser " + Attaque + " mais rate son attaque.                     "))
    label_combat.grid(row=0, column=0, sticky=NW)
  if pokemon_adverse_actuel["PV"] > 0 :
    label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)
  else : 
    label_poke_adverse = Label(frame_pv, text="PV Adverse = K.O.     ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)
  
#DEUXIEME ATTAQUE DE MON POKEMON
def att2_mon_poke():
  global degats
  global Attaque
  Attaque = pokemon_actuel["Att2"]
  power = data_pui.get(Attaque) # Récupère la puissance de l'attaque
  nb_1_100 = randrange(1, 101)
  
  if nb_1_100 in range (power["precision"]) :


    if power["catégorie"] == "phy":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statatt"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdef"] * 50)  # Calcul des dégats infligés si l'attaque est physique
    elif power["catégorie"] == "spe":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statattspe"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdefspe"] * 50)  # Calcul des dégats infligés si l'attaque est spéciale

    ineff()
    supeff()
    peueff()
    stab()
    critique()
    pokemon_adverse_actuel["PV"] -= degats
    if pokemon_adverse_actuel["PV"] > 0:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV.                      ")
      label_combat.grid(row=0, column=0, sticky=NW)
    else:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV. Il est K.O.                     ")
      label_combat.grid(row=0, column=0, sticky=NW)
  
  else:
    label_combat = Label(frame_info_combat, text=(pokemon_actuel["name"] + " tente d'utiliser " + Attaque + " mais rate son attaque.                     "))
    label_combat.grid(row=0, column=0, sticky=NW)

  if pokemon_adverse_actuel["PV"] > 0 :
    label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)
  else : 
    label_poke_adverse = Label(frame_pv, text="PV Adverse = K.O.     ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)

#TROISIEME ATTAQUE DE MON POKEMON
def att3_mon_poke():
  global degats
  global Attaque
  Attaque = pokemon_actuel["Att3"]
  power = data_pui.get(Attaque) # Récupère la puissance de l'attaque
  nb_1_100 = randrange(1, 101)
  if nb_1_100 in range (power["precision"]) :


    if power["catégorie"] == "phy":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statatt"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdef"] * 50)  # Calcul des dégats infligés si l'attaque est physique
    elif power["catégorie"] == "spe":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statattspe"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdefspe"] * 50)  # Calcul des dégats infligés si l'attaque est spéciale
    
    ineff()
    supeff()
    peueff()
    stab()
    critique()
    pokemon_adverse_actuel["PV"] -= degats
    if pokemon_adverse_actuel["PV"] > 0:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV.                      ")
      label_combat.grid(row=0, column=0, sticky=NW)
    else:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV. Il est K.O.                     ")
      label_combat.grid(row=0, column=0, sticky=NW)
    
  else:
    label_combat = Label(frame_info_combat, text=(pokemon_actuel["name"] + " tente d'utiliser " + Attaque + " mais rate son attaque.                     "))
    label_combat.grid(row=0, column=0, sticky=NW)
  if pokemon_adverse_actuel["PV"] > 0 :
    label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)
  else : 
    label_poke_adverse = Label(frame_pv, text="PV Adverse = K.O.     ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)

#QUATRIEME ATTAQUE DE MON POKEMON
def att4_mon_poke():
  global degats
  global Attaque

  Attaque = pokemon_actuel["Att4"]
  power = data_pui.get(Attaque) # Récupère la puissance de l'attaque
  nb_1_100 = randrange(1, 101)

  if nb_1_100 in range (power["precision"]) :


    if power["catégorie"] == "phy":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statatt"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdef"] * 50)  # Calcul des dégats infligés si l'attaque est physique
    elif power["catégorie"] == "spe":
      degats = (((100 * 0.4 + 2) * pokemon_actuel["Statattspe"] * power["pui"]) + 2) // (pokemon_adverse_actuel["Statdefspe"] * 50)  # Calcul des dégats infligés si l'attaque est spéciale
    
    ineff()
    supeff()
    peueff()
    stab()
    critique()

    pokemon_adverse_actuel["PV"] -= degats

    if pokemon_adverse_actuel["PV"] > 0:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV.                      ")
      label_combat.grid(row=0, column=0, sticky=NW)
    else:
      label_combat = Label(frame_info_combat, text= pokemon_actuel["name"] + " utilise " + Attaque + ", " + pokemon_adverse_actuel["name"] + " ennemi perd " + str(degats) + "PV. Il est K.O.                     ")
      label_combat.grid(row=0, column=0, sticky=NW)
    
  else:

    label_combat = Label(frame_info_combat, text=(pokemon_actuel["name"] + " tente d'utiliser " + Attaque + " mais rate son attaque.                     "))
    label_combat.grid(row=0, column=0, sticky=NW)


  if pokemon_adverse_actuel["PV"] > 0 :
    label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)
  else : 
    label_poke_adverse = Label(frame_pv, text="PV Adverse = K.O.     ")
    label_poke_adverse.grid(row=1, column=0, sticky=NW)


#ATTAQUES DU POKEMON ADVERSE
def att_poke_adverse():

  global degats_adverse
  global Attaque_adverse

  i = randrange(1, 5)

  if i == 1:
      Attaque_adverse = pokemon_adverse_actuel["Att1"]
  elif i == 2:
      Attaque_adverse = pokemon_adverse_actuel["Att2"]
  elif i == 3:
      Attaque_adverse = pokemon_adverse_actuel["Att3"]
  elif i == 4:
      Attaque_adverse = pokemon_adverse_actuel["Att4"]

  power_adverse = data_pui.get(Attaque_adverse)

  nb_1_100 = randrange(1, 101)

  if nb_1_100 in range (power_adverse["precision"]) :


    if power_adverse["catégorie"] == "phy":
      degats_adverse = (((100 * 0.4 + 2) * pokemon_adverse_actuel["Statatt"] * power_adverse["pui"]) + 2) // (pokemon_actuel["Statdef"] * 50)  # Calcul des dégats recu si l'attaque est physique
    elif power_adverse["catégorie"] == "spe":
      degats_adverse = (((100 * 0.4 + 2) * pokemon_adverse_actuel["Statattspe"] * power_adverse["pui"]) + 2) // (pokemon_actuel["Statdefspe"] * 50)  # Calcul des dégats recu si l'attaque est spéciale

    ineff_adverse()
    supeff_adverse()
    peueff_adverse()
    stab_adverse()
    critique_adverse()
    pokemon_actuel["PV"] -= degats_adverse

    if pokemon_actuel["PV"] > 0:
      label_combat2 = Label(frame_info_combat, text= pokemon_adverse_actuel["name"] + " ennemi utilise " + Attaque_adverse + ", " + pokemon_actuel["name"] + " perd " + str(degats_adverse) + "PV.                       ")
      label_combat2.grid(row=1, column=0, sticky=NW)
    else:
      label_combat2 = Label(frame_info_combat, text= pokemon_adverse_actuel["name"] + " ennemi utilise " + Attaque_adverse + ", " + pokemon_actuel["name"] + " perd " + str(degats_adverse) + "PV. Il est K.O.                      ")
      label_combat2.grid(row=1, column=0, sticky=NW)
  
  else:

    label_combat2 = Label(frame_info_combat, text= pokemon_adverse_actuel["name"] + " ennemi tente d'utiliser " + Attaque_adverse + " mais rate son attaque                     ")
    label_combat2.grid(row=1, column=0, sticky=NW)


  if pokemon_actuel["PV"] > 0 :
    label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
    label_poke_allie.grid(row=0, column=0, sticky=NW)
  else :
    label_poke_allie = Label(frame_pv, text="PV Allié = K.O.     ")
    label_poke_allie.grid(row=0, column=0, sticky=NW)













def switch():
  frame_attaque.grid_forget()
  frame_changement.grid(row = 0, column = 1, sticky = N, pady = 20)

#LOSE

frame_lose = Frame(fenetre)
def switch_frame_lose():
  frame_fenetre_combat.pack_forget()
  frame_lose.pack()
  son_marathonchampions.stop()
texte_lose = Label(frame_lose, text="YOU LOSE")
texte_lose.pack()
Button(frame_lose, text="Retour au bureau", command=frame_lose.quit).pack(padx=10, pady=10, side=BOTTOM)




def combat1() :
  
  while pokemon_actuel["PV"] > 0 and pokemon_adverse_actuel["PV"] > 0:

    if pokemon_actuel["Speed"] >= pokemon_adverse_actuel["Speed"]:
      att1_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      break


    elif pokemon_adverse_actuel["Speed"] > pokemon_actuel["Speed"]:
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      att1_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      break

  if pokemon1["PV"] <= 0 and pokemon2["PV"] <= 0 and pokemon3["PV"] <= 0:
    switch_frame_lose()
  if pokemon_adverse1["PV"] <= 0 and pokemon_adverse2["PV"] <= 0 and pokemon_adverse3["PV"] <= 0:
    frame_fenetre_combat.pack_forget()
    if Olga_Flagadoss["PV"] <= 0 and Olga_Lippoutou["PV"] <= 0 and Olga_Lokhlass["PV"] <= 0:
      frame_ligue.pack()
    elif Pierre_Grolem["PV"] <= 0 and Pierre_Onix["PV"] <= 0 and Pierre_Rhinoferos["PV"] <= 0:
      frame_champions.pack()
    pokemon1["PV"] = max_PV_poke1
    pokemon2["PV"] = max_PV_poke2
    pokemon3["PV"] = max_PV_poke3
    Ondine_fight()
    Bob_fight()
    Erika_fight()
    Koga_fight()
    Morgan_fight()
    Auguste_fight()
    Giovanni_fight()
    Win_Giovanni()
    Aldo_fight()
    Agatha_fight()
    Peter_fight()
    Maitre_fight()
    Win_Master()
    Win_Red()

def combat2() :

  while pokemon_actuel["PV"] > 0 and pokemon_adverse_actuel["PV"] > 0:

    if pokemon_actuel["Speed"] >= pokemon_adverse_actuel["Speed"]:
      att2_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      break


    elif pokemon_adverse_actuel["Speed"] > pokemon_actuel["Speed"]:
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      att2_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      break

  if pokemon1["PV"] <= 0 and pokemon2["PV"] <= 0 and pokemon3["PV"] <= 0:
    switch_frame_lose()
  if pokemon_adverse1["PV"] <= 0 and pokemon_adverse2["PV"] <= 0 and pokemon_adverse3["PV"] <= 0:
    frame_fenetre_combat.pack_forget()
    if Olga_Flagadoss["PV"] <= 0 and Olga_Lippoutou["PV"] <= 0 and Olga_Lokhlass["PV"] <= 0:
      frame_ligue.pack()
    elif Pierre_Grolem["PV"] <= 0 and Pierre_Onix["PV"] <= 0 and Pierre_Rhinoferos["PV"] <= 0:
      frame_champions.pack()
    pokemon1["PV"] = max_PV_poke1
    pokemon2["PV"] = max_PV_poke2
    pokemon3["PV"] = max_PV_poke3
    Ondine_fight()
    Bob_fight()
    Erika_fight()
    Koga_fight()
    Morgan_fight()
    Auguste_fight()
    Giovanni_fight()
    Win_Giovanni()
    Aldo_fight()
    Agatha_fight()
    Peter_fight()
    Maitre_fight()
    Win_Master()
    Win_Red()

def combat3() :
  
  while pokemon_actuel["PV"] > 0 and pokemon_adverse_actuel["PV"] > 0:

    if pokemon_actuel["Speed"] >= pokemon_adverse_actuel["Speed"]:
      att3_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      break


    elif pokemon_adverse_actuel["Speed"] > pokemon_actuel["Speed"]:
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      att3_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      break

  if pokemon1["PV"] <= 0 and pokemon2["PV"] <= 0 and pokemon3["PV"] <= 0:
    switch_frame_lose()
  if pokemon_adverse1["PV"] <= 0 and pokemon_adverse2["PV"] <= 0 and pokemon_adverse3["PV"] <= 0:
    frame_fenetre_combat.pack_forget()
    if Olga_Flagadoss["PV"] <= 0 and Olga_Lippoutou["PV"] <= 0 and Olga_Lokhlass["PV"] <= 0:
      frame_ligue.pack()
    elif Pierre_Grolem["PV"] <= 0 and Pierre_Onix["PV"] <= 0 and Pierre_Rhinoferos["PV"] <= 0:
      frame_champions.pack()

    pokemon1["PV"] = max_PV_poke1
    pokemon2["PV"] = max_PV_poke2
    pokemon3["PV"] = max_PV_poke3
    Ondine_fight()
    Bob_fight()
    Erika_fight()
    Koga_fight()
    Morgan_fight()
    Auguste_fight()
    Giovanni_fight()
    Win_Giovanni()
    Aldo_fight()
    Agatha_fight()
    Peter_fight()
    Maitre_fight()
    Win_Master()
    Win_Red()

def combat4() :
  
  while pokemon_actuel["PV"] > 0 and pokemon_adverse_actuel["PV"] > 0:

    if pokemon_actuel["Speed"] >= pokemon_adverse_actuel["Speed"]:
      att4_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      break


    elif pokemon_adverse_actuel["Speed"] > pokemon_actuel["Speed"]:
      att_poke_adverse()
      if pokemon_actuel["PV"] <= 0:
        switch()
        break
      att4_mon_poke()
      if pokemon_adverse_actuel["PV"] <= 0:
        changeadverse()
        break
      break

  if pokemon1["PV"] <= 0 and pokemon2["PV"] <= 0 and pokemon3["PV"] <= 0:
    switch_frame_lose()
  if pokemon_adverse1["PV"] <= 0 and pokemon_adverse2["PV"] <= 0 and pokemon_adverse3["PV"] <= 0:
    frame_fenetre_combat.pack_forget()
    if Olga_Flagadoss["PV"] <= 0 and Olga_Lippoutou["PV"] <= 0 and Olga_Lokhlass["PV"] <= 0:
      frame_ligue.pack()
    elif Pierre_Grolem["PV"] <= 0 and Pierre_Onix["PV"] <= 0 and Pierre_Rhinoferos["PV"] <= 0:
      frame_champions.pack()

    pokemon1["PV"] = max_PV_poke1
    pokemon2["PV"] = max_PV_poke2
    pokemon3["PV"] = max_PV_poke3
    Ondine_fight()
    Bob_fight()
    Erika_fight()
    Koga_fight()
    Morgan_fight()
    Auguste_fight()
    Giovanni_fight()
    Win_Giovanni()
    Aldo_fight()
    Agatha_fight()
    Peter_fight()
    Maitre_fight()
    Win_Master()
    Win_Red()


##########
#FRAME DE LA FENETRE COMBAT
##########


##Frame PV
frame_pv = LabelFrame(frame_fenetre_combat, text="Info PV", borderwidth=1, relief=GROOVE)
label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
label_poke_allie.grid(row=0, column=0, sticky=NW)
label_poke_adverse.grid(row=1, column=0, sticky=NW)
frame_pv.grid(row=0, column=1, sticky = SW, pady=30)

##Frame info combat
frame_info_combat = LabelFrame(frame_fenetre_combat, text="Info Combat", borderwidth=1, relief=GROOVE)
label_combat = Label(frame_info_combat, text= "")
label_combat2 = Label(frame_info_combat, text= "")
frame_info_combat.grid(row=1, column=0, sticky = SW, padx=18)
label_combat.grid(row=0, column=0, sticky=NW)
label_combat2.grid(row=1, column=0, sticky=NW)

##Frame Action
frame_action = LabelFrame(frame_fenetre_combat, text="Choix de l'action", borderwidth=1, relief=GROOVE)
frame_action.grid(row = 0, column = 1, sticky = N, pady = 20)
Button(frame_action, text="Attaques", command=pop_frame_attaque).pack(padx=10, pady=10, side=TOP)
Button(frame_action, text="Changement de pokemon", command=pop_frame_changement).pack(padx=10, pady=10, side=BOTTOM)

##Frame Attaque
frame_attaque = LabelFrame(frame_fenetre_combat, text="Attaques", borderwidth=1, relief=GROOVE)
bouton_att1 = Button(frame_attaque, text=pokemon_actuel["Att1"], command=combat1)
bouton_att1.pack(padx=10, pady=10, side=TOP)
bouton_att2 = Button(frame_attaque, text=pokemon_actuel["Att2"], command=combat2)
bouton_att2.pack(padx=10, pady=10, side=TOP)
bouton_att3 = Button(frame_attaque, text=pokemon_actuel["Att3"], command=combat3)
bouton_att3.pack(padx=10, pady=10, side=TOP)
bouton_att4 = Button(frame_attaque, text=pokemon_actuel["Att4"], command=combat4)
bouton_att4.pack(padx=10, pady=10, side=TOP)
bouton_retour = Button(frame_attaque, text="Retour", command=retour_frame_action1)
bouton_retour.pack(padx=10, pady=10, side=TOP)

##Frame Changement
frame_changement = LabelFrame(frame_fenetre_combat, text="Changement de Pokemon", borderwidth=1, relief=GROOVE)
poke1 = Button(frame_changement, text=pokemon1["name"], command=change1)
poke1.pack(padx=10, pady=10, side=TOP)
poke2 = Button(frame_changement, text=pokemon2["name"], command=change2)
poke2.pack(padx=10, pady=10, side=TOP)
poke3 = Button(frame_changement, text=pokemon3["name"], command=change3)
poke3.pack(padx=10, pady=10, side=TOP)
bouton_retour2 = Button(frame_changement, text="Retour", command=retour_frame_action2)
bouton_retour2.pack(padx=10, pady=10, side=TOP)


##########
#SWITCH DE FENETRE
##########

def switch_fenetre_modejeu():
  global bouton_switchcombat
  frame_fenetre_home.pack_forget()
  frame_fenetre_modejeu.pack()

def switch_combat_marathonchampions():
  global choisir1
  frame_fenetre_modejeu.pack_forget()
  frame_champions.pack()



def switch_combat_ligue():
  global choisir2
  frame_fenetre_modejeu.pack_forget()
  frame_ligue.pack()

def switch_combat_Olga():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Olga_Flagadoss
  pokemon_adverse2=Olga_Lippoutou
  pokemon_adverse3=Olga_Lokhlass
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_ligue.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_conseil4.play(loops=-1, maxtime=0, fade_ms=0)

def switch_combat_Aldo():

  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Aldo_Tygnon
  pokemon_adverse2=Aldo_Kicklee
  pokemon_adverse3=Aldo_Mackogneur
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_ligue.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_conseil4.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Agatha():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Agatha_Nosferalto
  pokemon_adverse2=Agatha_Arbok
  pokemon_adverse3=Agatha_Ectoplasma
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_ligue.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_conseil4.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Peter():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Peter_Ptera
  pokemon_adverse2=Peter_Leviator
  pokemon_adverse3=Peter_Dracolosse
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_ligue.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_conseil4.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Master():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Maitre_Arcanin
  pokemon_adverse2=Maitre_Alakazam
  pokemon_adverse3=Maitre_Tortank
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_ligue.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_maitre_league.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Pierre():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Pierre_Onix
  pokemon_adverse2=Pierre_Rhinoferos
  pokemon_adverse3=Pierre_Grolem
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

def switch_combat_Ondine():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Ondine_Staross
  pokemon_adverse2=Ondine_Hypocean
  pokemon_adverse3=Ondine_Tartard
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Bob():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Bob_Electrode
  pokemon_adverse2=Bob_Magneton
  pokemon_adverse3=Bob_Raichu
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Erika():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Erika_Parasect
  pokemon_adverse2=Erika_Empiflor
  pokemon_adverse3=Erika_Rafflesia
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Koga():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Koga_Smogogo
  pokemon_adverse2=Koga_Nidoking
  pokemon_adverse3=Koga_Grotadmorv
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Morgan():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Morgan_Aeromite
  pokemon_adverse2=Morgan_Noadkoko
  pokemon_adverse3=Morgan_Alakazam
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Auguste():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Auguste_Galopa
  pokemon_adverse2=Auguste_Arcanin
  pokemon_adverse3=Auguste_Sulfura
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)

def switch_combat_Giovanni():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Giovanni_Triopikeur
  pokemon_adverse2=Giovanni_Nidoqueen
  pokemon_adverse3=Giovanni_Mewtwo
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)

  frame_champions.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_marathonchampions.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)




def switch_combat_ash():
  global pokemon_adverse1
  global pokemon_adverse2
  global pokemon_adverse3
  global pokemon_adverse_actuel
  global gif_poke_adverse
  pokemon_adverse1=Red_Dracaufeu
  pokemon_adverse2=Red_Ronflex
  pokemon_adverse3=Red_Pikachu
  pokemon_adverse_actuel=pokemon_adverse1
  gif_poke_adverse = PhotoImage(file=pokemon_adverse_actuel["sprite"])
  gif_poke_adverse = gif_poke_adverse.zoom(3)
  element_gif_poke_adverse = canvas_background.create_image(825, 135, image=gif_poke_adverse)
  
  label_poke_adverse = Label(frame_pv, text="PV Adverse = " + str(pokemon_adverse_actuel["PV"]) + "    ")
  label_poke_adverse.grid(row=1, column=0, sticky=NW)
  frame_fenetre_modejeu.pack_forget()
  frame_fenetre_combat.pack()
  son_precombat.stop()
  son_red.play(loops=-1, maxtime=0, fade_ms=0)

  global label_poke_allie
  label_poke_allie.grid_forget()
  label_poke_allie = Label(frame_pv, text="PV Allié = " + str(pokemon_actuel["PV"]) + "    ")
  label_poke_allie.grid(row=0, column=0, sticky=NW)


def retour_fenetre_home():
  global bouton_retour1
  frame_fenetre_modejeu.pack_forget()
  frame_fenetre_home.pack()

bouton_quitter = Button(frame_fenetre_home, text="Retour au bureau", command=frame_fenetre_home.quit).pack(padx=10, pady=10, side=BOTTOM)
bouton_switchcombat = Button(frame_fenetre_home, text="Sélection du mode de jeu", command=switch_fenetre_modejeu)
choisir1 = Button(frame_marathonchampions, text="Choisir", command=switch_combat_marathonchampions).pack(padx=10, pady=10, side=BOTTOM)
choisir2 = Button(frame_plateauindigo, text="Choisir", command=switch_combat_ligue).pack(padx=10, pady=10, side=BOTTOM)
choisir3 = Button(frame_ash, text="Choisir", command=switch_combat_ash).pack(padx=10, pady=10, side=BOTTOM)
bouton_retour1 = Button(frame_fenetre_modejeu, text="Retour", command=retour_fenetre_home).pack(padx=10, pady=10, side=TOP)

######
#LIGUE
######

sprite_olga = PhotoImage(file="sprite_champions/Olga.png")
sprite_olga = sprite_olga.zoom(2)
canvas_olga = Canvas(frame_ligue, width=300, height=200)
sprite_canvas_olga = canvas_olga.create_image(150, 100, image=sprite_olga)
canvas_olga.grid(row = 0, column = 0, sticky = NW)
Olga = Button(frame_ligue, text="Olga", command = switch_combat_Olga).grid(row = 0, column = 1, sticky = W)


sprite_aldo = PhotoImage(file="sprite_champions/Aldo.png")
sprite_aldo = sprite_aldo.zoom(2)
def Aldo_fight():
  if Olga_Flagadoss["PV"] <= 0 and Olga_Lippoutou["PV"] <= 0 and Olga_Lokhlass["PV"] <= 0:
    canvas_aldo = Canvas(frame_ligue, width=300, height=200)
    sprite_canvas_aldo = canvas_aldo.create_image(150, 100, image=sprite_aldo)
    canvas_aldo.grid(row = 1, column = 0, sticky = NW)
    Aldo = Button(frame_ligue, text="Aldo", command = switch_combat_Aldo).grid(row = 1, column = 1, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_conseil4.stop()
    son_precombat.play()


sprite_agatha = PhotoImage(file="sprite_champions/Agatha.png")
sprite_agatha = sprite_agatha.zoom(2)
def Agatha_fight():
  if Aldo_Kicklee["PV"] <= 0 and Aldo_Tygnon["PV"] <= 0 and Aldo_Mackogneur["PV"] <= 0:
    canvas_agatha = Canvas(frame_ligue, width=300, height=200)
    sprite_canvas_agatha = canvas_agatha.create_image(150, 100, image=sprite_agatha)
    canvas_agatha.grid(row = 2, column = 0, sticky = NW)
    Agatha = Button(frame_ligue, text="Agatha", command = switch_combat_Agatha).grid(row = 2, column = 1, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_conseil4.stop()
    son_precombat.play()


sprite_peter = PhotoImage(file="sprite_champions/Peter.png")
sprite_peter = sprite_peter.zoom(2)
def Peter_fight():
  if Agatha_Arbok["PV"] <= 0 and Agatha_Nosferalto["PV"] <= 0 and Agatha_Ectoplasma["PV"] <= 0:
    canvas_peter = Canvas(frame_ligue, width=300, height=200)
    sprite_canvas_peter = canvas_peter.create_image(150, 100, image=sprite_peter)
    canvas_peter.grid(row = 0, column = 3, sticky = NW)
    Peter = Button(frame_ligue, text="Peter", command = switch_combat_Peter).grid(row = 0, column = 4, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_conseil4.stop()
    son_precombat.play()


sprite_blue = PhotoImage(file="sprite_champions/Blue.png")
sprite_blue = sprite_blue.zoom(3)
def Maitre_fight():
  if Peter_Ptera["PV"] <= 0 and Peter_Leviator["PV"] <= 0 and Peter_Dracolosse["PV"] <= 0:
    canvas_blue = Canvas(frame_ligue, width=300, height=200)
    sprite_canvas_blue = canvas_blue.create_image(150, 100, image=sprite_blue)
    canvas_blue.grid(row = 1, column = 3, sticky = NW)
    Master = Button(frame_ligue, text="Maître", command = switch_combat_Master).grid(row = 1, column = 4, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_conseil4.stop()
    son_precombat.play()

def Win_Master():
  if Maitre_Alakazam["PV"] <= 0 and Maitre_Arcanin["PV"] <= 0 and Maitre_Tortank["PV"] <= 0:
    frame_ligue.pack_forget()
    frame_win_ligue.pack()
    son_maitre_league.stop()

########
#CHAMPIONS
########

sprite_pierre = PhotoImage(file="sprite_champions/Pierre.png")
canvas_pierre = Canvas(frame_champions, width=200, height=150)
sprite_canvas_pierre = canvas_pierre.create_image(100, 75, image=sprite_pierre)
canvas_pierre.grid(row = 0, column = 0, sticky = NW)
Pierre = Button(frame_champions, text="Pierre", command = switch_combat_Pierre).grid(row = 0, column = 1, sticky = W)


sprite_ondine = PhotoImage(file="sprite_champions/Ondine.png")
def Ondine_fight():
  if Pierre_Grolem["PV"] <= 0 and Pierre_Onix["PV"] <= 0 and Pierre_Rhinoferos["PV"] <= 0:
    canvas_ondine = Canvas(frame_champions, width=200, height=150)
    sprite_canvas_ondine = canvas_ondine.create_image(100, 75, image=sprite_ondine)
    canvas_ondine.grid(row = 1, column = 0, sticky = NW)
    Ondine = Button(frame_champions, text="Ondine", command = switch_combat_Ondine).grid(row = 1, column = 1, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_marathonchampions.stop()
    son_precombat.play()


sprite_bob = PhotoImage(file="sprite_champions/Bob.png")
def Bob_fight():
  if Ondine_Hypocean["PV"] <= 0 and Ondine_Staross["PV"] <= 0 and Ondine_Tartard["PV"] <= 0:
    canvas_bob = Canvas(frame_champions, width=200, height=150)
    sprite_canvas_bob = canvas_bob.create_image(100, 75, image=sprite_bob)
    canvas_bob.grid(row = 2, column = 0, sticky = NW)
    Bob = Button(frame_champions, text="Major Bob", command = switch_combat_Bob).grid(row = 2, column = 1, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_marathonchampions.stop()
    son_precombat.play()


sprite_erika = PhotoImage(file="sprite_champions/Erika.png")
def Erika_fight():
  if Bob_Electrode["PV"] <= 0 and Bob_Magneton["PV"] <= 0 and Bob_Raichu["PV"] <= 0:
    canvas_erika = Canvas(frame_champions, width=200, height=150)
    sprite_canvas_erika = canvas_erika.create_image(100, 75, image=sprite_erika)
    canvas_erika.grid(row = 3, column = 0, sticky = NW)
    Erika = Button(frame_champions, text="Érika", command = switch_combat_Erika).grid(row = 3, column = 1, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_marathonchampions.stop()
    son_precombat.play()

sprite_koga = PhotoImage(file="sprite_champions/Koga.png")
def Koga_fight():
  if Erika_Empiflor["PV"] <= 0 and Erika_Parasect["PV"] <= 0 and Erika_Rafflesia["PV"] <= 0:
    canvas_koga = Canvas(frame_champions, width=200, height=150)
    sprite_canvas_koga = canvas_koga.create_image(100, 75, image=sprite_koga)
    canvas_koga.grid(row = 0, column = 3, sticky = NW)
    Koga = Button(frame_champions, text="Koga", command = switch_combat_Koga).grid(row = 0, column = 4, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_marathonchampions.stop()
    son_precombat.play()

sprite_morgane = PhotoImage(file="sprite_champions/Morgane.png")
def Morgan_fight():
  if Koga_Grotadmorv["PV"] <= 0 and Koga_Nidoking["PV"] <= 0 and Koga_Smogogo["PV"] <= 0:
    canvas_morgane = Canvas(frame_champions, width=200, height=150)
    sprite_canvas_morgan = canvas_morgane.create_image(100, 75, image=sprite_morgane)
    canvas_morgane.grid(row = 1, column = 3, sticky = NW)
    Morgan = Button(frame_champions, text="Morgane", command = switch_combat_Morgan).grid(row = 1, column = 4, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_marathonchampions.stop()
    son_precombat.play()

sprite_auguste = PhotoImage(file="sprite_champions/Auguste.png")
def Auguste_fight():
  if Morgan_Aeromite["PV"] <= 0 and Morgan_Noadkoko["PV"] <= 0 and Morgan_Alakazam["PV"] <= 0:
    canvas_auguste = Canvas(frame_champions, width=200, height=150)
    sprite_canvas_auguste = canvas_auguste.create_image(100, 75, image=sprite_auguste)
    canvas_auguste.grid(row = 2, column = 3, sticky = NW)
    Auguste = Button(frame_champions, text="Auguste", command = switch_combat_Auguste).grid(row = 2, column = 4, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_marathonchampions.stop()
    son_precombat.play()

sprite_giovanni = PhotoImage(file="sprite_champions/Giovanni.gif")
def Giovanni_fight():
  if Auguste_Arcanin["PV"] <= 0 and Auguste_Galopa["PV"] <= 0 and Auguste_Sulfura["PV"] <= 0:
    canvas_giovanni = Canvas(frame_champions, width=200, height=150)
    sprite_canvas_giovanni = canvas_giovanni.create_image(100, 75, image=sprite_giovanni)
    canvas_giovanni.grid(row = 3, column = 3, sticky = NW)
    Giovanni = Button(frame_champions, text="Giovanni", command = switch_combat_Giovanni).grid(row = 3, column = 4, sticky = W)
    label_combat = Label(frame_info_combat, text="                                                                                                                              ")
    label_combat.grid(row=0, column=0, sticky=NW)
    label_combat2 = Label(frame_info_combat, text="                                                                                                                             ")
    label_combat2.grid(row=1, column=0, sticky=NW)
    son_marathonchampions.stop()
    son_precombat.play()

def Win_Giovanni():
  if Giovanni_Mewtwo["PV"] <= 0 and Giovanni_Nidoqueen["PV"] <= 0 and Giovanni_Triopikeur["PV"] <= 0:
    frame_champions.pack_forget()
    frame_fenetre_combat.pack_forget()
    frame_win_champions.pack()
    son_marathonchampions.stop()

######
#RED
######

def Win_Red():
  if Red_Dracaufeu["PV"] <= 0 and Red_Pikachu["PV"] <= 0 and Red_Ronflex["PV"] <= 0:
    frame_fenetre_combat.pack_forget()
    frame_win_red.pack()
    son_marathonchampions.stop()
    son_precombat.play()




frame_fenetre_home.mainloop()