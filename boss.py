from queue_client import QueueClient
from task import Task


class Boss(QueueClient):
    def __init__(self):
        self.super()
        self.nb_taches = 0

    # créée taches et put dans task_queue
    def create_task(self, identifier=0, size=None):
        self.task_queue.put(Task(identifier, size))
        self.nb_taches += 1

    # et vérif que toutes les taches ajoutés dasn task_queue
    # sont réalisés (dasn result_queue)
    def verify_task(self):
        if self.nb_taches == self.result_queue.qsize():
            # toutes les tasks ont été faites
            print("Good Job!")
        else:
            print("Work Harder!")


if __name__ == "_main_":
    big_boss = Boss()
    big_boss.verify_task()
