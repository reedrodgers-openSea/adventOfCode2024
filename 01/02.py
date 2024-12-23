if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        similarity = 0
        left = []
        right = []
        for line in lines:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
        left.sort()
        right.sort()
        for i in range(len(left)):
            id = left[i]
            for j in range(len(right)):
                if right[j] == id:
                    similarity += right[j]
        print(similarity)


