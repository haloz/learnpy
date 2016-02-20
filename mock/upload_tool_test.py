from upload_tool import UploadToolService
from rm_tool import RmToolService
from unittest import mock
import unittest


class UploadToolServiceTestCase(unittest.TestCase):

    @mock.patch.object(RmToolService, "rm")
    def testUploadComplete(self, mock_rm):
        r = RmToolService()
        u = UploadToolService(r)

        u.upload_complete("test file")
        mock_rm.assert_called_with("test file")
        r.rm.assert_called_with("test file")
