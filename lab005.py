def is_valid_part(part):
    try:
        i_part = int(part)
        if part.startswith("0") and not i_part == 0:
            return False
        return 0 <= i_part < 256
    except ValueError as ve:
        return False

#print(is_valid_part("127"))
#print(is_valid_part("AAA"))
#print(is_valid_part("257"))
#print(is_valid_part("01"))
#print(is_valid_part("0"))

def is_valid_ip(ip:str):
    cnt = 0
    parts = ip.split(".")
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part): return False
        cnt += 1
    return True

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False

