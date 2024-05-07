# https://medium.com/@ishahmeer/20-git-commands-that-will-make-you-a-version-control-pro-1481a55c37b1

git init
git add origin <url>
git status
git add 
  .
git commit
  -m "<message>"
git push
  -u 
git branch
git checkout
git fetch
git merge
git pull
git stash
  stash pop
git reset
git revert

git log                                                         Display the basic commit history.
  - git log --oneline                                           Show a compact, one-line summary of each commit.
  - git log --graph                                             Visualize the commit history as an ASCII art graph.
  - git log --abbrev-commit                                     Show abbreviated SHA-1 hashes in the log.
  - git log --pretty=format"%h %an <%ae> %s"                    Include the author's name and email in the log.
  - git log --author="AuthorName"                               Show commits by a specific author.
  - git log branch_name                                         Display commits only in a specific branch.
  - git log -- <file_path>                                      List all commits that modified a specific file.
  - git log --color                                             Add color to the log for better readability.
  - git log --grep="keyword"                                    Search commit messages for a keyword.
  - git log -n 10                                               Limit the display to a specific number of recent commits (e.g., -n 10 shows the last 10 commits)
  - git log --pretty=format"%h %ad | %s%d [%an]" --date=short   Display commit dates in a custom format.

Scenario: You want Branch_B to make an exact copy of Branch_A
- git checkout Branch_B
- git reset --hard Branch_A

Scenario: Rename an existing branch
- git checkout Branch_B
- git branch -m B_Branch
- git push origin B_Branch

Scenario: set global defaultBranch name
- git config --global init.defaultBranch <name>
- git branch -m <name>

Scenario: create new repo
echo "# pantry" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin <remote repo url>
- git push -u origin main

Scenario: You want to push an existing local repo to a remote repo 
- git remote add origin <remote repo url>
- git branch -M main
- git push -u origin main

Scenario: Bring down a remote branch into local branch
- git fetch origin
- git checkout remote-branch-name OR git switch remote-branch-name
OR
- git checkout -b <local_branch_name> <remote>/<remote_branch_name>
- git checkout -b feature origin/feature

SCENARIO: You want to bring a branch from one repo into another repo
- git clone <destination_repo_url>
- cd <destination_repo_name>
- git remote add source_repo <source_repo_url>
- git fetch source_repo feature:feature
- git checkout feature

# GIT DIFF
git diff -u (meld, vimdiff, KDiff3)
