import time


def countdown(func):
    def wrapper():
        sec = 3
        while sec > 0:
            print(sec)
            time.sleep(1)
            sec -= 1
        print(func())
    return wrapper


@countdown
def what_time_is_it_now() -> str:
    return str(time.strftime("%H:%M"))


what_time_is_it_now()
