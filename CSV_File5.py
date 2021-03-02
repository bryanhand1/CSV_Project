# import modules needed
import csv
from datetime import datetime

# Open the needed files
open_file = open("sitka_weather_2018_simple.csv", "r")
sitka_file = csv.reader(open_file, delimiter=",")

open_file2 = open("death_valley_2018_simple.csv", "r")
death_valley_file = csv.reader(open_file2, delimiter=",")
