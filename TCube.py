# TCube
# ULi161013

def pl(qs):
    global c
    global i
    global s
    if all((all(0<=d<6 for d in q) and not m[q[0]][q[1]][q[2]]) for q in qs):
        c+=1
        for x, y, z in qs:
            m[x][y][z] = c
        if c == 54:
            print(m)
            s+=1
        else:
            i+=1
            foo()
            i-=1
        for x, y, z in qs:
            m[x][y][z] = 0
        c-=1

def foo():
    global i
    x,y,z = xyz[i]
    if not m[x][y][z]:
        # naming of positioning variants at the end of each line:
        # 1st letter = direction of 3 cuboids
        # sign and 2nd letter = direction of 4th cuboid
        pl(((x,y,z), (x+1,y,z), (x+2,y,z), (x+1,y+1,z))) # x+y
        pl(((x,y,z), (x+1,y,z), (x+2,y,z), (x+1,y,z+1))) # x+z
        pl(((x,y,z), (x-1,y+1,z), (x,y+1,z), (x+1,y+1,z))) # x-y
        pl(((x,y,z), (x-1,y,z+1), (x,y,z+1), (x+1,y,z+1))) # x-z
        pl(((x,y,z), (x,y+1,z), (x,y+2,z), (x+1,y+1,z))) # y+x
        pl(((x,y,z), (x,y+1,z), (x,y+2,z), (x,y+1,z+1))) # y+z
        pl(((x,y,z), (x,y+1,z), (x,y+2,z), (x-1,y+1,z))) # y-x
        pl(((x,y,z), (x,y-1,z+1), (x,y,z+1), (x,y+1,z+1))) # y-z
        pl(((x,y,z), (x,y,z+1), (x,y,z+2), (x+1,y,z+1))) # z+x
        pl(((x,y,z), (x,y,z+1), (x,y,z+2), (x,y+1,z+1))) # z+y
        pl(((x,y,z), (x,y,z+1), (x,y,z+2), (x-1,y,z+1))) # z-x
        pl(((x,y,z), (x,y,z+1), (x,y,z+2), (x,y-1,z+1))) # z-y
    else:
        i+=1
        foo()
        i-=1

m = [[[0 for x in range(6)] for x in range(6)] for x in range(6)]
c = 0
i = 0
s = 0
xyz = list()
for z in range(6):
    for y in range(6):
        for x in range(6):
            xyz.append((x,y,z))
foo()
print(s)
