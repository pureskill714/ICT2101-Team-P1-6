# ICT2101-Team-P1-6
Web-Based Maze Game with integration with Bluettoth Controlled Robotic Car

## Team Members
- Muhammad Abdurraheem Bin Abdul Hamid  `1501918@sit.singaporetech.edu.sg`
- Chen Dong  `2000522@sit.singaporetech.edu.sg`
- Pang Xue Ming  `2000989@sit.singaporetech.edu.sg`
- Satya Darshini   `2002122@sit.singaporetech.edu.sg`
- Zulekah Khan Binte Salahuddin Khan `2001222@sit.singaporetech.edu.sg`

## Dependencies and Prerequisities
- Implemented using Programming language such as Python, HTML, C, Javascript
- This project requires Python 3.6 or newer version with Flask Framework install. It is advisable to use Pycharm Community Edition IDE to run local web server.

## Project Pre-Requisites

- Establish Connection to HC-05 Bluetooth module

## How to run
1. Open terminal 
2. Navigate to the root directory of this project
3. Execute the command: set FLASK_APP=WebPortal
4. Execute the command: flask run if flask not found try use: python -m flask run
4. Open any browser and navigate to [localhost](http://127.0.0.1:5000/)

## Team P1-6's Workflow:
**Rules:**

- Features assigned to different members of the team MUST have their own branch per feature under dev branch.

- Individual code MUST be pushed to the respective feature branches before merging to the master branch.

**Feature Branch Management:**
1. one branch per feature
    - `<feature_name>` for WebPortal features
    - `<management_feature_name>` for project or repo management features 

2. Developers should create feature branch from dev branch
3. Push code to branch ONLY when it is completed 

**Development Branch Management:**
1. The master branch always reflects the production-ready state
2. Completed and tested features branches should be merged into dev branch
3. This code is again tested after merging with dev branch, if errors, proceed to merge with  the master branch

**Main Branch Management:**
1. only dev branch can be merged to the main branch

**Release Branch Management**
1. Developers can create release branch `rel_<version_num>`
2. All releases also branch off dev but merge back into BOTH dev and master

**Hotfix Branch Management**
1. Developers can create the hotfix branch `hotfix_<minor_version_num>`
2. All hotfixes branch off master and merge back into both dev and master

## User Acceptance Test
- Use case Diagram
- System State Diagram
- Video for System Test

## Whitebox Testing
- Selected class to demonstrate the test code
- Test Cases
- Test Suite Execution Instructions
- video for Test Suite Execution
