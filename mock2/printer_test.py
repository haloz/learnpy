import unittest
from unittest import mock
from printer import Printer


class PrinterTestCase(unittest.TestCase):
    def testPrintHello(self):
        p = Printer()
        p.printHello = mock.MagicMock(name="printHello")
        p.printHello()
        pass