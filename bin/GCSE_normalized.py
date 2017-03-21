#!/usr/bin/python
# -*- coding: utf-8 -*-

from io import StringIO
from matplotlib.pyplot import cm 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from more_itertools import unique_everseen
import textwrap
import math

boys = []
girls = []

tdata=pd.read_csv('GCSE_grades.csv')

All_Data = np.array(tdata)


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

bcmp_2012G = []
bcmp_2011G = []
bcmp_2012B = []
bcmp_2011B = []

for subjects in Girls_2012:
    if subjects[0] == 'Biology' or  subjects[0] == 'Chemistry' or  subjects[0] == 'Mathematics' or  subjects[0] == 'Mathematics (Addit.)' or  subjects[0] == 'Physics':
        bcmp_2012G.append(subjects)
BCMP_2012G = np.array(bcmp_2012G)
#print BCMP_2012G

for subjects in Boys_2012:
    if subjects[0] == 'Biology' or  subjects[0] == 'Chemistry' or  subjects[0] == 'Mathematics' or  subjects[0] == 'Mathematics (Addit.)' or  subjects[0] == 'Physics':
        bcmp_2012B.append(subjects)
BCMP_2012B = np.array(bcmp_2012B)
#print BCMP_2012B


f, ax = plt.subplots(1, figsize=(30,10))

bar_width = 0.2

# positions of the left bar-boundaries
bar_l = [i for i in range(len(BCMP_2012G[:,0]))] 

tick_pos = [i+(bar_width/2) for i in bar_l] 



xs = [i for i, _ in enumerate(BCMP_2012G)]


plt.bar(bar_l, BCMP_2012G[xs,5], width=bar_width,
             label='A+', alpha=0.5, color='#19B61C') 
plt.bar(bar_l, BCMP_2012G[xs,6], width=bar_width,
          bottom=BCMP_2012G[xs,5], label='A', alpha=0.5, color='#F4F80C')
plt.bar(bar_l, BCMP_2012G[xs,7], width=bar_width,
          bottom=[i+j for i,j in zip(BCMP_2012G[xs,5],BCMP_2012G[xs,6])], label='B', alpha=0.5, color='#FF5733')
plt.bar(bar_l, BCMP_2012G[xs,8], width=bar_width,
         bottom=[i+j+k for i,j,k in zip(BCMP_2012G[xs,5],BCMP_2012G[xs,6], BCMP_2012G[xs,7])], label='C', alpha=0.5, color='#0861A2')
plt.bar(bar_l, BCMP_2012G[xs,9], width=bar_width,
         bottom=[i+j+k+w for i,j,k,w in zip(BCMP_2012G[xs,5],BCMP_2012G[xs,6], BCMP_2012G[xs,7], BCMP_2012G[xs,8])], label='D', alpha=0.5, color='#5D26AE')
plt.bar(bar_l, BCMP_2012G[xs,10], width=bar_width,
         bottom=[i+j+k+w+e for i,j,k,w,e in zip(BCMP_2012G[xs,5],BCMP_2012G[xs,6], BCMP_2012G[xs,7],BCMP_2012G[xs,8], BCMP_2012G[xs,9])], label='E', alpha=0.5, color='#D61FAD')
plt.bar(bar_l, BCMP_2012G[xs,11], width=bar_width,
         bottom=[i+j+k+w+e+y for i,j,k,w,e,y in zip(BCMP_2012G[xs,5],BCMP_2012G[xs,6], BCMP_2012G[xs,7],BCMP_2012G[xs,8], BCMP_2012G[xs,9], BCMP_2012G[xs,10])], label='F', alpha=0.5, color='#C70039')
plt.bar(bar_l, BCMP_2012G[xs,12], width=bar_width,
         bottom=[i+j+k+w+y+e+q for i,j,k,w,e,y,q in zip(BCMP_2012G[xs,5],BCMP_2012G[xs,6], BCMP_2012G[xs,7],BCMP_2012G[xs,8],BCMP_2012G[xs,9], BCMP_2012G[xs,10], BCMP_2012G[xs,11])], label='G', alpha=0.5, color='#780D14')
