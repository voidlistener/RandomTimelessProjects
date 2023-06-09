#!/usr/bin/env python3
# -*- coding: cp1251 -*-
import sys
import locale
import numpy as np
from moviepy.editor import TextClip, CompositeVideoClip

locale.setlocale(locale.LC_ALL, '')
screensize = (100, 100)
duration = 3

text = ''.join(sys.argv[1:]) or "Default Running Line"

txtClip = TextClip(text, color='white', fontsize=40)
speed = (txtClip.size[0] + screensize[0] / 2) / duration

clip = CompositeVideoClip([txtClip.set_pos(lambda t: (100 - speed * t, 'center'))], size=screensize).set_duration(3)

clip.write_videofile(text + '.avi', fps=25, codec='mpeg4')