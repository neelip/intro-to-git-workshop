# Activity #2

### Part A: Git Branching & Remote  

#### Clone Repo
1. Open VSCode, and click Terminal at top options and open "New Terminal".  
    In the Terminal Window, make sure it reads "bash" on the right hand corner. 
2. Clone this repository:
   In the Terminal, type the following command and press enter.  
   It should prompt for a password, enter the password you created in the **Create GitHub Account Activity**.
   ```
    git clone git@github.com:neelip/intro-to-git-workshop.git
   ```   
3. The above step will copy all the contents from the repo into a new folder called "intro-to-git-workshop"  
   Check the contents of your current folder, you should see the new folder:
   ```
    ls
   ```
4. Change Terminal directory to this new folder: 
   ```
    cd intro-to-git-workshop
   ```
5. Now in the VSCode workspace, go to File> Open...  and select the folder "intro-to-git-workshop".  
   Once you found the folder, click "Open". 

You should now see the contents of the repository in your VSCode Workspace.  
You can check the git branch you are on by checking at the bottom left of the VSCode window, you see "main". 

Main (alternatively "Master") is usually considered as a production branch. 
The best practice is to not make changes direclty on the produciton branch. 

  
#### Create a New Branch 
1. In the Terminal, enter the following command to create & switch to a new branch:
   ```
   git checkout -b "neelima/thoughts"
   ```
2. In the Thoughts folder, open create a text file with your github id --> "neelip.txt".
   In this folder add your thoughts on what you have learned today and save the file.

#### Stage and Commit changes
1. Stage untracked files. Type this in Terminal:
   ```
   git add .
   ```
4. Commit staged files to master. Type this in Terminal:
   ```
   git commit -m "My thoughts on Git."
   ```
5. Check git log, your new commit should be added to the vlog:
   ```
   git log
   ```

#### Push to Remote
1. Check remote connection:
   ```
   git remote 
   ```  
   You should see "origin" in the list
2. (Optional for this workshop) Best Practice:
   ```
   git checkout main
   ```
   ```  
   git pull origin
   ```  
   ```
   git diff
   ```
   ```
   git checkout "neelima/thoughts"
   ```  
   ```
   git merge master
   ```
3. Push changes to remote:
   ```
   git push -u origin neelima/thoughts
   ```

### Part B: GitHub Pull Request (PR)  
Follow Demo. 

