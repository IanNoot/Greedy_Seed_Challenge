import random

def greedy_seeds_challenge():
    ## SEED CLASS
    class Seed:
        def __init__(self, crop, cost, value):
            self.crop = crop
            self.cost = cost
            self.value = value



    ## VARIABLES
    num_fields = random.randrange(20, 50)
    possible_crop_types = ["tulip", "corn", "asparagus", "potato", "cabbage", "carrot", "cotton", "celery", "turnip", "broccoli", "brussle_sprout", "heather", "grape", "blueberry", "strawberry"]
    crop_types = []
    seeds = []



    ## GENERATE INPUT LIST
    
    #Decide which crop types to use
    for i in random.randrange(3,7):
        crop_types.append(possible_crop_types.pop(random.randrange(0, len(possible_crop_types)) )  )

    #Create a base list of crops
    for crop in crop_types:
        for i in range(random.randrange(10,100)):
            seeds.append( Seed(crop, random.randrange(10, 200), random.randrange(10, 200)) )



    ## ASK FOR PLAYER INPUT
    player_input = Player().greedy_seeds(num_fields, seeds)
    player_success = False
    player_has_all_crops = False
    player_has_right_score = False

    ## CALCULATE CORRECT ANSWER
    optimal_seeds = []
    optimal_score = 0
    

    #Find the best seed of each crop type
    for crop in crop_types:
        best = Seed(None, 0, 0)
        indx = 0
        best_indx = 0
        
        for seed in seeds:
            if seed.crop == crop and (best.crop == None or best.cost - best.value < seed.cost - seed.value):
                best = seed
                best_indx = indx
            indx += 1
        
        optimal_seeds.append(best)
        seeds.pop(best_indx)

    #Find the remaining best seeds
    for i in range(num_fields - len(optimal_seeds)):
        best = Seed(None, 0, 0)
        indx = 0
        best_indx = 0
        
        for seed in seeds:
            if best.crop == None or best.cost - best.value < seed.cost - seed.value:
                best = seed
                best_indx = indx
            indx += 1
        
        optimal_seeds.append(best)
        seeds.pop(best_indx)
        
    #Score the optimal set
    value = 0
    cost = 0
    for seed in optimal_seeds:
        value += seed.value
        cost += seed.cost
    optimal_score = value - cost
    
    
    
    ## COMPARE PLAYER INPUT TO OPTIMAL ANSWER
    value = 0
    cost = 0
    for seed in player_input:
        value += seed.value
        cost += seed.cost
    player_score = value - cost
    
    if player_score == optimal_score:
        player_has_right_score = True
    
    for crop in crop_types:
        found = False
        for seed in player_input:
            if seed.crop == crop:
                found = True
        if found == False:
            player_has_all_crops = False
            break
    
    if player_has_all_crops and player_has_right_score:
        player_success = True
    
    optimal_seeds_string = ""
    player_seeds_string = ""
    
    for seed in optimal_seeds:
        optimal_seeds_string = optimal_seeds_string + f"\"{seed.crop}\", cost({seed.cost}), value({seed.value})\n"
    
    for seed in player_input:
        player_seeds_string = player_seeds_string + f"\"{seed.crop}\", cost({seed.cost}), value({seed.value})\n"
    
    return(player_success, optimal_seeds_string, player_seeds_string )