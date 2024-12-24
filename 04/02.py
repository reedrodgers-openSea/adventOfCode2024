if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        def checkWord(i, j, length):
            ne = ''
            se = ''
            for l in range(-1, length - 1):
                def safe_get_char(i, j, default=''):
                    if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
                        return lines[i][j]
                    return default
                
                ne += safe_get_char(i + l, j + l)
                se += safe_get_char(i - l, j + l)
            
            # words = [ne, se]
            print(i, j, ne, se)
            acceptable = ['MAS', 'SAM']
            return ne in acceptable and se in acceptable

        xmasCount = 0
        for i, hLine in enumerate(lines):
            for j, c in enumerate(hLine):
                if checkWord(i, j, 3):
                    xmasCount += 1
        
        print(xmasCount)
