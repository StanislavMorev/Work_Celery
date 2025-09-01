from datetime import datetime, timedelta

from celery import Celery
from time import sleep

app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')# брокер )

# celery -A tasks worker -l info --pool=solo запуск
# process.delay(2,3) запуск python -i tasks.py   
@app.task
def process(x, y):
    i = 0
    while i < 5:
        sleep(1)
        i += 1
        print('Обработка')

    return x**2 + y**2


# Пример с apply_async
'''
это сахар delay но с большим выбором действий


# выполнится через 10 секунд
process.apply_async((2, 3), countdown=10)
'''

if __name__ == '__main__':
    print(process.apply_async((2, 3), expires=60))