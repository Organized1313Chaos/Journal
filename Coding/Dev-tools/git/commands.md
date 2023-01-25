###git Commands

- check git verision in cmd--> git --version

**Basic**
1. `git init`
   initialize the git repository
2. `git log`
   displays all commits
3. `git reset --soft <commit sh>`
   go to a specific commit message and restores files and local history

   - soft reset: move your HEAD to where they were , but leave your local files
   - hard reset: local code and local history be just like it was at that commit
4. git add . 
   Stage all untracked files
   - git add `<filename>` 
   stage only files with the given filname
5. git commit -m "message|comment"

Note: git commit -am "message": add files to stages, make commits simultaneously.

6. git log: see logs of commits

7. git checkout hashcode: switch to different commits

8. git branch: get branch name
9. git branch branchname | git checkout -b branch_name: To create a new branch
10. git merge branch_name: Make sure you go to the main branch and then run the command over there 
**Basics 2: (Sunil Sir)**
   
1) `git status:` `Track Status`
2) `git pull origin master:` `Get the latest branch of branch master`
3) `git checkout -b branch_name:` `Switch to branch, if it doesn't exist, create one and switch it`
4) `git fetch all:` `Fetches all branches`

**Configurations: (Yatin, CWH)**

- git config --global user.name "name"
- git config --global user.email "email"


**Merge Two Repositories**

1. git remote -v
   display remote branches with fetch and pull request
2. git branch -a
   dsiplay all branches without commit message
3. git branch -a -vv
   dsiplay all branches with hash and commit message
4. git remote add repo-name
   Connect the new repository to an existing remote repository that has no data.
5. git remote remove repo-name
   remove existing remote repository.

**Git Branch Operations**

1. git switch branch-name
   switch to already existing branch
2. git checkout -b branch-name
   creates a new branch and switches to it.

**Notes:**
- Clone specific branch
  `git clone -b branch_name link`

- Before pulling
  ```
  git add .
  git stash
  git pull origin dev-branch_name
  ```

- To see previous (your own) changes after the pull
  `git stash pop`

- To Push
  ```
  git add .
  git commit -m "commit message"
  git push origin dev-branch_name
  ```

**Tree structure**
- tree -L <Level>

**Merge one Git Repository into Existing One**
1. [stackoverflow](https://stackoverflow.com/questions/1683531/how-to-import-existing-git-repository-into-another)
