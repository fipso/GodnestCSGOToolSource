# -*- coding: utf-16 -*-
import sys
import codecs

with codecs.open(sys.argv[1], "r", "utf-16") as file:
    lines = file.readlines()

lines = [x.strip() for x in lines]

chars = u"АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"

for line in lines:
    for char in line:
        for ruskiChar in chars:
            if char == ruskiChar:
                print(char)

# WORK IN PROGESS !
