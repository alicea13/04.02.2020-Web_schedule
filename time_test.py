import datetime
import schedule


i = 1


def process():
    global i
    print(f"Запустили уже {i} раз")
    i += 1
    print(datetime.datetime.now())


schedule.every().tuesday.at("12:43").do(process)

while True:
    schedule.run_pending()