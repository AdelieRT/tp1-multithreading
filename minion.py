from queue_client import QueueClient


class Minion(QueueClient):
    def __init__(self):
        super().__init__()

    # récupère les taches en cours sur task_queue les fait
    # et les mets dans result_queue
    def working(self):
        while not self.task_queue.empty():
            task = self.task_queue.get()
            task.work()
            self.result_queue.put(task)
            print("done")


if __name__ == "__main__":
    mignon = Minion()
    mignon.working()
