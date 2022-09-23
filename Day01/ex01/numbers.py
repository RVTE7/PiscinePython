if __name__ == "__main__":
    with open("numbers.txt", "r") as f:
        x = f.read()
        y = x.split(",")
        for z in range(len(y)):
            print(y[z].rstrip())