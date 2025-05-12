Greedy Algorithm (bag problem) Challenge

  Your algorithm needs to buy seeds for Farmer Joliphant’s new season, your algorithm 
is given a set number of fields to plant in and a list of buyable seeds, each seed in 
the list is a [seed] object with [cost] [return] and [crop] values. 
  Your algorithm must return a list of [seed] objects:
  
  - The length of the list must be the same as the number of available fields; Farmer
       Joliphant doesn’t want to buy more seeds than he can plant
    
  - There must be at least one [seed] with each [crop] value; Farmer Joliphant doesn’t
       understand supply and demand and believes that he must have a supply of
       everything in order to have demand
    
  - The amount of total [return]s minus total [cost]s should be optimized; Farmer Joliphant
       wants to make the most money possible, even if he has to take out loans to buy more
       expensive seeds
    
  - There cannot be duplicates in the seed list; the government in Farmer Joliphant's
       country has outlawed selling more than one field of a given crop seed to a given farmer
