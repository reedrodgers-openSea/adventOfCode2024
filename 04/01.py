if __name__ == "__main__":
    with open("test.txt", "r") as f:
        horizontal = []
        lines = f.readlines()
        for line in lines:
            horizontal.append(line)
        vertical = []
        for i in range(len(horizontal[0])):
            vertical.append([line[i] for line in horizontal])
        vertical = [[] for i in horizontal[0]] # empty list fo each character in the first horizontal line
        for line in horizontal:
            for 
        sum = 0
        for pair in numbers:
            sum += pair[0] * pair[1]
        print(sum)
