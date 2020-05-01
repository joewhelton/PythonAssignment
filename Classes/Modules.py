from config import *

class Modules:
    def __init__(self, dataFile):
        self.dataFile = dataFile
        self.module = []


class Module:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.students = []