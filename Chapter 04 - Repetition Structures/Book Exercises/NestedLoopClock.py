# This is to practice a nested loop by counting time
import time
year = 0
for year in range(10):
	for months in range(12):
		for weeks in range(1): 
			for days in range(7):
				for hours in range(24):
					for minutes in range(60):
						for seconds in range(60):
							print(f"{year} year(s), {months} month(s), {weeks} week(s), {days} day(s), {hours}:{minutes}:{seconds}")
							time.sleep(1)