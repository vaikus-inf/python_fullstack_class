import time, random

def work_time(func):
    def wrapper(*args, **kwargs):
        start_work = time.perf_counter()
        func(*args, **kwargs)
        finish_work = time.perf_counter()
        print(f'Execution: {round(finish_work - start_work, 2)} seconds')
    return wrapper    

@work_time
def create_design(*args) -> None:
    time.sleep(random.uniform(1, 3))

create_design('Логотип Васильевский рынок')
create_design('Макет сайта логомашины')