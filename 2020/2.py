l = [x.strip() for x in open('input').readlines()]
p1, p2 = 0, 0
for x in l:
    nums, letter, string = x.split()
    num1, num2 = map(int, nums.split('-'))
    letter = letter[0]

    p1 += num1 <= string.count(letter) <= num2
    p2 += (string[num1 - 1]==letter)+(string[num2-1]==letter)==1

print(p1, p2)

    
