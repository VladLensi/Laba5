from abc import ABC, abstractmethod

class TeamMember(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def get_details(self):
        pass
