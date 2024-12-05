from multiprocessing.managers import BaseManager
from queue_manager import manager
from task import Task

class QueueClient:
   def __init__(self):
       manager.connect()
       self.task_queue = manager.get_task_queue()
       self.result_queue = manager.get_result_queue()

class Boss(QueueClient):
    def __init__(self):
        self.super()
        self.nb_taches = 0

    # créée taches et put dans task_queue
    def create_task(self,identifier=0, size=None):
        self.task_queue.put(Task(identifier,size))
        self.nb_taches += 1
    
    # et vérif que toutes les taches ajoutés dasn task_queue 
    # sont réalisés (dasn result_queue)
    def verify_task(self):
        if(self.nb_taches == self.result_queue.qsize()):
            #toutes les tasks ont été faites
            print("Good Job!")
        else:
            print("Work Harder!")

class Minion(QueueClient):
    # récupère les taches en cours sur task_queue les fait
    # et les mets dans result_queue
    def working(self):
        for task in self.task_queue:
            task.work()
            self.result_queue.put(task)


if __name__== "_main_":
    big_boss = Boss()
    mignon = Minion()
    big_boss.create_task()
    big_boss.create_task()
    mignon.working()
    big_boss.verify_task()