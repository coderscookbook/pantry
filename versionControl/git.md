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
git log

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