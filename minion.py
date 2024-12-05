from queue_client import QueueClient


class Minion(QueueClient):
    def __init__(self):
        self.super()

    # récupère les taches en cours sur task_queue les fait
    # et les mets dans result_queue
    def working(self):
        for task in self.task_queue:
            task.work()
            self.result_queue.put(task)


if __name__ == "_main_":
    mignon = Minion()
    mignon.working()
