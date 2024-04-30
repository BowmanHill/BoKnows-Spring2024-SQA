# BoKnows-Spring2024-SQA

Team Name: BoKnows

Team Members: Bowman Hill, HBH0018@auburn.edu

Tasks
    A. Git hook is in .git/hooks/pre-commit, reports go in security.py
    B. fuzz.py fuzzes 
        1. empirical/report/median
        2. empirical/report/average
        3. empirical/report/reportProp
        4. empirical/frequency/reportProportion
        5. mining/mining/makeChunks
    C. Logging forensics added to five methods
        1. empirical/report/reportProp
        2. empirical/report/reportDensity
        3. empirical/frequency/reportProportion
        3. mining/git.repo.mining/deleteRepos
        4. mining/mining/main
    D. Github actions automatically executes fuzz.py