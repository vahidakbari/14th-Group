
def gen2(txt):
    start = 0
    while start <= len(txt):
        yield txt[start:start+1]
        start += 2


if __name__ == "__main__":
    alphabetstring = "CDEFGHIJKLMNOPQRSTUVWX"
    for t in gen2(alphabetstring):
        print(t)
