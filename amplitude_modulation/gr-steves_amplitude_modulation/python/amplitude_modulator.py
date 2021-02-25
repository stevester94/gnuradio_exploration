#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 gr-steves_amplitude_modulation author.
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

def sin_generator(samp_rate_Hz, amplitude, freq_Hz, phase_Hz):
    period_sec = 1.0/freq_Hz
    secs_per_sample = 1.0/samp_rate_Hz

    time = numpy.arange(0, period_sec, secs_per_sample) 

    sine_signal = amplitude * numpy.sin(2 * numpy.pi * freq_Hz * time + phase_Hz)

    while True:
        for s in sine_signal:
            yield s

class amplitude_modulator(gr.basic_block):
    """
    docstring for block amplitude_modulator
    """
    def __init__(self, samp_rate, amp_carrier, freq_carrier_Hz):
        gr.basic_block.__init__(self,
            name="amplitude_modulator",
            in_sig=[numpy.float32, ],
            out_sig=[numpy.float32, ])

        self.carrier_gen = sin_generator(samp_rate, amp_carrier, freq_carrier_Hz, 0)

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        for index in range(len(output_items[0])):
            s = next(self.carrier_gen)
            #output_items[0][index] = input_items[0][index]
            output_items[0][index] = s

        self.consume_each(len(output_items[0]))
        return len(output_items[0])
