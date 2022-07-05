from enum import Enum
# import matplotlib as plt  TODO: WTF IT WON'T IMPORT


def ldzero(numstr) -> str:
    return "%02d" % int(numstr)


""" LOL IM NOT GONNA IMPLEMENT ENUMS
class Material(Enum):
    HENTAI = 1
    IRL    = 2
    RENDER = 3
    ASMR   = 4


class Parties(Enum):
    MALE_MALE     = 1
    MALE_FEMALE   = 2
    FEMALE_FEMALE = 3
    SOLO_MALE     = 4
    SOLO_FEMALE   = 5
    OTHER         = 6
"""


class Fap:
    def __init__(self, year, month, day, hour, minute, duration, material, parties):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.material = material
        self.parties = parties

    def __str__(self):
        return f"{ldzero(self.year)}-{ldzero(self.month)}-{ldzero(self.day)} {ldzero(self.hour)}:{ldzero(self.minute)} for {self.duration}m, to {self.material} starring {self.parties}"


with open("data", "r+") as data:
    # 2D Array [[ele, ments], [ele, ments]] etc
    fap_array = [field.strip("\n").split(" ") for field in data]
    data.read()  # Push position to end of file for append mode. Pretty sure there's a better way to do this


def add_entry():
    entry_attrs = []
    date = input("Date (YYYY-MM-DD): ").split("-")
    for item in date:
        entry_attrs.append(item)
    time = input("Time (HH:MM): ").split(":")
    for item in time:
        entry_attrs.append(item)
    material = input("Material: ")
    entry_attrs.append(material)
    people = input("To whom (Genders): ")
    entry_attrs.append(people)
    for attr in entry_attrs:
        data.write(attr)

list_of_instances = []

monthly_totals = {
    "yearly": 0,
    "january": 0,
    "february": 0,
    "march": 0,
    "april": 0,
    "may": 0,
    "june": 0,
    "july": 0,
    "august": 0,
    "september": 0,
    "october": 0,
    "november": 0,
    "december": 0,
}

day_totals = {
    "monday": 0,
    "tuesday": 0,
    "wednesday": 0,
    "thursday": 0,
    "friday": 0,
    "saturday": 0,
    "sunday": 0
}

monthly_averages = {
    "yearly": 0,
    "january": 0,
    "february": 0,
    "march": 0,
    "april": 0,
    "may": 0,
    "june": 0,
    "july": 0,
    "august": 0,
    "september": 0,
    "october": 0,
    "november": 0,
    "december": 0,
}

streaks = {
    "yes_fap": 0,
    "no_fap": 0
}


def load_data():
    for entry in fap_array:
        aux = []
        for member in entry:
            aux.append(member)
        list_of_instances.append(Fap(aux[0], aux[1], aux[2], aux[3], aux[4], aux[5], aux[6], aux[7]))


def debug_print():
    for fap in list_of_instances:
        print(str(fap))


def sum_monthly():
    pass


def average_monthly():
    pass


def get_streaks():
    pass


def sum_daily():
    pass



load_data()
debug_print()