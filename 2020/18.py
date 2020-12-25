
import re
import fileinput
import sys

def findB(exp, i):
    par = 1
    i += 1
    while par != 0:
        if exp[i] == '(': par += 1
        elif exp[i] == ')': par -= 1
        i+=1
    return i-1

def arOp(num1, num2, op):
    return num1*num2 if op == '*' else num1+num2

def p1(exp, start, end):
    num = int(exp[start])
    op = None
    start += 1
    while start != end:
        if exp[start] == '+': op = '+'
        elif exp[start] == '*': op = '*'
        else: num = arOp(num, int(exp[start]), op)
        start += 1
    return num

def p2(exp, start, end):
    print(exp)
    num = int(exp[start])
    op = None
    start += 1
    while start < end:
        if exp[start] == '+': op = '+'
        elif exp[start] == '*': op = '*'
        else: 
            if op == '+':
                num = arOp(num,int(exp[start]),op)
            else:
                if start+1 == end or exp[start+1] == '*':
                    num = arOp(num,int(exp[start]),op)
                else:
                    temp = int(exp[start]) + int(exp[start+2])
                    while start+3 < end and exp[start+3] != '*':
                        temp += int(exp[start+4])
                        start += 2
                    num = arOp(num,temp,op)
                    start += 3
        start += 1
    print(num)
    return num

def removeParentheses(exp,start,end,part2):
    i = start
    num1 = 0
    newExp = []
    while True:
        if not i < len(exp): 
            if part2:
                return p2(newExp, 0, len(newExp))
            return p1(newExp, 0, len(newExp))
        if exp[i] == '(':
            k = findB(exp,i)
            temp = removeParentheses(exp[i+1:k],0,k-i-1,part2)
            newExp.append(str(temp))
            i = k+1
        elif exp[i] == ')': 
            i+=1
        else: 
            newExp.append(exp[i])
            i+=1
        
s1, s2 = 0, 0
lines = [x for x in list(fileinput.input())]
for line in lines:
    line = line.strip()
    exp = []
    for c in line:
        if c != ' ':
            exp.append(c)
    s1 += removeParentheses(exp, 0, len(exp),False)
    s2 += removeParentheses(exp, 0, len(exp),True)
        
print(s1, s2) 

