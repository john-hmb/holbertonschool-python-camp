#!/usr/bin/python3
#for i in range(0,99):
#    print("{0} = 0x{1:x}".format(i,i))

for i in range(0,100):
    if i<10:
    	print("0{}".format(i),end=",")
    else:
        print("{}".format(i),end=",")
