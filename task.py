import time
import numpy as np
import json


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        a_list = self.a.tolist()
        b_list = self.b.tolist()
        x_list = self.x.tolist()
        d = {
            "identifier": self.identifier,
            "size": self.size,
            "a": a_list,
            "b": b_list,
            "x": x_list,
            "time": self.time,
        }
        return json.dumps(d)

    @staticmethod
    def from_json(text: str) -> "Task":
        results = json.loads(text)
        task = Task(results["identifier"], results["size"])
        task.a = np.array(results["a"])
        task.b = np.array(results["b"])
        task.x = np.array(results["x"])
        task.time = results["time"]
        return task

    def __eq__(self, other: "Task") -> bool:
        return (
            self.identifier == other.identifier
            and self.size == other.size
            and (self.a == other.a).all
            and (self.b == other.b).all
            and (self.x == other.x).all
            and self.time == other.time
        )


# if __name__ == "__main__":
#     task = Task(0, 10)
#     task.work()
#     print("task time: ", task.time, " sec")
#     task_json = task.to_json()
#     # print(task_json)
#     json_task = Task.from_json(task_json)
#     # print(json_task)
#     print("task == task_test: ",task == json_task)
