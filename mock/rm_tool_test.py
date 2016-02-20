from rm_tool import rm
import mock
import unittest


class RmToolTestCase(unittest.TestCase):

    @mock.patch("rm_tool.os")
    def testRmTool(self, mock_os):
        rm("any file")
        mock_os.remove.assert_called_with("any file")
