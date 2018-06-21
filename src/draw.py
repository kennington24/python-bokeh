import math

from bokeh.io import show, output_file
from bokeh.plotting import figure, show, output_file
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
graph_data.randomize(12, 9, 150, 20)
graph_data.bfs(graph_data.vertexes[0])

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
  color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(-300, 420), y_range=(-300, 420),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=30, fill_color='color')

graph.edge_renderer.data_source.data = dict(start=[], end=[])

for vertex in graph_data.vertexes:

  for edge in vertex.edges:
    start = graph_data.vertexes.index(vertex)
    graph.edge_renderer.data_source.data['start'].append(start)

    end = graph_data.vertexes.index(edge.destination)
    graph.edge_renderer.data_source.data['end'].append(end)

### start of layout code
#setting the postion of the vertexes
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]
values = [v.value for v in graph_data.vertexes]

source = ColumnDataSource(data=dict(x=x, y=y, values=values))

labels = LabelSet(x='x', y='y', text='values', level='overlay',
                  text_align='center', text_baseline='middle', source=source, render_mode='canvas')

plot.add_layout(labels)
graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)