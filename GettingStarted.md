## Getting Started

## Repository Branches
There are 3 main branches in repository :
  - Master
    - Contains all readme files + tutorials for repository
    - Contains all necessary documentation
  - Simulation
    - Contain all details about world gazebo file with its launch file
  - motion_planning
    - Contain all algorithms necessary for motion_planning

## Working Environment
- Option 1 : Working with `Ubuntu 16 + Kinetic` with all ros packages installed
- Option 2 : Working on `RDS environment`

## SetUp Environment
  - Ros Development Studio:
      1- Create an account on Ros development studio
      2- Create a ROS project ( public / private)
      3- For cloning `motion_planning` branch from repo
            - Open ``shell terminal`` from navigation bar
            - ``cd catkin_ws/src`` 
            - git clone `https://github.com/RanaMostafaAbdElMohsen/TurtleBot_Ros.git`
            - Enter your credentials
            - git checkout `motion_planning`
      4- For cloning `Simulation` branch from repo
            - Open ``shell terminal`` from navigation bar
            - ``cd simulation_ws/src`` 
            - git clone `https://github.com/RanaMostafaAbdElMohsen/TurtleBot_Ros.git`
            - Enter your credentials
            - git checkout `Simulation`
            
## Before Commiting your changes
  - Ros Development Studio:
      - Save instance before you exist
        
## Pushing Changes on Remote Branch
Here are some instructions to make code more organised:
  - master branch is for documentation purposes do not push to it
  - When you are done with your changes + ready to push
      - `git checkout -b "new_branch_motion_planning"` or `git checkout -b "new_branch_Simulation"` ( Example rename branch as you like)
      - `commit your changes`
      - push your code
      - Make a `Pull request` and request review from other two in teams 
      - If it runs successfully on our instances:
            - Authorized to be push to its `parent` branch whether it was `motion_planning` or `simulation` branch
            
## Useful Tutorial Links
Tutorial link : [Click Here](https://www.theconstructsim.com/ros-projects-exploring-ros-using-2-wheeled-robot-part-1/?fbclid=IwAR329qyHD6eSoK7mos0zKBc82YJ35Bxid6k4rV9o9ltloKA5OX-vpYSQDKE)
