Enter the code folder by the following instruction:\
cd code
1. To run the test you should generate a batch of maps with the following instruction:\
  python run_experiments.py --size 15 --agent_num 8 --obs_rate 20 --map_num 100 --batch --generate_map\
  The number in the instruction can be changed if you want.

3. Then run the program with the instruction:\
   python run_experiments.py --instance "map/*" --solver CBS --batch --test
