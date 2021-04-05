# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:56:55 2021

@author: Matt
"""

import pandas as pd
import numpy as np
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib

#Loading Matches
df1 = pd.read_csv("TRA(H).csv")
df2 = pd.read_csv("CHE(A).csv")
df3 = pd.read_csv("GRI(A).csv")
df4 = pd.read_csv("COL(H).csv")
df5 = pd.read_csv("OLD(H).csv")
df6 = pd.read_csv("BRA(A).csv")
df7 = pd.read_csv("MOR(A).csv")
df8 = pd.read_csv("CAR(H).csv")
df9 = pd.read_csv("LEY(A).csv")
df10 = pd.read_csv("SCN(H).csv")
df11 = pd.read_csv("CRW(H).csv")
df12 = pd.read_csv("WAL(A).csv")
df13 = pd.read_csv("CAM(H).csv")
df14 = pd.read_csv("MAN(A).csv")
df15 = pd.read_csv("POV(H).csv")
df16 = pd.read_csv("SAL(A).csv")
df17 = pd.read_csv("HRG(H).csv")
df18 = pd.read_csv("FGR(H).csv")
df19 = pd.read_csv("SOU(A).csv")
df20 = pd.read_csv("BOL(H).csv")
df21 = pd.read_csv("HRG(A).csv")
df22 = pd.read_csv("STE(H).csv")

#Combining Dataframes
all_gw = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,
          df16,df17,df18,df19,df20,df21,df22]
df = pd.concat(all_gw)

#Filtering Team
df = df[df['teamId']==98]

#Filtering Player
df = df[df['playerId']==362157]

#Filtering Shots
df = df[((df['type/displayName']=="Goal") | (df['type/displayName']=="MissedShots") |
        (df['type/displayName']=="SavedShot"))]

#Fonts
matplotlib.font_manager._rebuild()
plt.rcParams['font.family'] = 'Myriad Pro'
colour = '#FFF8F8'
plt.rcParams['text.color'] = colour

#Custom Colormap
colors1 = ['#1B1B1B', '#E50038']
n_bins = 100
cmap_name = 'my_list'
cm1 = LinearSegmentedColormap.from_list('my_list', colors1, N=n_bins)

#Plot Pitch
fig, ax = plt.subplots()
fig.set_facecolor('#1B1B1B')
fig.patch.set_facecolor('#1B1B1B')
pitch = Pitch(pitch_type='opta', orientation='vertical',
              pitch_color='#1B1B1B', line_color='#3E3E3E',
              constrained_layout=True, tight_layout=False, goal_type="box",
              linewidth=0.5, view='half')
pitch.draw(ax=ax)
h = pitch.hexbin(df.x,df.y, ax=ax, cmap=cm1, alpha=0.7, linewidth=1,
                 gridsize=(12,12), linewidths=0, mincnt=1, edgecolors='#1B1B1B',
                 hatch='//////', vmin=0, vmax=2)
counts = h.get_array()
verts = h.get_offsets()
for i in range(len(counts)):
    pitch.annotate(int(counts[i]), xy=(verts[i][1], verts[i][0]),ha="center",va="center",
                   size=6,ax=ax,zorder=3)
#clip to rectangle
rect = Rectangle((pitch.top, pitch.left), pitch.bottom - pitch.top, pitch.right - pitch.left, facecolor="None")
ax.add_patch(rect)
h.set_clip_path(rect)
plt.text(100,103,"#10 Archie Collins", 
             fontsize=10, color="#FFF8F8", fontweight = 'bold')
plt.text(100,101,"All Shot Locations | EFL League Two 2020", 
             fontsize=6, color="#FFF8F8", alpha=0.5)
plt.text(12,101,"@trevillion_", color='#FFF8F8', fontsize=6, alpha=0.5)
plt.savefig('C:/Users/Matt/Documents/Football Data/matplotlib/Exeter City/EFL2 20-21/ArchieCollins.png', 
            dpi=500, bbox_inches="tight",facecolor='#1B1B1B')

