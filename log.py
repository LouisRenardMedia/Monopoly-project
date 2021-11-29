import random 
import numpy 
from datetime import datetime

from numpy.lib.function_base import append
class log:
    def  __init__(self, filename):
        self.file = open(filename,'a+')
        self.write("Start log at " + datetime.now().strftime("%H:%m:%S"))
    def write(self,message):
        self.file.write(message + "\n")
    def close(self):
        self.file.close()
log=log ("log.txt")
log.write("pos:"+str(pos))
log.close()