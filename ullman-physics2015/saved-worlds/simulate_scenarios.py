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
# Velocity loss while on surfaces
# Rest time on surfaces
# Average velocity
# Pre- and post-collision velocity ratio

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
    # print(len(pucks))

    # iterate through all paths to update scenario
    for path in observed_path:
        # iterate through positions for each path
        # print(path)
        positions = path[0]
        velocities = path[1]
        for i in range(len(positions)):
            # update new locations of pucks
            new_x, new_y = positions[i]
            pucks[i].update_pos(new_x, new_y)
            # for p in pucks:
            #     for surf in surfaces:
            #         if (physics.collision(p,surf)):
            #                         print("FOUNDDDDD")

    # after all paths get stats on each puck
    print("Average pairwise distance between particles", physics.average_dist(pucks))
    print("Total change in pairwise distance", physics.total_pairwise_dist(pucks))
    for puck1 in pucks:
        print(puck1.color)
        print("average  diff", puck1.get_averg_pos())
        print("total change", puck1.total_change())
        # Average pairwise distance between particles
        print('\n')
