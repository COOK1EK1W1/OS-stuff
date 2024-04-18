def FCFS(requests, arm_pos):
    print("\nRunning First Come First Served")

    total = 0 
    # loop through each request to the disk
    for pos in requests:

        # find the distance the arm has to move
        distance = abs(arm_pos - pos)

        # move the arm
        arm_pos = pos

        # add the distance to the total and print
        total += distance
        print(f"{arm_pos} -> {pos}: {distance}")

    print(f"Total: {total} arm moves")


def SSTF(requests: list[int], arm_pos):
    print("\nRunning Sortest Seek Time First")

    total = 0 

    # loop until there are no more requests
    while len(requests) > 0:

        # start a linear search to find the nearest request to the arm
        nearest = requests[0]
        for pos in requests[1:]:
            if abs(arm_pos - pos) < abs(arm_pos - nearest):
                nearest = pos

        # calculate the distance from the arm to the request
        distance = abs(arm_pos - nearest)

        # move the arm
        arm_pos = nearest

        # add the distance to the total and print
        total += distance
        print(f"{arm_pos} -> {nearest}: {distance}")

        # remember to remove the request from the list
        requests.remove(nearest)
    print(f"Total: {total} arm moves")

def elevator(requests: list[int], arm_pos):
    print("\nRunning Elevator")

    total = 0 
    # the direction the arm or "elevator" is moving (1 is up, 0 is down)
    dir = 1

    # loop over all the requests
    while len(requests) > 0:

        # if we're moving upwards
        if dir == 1:

            # find all the requests which are greater than the current arm position
            poss = list(filter(lambda x: x >= arm_pos, requests))

            if len(poss) > 0:
                # if there are requests above the arm then sort them from lowest to highest, the first item will be the nearest
                poss.sort()
                nearest = poss[0]

                # calculate the distance from the arm to the request
                distance = abs(arm_pos - nearest)

                # move the arm to the position
                arm_pos = nearest

                # update the total and print out
                total += distance
                print(f"{arm_pos} -> {nearest}: {distance}")

                # remeber to remove the request 
                requests.remove(nearest)
            else:
                # no requests in the upward direction, start going down
                dir = 0
        else:

            # find all the requests which are less than the current arm position
            poss = list(filter(lambda x:x <= arm_pos, requests))

            if len(poss) > 0:
                # if there are requests below the arm then sort them from highest to lowest, the first item will be the nearest
                poss.sort(reverse=True)
                nearest = poss[0]

                # caluclate the distance from the arm to the position
                distance = abs(arm_pos - nearest)

                # move the arm there
                arm_pos = nearest

                # increase our movement total and print out
                total += distance
                print(f"{arm_pos} -> {nearest}: {distance}")

                # remember to remove the request from the list
                requests.remove(nearest)

            else:
                dir = 1

    print(f"Total: {total} arm moves")


if __name__ == "__main__":

    # generic points from the slides
    requests = [11, 1, 36, 16, 34, 9, 12]

    # run all the algorithms
    # note: we also make copies of all the lists in place to avoid passing by reference
    FCFS(requests.copy(), 11)
    SSTF(requests.copy(), 11)
    elevator(requests.copy(), 11)
