from datetime import datetime
import pytz

timezones = ['Europe/Moscow', 'Europe/London', 'Asia/Tokyo']

# Получение текущего времени
now = datetime.now()

# Вывод текущей даты и времени для каждого часового пояса
for tz in timezones:
    tz_obj = pytz.timezone(tz)
    tz_time = now.astimezone(tz_obj)

    # Вывод времени в каждом часовом поясе
    formatted_time = tz_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Время в часовом поясе {tz}: {formatted_time}')
