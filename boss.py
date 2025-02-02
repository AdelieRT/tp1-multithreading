from queue_client import QueueClient
from task import Task
import time
import sys


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
        if (self.nb_taches == self.result_queue.qsize()) and self.nb_taches != 0:
            # toutes les tasks ont été faites
            # print("Good Job!")
            print(self.result_queue.get())

            # performance = 0
            # while not self.result_queue.empty():
            #     performance += self.result_queue.get().time
            # performance = performance / self.nb_taches
            # print(
            #     "Temps d'éxecution moyen: ",
            #     performance,
            #     " sec, pour ",
            #     self.nb_taches,
            #     " tache(s)",
            # )

        else:
            # print("Work Harder!")
            return -1

    def working(self, nb_taches=10):
        for i in range(nb_taches):
            self.create_task(size=600)
        start = time.perf_counter()
        while self.verify_task() == -1:
            pass
        temps_traitement = time.perf_counter() - start
        print("temps total de traitement: ", temps_traitement, " sec")


if __name__ == "__main__":
    big_boss = Boss()
    if len(sys.argv) > 1:
        big_boss.working(int(sys.argv[1]))
    else:
        big_boss.working()
