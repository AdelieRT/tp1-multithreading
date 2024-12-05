from multiprocessing.managers import BaseManager
from multiprocessing import Queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    task_queue = Queue(maxsize=100)
    QueueManager.register('get_task_queue', callable=lambda: task_queue)

    result_queue = Queue(maxsize=100)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)

    manager = QueueManager(address=('', 50000), authkey=b'yoyoledoggo')
    server = manager.get_server()
    server.serve_forever()
