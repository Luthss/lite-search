import sys

filename = ""

def main():
    if len(sys.argv) == 1:
        print("Please give the filename as an argument")
        return 0

    for count, item in enumerate(sys.argv):
        if count == 0:
            continue
        if count == 1:
            filename = item

    myfile = open(filename)

    for lines in myfile:
        print(lines, end="")

if __name__ == "__main__":
    main()

# cat clone ^