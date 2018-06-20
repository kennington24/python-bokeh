import math

from bokeh.io import show, output_file
from bokeh.plotting import figure, show, output_file
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, ColumnDataSource, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

source = ColumnDataSource(data=dict(names=['1']))

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
  color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(-1, 1), y_range=(-1, 1),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

### start of layout code
#setting the postion of the vertexes
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

labels = LabelSet(text='names', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='canvas')

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.add_layout(labels)

output_file('graph.html')
show(plot)