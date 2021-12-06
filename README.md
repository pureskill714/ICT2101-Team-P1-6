# ICT2101-Team-P1-6
Web-Based Maze Game with integration with Bluettoth Controlled Robotic Car

## Team Members
- Muhammad Abdurraheem Bin Abdul Hamid `Team Leader + Development lead` - `1501918@sit.singaporetech.edu.sg`
- Chen Dong `Development Lead & Code reviewer` - `2000522@sit.singaporetech.edu.sg`
- Pang Xue Ming  `Web Developer` - `2000989@sit.singaporetech.edu.sg`
- Satya Darshini   `Web Developer` - `2002122@sit.singaporetech.edu.sg`
- Zulekah Khan Binte Salahuddin Khan  `Web Developer` - `2001222@sit.singaporetech.edu.sg`

## Dependencies and Prerequisities
- Implemented using Programming language such as Python, HTML, C, Javascript
- This project requires Python 3.6 or newer version with Flask Framework install. It is advisable to use Pycharm Community Edition IDE to run local web server.

## Project Pre-Requisites

- Establish Connection to HC-05 Bluetooth module

## How to run
1. Open terminal in IDE (e.g. Pycharm Community Edition IDE)
2. Navigate to the root directory of this project
3. Execute the command: set FLASK_APP=WebPortal
4. Execute the command: flask run if flask not found try use: python -m flask run
4. Open any browser and navigate to [localhost](http://127.0.0.1:5000/)

## Team P1-6's Workflow:
**Rules:**

- Features assigned to different members of the team MUST have their own branch per feature under dev branch.

- Individual code MUST be pushed to the respective feature branches and tested & code review before create pull request 

**Feature Branch Management:**
1. one branch per feature
    - `feature/<feature_name>` for WebPortal features
2. Developers should create feature branch from dev branch
3. Create pull request and wait for the development lead to review and merge
4. Feature branch will be `remove` once code review is done by development lead and merge to the dev branch, branch that is still developing will not need to be remove.

**Development Branch Management:**
1. The dev branch always reflects the function ready state
2. Completed and tested features branches should be merged into dev branch
3. This code is again tested after merging with dev branch, if errors, create `bugfix/<Bug_name>` branch

**Bugfix Branch Management:**
1. Any Issue/bug found by developer or code review will have to create a issue 
    - Issue must be assigned to at least one developer
    - Issue must be label depend on the type of maintaintence (e.g `Bug`, `Enhancement`)
    - Issue must not be closed until code review is done by development lead and merged with `dev` branch.
2. create `bugfix/<Bug_name>` branch from dev
3. create pull request and wait and review and merge

**Master Branch Management:**
1. only dev branch can be merged to the main branch
2. Always represent the production ready state

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
