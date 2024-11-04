#!/usr/bin/env python3
import unittest
import numpy as np
from task import Task


class TaskTest(unittest.TestCase):
    def test_equals(self):
        np.testing.assert_allclose(Task.x @ Task.a, Task.b)


if __name__ == "__main__":
    unittest.main()
