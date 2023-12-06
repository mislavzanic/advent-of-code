from collections import Counter

def main(day):
    ids = 0
    power = 0
    for j,line in enumerate(day.lines()):
        s = line.split(" ")
        game = Counter()
        for i,item in enumerate(s):
            if not item.isnumeric(): continue
            color = s[i+1]
            if color[-1] == ';' or color[-1] == ',':
                color = color[:-1]
            game[color] = max(int(s[i]), game[color])
        if game['red'] <= 12 and game['blue'] <= 14 and game['green'] <= 13:
            ids += j+1
        power += game['red'] * game['green'] * game['blue']



    print(ids, power)
