import os, sys, pathlib
import yaml


class LoadConfig:
    def __init__(self):
        self.prepare_paths()


    def prepare_paths(self):
        print(sys.path.insert(0, os.getcwd()))

if __name__ == '__main__':
    LoadConfig()
