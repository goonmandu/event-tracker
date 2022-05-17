class Fap:
    def __init__(self, year, month, day, hour, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute


event = Fap(2022, 5, 18, 17, 32)

print(event.year, event.month, event.day, event.hour, event.minute)

