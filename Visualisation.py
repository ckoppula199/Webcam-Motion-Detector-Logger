from bokeh.plotting import show, figure, output_file
from bokeh.models import HoverTool, ColumnDataSource
from MotionDetector import df

p = figure(x_axis_type = 'datetime', height=100, width=500, sizing_mode='scale_width', title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks=1

cds = ColumnDataSource(df)

hover = HoverTool(tooltips=[("Start", "@Start"), ("End", "@End")])
p.add_tools(hover)


q = p.quad(left="Start", right="End", bottom=0, top=1, color='blue', source=cds)

output_file("Graph.html")
show(p)
