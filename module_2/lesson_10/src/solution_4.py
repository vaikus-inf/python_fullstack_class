def choose_ad_platform(budget: int = 0) -> str:
    if budget <= 0:
        return 'Для проведения рекламной кампании нужны деньги!'
    if 0 < budget < 1000:
        return 'Google'
    elif 1000 <= budget <= 5000:
        return 'Facebook'
    return 'Instagram'

print(choose_ad_platform(500))
print(choose_ad_platform(3000))
print(choose_ad_platform(6000))