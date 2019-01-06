 ############################################################################
 # 
 # Mediatek MT2625 Flash Utility ... Uploading OpenCPU Application
 #
 #   Copyright (C) 2019 Georgi Angelov. All rights reserved.
 #   Author: Georgi Angelov <the.wizarda@gmail.com> WizIO
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions
 # are met:
 #
 # 1. Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
 # 2. Redistributions in binary form must reproduce the above copyright
 #    notice, this list of conditions and the following disclaimer in
 #    the documentation and/or other materials provided with the
 #    distribution.
 # 3. Neither the name WizIO nor the names of its contributors may be
 #    used to endorse or promote products derived from this software
 #    without specific prior written permission.
 #
 # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 # "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 # LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 # FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 # COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 # INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 # BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 # OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 # AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 # LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 # ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 # POSSIBILITY OF SUCH DAMAGE.
 #
 ############################################################################
 # Dependency:
 #      https://github.com/pyserial/pyserial/tree/master/serial
 ############################################################################

import os, sys, struct
from serial import Serial
from pyMT2625 import MT2625

DEVICE      = "bc66"
APPLICATION = ""
COM_PORT    = "COM21"

print "MT2625 - OpenCPU Uploader 2019 Georgi Angelov\n"
if len(sys.argv) < 4:
    print "Usage: python upload.py bc66 path/application.bin COM_PORT"
    exit()

DEVICE      = sys.argv[1]
APPLICATION = sys.argv[2]
COM_PORT    = sys.argv[3]

m = MT2625( Serial( COM_PORT, 115200 ) ) 
m.connect( 10.0 ) # wait power-on timeout in seconds    
m.da_start()  
m.uploadApplication( DEVICE, APPLICATION )
m.da_finish()
