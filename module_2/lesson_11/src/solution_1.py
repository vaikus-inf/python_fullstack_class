def sum_sales_with_for(sales_list: list[int]) -> None:
    sum_sales: int = 0
    for item in sales_list:
        sum_sales += item

    print('Сумма продаж: ', end='')
    print(*sales_list, sep='+', end=f'={str(sum_sales)}\n')

sum_sales_with_for([100, 200, 300])
sum_sales_with_for([15, 23, 39, 50])