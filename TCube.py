# TCube
# build a d0*d1*d2 cuboid with (d0*d1*d2/4) T pieces
#   ________
# /________/|
# |__    __|/
#    |__|/

# ULi161013...

d0,d1,d2 = 6,6,6

def pl(i, cs):
    global n
    if all(0<=x<d0 and 0<=y<d1 and 0<=z<d2 and not m[x][y][z] for x,y,z in cs):
        n+=1
        for x,y,z in cs:
            m[x][y][z] = n
        foo(i+1)
        for x,y,z in cs:
            m[x][y][z] = 0
        n-=1

def foo(i):
    global s
    if i==d012:
        s+=1
        print('{0}:'.format(s))
        print('\n'.join('   '.join(' '.join('{0:02}'.format(e2)
            for e2 in e1) for e1 in e0) for e0 in m))
    else:
        x,y,z =i%d0,i//d0%d1,i//d01%d2
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

d01 = d0*d1
d012 = d01*d2
m = [[[0 for z in range(d2)] for y in range(d1)] for x in range(d0)]
n = s = 0
foo(0)
