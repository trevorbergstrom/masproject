from itertools import combinations

class Milp:
    number_resources = None
    feasible_paths = []
    
    def __init__(self, feasible_paths, number_resources):
        self.feasible_paths = feasible_paths
        self.number_resources = number_resources
    
    
    def get_path_combinations(self):
        return list(combinations(self.feasible_paths, self.number_resources))
    
    def start(self):
        comb = self.get_path_combinations()
        print(comb)