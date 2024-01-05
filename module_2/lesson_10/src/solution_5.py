def analyze_ad_efficiency(clicks: int = 0, impressions: int = 0, views: int = 0) -> str:
    clicks_on_impressions: float = clicks / impressions
    if clicks_on_impressions < 0.01 and views > impressions:
        return 'Недооцененная'
    elif 0.01 <= clicks_on_impressions < 0.05:
        return 'Низкая'
    elif 0.05 <= clicks_on_impressions < 0.1 and views > clicks:
        return 'Средняя'
    elif clicks_on_impressions > 0.1:
        return 'Высокая'
    return 'Неопределенная'

print(analyze_ad_efficiency(50, 10000, 15000))
print(analyze_ad_efficiency(200, 10000, 5000))
print(analyze_ad_efficiency(700, 10000, 800))
print(analyze_ad_efficiency(1200, 10000, 1000))
print(analyze_ad_efficiency(500, 10000, 200))