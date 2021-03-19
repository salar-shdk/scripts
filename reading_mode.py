import os

CONFIG_FILE = '/home/salar/scripts/bin/tmp_reading_mode.txt'

COLD_COMMAND = 'redshift -O 16666'
WARM_COMMAND = 'redshift -O 2666'
CLEAN_COMMAND = 'redshift -x'

with open(CONFIG_FILE,'r') as f:
    mode = int(f.read())

with open(CONFIG_FILE, 'w') as f:
    if mode == 4:
        mode = -1
        os.system(CLEAN_COMMAND)
    elif mode%2 == 0:
        os.system(COLD_COMMAND)
    else:
        os.system(WARM_COMMAND)
    mode += 1
    f.write(str(mode))
