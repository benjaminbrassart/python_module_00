from time import sleep, time
from math import floor

LINE_CLEAR = "\x1b[2K"

def ft_progress(it):
    start_time = time()
    last_time = start_time
    count_current = 0
    count_total = len(it)

    for elem in it:
        count_current += 1
        ratio = count_current / count_total
        percentage = round(ratio * 100)
        elapsed = time() - start_time

        arrow_len = floor(25 * ratio)
        if ratio == 1:
            arrow_len -= 1
        arrow = (("=" * arrow_len) + ">").ljust(25, " ")

        print(f" [{percentage:3d}%] [{arrow}] {count_current}/{count_total} | elapsed time {elapsed:.2f}s", end="\r")
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
