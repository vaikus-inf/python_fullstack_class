def convert_to_hex(r: int = 0, g: int = 0, b: int = 0) -> str:
    return(f'#{r:02X}{g:02X}{b:02X}')
    
print(f'HEX: {convert_to_hex(255, 0, 0)}')
print(f'HEX: {convert_to_hex(0, 255, 0)}')
print(f'HEX: {convert_to_hex(0, 0, 255)}')
print(f'HEX: {convert_to_hex(7, 36, 110)}')