from functools import reduce
import itertools as it
import re
from collections import defaultdict, Counter

def parseLiteral(packet, j):
    num = []
    for i in range(j,len(packet), 5):
        index = packet[i]
        num.append(packet[i+1:i+5])
        if index == '0':
            j = i + 5
            break
    return j,int('0b' + ''.join(num), 2)

def parse(packet,s,j):
    newj = j
    length = {'0':15,'1':11}
    version = int(packet[j:j+3],2)
    trID = int(packet[j+3:j+6],2)
    s += version
    num = 0
    if trID == 4:
        newj,num = parseLiteral(packet, j+6)
    else:
        nums = []
        l = packet[j+6]
        newj = j+7+length[l]
        if l == '0':
            numofbits = int(packet[j+7:newj],2)
            j = newj
            while numofbits + j > newj:
                s,newj,num= parse(packet, s, newj)
                nums.append(num)
        else:
            numofpackets = int(packet[j+7:newj],2)
            while numofpackets:
                s,newj,num= parse(packet, s, newj)
                numofpackets -= 1
                nums.append(num)
        if trID == 0: num = sum(nums)
        elif trID == 1: num = reduce(lambda acc,x: acc * x, nums)
        elif trID == 2: num = min(nums)
        elif trID == 3: num = max(nums)
        elif trID == 5: num = nums[0] > nums[1]
        elif trID == 6: num = nums[0] < nums[1]
        elif trID == 7: num = nums[0] == nums[1]
    return s, newj, num


def main(l):
    l = l[0]
    j = 0
    binrep = bin(int(l,16))[2:]
    while len(binrep) % 8 != 0:
        binrep = '0' + binrep
    s,_,res = parse(binrep,0,0)
    return s,res
