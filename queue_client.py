from queue_manager import QueueManager


class QueueClient:
    def __init__(self):
        manager = QueueManager(address=('127.0.0.1', 50000), authkey=b'yoyoledoggo')
        manager.connect()
        self.task_queue = manager.get_task_queue()
        self.result_queue = manager.get_result_queue()
