def FIFO(page_requests, memory_size):
    print("\nRunning First Come First Served")

    # this is where the active pages are stored
    active_pages = []
    total_faults = 0

    # loop through for each request for a page
    for page in page_requests:
        print(f"Access to {page}: \t", end="")

        # if the page is already in memory, do nothing
        if page in active_pages:
            print(f"{active_pages} -> No page faults")

        else:
            # else we need to evict a process 
            # just choose the first one if we have used up all the memory
            if len(active_pages) == memory_size:
                active_pages.pop(0)

            # then add the new page to the end of the queue
            active_pages.append(page)

            # increase our total, then print out
            total_faults += 1
            print(f"{active_pages} -> Page fault")

    print(f"Page faults: {total_faults}")

def secondChance(page_requests, memory_size):
    print("\nRunning Second Chance")

    # this is where our active pages will be stored
    # stored as tuples (page_id, R(ecently used) bit, M(odified) bit)
    active_pages: list[tuple[int, int, int]] = []

    total_faults = 0

    # loop through each request for a page
    for i, page in enumerate(page_requests):
        print(f"Access to {page}: \t", end="")

        # if the page is in the active pages we need to updates its R bit
        if page in [x[0] for x in active_pages]:
            print(f"{active_pages} -> No page faults")

            # don't worry about this line, its a bit of python magic, it just updates the R and M bit to true. ( I assume that subsequent requests are write operations, but it doesn't really matter cos were not using it)
            active_pages = [x if x[0] != page else (page, 1, 1) for x in active_pages]

        else:
            # else we need to evict a page

            # if theres not enough room in memory, go down the queue until we find a page which hasn't got their R bit set
            # also set each page's R bit to 0 as we go
            # and go back to the start if we reach the end
            if len(active_pages) == memory_size:
                i = 0
                while (active_pages[i%memory_size][1] == 1):
                    # remove the first element if its R bit set to 1
                    old = active_pages.pop(0)
                    # add to the end of the queue with R bit unset
                    active_pages.append((old[0], 0, old[2]))

                # weve gone through the list and the one on the front of the queue has no R bit set, remove them
                active_pages.pop(0)

            # New page can be loaded now
            active_pages.append((page, 0, 0))

            # add to the total, then print out
            total_faults += 1
            print(f"{active_pages} -> Page fault")

    print(f"Page faults: {total_faults}")

def NRU(page_requests, memory_size):
    print("\nRunning Not Recently used")

    # this is where our active pages will be stored
    # stored as tuples (page_id, R(ecently used) bit, M(odified) bit)
    active_pages: list[tuple[int, int, int]] = []
    total_faults = 0

    for page in page_requests:
        print(f"Access to {page}: \t", end="")

        # split the pages up into their classes
        # this isn't exactly what i do in the code, takeing 2x the R bit + the M bit gives us the class, Sort by that and that gives us the ordering we should evict in
        active_pages.sort(key=lambda x: x[1] * 2 + x[2])

        # check if the process is in memory
        if page in [x[0] for x in active_pages]:

            # it is so just set its R bit to true
            print(f"{active_pages} -> No page faults")
            # don't worry about this line, its a bit of python magic, it just updates the R and M bit to true. ( I assume that subsequent requests are write operations)
            active_pages = [x if x[0] != page else (page, 1, 1) for x in active_pages]

        else:
            # we need to evict
            if len(active_pages) == memory_size:
                # we already sorted the list so just remove the first item
                active_pages.pop(0)

            # add the page to the active pages
            active_pages.append((page, 0, 0))

            # increase our total and print
            total_faults += 1
            print(f"{active_pages} -> Page fault")

    print(f"Page faults: {total_faults}")

FIFO([0, 1, 3, 2, 1, 4, 1, 5, 6, 7], 3)
secondChance([4, 5, 5, 5, 6, 7, 8, 6, 7, 8, 6, 7, 8, 4, 1, 5, 2, 4, 4, 1], 4)
NRU([1,1,2,2,3,1,4,3], 3)
