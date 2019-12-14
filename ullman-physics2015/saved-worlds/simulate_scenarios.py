from scenarios import create_scenarios

# create scenarios for all  worlds
scenarios_list = create_scenarios('/Users/andreabolivar/Desktop/6.804/6.804_final/ullman-physics2015/saved-worlds')


# Summary statistics:
######### Average position along the x-axis
######### Total change along the x-axis
######### Average position along the y-axis
######### Total change along the y-axis
# Average pairwise distance between particles
# Total change in pairwise distance
# Velocity loss while on surfaces
# Rest time on surfaces
# Average velocity
# Pre- and post-collision velocity ratio
# Change in angle following collision

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
    for puck in pucks:
        print(puck.color)
        print("average  diff", puck.get_averg_pos())
        print("total change", puck.total_change())
        print('\n')

    break
