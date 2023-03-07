from abc import ABC, abstractmethod

class Serviceable(ABC, abstractmethod):

    @abstractmethod
    def needs_service():
        pass
