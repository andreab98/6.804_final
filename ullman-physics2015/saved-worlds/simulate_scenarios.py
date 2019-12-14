from scenarios import create_scenarios

# create scenarios for all  worlds
scenarios_list = create_scenarios('/Users/andreabolivar/Desktop/6.804/6.804_final/ullman-physics2015/saved-worlds')

for s in scenarios_list:
    print(s.name)
    observed_path = s.path

    # iterate through all paths to update scenario
    for path in observed_path:
        # iterate through positions for each path
        for curr_positions in path:
            # update new locations of pucks
            x_locs = curr_positions[0]
            y_locs = curr_positions[1]

            pucks = s.pucks
            print(pucks[0].position)
            for i in range(len(pucks)):
                print("x",x_locs[i])
                print("x",y_locs[i])
                pucks[i].update_pos(x_locs[i],y_locs[i])
                break
            print(pucks[i].position)
            break
        break
    break
