#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket, sys, threading, time, select

# variables globales

# adresse IP et port utilisés par le serveur
HOST = input("A quel IP voulez vous vous connectez ? ")
PORT = int(input("Quel port voulez vous utilisez ? "))

NOMBREJOUEUR = 2
dureemax = 120 # durée max pour lancer l'attaque ; en secondes
pause = 3 # pause entre deux attaques  ; en secondes

dict_clients = {}  # dictionnaire des connexions clients
dict_pseudos = {}  # dictionnaire des pseudos
dict_poke = {}
dict_attaque = {}
dict_reponses = {}
dict_scores = {}
dict_scores_total = {}



class ThreadClient(threading.Thread):
    '''dérivation de classe pour gérer la connexion avec un client'''
    
    def __init__(self,conn):

        threading.Thread.__init__(self)
        self.connexion = conn
        
        # Mémoriser la connexion dans le dictionnaire
        
        self.nom = self.getName() # identifiant du thread "<Thread-N>"
        dict_clients[self.nom] = self.connexion
        dict_scores[self.nom] = 0
        dict_scores_total[self.nom] = 0
        
        print("Connexion du client", self.connexion.getpeername(),self.nom ,self.connexion)
        
        message = bytes("Vous êtes connecté au serveur.\n","utf-8")
        self.connexion.send(message)
        
        
    def run(self):

        # Choix du pokémon

        self.connexion.send(b"Quel pokemon voulez vous choisir ? \n Vous avez le choix entre Dracaufeu, Tortank et Florizarre. \n")
        # attente réponse client
        poke = self.connexion.recv(4096)
        poke = poke.decode(encoding='UTF-8')
        
        dict_poke[self.nom] = poke
        
        print("Pokemon du client", self.connexion.getpeername(),">", poke)
        
        message = b"Vous avez choisi votre pokemon. \n"

        if poke == "Dracaufeu":
            message = b"Vous avez choisi Dracaufeu. \n Vos attaques sont :\n Lance-Flammes, Draco-Choc, Lame-d'Air, Lance-Soleil\n"
        elif poke == "Tortank":
            message = b"Vous avez choisi Tortank. \n Vos attaques sont :\n Hydrocanon, Blizzard, Coud'Krane, Surf\n"
        elif poke == "Florizarre":
            message = b"Vous avez choisi Florizarre. \n Vos attaques sont :\n Lance-Soleil, Bomb-Beurk, Ultralaser, Morsure\n"
        else :
            message = b"Vous n'avez pas rentrer un nom valide.\n Nous vous avons donc assigner le pokemon Dracaufeu. \n Vos attaques sont :\n Lance-Flammes, Draco-Choc, Lame-d'Air, Lance-Soleil\n"

        self.connexion.send(message)


        
        # Choix du pseudo    
        
        self.connexion.send(b"Entrer un pseudo :\n")
        # attente réponse client
        pseudo = self.connexion.recv(4096)
        pseudo = pseudo.decode(encoding='UTF-8')
        
        dict_pseudos[self.nom] = pseudo
        
        print("Pseudo du client", self.connexion.getpeername(),">", pseudo)
        
        message = b"Attente des autres clients...\n"
        self.connexion.send(message)
    


        



        # Combat
       
        while True:
            
            try:
                # attente réponse client
                reponse = self.connexion.recv(4096)
                reponse = reponse.decode(encoding='UTF-8')
            except:
                # fin du thread
                break
                
            # on enregistre la première réponse
            # les suivantes sont ignorées
            if self.nom not in dict_reponses:
                dict_reponses[self.nom] = reponse, time.time()
                print("Réponse du client",self.nom,">",reponse)

        print("\nFin du thread",self.nom)
        self.connexion.close()


def MessagePourTous(message):
    """ message du serveur vers tous les clients"""
    for client in dict_clients:
        dict_clients[client].send(bytes(message,"utf8"))
        
        
# Initialisation du serveur

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket Ã  l'adresse choisie a échoué.")
    sys.exit()
print("Serveur prêt (port",PORT,") en attente de clients...")
mySocket.listen(5)


# len(dict_clients) = nb de joueurs connectés

while len(dict_clients) < NOMBREJOUEUR:
    # Attente connexion nouveau client
    try:
        connexion, adresse = mySocket.accept()
    except:
        sys.exit()
    # Créer un nouvel objet thread pour gérer la connexion
    th = ThreadClient(connexion)
    th.setDaemon(1)
    th.start()
    

while len(dict_pseudos) < NOMBREJOUEUR:
    # on attend que tout le monde ait entré son pseudo
    pass


MessagePourTous("\nLe combat va commencer !\n Votre objectif est d'infliger le plus de dégats à votre adversaire en 5\n")

# questions
index = 0
while index < 5:
    index += 1
    MessagePourTous("\nNouvelle attaque dans " + str(pause) + " secondes...\n")
    time.sleep(pause)

    timedebut = time.time()
    timefin = timedebut + dureemax
    dict_reponses = {}  # liste des réponses des clients
    dict_scores = {}

    message = "Quel attaque voulez vous utilisez ?"
    message += """
Réponse > """
    MessagePourTous(message)
        
    while time.time() < timefin and len(dict_reponses) <  NOMBREJOUEUR:
         # on attend que tout le monde ait répondu
         # ou que le délai soit écoulé
         pass


    for client in dict_reponses:
        try:
            reponse = dict_reponses[client][0]
            if reponse == "Lance-Flammes":
                dict_scores[client] = 25
            elif reponse == "Draco-Choc":
                dict_scores[client] = 20
            elif reponse == "Lame-d'Air":
                dict_scores[client] = 15
            elif reponse == "Lance-Soleil":
                dict_scores[client] = 35

            elif reponse == "Hydrocanon":
                dict_scores[client] = 35
            elif reponse == "Blizzard":
                dict_scores[client] = 30
            elif reponse == "Coud'Krane":
                dict_scores[client] = 25
            elif reponse == "Surf":
                dict_scores[client] = 20

            elif reponse == "Bomb-Beurk":
                dict_scores[client] = 25
            elif reponse == "Ultralaser":
                dict_scores[client] = 30
            elif reponse == "Morsure":
                dict_scores[client] = 15
            

            else :
                dict_scores[client] = 0
            
        except:
            # mauvaise réponse -1 pt
            dict_scores[client] = 0
            
        dict_scores_total[client] += dict_scores[client]    


    message = """

Résultat :
Client       Dégats infligés ce tour
"""

    for client in dict_reponses:
        duree = dict_reponses[client][1] - timedebut
        message += "%-10s  %3d pt\n"  %(dict_pseudos[client],dict_scores[client])
    message +="""    
Total :
Client       Dégats infligés au total
""" 

    for client in dict_scores_total:
        message += "%-10s  %3d pt\n"  %(dict_pseudos[client],dict_scores_total[client])

    MessagePourTous(message)
 
    if index == 4:
        dict_scores_total[client]


# Fin
MessagePourTous("\nFIN\nVous pouvez fermer l'application...\n")

# fermeture des sockets
for client in dict_clients:
    dict_clients[client].close()
    print("Déconnexion du socket", client)

input("\nAppuyer sur Entrée pour quitter l'application...\n")
# fermeture des threads (daemon) et de l'application



HEADER_LENGTH = 10



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)





server_socket.listen()


sockets_list = [server_socket]


clients = {}


