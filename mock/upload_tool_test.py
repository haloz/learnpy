from upload_tool import UploadToolService
from rm_tool import RmToolService
from unittest import mock
import unittest


class UploadToolServiceTestCase(unittest.TestCase):

    def testUploadComplete(self):
        mock_r = mock.create_autospec(RmToolService)
        u = UploadToolService(mock_r)

        u.upload_complete("test file")
        mock_r.rm.assert_called_with("test file")
