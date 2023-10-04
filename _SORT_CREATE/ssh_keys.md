# cli commands for creating ssh keys/connections
# create ssh key for Azure DevOps account
# followed github ssh keys directions
1. ssh -T git@github.com
2. ssh-keygen -t ed25519 -C <email address>
3. eval "$(ssh-agent -s)"
4. open ~/.ssh/config
    - if need to create one
        - touch ~/.ssh/config
    - if existing, add:


Host github.com
AddKeysToAgent yes
IdentityFile ~/.ssh/id_ed25519


5. ssh-add ~/.ssh/id_ed25519
6. pbcopy < ~/.ssh/id_ed25519.pub