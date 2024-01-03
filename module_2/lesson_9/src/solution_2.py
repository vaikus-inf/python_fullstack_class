def convert_to_hex(r: int = 0, g: int = 0, b: int = 0) -> str: 
    return(f'#{hex(r)[-2:]}{hex(g)[-2:]}{hex(b)[-2:]}'.replace('x', '0').upper())
    
print(f'HEX: {convert_to_hex(255, 0, 0)}')
print(f'HEX: {convert_to_hex(0, 255, 0)}')
print(f'HEX: {convert_to_hex(0, 0, 255)}')
print(f'HEX: {convert_to_hex(7, 36, 110)}')