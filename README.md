# KARTAL

### FlightGear JSBSim Integration for Reinforcement Learning Agent Environment Framework baseline

### How to Run

Following steps will guide through RL agent training using JSBSim FDM

1. Install python with requirements.txt (pip install -r requirements.txt)
2. (Optional) Install flightgear 2018.3.6 and add bin directory to the PATH environmental variable (for FG visualizations only)
3. Go the project directory and use 'python train.py' or 'python main.py'
4. Edit train.py file to manage and change train parameters (training length, algorithm, learning rate etc.)

### Libraries

[FlightGear](https://www.flightgear.org)

[Gym JSBSim](https://github.com/Gor-Ren/gym-jsbsim)

Another Gym JSBSim baseline [fork](https://github.com/jrjbertram/jsbsim_rl)

[JSBSim](https://github.com/JSBSim-Team/jsbsim)


### File Structure:

```
Project Directory
  ├── gym_jsbsim
  ├── jsbsim
  ├── model
  ├── train.py (to train an agent)
  └── main.py
```
