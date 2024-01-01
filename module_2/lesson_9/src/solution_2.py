def convert_to_hex(*args):
    return(hex(args[0])[2:] + hex(args[1])[2:] + hex(args[2])[2:])

print(convert_to_hex(255, 0, 1))