import os
import sys


class SystemInfo:

    @staticmethod
    def script_name():
        return os.path.basename(__file__)

    @staticmethod
    def python_path():
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def python_version():
        ver = sys.version.split("\n")
        return ver[0]

    @staticmethod
    def platform():
        return sys.platform

# print(SystemInfo().script_name())
# print(SystemInfo().python_path())
# print(SystemInfo().python_version())
# print(SystemInfo().platform())
