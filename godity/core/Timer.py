import time

class Timer():
    def __init__(self):
        self.last_time = time.time()

    def getTime(self):
        return time.time() - self.last_time

    def resetTime(self):
        self.last_time = time.time()