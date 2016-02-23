from jira import JIRA


class JiraBuddy(object):
    def connectToJira(self, server):        
        j = JIRA(server)
        return j
