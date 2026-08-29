#!/usr/bin/env python3

import time

# Count down from 10 to 1, pausing for one second per iteration.
for i in range(10, 0, -1):
    time.sleep(1)
    print(f"{i} seconds to launch!")

# Execute final launch sequence after the countdown completes.
print("Lift off!")
