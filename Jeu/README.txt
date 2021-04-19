Pour commencer 

Sur votre PC hôte (Windows), veuillez installer python depuis le site officiel : https://www.python.org/downloads/release/python-382/

Ensuite, veuillez lancer un terminal et dirigez dans votre dossier où vous avez cloné le repo git pour y rentrer cette commande :

pip install -r requirements.txt


Pour pouvoir jouer à notre jeu : 

Connectez-vous au serveur en ssh avec cette commande : ssh centos@51.210.13.32
Le mot de passe est : Pykemon

Dirigez vous vers le dossier "Pykemon" avec cette commande : cd Pykemon/

Lancez le fichier "serverpykemon.py" grâce à cette commande : python3 serverpykemon.py

L'input va vous demander une IP à rentrer, veuillez rentrer cette addresse : 51.210.13.32

Il en va de même pour le port : 1777



Vous pouvez désormais lancer le fichier clientpykemon.py sur votre PC hôte et à renseigner le champ port avec celui précédemment choisi : 1777

Bon combat !

