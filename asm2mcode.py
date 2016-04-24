import re
'''
test.txt

00FC436E 33 DB                xor         ebx,ebx  
00FC4370 89 5D FC             mov         dword ptr [ebp-4],ebx  
00FC4373 C6 45 FC 63          mov         byte ptr [ebp-4],63h  
00FC4377 C6 45 FD 6D          mov         byte ptr [ebp-3],6Dh  
00FC437B C6 45 FE 64          mov         byte ptr [ebp-2],64h  
00FC437F 6A 05                push        5  
00FC4381 8D 45 FC             lea         eax,[ebp-4]  
00FC4384 50                   push        eax  
00FC4385 B8 70 FF 84 75       mov         eax,7584FF70h  
00FC438A FF D0                call        eax  
00FC438C 6A 01                push        1  
00FC438E B8 30 7B 83 75       mov         eax,75837B30h  
00FC4393 FF D0                call        eax 

'''
t = open(r'C:\Users\hanbit\Desktop\test.txt')
op = ['mov','push','call','lea','pop','inc','dec','sub','call','ret','cmp','jmp','je','jne','jle','jz','jge','xor','or','and','shr','shl']
code = ''
for tt in t.readlines():
    L = tt.split()
    for c in L[1:]:
        if c not in op:
            code += '\\x'+c
        else:
            break       
print(code)
