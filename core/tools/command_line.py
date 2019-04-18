from core.tools.others.loader import *

ld = Loader()
class CommandLine:

    def __init__(self):
        self.kill = True

    def getCommands(self,):
        self.commands = ""
        if self.kill == True:
            try:
                self.commands = input("KingBrute> ")
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")

    def parseCommands(self,):
        if len(self.commands) == 0:
            self.commands = "pass"
        self.parsed_commands = self.commands.split()
        return self.parsed_commands

    def executeCommands(self,):
        if self.parsed_commands[0] == "kill":
            ld.load("Exiting program....", 3)
            self.kill = False
        elif self.parsed_commands[0] == "pass":
            pass
        else:
            print("No command named '{}'".format(self.parsed_commands[0]))
            
            


if __name__ == "__main__":
    cmd = CommandLine()
    cmd.getCommands()
    cmd.parseCommands()
    cmd.executeCommands()