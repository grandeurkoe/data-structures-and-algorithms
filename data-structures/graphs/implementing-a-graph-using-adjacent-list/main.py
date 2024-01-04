class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}
        self.number_of_nodes = 0

    
    def add_vertex(self, value):
        """Add Node or Vertex."""
        if value not in self.adjacency_list:
            self.adjacency_list[value] = []
            self.number_of_nodes += 1
            print(f"Add Vertex({value}).")
        else:
            print(f"Vertex({value}) already exists.")

    def add_edge(self, first_vertex, second_vertex):
        """Add Edge."""
        if first_vertex not in self.adjacency_list and second_vertex not in self.adjacency_list:
            self.add_vertex(first_vertex)
            self.add_vertex(second_vertex)
        if first_vertex in self.adjacency_list and second_vertex not in self.adjacency_list:
            self.add_vertex(second_vertex)
        elif first_vertex not in self.adjacency_list and second_vertex in self.adjacency_list:
            self.add_vertex(first_vertex)
        self.adjacency_list[first_vertex].append(second_vertex)
        self.adjacency_list[second_vertex].append(first_vertex)
        print(f"Add Edge between Vertex({first_vertex}) and Vertex({second_vertex}).")


    
    def show_connection(self):
        """Show Adjacency List."""
        print("\nGRAPH META DATA")
        print(f"Number of Nodes in Graph = {self.number_of_nodes}")
        for node in self.adjacency_list:
            print(f"Node({node}) ---> {self.adjacency_list[node]}")

my_graph = Graph()
print("OPERATION LOG")
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')
my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')
my_graph.show_connection()
