import match
# average pairwise distance between two pucks
def average_dist(puck1, puck2):

    assert len(puck1.positions) == len(puck2.positions)

    sum_dist = 0

    for i in range(len(puck1.positions)):
        a = abs(puck1.positions[i][0] -
                puck2.positions[i][0])**2

        b = abs(puck1.positions[i][1] -
                puck2.positions[i][1])**2

        sum_dist += (a+b)**.5

    return sum_dist/len(puck1.positions)


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
