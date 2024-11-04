#!/usr/bin/env python

import unittest
import numpy as np
from task import Task


class TaskTest(unittest.TestCase):
    def test_equals(self):
        t = Task()
        t.work()
        np.testing.assert_allclose(t.a @ t.x, t.b)


if __name__ == "__main__":
    unittest.main()
