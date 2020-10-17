import sys
import os

avg = sys.argv
objectName = avg[1]
if (objectName == 'saaspro'):
    path = "/Users/mr.heiue/apps/site/saaspro"
try:
    os.system("cd " + path)
    os.system("git pull && git add . && git commit -m 'wyz' && git push")
except:
    print("异常")
else:
    print("ok")
