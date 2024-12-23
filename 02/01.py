
def is_safe(report):
    increasing = None
    previous = None
    for num in report:
        if previous is None:
            previous = int(num)
            continue
        if increasing is None:
            increasing = int(num) > previous
        if int(num) > previous and not increasing:
            # print('unsafe', report, num, 'not increasing')
            return False
        if int(num) < previous and increasing:
            # print('unsafe', report, num, 'increasing')
            return False
        if abs(int(num) - previous) > 3:
            # print(int(num), previous)
            # print('unsafe', report, num, 'too big')
            return False
        if abs(int(num) - previous) < 1:
            # print('unsafe', report, num, 'too small')
            return False
        previous = int(num)
    return True


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        safeCount = 0
        for line in lines:
            report = line.split()
            if is_safe(report):
                print('safe', report)
                safeCount += 1
        print(safeCount)
