import unittest
from unittest import mock
from printer import Printer


class PrinterTestCase(unittest.TestCase):
    def testPrintHello(self):
        p = Printer()
        p.getHelloString = mock.MagicMock()
        p.printHello()
        p.getHelloString.assert_called_once_with()
  