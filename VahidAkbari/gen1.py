

def gen1(start, stop, step):
    while start < stop:
        yield start
        start += step


if __name__ == "__main__":
    for i in gen1(2.3,3.78,0.01):
        print(i)
