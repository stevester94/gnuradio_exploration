#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2021 <+YOU OR YOUR COMPANY+>.
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

class zero_upsampler(gr.basic_block):
    """
    docstring for block zero_upsampler
    """
    def __init__(self, interpolation_factor):
        gr.basic_block.__init__(self,
            name="zero_upsampler",
            in_sig=[numpy.float32, ],
            out_sig=[numpy.float32, ])
        
        self.interpolation_factor = interpolation_factor


    def forecast(self, noutput_items, ninput_items_required):
        """
        noutput_items: list
        ninput_items_required: we populate this
        """

        # print("[forecast] noutput_items:", noutput_items)
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items / self.interpolation_factor

    # def general_work(self, input_items, output_items):
    #     output_items[0][:] = input_items[0]
    #     consume(0, len(input_items[0]))
    #     #self.consume_each(len(input_items[0]))
    #     return len(output_items[0])
    def general_work(self, input_items, output_items):
        # print("[general_work] input_items", input_items[0].shape)
        # print("[general_work] output_items", output_items[0].shape)

        num_items_to_process = int(min(len(output_items[0]), len(input_items[0])) / self.interpolation_factor)

        index = 0
        num_consumed = 0
        for _ in range(num_items_to_process):
            output_items[0][index] = input_items[0][index]
            index += 1
            num_consumed += 1
            for __ in range(self.interpolation_factor-1):
                if index < num_items_to_process:
                    output_items[0][index] = 0
                    index += 1
    
        self.consume(0, num_consumed)
        # self.consume_each(len(output_items[0]))
        return len(output_items[0])
