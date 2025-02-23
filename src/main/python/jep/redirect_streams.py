#
# Copyright (c) 2016-2021 JEP AUTHORS.
#
# This file is licensed under the the zlib/libpng License.
#
# This software is provided 'as-is', without any express or implied
# warranty. In no event will the authors be held liable for any
# damages arising from the use of this software.
# 
# Permission is granted to anyone to use this software for any
# purpose, including commercial applications, and to alter it and
# redistribute it freely, subject to the following restrictions:
# 
#     1. The origin of this software must not be misrepresented; you
#     must not claim that you wrote the original software. If you use
#     this software in a product, an acknowledgment in the product
#     documentation would be appreciated but is not required.
# 
#     2. Altered source versions must be plainly marked as such, and
#     must not be misrepresented as being the original software.
# 
#     3. This notice may not be removed or altered from any source
#     distribution.
#

import sys

class StreamRedirect(object):
    "Redirects a Python output stream to a Java OutputStream"

    def __init__(self, javaOutputStream):
        from java.io import PrintStream
        self.printstream = PrintStream(javaOutputStream)
        self.printmethod = getattr(self.printstream, 'print')
        self.flushmethod = getattr(self.printstream, 'flush')

    def write(self, msg):
        self.printmethod(msg)

    def flush(self):
        self.flushmethod()

def redirectStdout(javaOutputStream):
    sys.stdout = StreamRedirect(javaOutputStream)

def redirectStderr(javaOutputStream):
    sys.stderr = StreamRedirect(javaOutputStream)
