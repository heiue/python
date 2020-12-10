from datetime import datetime
import time

print(datetime.utcnow())

print(datetime.today().timestamp())

print(int(time.time()))

print(time.strftime("%Y-%m-%d %H:%M:%S"), int(time.time()))