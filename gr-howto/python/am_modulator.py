#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 gr-howto author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class am_modulator(gr.basic_block):
    """
    docstring for block am_modulator
    """
    def __init__(self):
        print("__init__", flush=True)
        gr.basic_block.__init__(self,
            name="am_modulator",
            in_sig=[numpy.float32, ],
            out_sig=[numpy.float32, ])

    # This method is intended to generate an estimate for how many input items we expect to 
    # require, given the output requested is <noutput_items>
    #
    # I'm not sure why this code originally assumed that ninput_items_required was 
    # a vector, but in practice it was just an integer.

# Wellp I had to delete it anyways

#    def forecast(self, noutput_items, ninput_items_required):
#        print("forecast", flush=True)
#        print(ninput_items_required, flush=True)
#        print(noutput_items, flush=True)
#        #ninput_items_required = [noutput_items,]

    # input and output items are multidim arrays (Assuming one per each input?)
    def general_work(self, input_items, output_items):
        for index in range(len(output_items[0])):
            output_items[0][index] = input_items[0][index]
    
        self.consume_each(len(output_items[0]))
        return len(output_items[0])
