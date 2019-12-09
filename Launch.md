# Tutorial 
This documentation is to wrap-up all commands and how to use commands on `RDS`

## Fetching Files from Remote Repo
Please refer to `GettingStarted.md` for details

### Starting Simulation
Displaying our simulated world with all objects and ROS turtlebot on `Gazebo`
- Launch `Ros Development Studio` 
- Open your created project + follow steps ``GettingStarted.md``
- Navigation Bar, click Simulation -> click Launch -> choose `turtlebot_world.launch`

### Starting Rviz 
Display `SLAM algorithm` with turtlebot on Rviz
  - Prequisities:
      - Wait till `Gazebo simulation` is launched completely 
  1- Open a shell using navigation bar 
  2- Type command : ``roslaunch motion_plan gmapping.launch``
  3- Wait for 30 secs -> (running)
  4- Open Graphical Tool using navigation bar 
      - Resize Window
      - Add Robot State using `Add Button -> Robot State`
            - observe robot spawned in Rviz
      - Click `Add Button -> Laser Sensor`
            - Click on Laser Sensor 
            - Find topic for Laser Sensor in Menu
            - Type in `/laser/scan`
      - Click `Add Button -> Map`
            - Click on Map
            - Find topic for Map in Menu
            - Type in `/map`
            - There should be no warning appear
                  - you should see grey shadow for Map visible on Rviz
            - If Warning appear that map is not found
                  - means you have launched `roslaunch motion_plan gmapping.launch before Gazebo Simulation is launched completely`
                  - Corrective Action
                      - Close everything including Gazebo Simulation + restart process
                      
### Running ObstacleAvoidance Algorithm
After Starting Rviz
- Open a new shell from navigation bar 
- Type in command `roslaunch motion_plan obstacleAvoidance.launch`
- Await and you will find turtle_bot moving in simulation
- Observe while it is building a map in Graphical Tool
                      
