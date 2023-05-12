from time import sleep, time

LINE_CLEAR = "\x1b[2K"

def ft_progress(it):
    start_time = time()
    last_time = start_time
    count_total = len(it)

    for elem in it:
        elapsed = time() - start_time

        print(f"| elapsed time {elapsed:.2f}s", end="\r")
        # print(end=LINE_CLEAR)
        yield elem

if __name__ == "__main__":
    listy = range(1000)
    ret = 0

    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
