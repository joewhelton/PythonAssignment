# Stuff for testing functionality as I go, not formal unit testing

from config import *
from Classes.Modules import Modules

def main():
    modules = Modules("Modules.txt")
    modules.load_data()
    print(f"{modules.module[0].code} - {modules.module[0].title}")

main()