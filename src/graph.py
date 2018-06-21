import random

class Edge:
  def __init__(self, destination):
    self.destination = destination

class Vertex:
  def __init__(self, value, color, **pos):
    self.value = value
    self.color = color
    self.pos = pos
    self.edges =[]

class Graph:
  def __init__(self):
    self.vertexes = []

  def debug_create_test_data(self):
    debug_vertex_1 = Vertex('t1', 'red', x=40, y=40)
    debug_vertex_2 = Vertex('t2', 'blue', x=140, y=140)
    debug_vertex_3 = Vertex('t3', 'pink', x=300, y=400)

    debug_edge_1 = Edge(debug_vertex_2)
    debug_vertex_1.edges.append(debug_edge_1)

    debug_edge_2 = Edge(debug_vertex_2)
    debug_vertex_3.edges.append(debug_edge_2)

    self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3])

  def bfs(self, start):
        random_color = "#" + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        queue = []
        found = []
        found.append(start)
        queue.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0)
        return found

  def randomize(self, width, height, pxBox, probability):
        def connectVerts(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        count = 0
        grid = []

        for y in range(height):
            row = []
            for x in range(width):
                v = Vertex('default', 'white', x=200, y=200)
                v.value = f"v{count}"
                count += 1
                row.append(v)
            grid.append(row)
        # print(grid)

        for y in range(height):
            for x in range(width):
                if (y < height - 1):
                    if random.randint(0, 100) < probability:
                        print(f"testing data       x: {x}  y: {y}")
                        connectVerts(grid[y][x], grid[y+1][x])
                if (x < width - 1):
                    if random.randint(0, 100) < probability:
                        connectVerts(grid[y][x], grid[y][x+1])

        boxBuffer = 0.8
        boxInner = pxBox * boxBuffer
        boxInnerOffset = (pxBox - boxInner) / 2

        for y in range(height):
            for x in range(width):
                # print(grid[y][x].pos)
                grid[y][x].pos['x'] = (
                    x * pxBox + boxInnerOffset + (random.randint(0, 100) / 100) * boxInner) % 1
                grid[y][x].pos['y'] = (
                    y * pxBox + boxInnerOffset + (random.randint(0, 100) / 100) * boxInner) % 1

        for y in range(height):
            for x in range(width):
                self.vertexes.append(grid[y][x])