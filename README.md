anaconda3\
python = 3.6

Dependencies:
matplotlib==3.3.4

Enter the code folder: cd code

1. To run the test you should generate a batch of maps:\
  To generate the simple map, first make a new folder for map, then:\
  python run_experiments_single_agent.py --size <num> --agent_num <num> --obs_rate <num> --map_num <num> --batch --generate_map --output_file <folder_name>\
  example:\
  python run_experiments_single_agent.py --size 10 --agent_num 1 --obs_rate 20 --map_num 100 --batch --generate_map --output_file map

    To generate the map of benchmark:\
    python run_experiments_single_agent.py --agent_num <num> --map_num <num> --batch --generate_map --benchmark <file_name> --output_file <folder_name>\
    example:\
    python run_experiments_single_agent.py --agent_num 5 --map_num 100 --batch --generate_map --benchmark maze-32-32-2.map --output_file maze-32-32-2

3. The test of single agent task:\
   python run_experiments_single_agent.py --instance "<file_name>/\*" --solver CBS --batch --test\
   example:\
   python run_experiments_single_agent.py --instance "maze-32-32-2/\*" --solver CBS --batch --test

4. The test of MAPF:\
   python run_experiments_MAPF.py --instance "<file_name>/\*" --solver CBS --batch --test\
   example:\
   python run_experiments_MAPF.py --instance "maze-32-32-2_5_MAPF/\*" --solver CBS --batch --test
