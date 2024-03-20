Enter the code folder: cd code

1. To run the test you should generate a batch of maps:\
  To generate the simple map:\
  python run_experiments.py --size 15 --agent_num 8 --obs_rate 20 --map_num 100 --batch --generate_map

    To generate the map of benchmark:\
    python run_experiments.py --agent_num 5 --map_num 100 --batch --generate_map --benchmark <file_name>
  
    The number in the command can be changed if you want.

2. The test of single agent task:\
   python run_experiments_single_agent.py --instance "<file_name>/*" --solver CBS --batch --test\
   example:\
   python run_experiments_single_agent.py --instance "maze-32-32-2/*" --solver CBS --batch --test

4. The test of MAPF:\
   python run_experiments_MAPF.py --instance "<file_name>/*" --solver CBS --batch --test\
   example:\
   python run_experiments_MAPF.py --instance "maze-32-32-2_5_MAPF/*" --solver CBS --batch --test
