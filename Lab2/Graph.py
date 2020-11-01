class Graph:

    def __init__(self):
        self.graph = dict()

    def new_vertex(self, vertex):
        try:
            self.graph[vertex] = set()
        except TypeError:
            print('Wrong key')

    def remove_vertex(self, vertex):
        try:
            for vert in self.graph[vertex]:
                self.graph[vert].remove(vertex)
            del self.graph[vertex]
        except KeyError:
            print('there isn\'t this vertex')

    def new_edge(self, vertex1, vertex2):
        if vertex1 != vertex2 and vertex1 in self.graph.keys() and vertex2 in self.graph.keys():
            if vertex2 in self.graph[vertex1]:
                print('edge is already in graph')
            else:
                self.graph[vertex1].add(vertex2)
                self.graph[vertex2].add(vertex1)

    def remove_edge(self, vertex1, vertex2):
        try:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
        except KeyError:
            print('there isn\'t this edge')

    def neighbours(self, vertex):
        try:
            return self.graph[vertex]
        except KeyError:
            print('There isn\'t this vertex')

    def dfs(self, vertex, done=[]):
        if vertex not in self.graph.keys():
            print('illegal operation')
        yield vertex

        done.append(vertex)

        for _ in self.graph[vertex]:
            self.dfs(vertex, done)

    def bfs(self, vertex):
        done = {vertex}
        q = []

        if vertex not in self.graph.keys():
            print('there isn\'t this vertex')
        q.append(vertex)

        while len(q) > 0:
            vert = q.pop()
            yield vert
            for vert2 in self.graph[vert]:
                if vert2 not in done:
                    q.append(vert2)