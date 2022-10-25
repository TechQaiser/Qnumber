import os
import platform as d
main = d.uname().machine
if '64' in main:
    import detail
    detail.main()
elif '32' in main:
    import detail32
    detail32.main()
else:
    exit(' Sorry Your Device Is Not Reachable !')

