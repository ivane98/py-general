class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])
    
    def get_connections(self):
        return self.connected_to.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, nbr):
        return self.connected_to[nbr]
    

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vert = Vertex(key)
        self.vert_list[key] = new_vert
        return new_vert
    
    def get_vert(self, n):
        for n in self.vert_list:
            return self.vert_list[n]
        
    def __contains__(self, n):
        return n in self.vert_list
    
    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        return self.vert_list.keys()
    
    def __iter__(self):
        return iter(self.vert_list.values())
    

###################################
def legal_coord(x, bd_size):
    if x >= 0 and x < bd_size:
        return True
    else:
        return False
    
def get_legal_moves(x, y, bd_size):
    new_moves = []
    move_offsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    
    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]

        if legal_coord(new_x, bd_size) and legal_coord(new_y, bd_size):
            new_moves.append((new_x, new_y))
    
    return new_moves


def pos_to_node_id(row, column, board_size):
    return (row * board_size) + column

def knight_graph(bd_size):
    kt_graph = Graph()

    for row in range(bd_size):
        for col in range(bd_size):
            node_id = pos_to_node_id(row, col, bd_size)
            new_position = get_legal_moves(row, col, bd_size)
            for e in new_position:
                nid = pos_to_node_id(e[0], e[1], bd_size)
                kt_graph.add_edge(node_id, nid)

    return kt_graph


def knight_tour(n, path, u, limit):
    u.set_color('gray')
    path.append(u)

    if n < limit:
        nbr_list = list(u.get_connections())
        i = 0
        done = False

        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knight_tour(n+1, path, nbr_list[i], limit)
            i+= 1
        if not done:
            path.pop()
            u.set_color('white')
    else:
        done = True
    
    return done


    
###################################

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)

        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == 'white':
                next_vertex.set_pred(start_vertex)
                self.dfs_visit(next_vertex)
        
        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)

    
    def dfs(self):
        for a_vertex in self:
            a_vertex.set_color('white')
            a_vertex.set_pred(-1)
        for a_vertex in self:
            if a_vertex.get_color() == 'white':
                self.dfs_visit(a_vertex)



##################################
