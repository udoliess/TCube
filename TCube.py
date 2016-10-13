# TCube
# build a 6*6*6 cube with 54 T pieces
#   ________
# /________/|
# |__    __|/
#    |__|/

# ULi161013

def pl(i, cs):
    global n
    if all((all(0<=d<6 for d in c) and not m[c[0]][c[1]][c[2]]) for c in cs):
        n+=1
        for x,y,z in cs:
            m[x][y][z] = n
        foo(i+1)
        for x,y,z in cs:
            m[x][y][z] = 0
        n-=1

def foo(i):
    global s
    if i==216:
        s+=1
        print('{0}:'.format(s))
        print('\n'.join('  '.join(' '.join('{0:02}'.format(e2)
            for e2 in e1) for e1 in e0) for e0 in m))
    else:
        x,y,z =i%6,i//6%6,i//36%6
        if not m[x][y][z]:
            # naming of piece orientation at the end of each source line:
            # 1st letter = direction of 3 cubes line
            # sign and 2nd letter = direction of 4th cube
            pl(i, ((x,y,z), (x+1,y,z), (x+2,y,z), (x+1,y+1,z))) # x+y
            pl(i, ((x,y,z), (x+1,y,z), (x+2,y,z), (x+1,y,z+1))) # x+z
            pl(i, ((x,y,z), (x-1,y+1,z), (x,y+1,z), (x+1,y+1,z))) # x-y
            pl(i, ((x,y,z), (x-1,y,z+1), (x,y,z+1), (x+1,y,z+1))) # x-z
            pl(i, ((x,y,z), (x,y+1,z), (x,y+2,z), (x+1,y+1,z))) # y+x
            pl(i, ((x,y,z), (x,y+1,z), (x,y+2,z), (x,y+1,z+1))) # y+z
            pl(i, ((x,y,z), (x,y+1,z), (x,y+2,z), (x-1,y+1,z))) # y-x
            pl(i, ((x,y,z), (x,y-1,z+1), (x,y,z+1), (x,y+1,z+1))) # y-z
            pl(i, ((x,y,z), (x,y,z+1), (x,y,z+2), (x+1,y,z+1))) # z+x
            pl(i, ((x,y,z), (x,y,z+1), (x,y,z+2), (x,y+1,z+1))) # z+y
            pl(i, ((x,y,z), (x,y,z+1), (x,y,z+2), (x-1,y,z+1))) # z-x
            pl(i, ((x,y,z), (x,y,z+1), (x,y,z+2), (x,y-1,z+1))) # z-y
        else:
            foo(i+1)

m = [[[0 for x in range(6)] for x in range(6)] for x in range(6)]
n = s = 0
foo(0)
