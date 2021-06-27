def typing_speed(words, time) -> float:
	if  words >= 0 and time >= 0:
		return 60 * words/time

print(typing_speed(10, 2))