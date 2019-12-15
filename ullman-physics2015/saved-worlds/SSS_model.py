import scenarios as scen
import simulate_scenarios

def sss_model(obs_path, scenario_id):
    poss_worlds = {}
    diff = {}
    for s in scen.scenarios:
        stats  = simulate_scenarios.scenario_stats(s) # simulation for stats


    return


# TESTING
w10s1 = [p[0] for p in scen.scenarios[0].path]
print(w10s1)
print(sss_model(w10s1, 2))
