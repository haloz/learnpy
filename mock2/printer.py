
class Printer(object):

    def printHello(self):
        output = self.getHelloString()
        print(output)

    def getHelloString(self):
        return "Hello"
