from enum import Enum
# import matplotlib  TODO: pip3 install matplotlib

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

    def to_string(self):  # TODO: Format ints to be 2 digits long with leading zeroes
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute} for {self.duration}m, to {self.material} starring {self.parties}"


with open("data", "r+") as data:
    # 2D Array
    fap_array = [field.strip("\n").split(" ") for field in data]

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

daily_totals = {
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
        print(fap.to_string())


def sum_monthly():
    pass