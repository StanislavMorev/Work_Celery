from celery import Celery
import random

app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')# брокер )

# Retry(повтор задачи)


@app.task(bind=True, max_retries=3, default_retry_delay=5)
# максимум 3 попытки,пауза 5 сек
def unstable_task(self):
    if random.choice([True, False]):
        print('Упало проем снова')
        raise self.retry(exc=Exception('Случайная ошибка')) # повтор задачи
    return "Успех"