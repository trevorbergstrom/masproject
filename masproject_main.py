import grid
import milp

class Program:
    def init(self):
        gp = grid.GeneratePaths()
        
        
        gp.init_grid()
        gp.generate_starting_point()
        gp.generate_routes(0, gp.starting_node, [])   
        #gp.print_paths(gp.feasible_paths)
        milp = Milp(gp.feasible_paths, 2)

if __name__ == '__main__':
    program = Program()
    program.init()