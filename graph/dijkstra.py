class Node:
    def __init__(self, links: list = None, key = None):
        """A node used in the graph

        Args:
            links (list): list of tuples, formatted as such: [(node: Node, distance: float)]
        """
        self.links = links
        self.key = key
        self.reset()

    def reset(self): 
        self.weight = float ("inf")
        self.prev = None

    def __str__(self):
        return f"Links to {[i[0].key for i in self.links]}. Current weight: {self.weight}, {f'key: {self.key}' if self.key != None else ''}"

def dijkstra(start: Node, goal: Node, unvisited: set): 
    """Finds the shortest path using the Dijkstra algorithm

    Args:
        start (node): The starting nodes
        goal (node): Goal node
        unvisited (set): Intermediary nodes including goal
    """

    #Setup

    start.reset()
    goal.reset()
    for i in unvisited: 
        i.reset()

    start.weight = 0
    currentNode = start

    #Initial run
    for i in currentNode.links:
        i[0].weight = i[1]
        i[0].prev = currentNode

    while len(unvisited) > 0 and min(unvisited, key=lambda x: x.weight).weight < float("inf"):
        currentNode = min(unvisited, key=lambda x: x.weight)
        
        for i in currentNode.links: 
            if i[0] in unvisited: 
                if currentNode.weight + i[1] < i[0].weight: 
                    i[0].weight = currentNode.weight + i[1]
                    i[0].prev = currentNode
        
        unvisited.remove(currentNode)

    path = [goal]
    currentNode = goal

    while currentNode != start: 
        path.append(currentNode.prev)
        currentNode = currentNode.prev

    path = path[::-1]
    
    return path

if __name__ == "__main__": 
    """
    Test is the example from this video: https://youtu.be/GazC3A4OQTE
    """

    #Making nodes
    S = Node(key = "S")
    A = Node(key = "A")
    B = Node(key = "B")
    C = Node(key = "C")
    D = Node(key = "D")
    E = Node(key = "E")
    F = Node(key = "F")
    G = Node(key = "G")
    H = Node(key = "H")
    I = Node(key = "I")
    J = Node(key = "J")
    K = Node(key = "K")
    L = Node(key = "L")

    #Node linking
    S.links = [(A, 7), (B, 2), (C, 3)]
    A.links = [(S, 7), (B, 3), (D, 4)]
    B.links = [(S, 2), (A, 3), (D, 4), (H, 1)]
    C.links = [(S, 3), (L, 2)]
    D.links = [(A, 4), (B, 4), (F, 5), (H, 3)]
    E.links = [(G, 2), (K, 5)]
    F.links = [(D, 5), (H, 3)]
    G.links = [(H, 2), (E, 2)]
    H.links = [(B, 1), (F, 3), (G, 2)]
    I.links = [(L, 4), (J, 6), (K, 4)]
    J.links = [(L, 4), (K, 4), (I, 6)]
    K.links = [(I, 4), (J, 4), (E, 5)]
    L.links = [(C, 2), (I, 4), (J, 4)]

    path = dijkstra(S, E, {A, B, C, D, E, F, G, H, I, J, K, L})

    print([i.key for i in path])