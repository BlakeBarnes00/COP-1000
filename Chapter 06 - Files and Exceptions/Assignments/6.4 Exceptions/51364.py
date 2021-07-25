sum=0
badvalues=""
try:
	sum += int(x)
except ValueError:
	badvalues += " x"
try:
	sum += int(y)
except ValueError:
	badvalues += " y"
try:
	sum += int(z)
except ValueError:
	badvalues += " z"
if badvalues==" ":
	print(sum)
else:
	print("bad value(s) in:"+badvalues)