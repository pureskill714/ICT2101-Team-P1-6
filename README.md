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
3. Only `Development lead` can merge dev branch to master branch
    - Both Development lead have to approve with the merging to proceed

**Release Branch Management**
1. Development lead can create release branch `rel_<version_num>`
2. All releases also branch off dev but merge back into BOTH dev and master

**Hotfix Branch Management**
1. Developers can create the hotfix branch `hotfix_<minor_version_num>`
2. All hotfixes branch off master and merge back into both dev and master

## Standard Operating Procdeure (SOP)
**Note `Github Desktop` were mostly use for commit/push/merge/pull request**

**1) Creating Features in Project Board:**

    - Assign different priority(e.g high,medium & low) to different feature on team's Project Board
    - Create different feature branch from dev branch base on corresponding feature assign in Project board
    - Assign each feature to different Developer to commit with the specify feature
    
    # Feature to branch off from dev
    git checkout -b feature/<feature_name> dev
    
    # UI to branch off from dev
    git checkout -b UI/<UI_name> dev
    
    
**2) Commit to Feature Progress:**

    - Commit and push working progress of feature/<feature_name> branch to that specifyy feature branch with modify code once the component of the feature is completed and unit testing is done
    
    # add commit messgae and push the modify code changes to Github repo of the specify feature once componenet is complete
    git commit -a -m "added feature to <feature_name> branch"
    git push
    
**3) Merge completed Feature branch to dev branch:** 

    3.1) After code reviewer/development lead approved, merge completed feature branch into dev
            3.1.1) Navigate to pull requests on Github respo 
            3.1.2) Click one new pull request 
            3.1.3) Select dev branch and the corresponding feature branch to merge 
            3.1.4) Select Create pull request button
            3.1.5) Input meaningful comment and title 
            3.1.6) Select 2 developement lead for reviewers setting 
            3.1.7) Assign Labels according to the type of feature and click on Create Pull Request 
            3.1.8) Once approval given from the two 2 development lead, click on merge pull request button 
            3.1.9) Click on the confirm merge button
                   
    3.2 Delete feature branch once merge to dev branch is completed
            3.2.1) OnlY developer lead are able to delete any feature branch.
            3.2.2) git branch -d <feature_name> branch
            
 **4)  Issues for bug fixes and other maintenance during Development process:** 
 
    4.1) Issue/bug found in the dev branch, developer will branch out from dev branch and resolved from the specify branch
    4.2) Issue/bug found in the feature/UI branch, developer will continue to resolved from that branch.
    4.3) Only merge back to dev branch once issues have been resolved and approved by the developer lead.
    4.3) Additonally issue/bug/enhancement found will have to create a new issue
            4.3.1) Navigate to Issues tab on Github respo
            4.3.2) click on new issue and write meaningful title and comment 
            4.3.3) Assign the issue to respective developer and to a developer lead (verify and close the issue)
            4.3.4) Assign a label depend on the issue type
            4.3.5) Click on Submit new issue once all the above field is fill up.
            4.3.6) Developer can only closed the issue once assigned developer lead commented "Fixed" on the issue.
           
  **5)  Merge Dev branch with Main Branch & release of new version branch:** 
   
    5.1) After completed development process, merge dev branch to master branch by development lead
            5.1.1) Navigate to pull requests on Github respo 
            5.1.2) Click one new pull request 
            5.1.3) Select master branch and the dev branch from dropdown list
            5.1.4) Select Create pull request button
            5.1.5) Input meaningful comment and title 
            5.1.6) Select other developement lead for reviewers setting 
            5.1.7) Assign Labels according to the type of feature and click on Create Pull Request 
            5.1.8) Once approval given from the two 2 development lead, click on merge pull request button 
            5.1.9) Click on the confirm merge button
            
      5.2) Once dev branch merge with master branch is completed, create a new "rel-<version_num>" branch by development lead
            5.2.1) git checkout -b "rel_<version_num>" dev
            
               
  **6)  Hotfix branch:** <br>
  - As version have been release to public, hotfix have to been done fast and efficient.
  - Create a `high-priority` issue on github project board wtih label hotfix and assign the specify developer and mention them in the comment.
  - Conduct step 4 for for bug/issue fixes once done,
  - Perform step 3 for merging hotfix feature back into dev and master branch
  - Once all done and review by development lead, development lead will closed the hotfix issues

## User Acceptance Test
- Use case Diagram (No change from M2)
- System State Diagram (No change from M2)
- Video for System Test

https://user-images.githubusercontent.com/72610274/144871833-619afa21-03fb-44c9-8782-d9237b89b661.mp4


## Whitebox Testing
- Selected class to demonstrate the test code
    - `CarController` Class is used (In CarController.py located at main directory)
- Test Cases (In testCarController.py)
    - `test_instance()` to check if instance is created
    - `test_password()` to check if password is set correctly
    - `test_statset` to check if car stat is set correctly
    - `test_changepassword()` to check if car password can be changed
    - `test_bluetothSetup()` to check if bluetooth configuration is set
    - `test_openconnection()` to check if bluetooth can be open
    - `test_testconnection()` to test if the connection is not lost
    - `test_sendCommand()` to test if command can be send successfully
- Code coverage statistic
    - Statement Coverage<br />
      ![1](https://user-images.githubusercontent.com/72610274/144872048-348b20ab-f3b7-4915-9582-f2dd6d68b5f4.PNG)
    - Branch Coverage<br />
      ![2](https://user-images.githubusercontent.com/72610274/144872223-9af074eb-5462-4ae6-a609-c86928d3769a.PNG)
    - We use `pytest` for testing and `coverage` for calculate code coverage.<br />
      A test class need to be create and write test function with `assert` and run the command, then it will auto call those function and produce a pass fail report of the function run.<br />
      `coverage` will help to calculate the execution of the file is is being run and generate the coverage report.<br />
      The percentage is not 100% because there are some case where we are unable to simulate.
- Test Suite Execution Instructions<br />
    Test statement coverage
    ```bash
    coverage run -m pytest testCarController.py
    ```
    To get the report
    ```bash
    coverage report
    ```
    Test branch coverage
    ```bash
    coverage run --branch -m pytest testCarController.py
    ```
    To get the report
    ```bash
    coverage report
    ```

- video for Test Suite Execution


https://user-images.githubusercontent.com/72610274/144871777-bf14f20d-02ee-4436-96ca-badefa023a6f.mp4

