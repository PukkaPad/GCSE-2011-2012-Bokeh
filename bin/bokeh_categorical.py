from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row
from bokeh.layouts import gridplot
from bokeh.palettes import Viridis3
from bokeh.models import Range1d
import numpy as np
import pandas as pd
import os

# seting work directory
#os.chdir('./bin')
#os.getcwd() # checking the working directory

boys = []
girls = []

tdata=pd.read_csv('GCSE_grades.csv')

All_Data = np.array(tdata)
#print All_Data

for row in All_Data:
    if row[1] == 'Male':
        boys.append(row)
    elif row[1] == 'Female':
        girls.append(row)

Boys = np.array(boys)
Girls = np.array(girls)

boys_2011 = []
boys_2012 = []
for subject in Boys:
    if subject[2] == 2012:
        boys_2012.append(subject)
    if subject[2] == 2011:
        boys_2011.append(subject)
Boys_2011 = np.array(boys_2011)
Boys_2012 = np.array(boys_2012)

girls_2011 = []
girls_2012 = []
for subject in Girls:
    
    if subject[2] == 2012:
        girls_2012.append(subject)
    if subject[2] == 2011:
        girls_2011.append(subject)
Girls_2011 = np.array(girls_2011)
Girls_2012 = np.array(girls_2012)

