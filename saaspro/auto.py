import sys
import os

avg = sys.argv
objectName = avg[1]
print(objectName)
if (objectName == 'saaspro'):
    path = "/Users/mr.heiue/apps/site/saaspro"
print(path)
try:
    os.system("cd " + path + " && git pull && git add . && git commit -m 'wyz' && git push")
    # os.system("git pull && git add . && git commit -m 'wyz' && git push")
except:
    print("异常")
else:
    print("ok")
