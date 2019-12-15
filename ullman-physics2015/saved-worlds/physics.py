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

# def collision(obj1, obj2):
#     # check for puck to puck collision
#     if type(obj1) == struct.puck and type(obj2) == struct.puck:
#         obj.
#     # check for puck to puck and surface collision
#     if type(obj1) == struct.puck and type(obj2) == struct.surface:
#         as
#     if type(obj2) == struct.puck and type(obj1) == struct.surface:
#
#     return

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
