from bokeh.plotting import show, figure, output_file
from bokeh.models import HoverTool, ColumnDataSource
from MotionDetector import df

#create new columns with strings representing times to be used when hovering over data
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# create a data source for the columns
cds = ColumnDataSource(df)

#create the graph object and give it some specific attributes
p = figure(x_axis_type = 'datetime', height=100, width=500, sizing_mode='scale_width', title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks=1

# hover tool implementation
hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

# determines type of graph, in this case a quadrat graph
q = p.quad(left="Start", right="End", bottom=0, top=1, color='blue', source=cds)

# save graph as Graph.html and launch the webpage with the graph
output_file("Graph.html")
show(p)
