def FIFO(page_requests, memory_size):
    print("\nRunning First Come First Served")
    active_pages = []
    total_faults = 0

    for page in page_requests:
        print(f"Access to {page}: \t", end="")

        if page in active_pages:
            print(f"{active_pages} -> No page faults")

        else:
            if len(active_pages) == memory_size:
                active_pages.pop(0)

            active_pages.append(page)
            total_faults += 1
            print(f"{active_pages} -> Page fault")

def secondChance(page_requests, memory_size):
    print("\nRunning Second Chance")
    active_pages: list[tuple[int, int, int]] = []
    total_faults = 0

    # stored as tuples (page_id, R bit, M bit)

    for i, page in enumerate(page_requests):
        print(f"Access to {page}: \t", end="")

        if page in [x[0] for x in active_pages]:
            print(f"{active_pages} -> No page faults")
            active_pages = [x if x[0] != page else (page, 1, 1) for x in active_pages]

        else:
            if len(active_pages) == memory_size:

                i = 0
                while (active_pages[i%memory_size][1] == 1):
                    old = active_pages.pop(0)
                    active_pages.append((old[0], 0, old[2]))
                active_pages.pop(0)


            active_pages.append((page, 0, 0))
            total_faults += 1
            print(f"{active_pages} -> Page fault")

def NRU(page_requests, memory_size):
    print("\nRunning Not Recently used")
    active_pages = []
    total_faults = 0

    # stored as tuples (page_id, R bit, M bit)

    for i, page in enumerate(page_requests):
        print(f"Access to {page}: \t", end="")
        active_pages.sort(key=lambda x: x[1] * 2 + x[2])

        if page in [x[0] for x in active_pages]:
            print(f"{active_pages} -> No page faults")
            active_pages = [x if x[0] != page else (page, 1, 1) for x in active_pages]

        else:
            if len(active_pages) == memory_size:
                active_pages.pop(0)

            active_pages.append((page, 0, 0))
            total_faults += 1
            print(f"{active_pages} -> Page fault")

FIFO([0, 1, 3, 2, 1, 4, 1, 5, 6, 7], 3)
secondChance([4, 5, 5, 5, 6, 7, 8, 6, 7, 8, 6, 7, 8, 4, 1, 5, 2, 4, 4, 1], 4)
NRU([1,1,2,2,3,1,4,3], 3)
