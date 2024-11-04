#!/usr/bin/env python

import unittest
import numpy as np
from task import Task


class TaskTest(unittest.TestCase):
    def test_equals(self):
        t = Task()
        np.testing.assert_allclose(t.x @ t.a, t.b)


if __name__ == "__main__":
    unittest.main()
