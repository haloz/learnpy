from rm_tool import rm
import mock
import unittest


class RmToolTestCase(unittest.TestCase):

    @mock.patch("rm_tool.os.path")
    @mock.patch("rm_tool.os")
    def testRmTool(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        rm("any file")
        self.assertFalse(
            mock_os.remove.called,
            "Failed to rm file if not present."
        )

        mock_path.isfile.return_value = True
        rm("any file")
        mock_os.remove.assert_called_with("any file")
