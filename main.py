from core.tools.command_line import *
from core.tools.others.connection import *
import time

cn = Connection()
cmd = CommandLine()


if __name__ == "__main__":
    if cn.check_connection() == True:
        print("\nSession started at {}".format(time.strftime("%X")))
        while cmd.kill:
            cmd.getCommands()
            cmd.parseCommands()
            cmd.executeCommands()