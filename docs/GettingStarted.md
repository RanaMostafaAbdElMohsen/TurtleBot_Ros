## Getting Started

## Repository Branch
There are 3 main branches in repository :
  - Master
    - Contains most `up-to-date working` branch of project so far
    - Contains all `updated` readme files + tutorials for repository
    - Contains all necessary documentation
  - History_Simulation_Buggy `( Deprecated )`
    - Contains earlier version of project but `buggy`
  - HIstory_Motion_Planning_Buggy `( Deprecated )`
    - Contains earlier version of project but `buggy` with all algorithms necessary for motion_planning
  -Exploration
    -Code for exploration(currently only move_base with gmapping is working)

## Working Environment
- Option 1 : Working with `Ubuntu 16 + Kinetic` with all ros packages installed
- Option 2 : Working on `RDS environment`

## SetUp Environment
  - Ros Development Studio:
      - Create an account on Ros development studio
      - Create a ROS project ( public / private)
      - For cloning `master` branch from repo
      - Open ``shell terminal`` from navigation bar
      - ``cd simulation_ws/src`` 
      - git clone `https://github.com/RanaMostafaAbdElMohsen/TurtleBot_Ros.git`
      - Enter your credentials
      - git checkout `master`
      - From Shell terminal : `cd ..`
      - Type in terminal: `catkin_make`

            
## Before Commiting your changes
  - Ros Development Studio:
      - Save instance before you exist
        
## Pushing Changes on Remote Branch
Here are some instructions to make code more organised:
  - master branch is for documentation purposes do not push to it
  - When you are done with your changes + ready to push
      - `git checkout -b "new_branch_changes"` ( Example rename branch as you like)
      - `commit your changes`
      - push your code
      - Make a `Pull request` and request review from other two in teams 
      - If it runs successfully on our instances
      - Authorized to be push to `master` branch

            
## Useful Tutorial Links
Found a turtorial on turtle_ros where I can perform localization and create a map etc...
Tutorial link : [Click Here](https://www.youtube.com/playlist?list=PLK0b4e05LnzZA_fWYi1_VEuBzNw9BGo6s&fbclid=IwAR39AzthImdkdXIoZ23oz6d5_kM8vbEb2z-jmNkq4VQ6qI12-wcaGFyi5t4)

## Progress so far 
- Done Video 1 from Playlist
- Done Video 2 from Playlist

