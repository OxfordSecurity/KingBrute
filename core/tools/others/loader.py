import sys
import time
class Loader:

    def __init__(self,):
        pass

    def load(self, load_text, ranger = 3,):
        self.ranger = ranger * 10
        k = 0
        self.load_text = list(load_text)
        while(k <= self.ranger):
            for alph in range(len(self.load_text)):
                cur_alph = self.load_text[alph]
                if self.load_text[alph] == ".":
                    self.load_text[alph] = "-"
                else:
                    self.load_text[alph] = self.load_text[alph].upper()
                sys.stdout.write('\r')
                sys.stdout.write("".join(self.load_text))   
                sys.stdout.flush()
                self.load_text[alph] = cur_alph
                time.sleep(.1)
                k += 1
