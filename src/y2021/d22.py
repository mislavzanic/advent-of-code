import itertools as it
import re
from collections import defaultdict,Counter


def get_volume(c):
    if c == None: return 0
    return (1+c[0][1] - c[0][0]) * (1+c[1][1] - c[1][0]) * (1+c[2][1] - c[2][0])


def get_intersection(cube1,cube2):
    if cube1 == None or cube2 == None: return None
    if cube1[0][1] <= cube2[0][0] or cube2[0][1] <= cube1[0][0]: return None
    if cube1[1][1] <= cube2[1][0] or cube2[1][1] <= cube1[1][0]: return None
    if cube1[2][1] <= cube2[2][0] or cube2[2][1] <= cube1[2][0]: return None
    sx,sy,sz = max(cube1[0][0],cube2[0][0]),max(cube1[1][0],cube2[1][0]),max(cube1[2][0],cube2[2][0])
    SX,SY,SZ = min(cube1[0][1],cube2[0][1]),min(cube1[1][1],cube2[1][1]),min(cube1[2][1],cube2[2][1])
    return ((sx,SX),(sy,SY),(sz,SZ))


def parse(l):
    cubes = []
    for step,line in enumerate(l):
        temp = line.split()
        m = re.match(r'x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', temp[1]).groups()
        mx,MX,my,MY,mz,MZ = map(int,(m[i] for i in range(0,6)))
        cubes.append((((mx,MX),(my,MY),(mz,MZ)), temp[0] == 'on'))
    return cubes


def calc(cubes):
    return get_volume(cubes[0][0]) - IEP([(get_intersection(cubes[0][0],x[0]),cubes[0][1]) for x in cubes[1:] if get_intersection(cubes[0][0],x[0])])


def IEP(cubes):
    return sum(
        calc(cubes[index:])
        for index,cube in enumerate(cubes)
        if cube[1]
    )


def main(l):
    cubes = parse(l)
    m,M = -50,50
    mcubes = [(get_intersection(x[0],((m,M),(m,M),(m,M))),x[1]) for x in cubes]
    return IEP(mcubes),IEP(cubes)
