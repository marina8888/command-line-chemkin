import os


def main():
    for file in os.listdir("./solutions"):
        with open('./solutions/' + file, 'r') as fd:
            contents = fd.read()
            filtered = "".join(contents.split('FINAL SOLUTION:')[-1].splitlines(True)[2:])
        with open('./solutions/' + file, 'w') as fd:
            fd.write(filtered)


if __name__ == "__main__":
    main()
