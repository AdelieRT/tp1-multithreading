#!/usr/bin/env python

import unittest
import numpy as np
from task import Task


class TaskTest(unittest.TestCase):
    def test_equals(self):
        t = Task()
        t.work()
        np.testing.assert_allclose(t.a @ t.x, t.b)

    def test_tp3(self):
        a = Task()
        txt = a.to_json()
        b = Task.from_json(txt)
        np.testing.assert_equal(a, b)


if __name__ == "__main__":
    unittest.main()
