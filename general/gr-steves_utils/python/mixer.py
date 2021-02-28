#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 gr-steves_utils author.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy
from gnuradio import gr

class mixer(gr.basic_block):
    """
    docstring for block mixer
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="mixer",
            in_sig=[numpy.complex64, numpy.complex64],
            out_sig=[numpy.complex64, ])

    def forecast(self, noutput_items, ninput_items_required):
        #print("Forecast noutput_items: ", noutput_items)

        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        #print("Length of input items: ", len(input_items))
        #for i in input_items:
            #print(len(i))
        #for o in output_items:
            #print(len(o))

        #print("First input: ", input_items[0][0])
        
        #print("Length of output items: ", len(output_items))

        for index in range(len(output_items[0])):
            output_items[0][index] = input_items[0][index] * input_items[1][index]

        self.consume_each(len(output_items[0]))
        return len(output_items[0])
