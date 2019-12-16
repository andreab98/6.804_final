from scenarios import create_scenarios
import physics

# create scenarios for all  worlds
scenarios_list = create_scenarios('/Users/andreabolivar/Desktop/6.804/6.804_final/ullman-physics2015/saved-worlds')

# Summary statistics:
#1####### Average position along the x-axis
#2####### Total change along the x-axis
#3####### Average position along the y-axis
#4####### Total change along the y-axis
#5####### Average pairwise distance between particles
#6####### Total change in pairwise distance
#7####### Velocity loss while on surfaces
#8####### Rest time on surfaces
#9####### Average velocity
#10###### Pre- and post-collision velocity ratio

# Change in angle following collision
        # ;; get angle theta between 2 2D particles
        # (define (compute-angle particle1 particle2)
        # (let* ((x1 (first particle1))
        #        (x2 (first particle2))
        #        (y1 (second particle1))
        #        (y2 (second particle2))
        #        (rx (- x2 x1))
        #        (ry (- y2 y1))
        #        (default (atan (/ ry rx))))
        #   (if (> rx 0)
        #       (atan (/ ry rx))
        #       (if (and (< rx 0) (>= ry 0))
        #           (+ (atan (/ ry rx)) pi)
        #           (if (and (< rx 0) (< ry 0))
        #               (- (atan (/ ry rx)) pi)
        #               (if (and (= rx 0) (> ry 0))
        #                   (/ pi 2)
        #                   (if (and (= rx 0) (< ry 0))
        #                       (/ pi -2)
        #                       0.0)))))))

def scenario_stats(s):
    stats = {}
    # print(s.name)
    observed_path = s.path
    pucks = s.pucks
    surfaces = s.surfaces

    collision_times = {}
    collision_velocities = {}
    pre_post_collision = {}

    # iterate through all paths to update scenario
    for path in observed_path:
        # iterate through positions for each path
        # print(path)
        positions = path[0]
        velocities = path[1]
        for i in range(len(positions)):
            # update new locations of pucks
            new_x, new_y = positions[i]
            new_vx, new_vy = velocities[i]
            pucks[i].update_pos(new_x, new_y)
            pucks[i].update_v(new_vx, new_vy)

            # Rest time on surfaces
            for puck in pucks:
                for surf in surfaces:
                    if (physics.collision(puck,surf) and len(puck.positions)>1):
                        if(puck.positions[-1] == puck.positions[-2]):
                            if (puck, surf) in collision_times:
                                collision_times[(puck.color, surf.color)] += 1
                                collision_velocities[(puck.color, surf.color)].append(puck.velocity)
                            else:
                                collision_times[(puck.color, surf.color)] = 0
                                collision_velocities[(puck.color, surf.color)] = [puck.velocity]


            for p1 in pucks:
                for p2 in pucks:
                    if (p1!=p2 and physics.collision(p1, p2) and
                        ((p1.color,p2.color) not in pre_post_collision) and
                        len(p2.velocities)>1 and len(p1.velocities)>1):

                        # print("Pre- and post-collision velocity ratio")
                        # print("p1 x: ", p1.velocities[-2][0]/p1.velocities[-1][0])
                        # print("p2 x: ", p2.velocities[-2][0]/p2.velocities[-1][0])
                        # print("p1 y: ", p1.velocities[-2][1]/p1.velocities[-1][1])
                        # print("p2 y: ", p2.velocities[-2][1]/p2.velocities[-1][1])
                        pre_post_collision[(p1.color,p2.color)] = [(p1.velocities[-2][0]/p1.velocities[-1][0],
                                                p1.velocities[-2][1]/p1.velocities[-1][1]),
                                                (p2.velocities[-2][0]/p2.velocities[-1][0],
                                                p2.velocities[-2][1]/p2.velocities[-1][1])]

    stats["pre_post"] = pre_post_collision

    stats["rest_time_surf"] = collision_times
    # print("Rest time on surfaces", collision_times)

    velocity_loss = {}
    # print("Velocity loss while on surfaces")
    for k in collision_velocities.keys():
        if k not in velocity_loss:
            velocity_loss[k] = (collision_velocities[k][-1][0] -
                            collision_velocities[k][0][0],
                            collision_velocities[k][-1][1] -
                            collision_velocities[k][0][1])
        # else:
        #     velocity_loss[k].append((collision_velocities[k][-1][0] -
        #                     collision_velocities[k][0][0],
        #                     collision_velocities[k][-1][1] -
        #                     collision_velocities[k][0][1]))
        # print("x ", collision_velocities[k][-1][0] - collision_velocities[k][0][0])
        # print("y ", collision_velocities[k][-1][1] - collision_velocities[k][0][1])

    stats["velocity_loss"] = velocity_loss

    # after all paths get stats on each puck
    stats["dist_average"] = physics.average_dist(pucks)
    # print("Average pairwise distance between particles", physics.average_dist(pucks))

    stats["total_change"] = physics.total_pairwise_dist(pucks)
    # print("Total change in pairwise distance", physics.total_pairwise_dist(pucks))
    # print('\n')

    av_position = {}
    av_velocity = {}
    total_change = {}
    for puck1 in pucks:
        # print(puck1.color)
        av_position[puck1.color] = puck1.get_average_pos()
        # print("average  diff", puck1.get_average_pos())

        total_change[puck1.color] = puck1.total_change()
        # print("total change", puck1.total_change())

        av_velocity[puck1.color] = puck1.get_average_v()
        # print("average velocity", puck1.get_average_v())

        # print('\n')

    stats["av_position"] = av_position
    stats["total_change_pucks"] = total_change
    stats["av_velocity"] = av_velocity

    return stats

scenario_stats(scenarios_list[0])
