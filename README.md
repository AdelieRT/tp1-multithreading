# TP-MultiThreading
## Installation
Il suffit de clôner le projet et de se placer dans celui-ci, puis en fonction de ce que vous souhaitez faire vous pouvez suivre les instructions d'une des catégories qui suivent.
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
en remplacant **nb_tache** par le nombre de tâches que l'on souhaite traiter.
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
python3 boss.py nb_taches
```
en remplacant **nb_tache** par le nombre de tâches que l'on souhaite traiter.
- dans un quatrième terminal:
```
./build/low_level
```
Cette étape-ci peut-être répété autant de fois que voulu, elle permet de lancer un minion afin qu'il travaille sur les tâches données par le boss.
