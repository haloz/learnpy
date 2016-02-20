import os


class RmToolService(object):

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