marks = ['A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'U']
GilrsAD2011 = Girls_2011[0, 5:14]
GilrsAD2012 = Girls_2012[0, 5:14]
BoysAD2011 = Boys_2011[0, 5:14]
BoysAD2012 = Boys_2012[0, 5:14]

labels = ['Girls 2011', 'Girls 2012']

output_file("categorical.html")

#p = figure(y_range=marks, title = 'Test', plot_width=300, plot_height=300)
#p = figure(y_range=marks)
p = figure(y_range=marks, title = 'Art&Design 2011')
q = figure(y_range=marks, title = 'Art&Design 2012')
p1 = figure(y_range=marks, title = 'Addit. Science 2011')
q1 = figure(y_range=marks, title = 'Addit. Science 2012')
p1 = figure(y_range=marks, title = 'Biology 2011')
q1 = figure(y_range=marks, title = 'Biology 2012')
p2 = figure(y_range=marks, title = 'Business & Comm. Syst.2011')
q2 = figure(y_range=marks, title = 'Business & Comm. Syst. 2012')
p3 = figure(y_range=marks, title = 'Business 2011')
q3 = figure(y_range=marks, title = 'Business 2012')
p4 = figure(y_range=marks, title = 'Chemistry 2011')
q4 = figure(y_range=marks, title = 'Chemistry 2012')
p5 = figure(y_range=marks, title = 'Citizenship Studies 2011')
q5 = figure(y_range=marks, title = 'Citizenship Studies 2012')
p6 = figure(y_range=marks, title = 'Classical Subjects 2011')
q6 = figure(y_range=marks, title = 'Classical Subjects 2012')
p7 = figure(y_range=marks, title = 'Construction 2011')
q7 = figure(y_range=marks, title = 'Construction 2012')


#p.title.text = 'Categorical Plots (Art & Design)'
p.title.align = 'center'
q.title.align = 'center'
p1.title.align = 'center'
q1.title.align = 'center'
p2.title.align = 'center'
q2.title.align = 'center'
p3.title.align = 'center'
q3.title.align = 'center'
p4.title.align = 'center'
q4.title.align = 'center'
p5.title.align = 'center'
q5.title.align = 'center'
p6.title.align = 'center'
q6.title.align = 'center'
p7.title.align = 'center'
q7.title.align = 'center'

p.x_range = Range1d(-1, 41)
p1.x_range = Range1d(-1, 41)
p2.x_range = Range1d(-1, 41)
p3.x_range = Range1d(-1, 41)
p4.x_range = Range1d(-1, 41)
p5.x_range = Range1d(-1, 41)
p6.x_range = Range1d(-1, 41)
p7.x_range = Range1d(-1, 41)

q.x_range = Range1d(-1, 41)
q1.x_range = Range1d(-1, 41)
q2.x_range = Range1d(-1, 41)
q3.x_range = Range1d(-1, 41)
q4.x_range = Range1d(-1, 41)
q5.x_range = Range1d(-1, 41)
q6.x_range = Range1d(-1, 41)
q7.x_range = Range1d(-1, 41)

p.xaxis.axis_label = 'Percentage of Grades'
p.yaxis.axis_label = 'Grades'
q.xaxis.axis_label = 'Percentage of Grades'
q.yaxis.axis_label = 'Grades'

p1.xaxis.axis_label = 'Percentage of Grades'
p1.yaxis.axis_label = 'Grades'
q1.xaxis.axis_label = 'Percentage of Grades'
q1.yaxis.axis_label = 'Grades'

p2.xaxis.axis_label = 'Percentage of Grades'
p2.yaxis.axis_label = 'Grades'
q2.xaxis.axis_label = 'Percentage of Grades'
q2.yaxis.axis_label = 'Grades'

p3.xaxis.axis_label = 'Percentage of Grades'
p3.yaxis.axis_label = 'Grades'
q3.xaxis.axis_label = 'Percentage of Grades'
q3.yaxis.axis_label = 'Grades'

p4.xaxis.axis_label = 'Percentage of Grades'
p4.yaxis.axis_label = 'Grades'
q4.xaxis.axis_label = 'Percentage of Grades'
q4.yaxis.axis_label = 'Grades'

p5.xaxis.axis_label = 'Percentage of Grades'
p5.yaxis.axis_label = 'Grades'
q5.xaxis.axis_label = 'Percentage of Grades'
q5.yaxis.axis_label = 'Grades'

p6.xaxis.axis_label = 'Percentage of Grades'
p6.yaxis.axis_label = 'Grades'
q6.xaxis.axis_label = 'Percentage of Grades'
q6.yaxis.axis_label = 'Grades'

p7.xaxis.axis_label = 'Percentage of Grades'
p7.yaxis.axis_label = 'Grades'
q7.xaxis.axis_label = 'Percentage of Grades'
q7.yaxis.axis_label = 'Grades'


#p.circle(GilrsAD2011, marks, size=15, fill_color="orange", line_color="green", line_width=3)
p.circle(GilrsAD2011, marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q.square(GilrsAD2012, marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p.circle(BoysAD2011, marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q.square(BoysAD2012, marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

p1.circle(Girls_2011[1, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q1.square(Girls_2012[1, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p1.circle(Boys_2011[1, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q1.square(Boys_2012[1, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

p2.circle(Girls_2011[2, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q2.square(Girls_2012[2, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p2.circle(Boys_2011[2, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q2.square(Boys_2012[2, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

p3.circle(Girls_2011[3, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q3.square(Girls_2012[3, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p3.circle(Boys_2011[3, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q3.square(Boys_2012[3, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

p4.circle(Girls_2011[4, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q4.square(Girls_2012[4, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p4.circle(Boys_2011[4, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q4.square(Boys_2012[4, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

p5.circle(Girls_2011[5, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q5.square(Girls_2012[5, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p5.circle(Boys_2011[5, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q5.square(Boys_2012[5, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

p6.circle(Girls_2011[6, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q6.square(Girls_2012[6, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p6.circle(Boys_2011[6, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q6.square(Boys_2012[6, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

p7.circle(Girls_2011[7, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
q7.square(Girls_2012[7, 5:14], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p7.circle(Boys_2011[7, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')
q7.square(Boys_2012[7, 5:14], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')


# make a grid
grid = gridplot([p, q, p1, q1, p2, q2, p3, q3, p4, q4, p5, q5, p6, q6, p7, q7], ncols=4, plot_width=250, plot_height=250)

# show the results
show(grid)