import unittest
from unittest import mock
from jirabuddy import JiraBuddy


class JiraBuddyTestCase(unittest.TestCase):
    @mock.patch("jirabuddy.JIRA")
    def testConnectToJira(self, mock_jira):
        mock_jira.return_value = "blubb"
        
        j = JiraBuddy()
        ret = j.connectToJira("http://127.0.0.1")
        assert ret == "blubb"

