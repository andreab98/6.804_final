import math
import data_structures as struct

# average pairwise distance between two pucks
def average_dist(pucks):
    average = 0
    for i in range(len(pucks[0].positions)):
        sum_average = 0
        for p1 in pucks:
            for p2 in pucks:
                if p1 != p2:
                    a = (p1.positions[i][0] -
                            p2.positions[i][0])**2
                    b = (p1.positions[i][1] -
                            p2.positions[i][1])**2

                    sum_average += (a+b)**.5
        average += sum_average/6

    return average/len(pucks[0].positions)

# Total change in pairwise distance
def total_pairwise_dist(pucks):
    sum_average = 0
    for p1 in pucks:
        for p2 in pucks:
            if p1!=p2:
                a = abs(p1.positions[-1][0] -
                        p2.positions[-1][0])**2
                b = abs(p1.positions[-1][1] -
                        p2.positions[-1][1])**2
                sum_average += (a+b)**.5

    return sum_average/6

def collision(obj1, obj2):
    # check for puck to puck collision
    if type(obj1) == struct.Puck and type(obj2) == struct.Puck:
        dist  = ((obj1.position[0]-obj2.position[0])**2+
                    (obj1.position[1]-obj2.position[1])**2)**.5
        return dist < (obj1.size+obj2.size)

    # check for puck to puck and surface collision
    if type(obj1) == struct.Puck and type(obj2) == struct.Surface:
        print(obj1.position)
        print(obj2.upperleft)
        print(obj2.lowerright)
        ul_x, ul_y = obj2.upperleft
        lr_x, lr_y = obj2.lowerright

        x, y = obj1.position

        return (((x+obj1.size)>ul_x) or
            ((x-obj1.size)<lr_x) or
            ((y+obj1.size)>lr_y) or
            ((y-obj1.size)<ul_y))

    if type(obj2) == struct.Puck and type(obj1) == struct.Surface:
        ul_x, ul_y = obj1.upperleft
        lr_x, lr_y = obj1.lowerright

        x, y = obj2.position

        return (((x+obj2.size)>ul_x) or
            ((x-obj2.size)<lr_x) or
            ((y+obj2.size)>lr_y) or
            ((y-obj2.size)<ul_y))

    return False

#######HELP WITH THIS FUNCTION########
# def compute_angle(puck1, puck2, time_index):
#         x1, y1 = puck1.positions[time_index]
#         x2, y2 = puck1.positions[time_index]
#         rx = x2-x1
#         ry = y2-y2
#
#         if rx > 0:
#             math.atan2(ry, rx)
#             if rx < 0 and ry>=0:
#                 math.atan2(ry, rx) + math.pi
#                 if rx<0 and ry>0:
#                     math.atan2(ry, rx) - math.pi
#                     if rx == 0 and ry>0:
#                         pi/2
#                         if rx==0 and ry>0:
#                             pi/(-2)
#         return math.atan2(ry, rx)
