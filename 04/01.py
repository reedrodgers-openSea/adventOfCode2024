if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        def fetchWords(i, j, length):
            n, ne, e, se, s, sw, w, nw = ["" for k in range(8)]
            for l in range(length):
                def safe_get_char(i, j, default=''):
                    if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
                        return lines[i][j]
                    return default
                
                n += safe_get_char(i + l, j)
                ne += safe_get_char(i + l, j + l)
                e += safe_get_char(i, j + l)
                se += safe_get_char(i - l, j + l)
                s += safe_get_char(i - l, j)
                sw += safe_get_char( i - l, j - l)
                w += safe_get_char(i, j - l)
                nw += safe_get_char(i + l, j - l)
            
            words = [n, ne, e, se, s, sw, w, nw]
            print(i, j, words)
            return [word for word in words if len(word) == length]

        xmasCount = 0
        for i, hLine in enumerate(lines):
            for j, c in enumerate(hLine):
                words = fetchWords(i, j, 4)
                for word in words:
                    if word == 'XMAS':
                        xmasCount += 1
        
        print(xmasCount)
