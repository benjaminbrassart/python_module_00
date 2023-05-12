from time import sleep

def ft_progress(it):
    for elem in it:
        yield elem

if __name__ == "__main__":
    listy = range(1000)
    ret = 0

    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
