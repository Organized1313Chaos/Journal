###git Commands

**Basic**
1. `git init`
   initialize the git repository
2. `git log`
   displays all commits
3. `git reset --soft <commit sh>`
   go to a specific commit message and restores files and local history

   - soft reset: move your HEAD to where they were , but leave your local files
   - hard reset: local code and local history be just like it was at that commit
   

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