sellers =  ['Света', 'Маша', 'Олег', 'Паша']
work_on_even_days = sellers[::2]
work_on_odd_days = sellers[1::2]
print('В чётные дни работают:', *work_on_even_days, '\n', '\nВ нечётные дни:', *work_on_odd_days)