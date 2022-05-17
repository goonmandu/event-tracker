from enum import Enum


class Material(Enum):
    HENTAI = 1
    IRL = 2
    RENDER = 3
    ASMR = 4


class Parties(Enum):
    MALE_MALE = 1
    MALE_FEMALE = 2
    FEMALE_FEMALE = 3
    SOLO_MALE = 4
    SOLO_FEMALE = 5
    OTHER = 6


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


with open("data", "r+") as data:
    fap_array = []
