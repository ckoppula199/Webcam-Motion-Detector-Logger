from bokeh.plotting import show, figure, output_file
from MotionDetector import df

p = figure(x_axis_type = 'datetime', height=100, width=500, sizing_mode='scale_width', title='Motion Graph')
q = p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color='blue')

output_file("Graph.html")
show(p)
