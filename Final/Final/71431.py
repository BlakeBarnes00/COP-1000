seconds = int(input("Enter number of seconds:"))
minutes = seconds // 60
seconds = seconds % 60

hours = minutes // 60
minutes = minutes % 60

days = hours // 24
hours = hours % 24

print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), and {seconds} second(s).")