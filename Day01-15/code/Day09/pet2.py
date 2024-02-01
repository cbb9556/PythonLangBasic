from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(sel, name):
        sel._name = name

    @abstractmethod
    def voice_make(self):
        pass

