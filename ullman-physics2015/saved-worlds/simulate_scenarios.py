from scenarios import create_scenarios
import physics

# create scenarios for all  worlds
scenarios_list = create_scenarios('/Users/andreabolivar/Desktop/6.804/6.804_final/ullman-physics2015/saved-worlds')

# Summary statistics:
######### Average position along the x-axis
######### Total change along the x-axis
######### Average position along the y-axis
######### Total change along the y-axis
######### Average pairwise distance between particles
######### Total change in pairwise distance
######### Velocity loss while on surfaces
######### Rest time on surfaces
######### Average velocity
######### Pre- and post-collision velocity ratio

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


for s in scenarios_list:
    # print(s.name)
    observed_path = s.path
    pucks = s.pucks
    surfaces = s.surfaces

    collision_times = {}
    collision_velocities = {}

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
            for p1 in pucks:
                for p2 in pucks:
                    if p1!=p2 and physics.collision(p1, p2):
                        print("Pre- and post-collision velocity ratio")
                        print("p1 x: ", p1.velocities[-2][0]/p1.velocities[-1][0])
                        print("p2 x: ", p2.velocities[-2][0]/p2.velocities[-1][0])
                        print("p1 y: ", p1.velocities[-2][1]/p1.velocities[-1][1])
                        print("p2 y: ", p2.velocities[-2][1]/p2.velocities[-1][1])
                        print('\n')

            # Rest time on surfaces
            for puck in pucks:
                for surf in surfaces:
                    if (physics.collision(puck,surf) and len(puck.positions)>1):
                        if(puck.positions[-1] == puck.positions[-2]):
                            if (puck, surf) in collision_times:
                                collision_times[(puck, surf)] += 1
                                collision_velocities[(puck, surf)].append(puck.velocity)
                            else:
                                collision_times[(puck, surf)] = 0
                                collision_velocities[(puck, surf)] = [puck.velocity]

    print("Rest time on surfaces", collision_times)

    print("Velocity loss while on surfaces")
    for k in collision_velocities.keys():
        print("x ", collision_velocities[k][-1][0] - collision_velocities[k][0][0])
        print("y ", collision_velocities[k][-1][1] - collision_velocities[k][0][1])



    # after all paths get stats on each puck
    print("Average pairwise distance between particles", physics.average_dist(pucks))
    print("Total change in pairwise distance", physics.total_pairwise_dist(pucks))
    print('\n')
    for puck1 in pucks:
        print(puck1.color)
        print("average  diff", puck1.get_average_pos())
        print("total change", puck1.total_change())
        print("average velocity", puck1.get_average_v())
        # Average pairwise distance between particles
        print('\n')
