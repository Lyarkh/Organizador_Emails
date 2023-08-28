from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def build(self):
        ...