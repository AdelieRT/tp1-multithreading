from multiprocessing.managers import BaseManager
from multiprocessing import Queue

class QueueManager(BaseManager):
    # def __init__(self, task_queue=np.randint(3,100), result_queue=np.randint(3,100)):
    #     super.__init__()
    #     self.task_queue = Queue(task_queue)
    #     self.result_queue = Queue(result_queue)
    pass
        
if __name__== "_main_":
    task_queue = Queue(maxsize=100)
    QueueManager.register('get_task_queue',callable=lambda:task_queue)

    result_queue = Queue(maxsize=100)
    QueueManager.register('get_result_queue',callable=lambda:result_queue)

    manager = QueueManager(address=('', 50000), authkey=b'yoyoledoggo')
    server = manager.get_server().serve_forever()


