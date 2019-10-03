#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright (C) Incuvers, Inc - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by David Sean
#

import os
import svgwrite as sw


class Badger(object):

    def __init__(self, **kwargs):
        #        self.img = cv.imread('badge.png')

        self.fname = kwargs.get('fname', 'mybadge.svg')
        self.base_color = sw.utils.rgb(r=87, b=87, g=87, mode='RGB')
        self.state_color = sw.utils.rgb(r=153, b=153, g=153, mode='RGB')
        self.type_color = sw.utils.rgb(r=200, b=200, g=200, mode='RGB')
        self.result_color = sw.utils.rgb(r=255, b=255, g=255, mode='RGB')

        self.dwg = sw.Drawing(self.fname, (170, 20), debug=True)
        self.init_blank()
        self.add_logo()

    def define(self, type, result):
        """ Define badge fields.

        Args:
            type (string): a build type, like "cov" , "test" or "doc". Please keep shorter than 7 chars

            result (string): result of build, like "80.2", "OK", "Fail". Keep shorter than 5 chars.

        """
        if (len(type) > 5):
            print("WARNING: length of 'type' too long, will truncate")
            type = type[0:6]
        if (len(result) > 5):
            print("WARNING: length of 'result' too long, will truncate")
            result = result[0:5]

        type_paragraph = self.dwg.add(self.dwg.g(font_size=12, fill=self.type_color))
        type_paragraph.add(self.dwg.text(type, (58, 15)))

        result_paragraph = self.dwg.add(self.dwg.g(font_size=15, fill=self.result_color))
        result_paragraph.add(self.dwg.text(result, (116, 16)))

    def add_logo(self):
        self.dwg.add(sw.image.Image(os.path.dirname(os.path.realpath(__file__)) +
                                    "/incuvers.svg", insert=(3, 1), size=(50, 20)))

    def init_blank(self):
        px = sw.px

        self.dwg.add(sw.shapes.Rect(insert=(0, 0),
                                    size=(110*px, 20*px), rx=4*px, ry=4*px, fill=self.base_color))
        self.dwg.add(sw.shapes.Rect(insert=(4*px, 0),
                                    size=(110*px, 20*px), rx=0*px, ry=0*px, fill=self.base_color))
        self.dwg.add(sw.shapes.Rect(insert=(110*px, 0*px),
                                    size=(60*px, 20*px), rx=4*px, ry=4*px, fill=self.state_color))
        self.dwg.add(sw.shapes.Rect(insert=(110*px, 0*px),
                                    size=(56*px, 20*px), rx=0*px, ry=0*px, fill=self.state_color))

    def save(self):
        self.dwg.save()
        self.dwg.saveas(self.fname)
