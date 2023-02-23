#!/bin/python3

import sys #system functions and parameters
#import (very important)
from datetime import datetime as dt #can import and then use alias. Now only have to use dt to reference datetime

print(sys.version)
print(dt.now())


sys.exit() #graceful exit, used when there are errors 
