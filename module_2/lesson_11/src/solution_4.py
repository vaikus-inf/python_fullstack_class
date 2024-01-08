def convert_units_with_while(list_values, measurement_system) -> None:
    i: int = 0
    while i < len(list_values):
        print(f'{list_values[i]} {measurement_system[:-1]}({measurement_system[-1]}) = {list_values[i] * 3.28084} foot(feet)')
        i += 1

convert_units_with_while([1, 2], 'meters')