#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_correct_output(self):
        b = Base()
        self.assertFalse(print(b.id), 1)
        b = Base()
        self.assertFalse(print(b.id), 2)
        b = Base()
        self.assertFalse(print(b.id), 3)
        b = Base(12)
        self.assertFalse(print(b.id), 12)
        b = Base()
        self.assertFalse(print(b.id), 4)

    def test_empty(self):
        b = Base()
        self.assertFalse(print(b.id), 1)
        b = Base()
        self.assertFalse(print(b.id), 2)
        b = Base()
        self.assertFalse(print(b.id), 3)
        b = Base()
        self.assertFalse(print(b.id), 4)
