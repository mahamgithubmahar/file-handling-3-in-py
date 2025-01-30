dat=open("codingal1.txt",'x')
dat.close()

import os
if os.path.exists("codingal2.txt"):
    os.remove("codingal2.txt")
else:
    print("error")