# TP-MultiThreading
## Installation
Ce projet a des dépendances. Il vous faut:
- CMake
- uv
- python 3.8 ou supérieur
- git

Si vous n'avez pas uv d'installer, lancez dans un terminal:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Si vous n'avez pas CMake d'installer, lancez dans un terminal (si vous êtes sous Debian ou Ubuntu):
```
sudo apt update && sudo apt upgrade
```
et
```
sudo apt install cmake
```
Ensuite vous pouvez clôner ce projet et vous placer dans le projet, soit:
```
git clone git@github.com:AdelieRT/tp1-multithreading.git
```
puis
```
cd tp1-multithreading
```
Une fois au sein du projet, vous devez lancer la commande suivante afin de se syncroniser avec l'environnment uv du projet et avoir toutes les librairies dépendantes:
```
uv sync && source .venv/bin/activate
```
Désormais, vous êtes libre de vos mouvements et en fonction de ce que vous souhaitez faire vous pouvez suivre les instructions d'une des catégories qui suivent.

## Tester le traitement de tâches par des minions en Python
Il faut lancer les processus suivant dans l'ordre ci-dessous:
- dans un premier terminal:
```
python3 queue_manager.py
```
- dans un second terminal:
```
python3 boss.py nb_taches
```
en remplacant **nb_taches** par le nombre de tâches que l'on souhaite traiter.
- dans un troisième terminal:
```
python3 minion.py
```
Cette étape-ci peut-être répété autant de fois que voulu, elle permet de lancer un minion afin qu'il travaille sur les tâches données par le boss.
## Tester le traitement de tâches en C++
Il faut lancer les processus suivant dans l'ordre ci-dessous:
- dans un premier terminal:
```
python3 queue_manager.py
```
- dans un second terminal:
```
python3 proxy.py
```
- dans un troisième terminal:
```
./build/low_level
```
- dans un quatrième terminal:
```
python3 boss.py nb_taches
```
en remplacant **nb_taches** par le nombre de tâches que l'on souhaite traiter.

## Résultats
### 30 tâches de taille 600 en Python
Avec 1 minion: temps total de traitement:  2.518523254000229  sec

Avec 2 mininons: temps total de traitement:  2.717490029000146  sec

Avec 3 mininons: temps total de traitement:  3.90479165799934  sec

Avec 4 mininons: temps total de traitement:  5.313551777000612  sec
### 30 tâches de taille 600 en C++
temps total de traitement:  48.84343313700083  sec
### 60 tâches de taille 600 en Python
Avec 1 minion: temps total de traitement:  3.867083327999353  sec

Avec 2 mininons: temps total de traitement:  4.7802756919991225  sec

Avec 3 mininons: temps total de traitement:  6.753732252000191  sec

Avec 4 mininons: temps total de traitement:  7.117583695000576  sec
### 60 tâches de taille 600 en C++
temps total de traitement:  101.3843936180001  sec

## Résultats SIMPLE
Ici nous regardons simplement le temps d'éxecutions des tâches. Pour reproduire cela il suffit de:
- Pour le C++ **commenter le code sous le commentaire "CODE COMPLEXE" et de décommenter le code sous le commentaire "CODE SIMPLE"** dans le fichier **low_level.cpp**. De compiler low_level.cpp puis de lancer:
```
./build/low_level nb_taches
```
en remplacant **nb_taches** par le nombre de tâches que l'on souhaite traiter.
- Pour le Python **décommenter le code sous le commentaire "CODE SIMPLE"** dans le fichier **task.py**. Puis de lancer:
```
python3 task.py nb_taches
```
en remplacant **nb_taches** par le nombre de tâches que l'on souhaite traiter.
### 30 tâches SIMPLE de taille 600 en Python
Simple, c'est à dire sans serveur et sans minion, ici on ne regarde que le temps de traitement des tâches:

temps de traitement total des  30  tache(s) : 0.11691985799916438 sec
### 30 tâches SIMPLE  de taille 600 en C++
Simple, c'est à dire sans serveur, ici on ne regarde que le temps de traitement des tâches:

temps de traitement total des 30 tache(s) : 0.865456 sec
### 60 tâches SIMPLE  de taille 600 en Python
Simple, c'est à dire sans serveur et sans minion, ici on ne regarde que le temps de traitement des tâches:

temps de traitement total des  60  tache(s) : 0.2588201630042022 sec
### 60 tâches SIMPLE  de taille 600 en C++
Simple, c'est à dire sans serveur, ici on ne regarde que le temps de traitement des tâches:

temps de traitement total des 60 tache(s) : 1.72696 sec
### 90 tâches SIMPLE  de taille 600 en Python
Simple, c'est à dire sans serveur et sans minion, ici on ne regarde que le temps de traitement des tâches:

temps de traitement total des  90  tache(s) : 0.37690438200843346 sec
### 90 tâches SIMPLE  de taille 600 en C++
Simple, c'est à dire sans serveur, ici on ne regarde que le temps de traitement des tâches:

temps de traitement total des 90 tache(s) : 2.63066 sec
