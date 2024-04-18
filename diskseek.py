requests = [11, 1, 36, 16, 34, 9, 12]
arm_pos = 11

def FCFS(requests, arm_pos):
    total = 0 
    for pos in requests:
        distance = abs(arm_pos - pos)
        print(f"{arm_pos} -> {pos}: {distance}")
        total += distance
        arm_pos = pos
    print(f"Total: {total} arm moves")




def SSTF(requests: list[int], arm_pos):
    total = 0 
    while len(requests) > 0:
        nearest = requests[0]
        for pos in requests[1:]:
            if abs(arm_pos - pos) < abs(arm_pos - nearest):
                nearest = pos

        distance = abs(arm_pos - nearest)
        print(f"{arm_pos} -> {nearest}: {distance}")
        total += distance
        arm_pos = nearest
        requests.remove(nearest)
    print(f"Total: {total} arm moves")

def elevator(requests: list[int], arm_pos):
    total = 0 
    dir = 1 # 1 is up, 0 is down
    while len(requests) > 0:
        if dir == 1:
            poss = list(filter(lambda x: x >= arm_pos, requests))
            if len(poss) > 0:
                poss.sort()
                nearest = poss[0]
                distance = abs(arm_pos - nearest)
                print(f"{arm_pos} -> {nearest}: {distance}")
                total += distance
                arm_pos = nearest
                requests.remove(nearest)
            else:
                dir = 0
        else:
            poss = list(filter(lambda x:x <= arm_pos, requests))
            if len(poss) > 0:
                poss.sort(reverse=True)
                nearest = poss[0]
                distance = abs(arm_pos - nearest)
                print(f"{arm_pos} -> {nearest}: {distance}")
                total += distance
                arm_pos = nearest
                requests.remove(nearest)

            else:
                dir = 1

    print(f"Total: {total} arm moves")

print("\nFCFS")
FCFS([x for x in requests], 11)

print("\nSSTF")
SSTF([x for x in requests], 11)

print("\nElevator")
elevator([x for x in requests], 11)
