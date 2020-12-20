minimum_sleep = int(input())
maximum_sleep = int(input())
current_sleep = int(input())
if current_sleep > maximum_sleep:
    print("Excess")
else:
    if current_sleep >= minimum_sleep:
        print("Normal")
    else:
        print("Deficiency")
