speed = int(input("What was your average speed in km/h? \n"))
allowed_speed = int(input("What was the allowed speed on the road? \n"))
demerit_points = (speed - allowed_speed)/5
if speed <= allowed_speed:
    print("OK")
if speed > allowed_speed:
    print("Points:" )
    print(int(demerit_points))
if demerit_points > 12:
    print("Time to go to jail!")