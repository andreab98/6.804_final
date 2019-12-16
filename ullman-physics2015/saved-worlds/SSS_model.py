import scenarios as scen
from simulate_scenarios import scenario_stats
import data_structures as  struct

###############
# Input: test_s: test scenario
#       scenario_ids: ids of the known scenarios
###############
def sss_model(test_s, scenario_ids):
    poss_worlds = {}
    diff = {}
    #searches for 1 scenario from each world
    for s in scen.scenarios:
        if (int(s.name.split('_')[-1]) in scenario_ids and
            test_s.name != s.name):
            poss_worlds[s.name] = scenario_stats(s)

    # test summary stats
    test_stats = scenario_stats(test_s)

    worlds = list(poss_worlds.keys())
    # check each summary statistics for  each world
    w_guess = [0 for i in range(len(worlds))]

    dist_average = (10000000,None)
    total_change = (10000000,None)
    for i in range(len(worlds)):
        diff = test_stats["dist_average"] - poss_worlds[worlds[i]]['dist_average']
        if abs(diff)<dist_average[0]:
            dist_average = (abs(diff), i)

        diff = test_stats["total_change"] - poss_worlds[worlds[i]]['total_change']
        if abs(diff)<total_change[0]:
            total_change = (abs(diff), i)
    if dist_average[1]:
        w_guess[dist_average[1]]+=1
    if total_change[1]:
        w_guess[total_change[1]]+=1

    for color in ['yellow','blue','red']:
        min_vel = (100000,None)
        min_pos = (100000,None)
        min_t = (100000,None)

        for i in range(len(worlds)):
            if (color in test_stats['av_velocity'] and
                color in poss_worlds[worlds[i]]['av_velocity']):
                diff_x = (test_stats["av_velocity"][color][0] -
                    poss_worlds[worlds[i]]['av_velocity'][color][0])
                diff_y = (test_stats["av_velocity"][color][1] -
                    poss_worlds[worlds[i]]['av_velocity'][color][1])

                if (abs(diff_x)+abs(diff_y))<min_vel[0]:
                    min_vel = (abs(diff_x)+abs(diff_y),i)

            if (color in test_stats['av_position'] and
                color in poss_worlds[worlds[i]]['av_position']):
                diff_x = (test_stats["av_position"][color][0] -
                    poss_worlds[worlds[i]]['av_position'][color][0])
                diff_y = (test_stats["av_position"][color][1] -
                    poss_worlds[worlds[i]]['av_position'][color][1])

                if (abs(diff_x)+abs(diff_y))<min_pos[0]:
                    min_pos = (abs(diff_x)+abs(diff_y),i)

            if (color in test_stats['total_change_pucks'] and
                color in poss_worlds[worlds[i]]['total_change_pucks']):
                diff_x = (test_stats["total_change_pucks"][color][0] -
                    poss_worlds[worlds[i]]['total_change_pucks'][color][0])
                diff_y = (test_stats["total_change_pucks"][color][1] -
                    poss_worlds[worlds[i]]['total_change_pucks'][color][1])

                if (abs(diff_x)+abs(diff_y))<min_t[0]:
                    min_t = (abs(diff_x)+abs(diff_y),i)

        if min_t[1]:
            w_guess[min_t[1]] += 1
        if min_vel[1]:
            w_guess[min_vel[1]] += 1
        if min_pos[1]:
            w_guess[min_pos[1]] += 1

        print(color)
        print(w_guess)

        for color2 in ['yellow','blue','red']:
            if ((color,color2) in test_stats["total_change_pucks"] and
                (color,color2) in poss_worlds[worlds[i]]["total_change_pucks"]):
                min_t = (10000000000, None)
                for i in range(len(worlds)):
                    p1_test = test_stats["total_change_pucks"][(color,color2)][0]
                    p2_test = test_stats["total_change_pucks"][(color,color2)][1]
                    p1_actual = poss_worlds[worlds[i]]["total_change_pucks"][(color,color2)][0]
                    p2_actual = poss_worlds[worlds[i]]["total_change_pucks"][(color,color2)][1]
                    p1_x_diff = abs(p1_test[0] - p1_actual[0])
                    p1_y_diff = abs(p1_test[1] - p1_actual[1])
                    p2_x_diff = abs(p2_test[0] - p2_actual[0])
                    p2_y_diff = abs(p2_test[1] - p2_actual[1])
                    if -1e9<=(p1_x_diff+p1_y_diff+p2_x_diff+p2_y_diff)<min_t[0]:
                        min_t = (p1_x_diff+p1_y_diff+p2_x_diff+p2_y_diff,i)
                if min_t[1]:
                    w_guess[min_t[1]]+=1

        for surf in ['brown', 'darkmagenta', 'yellowgreen']:
            min_t = (10000000000, None)
            min_v = (10000000000, None)

            for i in range(len(worlds)):
                if ((color, surf) in test_stats["rest_time_surf"] and
                    (color, surf) in poss_worlds[worlds[i]]["rest_time_surf"]):
                    test = test_stats["rest_time_surf"][(color,surf)]
                    actual = poss_worlds[worlds[i]]["rest_time_surf"][(color,surf)]
                    if abs(test-actual)<min_t[0]:
                        min_t = (abs(test-actual),i)

                if ((color, surf) in test_stats["velocity_loss"] and
                    (color, surf) in poss_worlds[worlds[i]]["velocity_loss"]):
                    test = test_stats["velocity_loss"][(color,surf)]
                    actual= poss_worlds[worlds[i]]["velocity_loss"][(color,surf)]
                    diff_x = test[0] - actual[0]
                    diff_y = test[1] - actual[1]
                    if -1e9<=(abs(diff_x)+abs(diff_y))<min_v[0]:
                        min_v = (abs(diff_x)+abs(diff_y),i)

            if min_t[1]:
                w_guess[min_t[1]] += 1
            if min_v[1]:
                w_guess[min_v[1]] += 1

    final_guess = []
    world_guess = {}
    for val in range(len(w_guess)):
        name = worlds[val].split('_')
        world = name[0]
        if world in world_guess:
            world_guess[world]+=w_guess[val]
        else:
            world_guess[world]=w_guess[val]
    print(world_guess)
    max_val = max(list(world_guess.values()))
    for w in world_guess:
        if world_guess[w]==max_val:
            final_guess.append(w)
    return final_guess


# TESTING
num_correct = 0
for test_s in scen.scenarios:
    results = {}
    curr = test_s.name.split('_')[-1]
    ids = [1,2]

    r = sss_model(test_s, ids)
    for w in r:
        if w in results:
            results[w] += 1
        else:
            results[w] = 1
    max_num = 0
    correct_w = ""
    for w in results:
        if results[w]>max_num:
            correct_w = w

    if correct_w == test_s.name.split('_')[0]:
        num_correct += 1

    print(test_s.name)
    print("correct: ", (correct_w == test_s.name.split('_')[0]))

    print(num_correct)
