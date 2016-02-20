from rm_tool import RmToolService
from unittest import mock
import unittest


class RmToolTestCase(unittest.TestCase):

    @mock.patch("rm_tool.os.path")
    @mock.patch("rm_tool.os")
    def testRmTool(self, mock_os, mock_path):
        rmsvr = RmToolService()
        mock_path.isfile.return_value = False
        rmsvr.rm("any file")
        self.assertFalse(
            mock_os.remove.called,
            "Failed to rm file if not present."
        )

        mock_path.isfile.return_value = True
        rmsvr.rm("any file")
        mock_os.remove.assert_called_with("any file")
