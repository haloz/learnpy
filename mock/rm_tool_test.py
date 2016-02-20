from rm_tool import rm
import tempfile
import unittest
import os.path


class RmToolTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wt") as f:
            f.write("delete test file")

    def testRmTool(self):
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to delete the file")
