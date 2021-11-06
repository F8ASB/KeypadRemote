# KeypadRemote
Il s'agir d'un commande à distance pour Hotspot RRF avec un clavier numérique USB ou Bluetooth. Une description complète du projet est dispobible sur [mon blog F8ASB.COM]( http://blog.f8asb.com/2021/11/06/keypadremote-le-…r-les-malvoyants/):


Reprendre l'ensemble des fichiers sons RRF sur le lien suivant:
[https://github.com/F8ASB/fr_FR_Agnes/tree/fr_FR_Agnes/RRF](https://github.com/F8ASB/fr_FR_Agnes/tree/fr_FR_Agnes/RRF)

et les mettres selon le chemin suivant du hotspot:
`/usr/share/svxlink/sounds/fr_FR/RRF`

Installer la dependance Keyboard:
`pip3 install keyboard`

Se connecter en SSH et aller dans le dossier Spotnik
`cd /opt/spotnik/`

copier les fichiers du projet

`gitclone https://github.com/F8ASB/KeypadRemote.git`

Dans le fichier /etc/spotnik/svxlink.cfg accéssible depuis le menu spot
dans la partie simplexLogic aller dans les parametre `FX_GAIN_LOW=` et mettre la valeur `10`.
Cela permettra de ne pas baisser la modulation voir de l'amplifier un peu si il y a un QSO dans le salon en cours afin de permettre de bien entendre les commandes vocales.

### **DOCUMENTATION EN COURS D'ECRITURE**
