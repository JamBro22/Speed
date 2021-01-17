# calculate demerit points based on speed
def calculate_demerit_points_for_speeding(current_speed, speed_limit):
    demerit_points = int((current_speed - speed_limit)/5)

    # if the speed travelled is less than the speed limit, return ok
    if current_speed <= speed_limit:
        return "OK"
    # if the speed travelled is more than the speed limit, return the points
    elif current_speed > speed_limit:
        # if the points exceed 12, return "Time to go to jail"
        if demerit_points > 12:
            return "Time to go to jail!"
        return "Points: {}".format(demerit_points)


# run from main
if __name__ == "__main__":
    # get current speed
    speed = int(input("Enter your current speed: "))
    # get speed limit
    allowed_speed = int(input("Enter the speed limit: "))

    # calculate demerit points and print results
    points = calculate_demerit_points_for_speeding(speed, allowed_speed)
    print(points)
