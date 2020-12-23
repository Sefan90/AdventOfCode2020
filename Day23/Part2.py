data = open("input.txt").read()

clock = [int(i) for i in data]
for x in range(max(clock) + 1, 1000000 + 1):
    clock.append(x)
first = clock[0]
last = clock[-1]
clock_dict = {clock[k-1]:clock[k] for k in range(1, len(clock))}
clock_dict[last] = first
# dict[key=current cup value] = value = next cup value

curr_cup_key = first
move = 1

for _ in range(10000000):
    pick_up = []
    #Save pointer number for third ahead
    third_pointer = clock_dict[clock_dict[clock_dict[clock_dict[curr_cup_key]]]]
    #Save a list of our values so we can make sure to not jump to those
    tmp_lista = [clock_dict[curr_cup_key],clock_dict[clock_dict[curr_cup_key]],clock_dict[clock_dict[clock_dict[curr_cup_key]]]]
    #Save pointer for the value our number is headed, make sure our number exists and is not in our lista
    lookahead_key = 0
    for counter in range(1,5):
        tmp_key = curr_cup_key - counter
        if tmp_key < 1:
            tmp_key += len(clock)
        if tmp_key not in tmp_lista:
            lookahead_key = tmp_key
            break
    lookahead_pointer = clock_dict[lookahead_key]
    #Repoint headed number to start of our three
    clock_dict[lookahead_key] = clock_dict[curr_cup_key]
    #Repoint last of our three to our saved value
    clock_dict[clock_dict[clock_dict[clock_dict[curr_cup_key]]]] = lookahead_pointer
    #Repoint current to value of 3 ahead
    clock_dict[curr_cup_key] = third_pointer
    curr_cup_key = clock_dict[curr_cup_key]

first = clock_dict[1]
second = clock_dict[clock_dict[1]]

print(first * second)