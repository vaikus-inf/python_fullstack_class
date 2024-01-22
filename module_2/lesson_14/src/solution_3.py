from typing import Iterator

def report_generator(*report_pages) -> Iterator[str]:
    return (f'{i + 1}-я страница отчета' for i in range(len(report_pages)))

print(report_generator('Стр1', 'Стр2'))