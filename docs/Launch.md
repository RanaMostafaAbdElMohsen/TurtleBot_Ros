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
    - type `roslaunch motion_plan gmapping.launch  

### Starting Rviz 
- Open a shell terminal:
    - type `roslaunch motion_plan view_localization.launch`
                      
### Running Move_Base Algorithm
This allows robot to localize itself and go to a certain goal `Refer for Video 1 in tutorial for more details`
- Open a new shell from navigation bar 
- Kill all open terminals except `gazebo simulation`
- Type in command `roslaunch motion_plan move_base.launch`
- Open a new shell and start `Rviz` as instructed above
- Open Graphical Tool
- Watch Tutorial part to give robot `2d pose estimate` and `2d nav goal`
                      
