# RORO
by Samy Abdellatif

This repo is basically for the purpose of learning how to build python distribution packages for several platforms. the python code is in the example_pkg/roroclass.py .. importing python module `turtle` and it has single class roro_class() which contains one method draw_art(lncolor,bgcolor,speed).

draw_art(str::line_color , str::background_color, int::speed) takes three arguement of types string, string, and integer (e.g: draw_art("#FFFFFF","#6699DD",4)) to draw the word RORO in a window screen.

Sample test

from roro import roroclass

roro_instance = roroclass.roro_class()

roro_instance.draw_art("#FFFFFF","#0FFFF0",4)
