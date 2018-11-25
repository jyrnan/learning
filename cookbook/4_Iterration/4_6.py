from collections import deque

class Linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, start=1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('4_4.py') as f:
    lines = Linehistory(f)
    for line in lines:
        if "Node" in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline))