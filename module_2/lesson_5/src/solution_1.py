company_name = input('Введите название компании: ')
len_half_name: int = len(company_name) // 2
new_company_name = company_name[len_half_name:] + company_name[:len_half_name]
print(new_company_name)