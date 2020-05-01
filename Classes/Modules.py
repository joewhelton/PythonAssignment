from config import *
from Classes.Students import Student

class Modules:
    def __init__(self, dataFile):
        self.dataFile = dataFile
        self.module = []

    def load_data(self):
        connection = open(DATA_PATH + self.dataFile)
        while True:
            line = connection.readline()
            if line == "":
                break
            data = line.split(",")
            self.module.append(Module(data[0], data[1]))


class Module:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.students = []