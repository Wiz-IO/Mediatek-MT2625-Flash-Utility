############################################################################
 # 
 # MT2625 Flash Utility ... Backup NVDM
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

FILE_NAME = ""
COM_PORT  = "COM21"

print "MT2625 - NVDM Backup 2019 Georgi Angelov\n"
if len(sys.argv) < 3:
    print "Usage: python backup.py backup.bin COM_PORT"
    exit()

FILE_NAME = sys.argv[1]
COM_PORT  = sys.argv[2]

print "SAVE TO:", FILE_NAME

m = MT2625( Serial( COM_PORT, 115200 ) ) 
m.connect( 5.0 ) # wait power-on timeout in seconds  
m.da_start( True ) # read nvdm info 
m.downloadNVDM( FILE_NAME )
m.da_finish()

