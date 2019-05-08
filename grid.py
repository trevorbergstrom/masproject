import random

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
        return "X: %s, Y:%s, " % (self.x, self.y)
        #return "X: %s, Y:%s, AnimalDensity:%s, HasBeenVisited:%s" % (self.x, self.y, self.animal_density, self.has_been_visited)

class GeneratePath:
    grid = []
    starting_node = None
    max_route_length = 8
    feasible_paths = []



    def init_grid(self):
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Cell(i,j, random.randint(1,10)))
            self.grid.append(row)

    def generate_starting_point(self):
        starting_x = random.randint(0,4)
        starting_y = random.randint(0,4)
        self.starting_node = self.grid[starting_x][starting_y]
        print("Starting Node ", self.starting_node)

    def generate_route(self, depth, node, parent_node, path):
        #if limit is reached and currentnode is starting node
        #add to feasible_paths and return
        if depth is self.max_route_length:
            if node is self.starting_node:
                self.feasible_paths.append(path)
                print("in max depth", path)
            return

        #foreach adjacent node not visited so far
        #add node to path and increase limit
        node.has_been_visited = True;
        adjacent_nodes = self.get_adjacent_nodes(node, parent_node)
        for adjacent_node in adjacent_nodes:
            #if not adjacent_node.has_been_visited:
            path.append(adjacent_node)
            self.generate_route(depth+1, adjacent_node, node, path )

    def get_adjacent_nodes(self, node, parent_node):
        adjacent_nodes = []
        #right_node
        self.append_node(node.x+1,node.y, adjacent_nodes, parent_node)
        #left_node
        self.append_node(node.x-1,node.y, adjacent_nodes, parent_node)
        #top_node
        self.append_node(node.x,node.y-1, adjacent_nodes, parent_node)
        #bottom_node
        self.append_node(node.x,node.y+1, adjacent_nodes, parent_node)
        return adjacent_nodes

    def append_node(self,x,y, adjacent_nodes, parent_node):
        cell = None
        try:
            cell = self.grid[x][y]
            if not cell == parent_node:
                adjacent_nodes.append(cell)
        except:
            print("Not valid cell")

if __name__ == '__main__':
    gp = GeneratePath()
    gp.init_grid()
    gp.generate_starting_point()
    gp.generate_route(0, gp.starting_node, None, [])
    print(gp.feasible_paths, "Feasible Paths ", len(gp.feasible_paths))
