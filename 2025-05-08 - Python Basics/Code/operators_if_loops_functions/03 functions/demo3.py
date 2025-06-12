from datetime import datetime
import time

def print_time():
    now = datetime.now()
    print(now.time())

print_time()
time.sleep(1)
print_time()
time.sleep(3)
print_time()
