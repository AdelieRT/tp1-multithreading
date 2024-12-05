from queue_client import QueueClient
from task import Task


class Boss(QueueClient):
    def __init__(self):
        super().__init__()
        self.nb_taches = 0

    # créée taches et put dans task_queue
    def create_task(self, identifier=0, size=None):
        self.task_queue.put(Task(identifier, size))
        self.nb_taches += 1

    # et vérif que toutes les taches ajoutés dasn task_queue
    # sont réalisés (dasn result_queue)
    def verify_task(self):
        if self.nb_taches == self.result_queue.qsize() and self.nb_taches!=0:
            # toutes les tasks ont été faites
            print("Good Job!")
        else:
            print("Work Harder!")
            return -1


if __name__ == '__main__':
    big_boss = Boss()
    big_boss.create_task()
    big_boss.create_task()
    big_boss.create_task()
    while(big_boss.verify_task()==-1):
        pass

    