plt.bar(bar_l, BCMP_2012G[xs,13], width=bar_width,
         bottom=[i+j+k+w+e+y+q+f for i,j,k,w,e,y,q,f in zip(BCMP_2012G[xs,5],BCMP_2012G[xs,6], BCMP_2012G[xs,7], BCMP_2012G[xs,8],BCMP_2012G[xs,9],BCMP_2012G[xs,10],BCMP_2012G[xs,11],BCMP_2012G[xs,12])], label='U', alpha=0.5, color='#5A5858')

#make labels
rects = ax.patches
labels = ['Girls']
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height *5, label, ha='center', va='bottom')

bar_l1 = [i + 0.2 for i in range(len(BCMP_2012G[:,0]))] 

plt.bar(bar_l1 , BCMP_2012B[xs,5], width=bar_width,
            alpha=0.5, color='#19B61C') 
plt.bar(bar_l1, BCMP_2012B[xs,6], width=bar_width,
          bottom=BCMP_2012B[xs,5],  alpha=0.5, color='#F4F80C')
plt.bar(bar_l1, BCMP_2012B[xs,7], width=bar_width,
          bottom=[i+j for i,j in zip(BCMP_2012B[xs,5],BCMP_2012B[xs,6])], alpha=0.5, color='#FF5733')
plt.bar(bar_l1, BCMP_2012B[xs,8], width=bar_width,
         bottom=[i+j+k for i,j,k in zip(BCMP_2012B[xs,5],BCMP_2012B[xs,6], BCMP_2012B[xs,7])] , alpha=0.5, color='#0861A2')
plt.bar(bar_l1, BCMP_2012B[xs,9], width=bar_width,
         bottom=[i+j+k+w for i,j,k,w in zip(BCMP_2012B[xs,5],BCMP_2012B[xs,6], BCMP_2012B[xs,7], BCMP_2012B[xs,8])], alpha=0.5, color='#5D26AE')
plt.bar(bar_l1, BCMP_2012B[xs,10], width=bar_width,
         bottom=[i+j+k+w+e for i,j,k,w,e in zip(BCMP_2012B[xs,5],BCMP_2012B[xs,6], BCMP_2012B[xs,7],BCMP_2012B[xs,8], BCMP_2012B[xs,9])], alpha=0.5, color='#D61FAD')
plt.bar(bar_l1, BCMP_2012B[xs,11], width=bar_width,
         bottom=[i+j+k+w+e+y for i,j,k,w,e,y in zip(BCMP_2012B[xs,5],BCMP_2012B[xs,6], BCMP_2012B[xs,7],BCMP_2012B[xs,8], BCMP_2012B[xs,9], BCMP_2012B[xs,10])], alpha=0.5, color='#C70039')
plt.bar(bar_l1, BCMP_2012B[xs,12], width=bar_width,
         bottom=[i+j+k+w+y+e+q for i,j,k,w,e,y,q in zip(BCMP_2012B[xs,5],BCMP_2012B[xs,6], BCMP_2012B[xs,7],BCMP_2012B[xs,8],BCMP_2012B[xs,9], BCMP_2012B[xs,10], BCMP_2012B[xs,11])], alpha=0.5, color='#780D14')
plt.bar(bar_l1, BCMP_2012B[xs,13], width=bar_width,
         bottom=[i+j+k+w+e+y+q+f for i,j,k,w,e,y,q,f in zip(BCMP_2012B[xs,5],BCMP_2012B[xs,6], BCMP_2012B[xs,7], BCMP_2012B[xs,8],BCMP_2012B[xs,9],BCMP_2012B[xs,10],BCMP_2012B[xs,11],BCMP_2012B[xs,12])], alpha=0.5, color='#5A5858')

subjects = BCMP_2012G[:,0]
xs = [i + 0.1 for i, _ in enumerate(subjects)]
plt.xticks([i + 0.2 for i, _ in enumerate(subjects)], subjects, fontsize=10, ha = 'center')
plt.yticks([10 * i for i in range(11)])
lgd = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


labels = ['Boys']
plt.annotate(labels, xy = (20, 20), xytext=(3, -5))
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()*1.5, height * 5, label, ha='center', va='bottom')


plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width*2])
plt.ylabel('Normalised results [%] by grade')

plt.title('2012 GCSE Reults')
#plt.show()

plt.savefig('Normalised_GCSE_2012_Both.png', orientaton = 'portrait', bbox_extra_artists=(lgd,), bbox_inches='tight')

