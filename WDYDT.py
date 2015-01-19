import time
import os.path
print("So, what did you do today?\n")
path="entry\\"+time.strftime("%Y %m %d")+".txt"
if os.path.isfile(path):
    f=open(path,'r')
    print f.read()
    f.close()
f=open(path,'a')
f.write("\n")
ex=0
while not ex:
    st=raw_input()
    if st=='':
        ex=1
    else:
        f.write(st+"\n")
f.close()
