import datetime
def period_is_late(last,today,cycle_length):
    return True if today.toordinal() - last.toordinal() > cycle_length else False

if __name__ == "__main__":
    datetime_1 = datetime.datetime.now()
    datetime_2 = datetime.datetime.now()
    cycle_length = 0
    print(period_is_late(datetime_1,datetime_2, cycle_length))
    