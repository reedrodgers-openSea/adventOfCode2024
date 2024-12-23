from pprint import pprint

def parse_dos(line: str) -> list[str]:
    chunks = line.split('do()')
    dos = []
    for chunk in chunks:
        result = chunk.split("don't()")
        dos.append(result[0])
    pprint(line.split("don't"))
    print('\n')
    pprint(dos)
    print('\n')
    print('\n')
    print('\n')

    return dos

def parse(line):
    chunks = line.split('mul(')
    pairs = []
    for chunk in chunks:
        nums = chunk.split(')')[0].split(',')
        if len(nums) != 2:
            continue
        num1 = None
        num2 = None
        try:
            num1 = int(nums[0])
            num2 = int(nums[1])
        except(ValueError):
            # print(nums, num1, num2)
            continue
        pairs.append((num1, num2))
    return pairs

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        numbers = []
        for line in lines:
            dos = parse_dos(line)
            numbers = numbers + parse(str.join("", dos))
        sum = 0
        for pair in numbers:
            sum += pair[0] * pair[1]
        print(sum)
