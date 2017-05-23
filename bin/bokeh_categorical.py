from __future__ import division
from itertools import chain
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row
from bokeh.layouts import gridplot
from bokeh.palettes import Viridis3
from bokeh.models import Range1d
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


# seting work directory
#os.chdir('./bin')
#os.getcwd() # checking the working directory

tdata=pd.read_csv('GCSE_grades.csv')

AllData = pd.DataFrame(tdata)

Boys_2011 = AllData.loc[(AllData['Gender'] == 'Male') & (AllData['Year'] == 2011)]
Boys_2012 = AllData.loc[(AllData['Gender'] == 'Male') & (AllData['Year'] == 2012)]

Girls_2011 = AllData.loc[(AllData['Gender'] == 'Female') & (AllData['Year'] == 2011)]
Girls_2012 = AllData.loc[(AllData['Gender'] == 'Female') & (AllData['Year'] == 2012)]

Boys_2011 = Boys_2011.drop(Boys_2011.columns[1:5], 1)
Boys_2012 = Boys_2011.drop(Boys_2011.columns[1:5], 1)
Girls_2011 = Girls_2011.drop(Girls_2011.columns[1:5], 1)
Girls_2012 = Girls_2011.drop(Girls_2011.columns[1:5], 1)
df = Girls_2011.set_index('Subject').T
marks = ['A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'U']
df['Marks'] = range(len(marks))
dboys = Boys_2011.set_index('Subject').T

# 4 columns per row, so:
#print ('Number of rows:' ), len(df.columns)/4

x_column = 'Marks'
cols = list(df.columns.values)
cols.remove(x_column)
#print (cols)

fig, axes = plt.subplots(nrows=int(len(df.columns)/4), ncols=4, sharex=True, sharey=True, figsize=(30,30))
flat_axes = chain(*axes)

for y_column, ax in zip(cols, flat_axes):
    if y_column != x_column:
        x = df[x_column]
        y = df[y_column]

        ax.plot(x, y, 'ok', label=y_column)
        ax.set_title(y_column)
        ax.set_xticks(x)
        ax.set_xticklabels(marks, fontsize=18)
        ax.figure.savefig('./Girls2011exams.pdf')


    plt.subplots_adjust(hspace=1)

    plt.tight_layout()
#plt.show()


### bokeh ###
output_file("categorical.html")

p1 = figure(y_range=marks, title = 'Biology')
p2 = figure(y_range=marks, title = 'Chemistry')

p1.title.align = 'center'
p2.title.align = 'center'


p1.x_range = Range1d(-1, 41)
p2.x_range = Range1d(-1, 41)


p1.xaxis.axis_label = 'Percentage of Grades'
p1.yaxis.axis_label = 'Grades'
p2.xaxis.axis_label = 'Percentage of Grades'
p2.yaxis.axis_label = 'Grades'


p1.circle(df['Biology'], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p1.circle(dboys['Biology'], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')


p2.circle(df['Chemistry'], marks, size=10, fill_color="green", line_color="black", line_width=1, legend = 'Girls')
p2.circle(dboys['Chemistry'], marks, size=10, fill_color="yellow", line_color="black", line_width=1, legend = 'Boys')

# make a grid
grid = gridplot([p1, p2], ncols=2, plot_width=500, plot_height=500)

# show the results
show(grid)
