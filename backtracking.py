from abc import ABC, abstractmethod

class Backtracking(ABC):
    def __init__(self):
        pass

    def solve(self, state, pos=0):
        if self.end(pos):
            return state
        for s in self.get_possible_states(state, pos):
            #if self.check(s):
            result = self.solve(s, pos+1)
            if result:
                return result
        return False


    @abstractmethod
    def get_possible_states(self, state, pos):
        pass

    @abstractmethod
    def copy(self, state):
        pass

    @abstractmethod
    def end(self, pos):
        pass