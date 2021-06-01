# Write a loop that reads strings from standard input, where the string
# is either "duck" or "goose". The loop terminates when "goose" is read
# in. After the loop, your code should print the number of "ducks" that
# were read

duckCount = 0
bird = ''

while bird != "goose":
	bird = input()
	if bird == "duck":
		duckCount += 1

print(f"Duck count: {duckCount}")