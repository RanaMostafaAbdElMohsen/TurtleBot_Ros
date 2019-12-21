# Tutorial
This documentation is to wrap-up all commands and how to use commands on `RDS`

## Fetching Files from Remote Repo
Please refer to `GettingStarted.md` for details

### Starting Simulation
Displaying our simulated world with all objects and ROS turtlebot on `Gazebo`
- Launch `Ros Development Studio`
- Open your created project + follow steps ``GettingStarted.md``
- Inside motion_plan, two folders:
        - launch : simulation and motion_planning launches
        - worlds : world files created so far
- Navigation Bar, click Simulation -> click Launch -> choose `tb_main.launch`

### Starting SLAM algorithm
- Open a shell terminal:
    - type `roslaunch source_code gmapping.launch`  

### Starting Rviz
- Open a shell terminal:
    - type `roslaunch source_code view_localization.launch`

### Running Move_Base Algorithm
This allows robot to localize itself and go to a certain goal `Refer for Video 1 in tutorial for more details`
- Open a new shell from navigation bar
- Kill all open terminals except `gazebo simulation`
- Type in command `roslaunch source_code move_base.launch`
- Open a new shell and start `Rviz` as instructed above
- Open Graphical Tool
- Watch Tutorial part to give robot `2d pose estimate` and `2d nav goal`

### Map Generation
Instructions for generating map
- Starting SLAM algorithm as instructed above
- Open a shell terminal
- Type `rosrun rviz rviz`
- Open graphical Tools
- Resize
- Click `Add -> By Topic -> map`
- Click `Add -> Robot State`
- Click `Add -> Laser Scan -> Adjust size (laser size) to be 0.03m + Topic -> /kabouki/laser/scan`
- Open another shell terminal
- Type `roslaunch turtlebot_teleop keyboard_teleop.launch`
- Move turtlebot around till loop closure more than once
- Observe map on rviz
- `Kill turtlebot_teleop terminal` once finding map satisfactory
- Open a shell terminal
- Navigate to map folder : `cd simulation_ws/src/source_code/map`
- Save map by typing in terminal `rosrun map_server map_saver -f my_map`

### Running autonmous mappping
#### First time
- Type in the shell `sudo apt-get update`
- Type `sudo apt install ros-${ROS_DISTRO}-explore-lite`
#### Run commands
- Open a new shell from navigation bar
- Kill all open terminals except `gazebo simulation`
- Type in command `roslaunch source_code explore_demo.launch`
- Open a new shell and start `Rviz` as instructed above
- Open Graphical Tool

### Sending a goal
#### First time
- Type in the shell `rosdep update`
- Type `sudo rosdep fix-permissions`
- Make sure the script send_goal.py is excutable (`chmod +x send_goal.py`)
#### Run commands
- Open a new shell from navigation bar
- Kill all open terminals except `gazebo simulation`
- Run move base algorithm as mentioned above
- Type in command `rosrun source_code send_goal.py x y theta` replace x y theta with you desired coordinates


