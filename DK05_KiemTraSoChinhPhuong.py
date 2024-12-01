import math
import sys
a= input()
aa= int(a)
if aa >=0 :
    ix= int(math.sqrt(aa))
    if ix * ix == aa:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    sys.exit()
   