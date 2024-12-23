
def is_safe(report):
    increasing = None
    previous = None
    for i, num in enumerate(report):
        if previous is None:
            previous = int(num)
            continue
        if increasing is None:
            increasing = int(num) > previous
        if int(num) > previous and not increasing:
            # print('unsafe', report, num, 'not increasing')
            return {'safe': False, 'failure': i - 1}
        if int(num) < previous and increasing:
            # print('unsafe', report, num, 'increasing')
            return {'safe': False, 'failure': i - 1}
        if abs(int(num) - previous) > 3:
            # print(int(num), previous)
            # print('unsafe', report, num, 'too big')
            return {'safe': False, 'failure': i - 1}
        if abs(int(num) - previous) < 1:
            # print('unsafe', report, num, 'too small')
            return {'safe': False, 'failure': i - 1}
        previous = int(num)
    return {'safe': True, 'failure': None}


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        lines = f.readlines()
        safeCount = 0
        for line in lines:
            report = line.split()
            result = is_safe(report)
            if result['safe']:
                safeCount += 1
            else:
                print('1st try ', report)
                next_list = list(report)
                del next_list[result['failure']]
                next_result = is_safe(next_list)
                if next_result['safe']:
                    safeCount += 1
                else:
                    print('2nd try', next_list)
                    final_list = list(report)
                    del final_list[result['failure'] + 1]
                    final_result = is_safe(final_list)
                    if final_result['safe']:
                        safeCount += 1
                    else:
                        print("final try", final_list)
        print(safeCount)
