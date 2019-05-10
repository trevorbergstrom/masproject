import random
import collections
import sys
import copy

class Cell:
    x = 0
    y = 0
    animal_density = 0
    has_been_visited = False

    def __init__(self, x, y, animal_density):
        self.x = x
        self.y = y
        self.animal_density = animal_density

    def __str__(self):
        return "X: %s, Y:%s, AnimalDensity:%s, HasBeenVisited:%s" % (self.x, self.y, self.animal_density, self.has_been_visited)

    def __repr__(self):
        return "(X: %s, Y:%s) " % (self.x, self.y)
        #return "X: %s, Y:%s, AnimalDensity:%s, HasBeenVisited:%s" % (self.x, self.y, self.animal_density, self.has_been_visited)
        
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
class GeneratePath:
    grid = []
    starting_node = None
    max_route_length = 6
    feasible_paths = []
    grid_size = 5



    def init_grid(self):
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                row.append(Cell(i,j, random.randint(1,10)))
            self.grid.append(row)

    def generate_starting_point(self):
        starting_x = random.randint(0,self.grid_size-1)
        starting_y = random.randint(0,self.grid_size-1)
        #self.starting_node = self.grid[starting_x][starting_y]
        self.starting_node = self.grid[0][0]
        #print("Starting Node ", self.starting_node)

    def generate_route(self, depth, node, parent_node, path):
        #if limit is reached and currentnode is starting node
        #add to feasible_paths and return
        node.has_been_visited = True
        path.append(node)
        
        if depth is self.max_route_length:
            if node is self.starting_node:
              if self.is_path_duplicate(path, self.feasible_paths) is False:
                self.feasible_paths.append(copy.deepcopy(path))
                #return True
            #path = []
            #return False
        else:
        #foreach adjacent node not visited so far
        #add node to path and increase limit
            adjacent_nodes = self.get_adjacent_nodes(node, parent_node, path)
            for adjacent_node in adjacent_nodes:
                #if adjacent_node.has_been_visited is False:
                self.generate_route(depth+1, adjacent_node, node, path )
                    
        path.pop()
        node.has_been_visited = False

    def get_adjacent_nodes(self, node, parent_node, path):
        adjacent_nodes = []
        #left_node
        self.append_node(node.x-1,node.y, adjacent_nodes, parent_node, path)
        #right_node
        self.append_node(node.x+1,node.y, adjacent_nodes, parent_node, path)
        #top_node
        self.append_node(node.x,node.y+1, adjacent_nodes, parent_node, path)
        #bottom_node
        self.append_node(node.x,node.y-1, adjacent_nodes, parent_node, path)
        return adjacent_nodes

    def append_node(self, x, y, adjacent_nodes, parent_node, path):
        if x<0 or y <0 or x is self.grid_size or y is self.grid_size:
            return
        cell = self.grid[x][y]
#         if(cell is parent_node):
#             return
        if cell is not self.starting_node:
            if cell in path:
                return
        adjacent_nodes.append(cell)
    

    def is_path_duplicate(self, path, feasible_paths):
      for p in feasible_paths:
        if(collections.Counter(p)== collections.Counter(path)):
          return True
      return False



if __name__ == '__main__':
    gp = GeneratePath()
    gp.init_grid()
    
    gp.generate_starting_point()
    print('starting node', gp.starting_node)
    gp.generate_route(0, gp.starting_node, None, [])
    print('Num of feasible paths', len(gp.feasible_paths))
    print("Feasible Paths ", gp.feasible_paths )
    print('length of one path',len(gp.feasible_paths[0]))
   
    