if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        diff = 0
        left = []
        right = []
        for line in lines:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
        left.sort()
        right.sort()
        for i in range(len(left)):
            diff += abs(left[i] - right[i])
        print(diff)


