error = 0
for x , y in zip(winning_speed , your_speed):
    if error < x - y:
        error = x-y
error
