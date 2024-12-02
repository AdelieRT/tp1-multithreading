from multiprocessing.managers import BaseManager
from queue_manager import manager

class QueueClient:
   def __init__(self):
       manager.connect()
       self.task_queue = manager.get_task_queue()
       self.result_queue = manager.get_result_queue()

class Boss(QueueClient):
    # créée taches et put dans task_queue
    # et vérif que toutes les taches ajoutés dasn task_queue sont réalisés (dasn result_queue)
    pass

class Minion(QueueClient):
    # récupère les taches en cours sur task_queue les fait
    # et les mets dans result_queue
    pass

if __name__== "_main_":
    pass