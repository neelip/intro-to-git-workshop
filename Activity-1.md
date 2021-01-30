# Activity #1

### Part A: Setup

#### Create GitHub Account
1. Create Account: https://github.com/join
2. Verify Account

#### Setup SSH Connection to GitHub
1. Generate a new SSH key: https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

2. Add SSH key to the ssh-agent

3. Add SSH key to your GitHub account: https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account

#### Setup VSCode
1. Download VSCode: Pick a download version that fits your OS specifications.
https://code.visualstudio.com/download
2. Download Python Version 3.9.1 : https://www.python.org/downloads/
3. Install the Python extension in VSCode. 


### Part B: Intialize Git Repo and Create a Flask app

#### Initialize Git
1. Open a new directory:
    mkdir myFirstRepo
    cd myFirstRepo
2. Initialize git:
    git init
3. Now open this folder in VSCode workspace.
4. Once you open the folder in VSCode, you should see "master" at the bottom left of the VSCode window. This is your main branch.  
The branches "main" and "master" mean the same for this workshop, it is just a difference in naming convention.

#### Create Simple Flask App:

#### A. Set Python Interpreter
1. Open Command Palette in VSCode with this keyboard shortcut:
        Command + Shift + P (Mac)
        Control + Shift + P (Windows)
2. Once the Command Palette opens enter "Python:" and from the dropdown list select
        "Python: Select Interpreter"
3. Select the recently installed Python 3.9.1 version as shown below.
4. Once you selected the Python Interpreter you will see it displayed at the bottom left of the VSCode Window.  
    *Tip*: If you ever need to change the Python Interpreter, you can just click directly on the displayed Python Interpreter rather than going thru the Command Palette.

#### B. Create a Python Environment
1. In the Terminal, enter the following command:
   ```
   pip3 install --user virtualenv
   ```
2. Once virtualenv is installed, enter the following command:
   ```
   python3 -m venv venv
   ```
3. Activate virtual environment: 
   ```
   source venv/bin/activate
   ```
4. Install flask:
   ```
   pip3 install flask
   ```
#### C. Write Code
1. Create a file called "app.py". Add this code and save the file:
   ```
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def index():
      return 'Web App with Python Flask!'
   
   # If planning to run thru the terminal
   # app.run(host='0.0.0.0', port=81)
   ```
2. Follow demo to setup a debugger for a easy way to run the app or else use the method below.

#### D. Add and Commit

1. In the Terminal, type the following command:
   ```
   git log
   ```  
   Expected Output: "fatal: your current branch 'master' does not have any commits yet"  
     
   ```
   git status
   ```
   Expected Output: "On branch master

                    No commits yet

                    Untracked files:
                    (use "git add <file>..." to include in what will be committed)
                            ../.vscode/
                            ../app.py
                            venv/

                    nothing added to commit but untracked files present..."
2. create a file ".gitignore" and add the following code:
   ```
   venv/
   .vscode/settings.json
   __pycache__/
   ```
3. Stage untracked files. Type this in Terminal:
   ```
   git add .
   ```
4. Commit staged files to master. Type this in Terminal:
   ```
   git commit -m "My first commit: Simple Flask App"
   ```
5. Check git log, your new commit should be added to the vlog

### Part C: Create Repository on GitHub and Push changes

1. Create GitHub Repository called "MyFirstRepo". Follow Demo.
2. Add Git Remote:
   ```
   git remote add origin <ssh link of the repo on GitHub>
   ```
3. Update local with any new changes on the remote:
   ```
   git pull origin 
   ```
4. Push the recent commits to remote:
   ```
   git push origin 
   ```  
   (enter password if needed)  


#### (Optional) Run Flask App
1. Open app.py file that existes in our VSCode workspace.
2. On the file itself right-click to get a drop-down menu, and find "Run Python File in Terminal". Select this option. 
3. You should see something like this:
   ```
   * Serving Flask app "SimpleFlaskApp" (lazy loading)
   * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
   * Debug mode: off
   * Running on http://0.0.0.0:81/ (Press CTRL+C to quit)
   ```
4. Open http://0.0.0.0:81/ to the flask app. 


   
