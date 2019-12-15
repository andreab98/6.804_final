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
# Total change in pairwise distance
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
    print(s.name)
    observed_path = s.path
    pucks = s.pucks
    print(len(pucks))

    # iterate through all paths to update scenario
    for path in observed_path:
        # iterate through positions for each path
        for curr_positions in path:
            # update new locations of pucks
            for i in range(len(pucks)):
                # print(curr_positions[i][1])
                pucks[i].update_pos(curr_positions[i][0],
                                    curr_positions[i][1])

    # after all paths get stats on each puck
    for puck1 in pucks:
        print(puck1.color)
        print("average  diff", puck1.get_averg_pos())
        print("total change", puck1.total_change())
        print('\n')

        # Average pairwise distance between particles
        for puck2 in pucks:
            print(puck1.color, puck2.color)
            print(physics.average_dist(puck1, puck2))
            print('\n')

    break