def orientation(point1,point2,point3):
    ori=(point2[1]-point1[1])*(point3[0]-point1[0])-(point3[1]-point1[1])*(point2[0]-point1[0])
    if ori==0:
        return 0    #on the line
    elif ori>0:
        return 1    #right
    else:
        return -1   #left

def do_intersect(point1,point2,point3,point4):
    o1=orientation(point1,point2,point3)
    o2=orientation(point1,point2,point4)
    o3=orientation(point3,point4,point1)
    o4=orientation(point3,point4,point2)
    on_segment=lambda point1,point2,point3:min(point1[0],point2[0])<=point3[0]<=max(point1[0],point2[0]) and min(point1[1],point2[1])<=point3[1]<=max(point1[1],point2[1])
    if o1!=o2 and o3!=o4:
        return True
    if o1==0 and on_segment(point1,point2,point3):
        return True
    if o2==0 and on_segment(point1,point2,point4):
        return True
    if o3==0 and on_segment(point3,point4,point1):
        return True
    if o4==0 and on_segment(point3,point4,point2):
        return True
    return False
