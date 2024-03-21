# initialize a variable used to hold latest maximum number
maximum = 0
# loop
while True:
    x = input()
    if x == "Stop":
        # output
        print(maximum)
        break
    # if Stop not given, convert x to integer to avoid runtime errors
    else:
        x = int(x)
    # processing code
    if x > maximum:
        maximum = x
