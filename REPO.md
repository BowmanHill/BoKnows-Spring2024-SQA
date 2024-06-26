# Software Quality Assurance Term Project
## Bowman Hill - BoKnows

## Lessons Learned

### Repo-setup
    1. This was relatively simple, I did learn I need to pare down the number of github accounts I have as the permissions battle was a bit of a struggle

### 4.a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (20%)
    1. This was also a relativley simple operation. 
    2. After initializing the repository all I had to do was copy the pre-commit.sample to pre-commit. 
    3. Then I added bandit into the precommit as well as a check to ensure bandit is installed
    4. Finally a conditional statement to add to the security_report.csv this task was completed.
<br>
Below is an image showing the hooks output and the risks recorded in the security_report.csv:
<br>

![alt text](https://github.com/BowmanHill/BoKnows-Spring2024-SQA/blob/main/ProjectImages/hookOutput.png)


### 4.b. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. (20%)

    1. The hardest part of this was choosing which five methods to fuzz. 
        fuzz.py fuzzes the following methods: 
            1. empirical/report/median
            2. empirical/report/average
            3. empirical/report/reportProp
            4. empirical/frequency/reportProportion
            5. empirical/frequency/reportEventDensity
    2. I started by using a previous fuzz.py file as a template and created a new try catch for each of the five methods chosen. With a list to store catches.
    3. Then I created execFuzz.yaml to automatically execute fuzz.py from Github Actions. 
    4. In order for my workflow to function properly I also created a requirements.txt to be able to install all necessary dependencies for the fuzz.py file.
<br>
Below is the workflow being run and the fuzz.py output in github Actions:
<br>

![alt text](https://github.com/BowmanHill/BoKnows-Spring2024-SQA/blob/main/ProjectImages/execFuzzWorkflowOutput.png)

### 4.c. Integrate forensics by modifying 5 Python methods of your choice. (20%)
    1. To integrate forensics I first create a simple logger file
    2. Logging forensics were then added to five methods in the Fame-ML and empirical methods
    3. Each of the logging spots is documented below
    
![alt text](https://github.com/BowmanHill/BoKnows-Spring2024-SQA/blob/main/ProjectImages/Log1.png)
![alt text](https://github.com/BowmanHill/BoKnows-Spring2024-SQA/blob/main/ProjectImages/Log2.png)
![alt text](https://github.com/BowmanHill/BoKnows-Spring2024-SQA/blob/main/ProjectImages/Log3.png)
![alt text](https://github.com/BowmanHill/BoKnows-Spring2024-SQA/blob/main/ProjectImages/Log4.png)
![alt text](https://github.com/BowmanHill/BoKnows-Spring2024-SQA/blob/main/ProjectImages/Log5.png)

### 4.d. Integrate continuous integration with GitHub Actions. (20%)
    1. I used codacity with GitHub Actions to implement continuous integration into the project.
    2. First I created a main.yaml file in the .github/workflows directory
    3. Then I pasted the basic codacity implementation from the previous workshop

You can see one of the workflow runs at 
<br>
https://github.com/BowmanHill/BoKnows-Spring2024-SQA/actions/runs/8898952410/job/24437203701




