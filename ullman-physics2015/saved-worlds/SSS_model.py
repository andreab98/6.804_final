import scenarios as scen
from simulate_scenarios import scenario_stats
import data_structures as  struct

def sss_model(test_s, scenario_id):
    poss_worlds = {}
    diff = {}
    #searches for 1 scenario from each world
    for s in scen.scenarios:
        # s.name.split('_')[-1] == scenario
        if s.name.split('_')[-1] == str(scenario_id):
            name = s.name.split('_')[0]
            # path = [p[0] for p in s.path]
            poss_worlds[name] = scenario_stats(s)

    # test summary stats
    test_stats = scenario_stats(test_s)
    # print(test_stats.keys())
    # ict_keys(['pre_post', 'rest_time_surf',
    # 'velocity_loss', 'dist_average', 'total_change',
    # 'av_position', 'av_velocity'])

    worlds = list(poss_worlds.keys())
    # check each summary statistics for  each world
    w_guess = [0 for i in range(10)]

    dist_average = (10000000,0)
    total_change = (10000000,0)
    for i in range(len(worlds)):
        diff = test_stats["dist_average"] - poss_worlds[worlds[i]]['dist_average']
        if diff<dist_average[0]:
            dist_average = (diff, i)

        diff = test_stats["total_change"] - poss_worlds[worlds[i]]['total_change']
        if diff<total_change[0]:
            total_change = (diff, i)

    w_guess[dist_average[1]]+=1
    w_guess[total_change[1]]+=1

    for color in ['yellow','blue','red']:
        min_vel = (10000000,0)
        min_pos = (10000000,0)
        min_t = (10000000,0)
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

        w_guess[min_vel[1]]+=1
        w_guess[min_pos[1]]+=1
        w_guess[min_t[1]]+=1

        for color2 in ['yellow','blue','red']:
            
        for surfaces in ['brown', 'darkmagenta', 'yellowgreen']:
            for name in poss_worlds:
                # total_change
                test = test_stats['total_change']
                actual = poss_worlds[name]['total_change']

            stats["pre_post"] = pre_post_collision

            stats["rest_time_surf"] = collision_times
                stats["velocity_loss"]


        print(actual)
        average position

    print(w_guess)

    return


# TESTING
w2s1 = scen.scenarios[0]
print(w2s1.name)
print(sss_model(w2s1, 2))
print("\n")

print(sss_model(w2s1, 3))
print("\n")

print(sss_model(w2s1, 4))
print("\n")

print(sss_model(w2s1, 5))
print("\n")

print(sss_model(w2s1, 6))
print("\n")
