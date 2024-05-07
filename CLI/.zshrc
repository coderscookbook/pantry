source ~/.antigenrc

export PATH="$PATH"
export PATH="$HOME/bin:$PATH"
eval "$(/opt/homebrew/bin/rtx activate zsh)"

# Git###################################################################################
alias branch='git --no-pager branch'
alias git.pm='git push origin main'
alias gitPush=gitPush.zsh
function git.ac() {
    # Step 1: git add .
    git add .

    # Step 2: git status
    git status

    # Step 3: Prompt to continue
    echo -n "Do you want to continue? (y/n) "
    read response

    if [ "$response" = "y" ]; then
        # Step 4a: Ask for a commit message
        echo -n "Enter commit message: "
        read commit_message

        # Step 5: git commit
        git commit -m "$commit_message"
    elif [ "$response" = "n" ]; then
        # Step 4b: git reset and exit
        git reset
        echo "Script aborted."
    else
        echo "Invalid response. Script aborted."
    fi
}

# Goto Buffer###########################################################################
alias .vim='vim ~/projects/pantry/_SORT_CREATE/vim.md'
alias .tmux='vim ~/projects/pantry/_SORT_CREATE/tmux_commands.md'
alias .chaos='vim ~/projects/obsidian/Vault_inChaos'
alias .scripts='vim ~/.zshrc'

# Goto Projects#########################################################################
alias .z2p='vim ~/projects/zero2prod'
alias z2p='cd ~/projects/zero2prod'

# Goto Dir##############################################################################
alias .pantry='vim ~/projects/pantry'
alias pantry='cd ~/projects/pantry'
alias .inChaos='vim ~/projects/Obsidian/Vault_inChaos'
alias inChaos='cd ~/projects/Obsidian/Vault_inChaos'
alias .yeschef='vim ~/projects/MindofaChef' 
alias yeschef='cd ~/projects/MindofaChef' 
alias .py4e='vim ~/projects/PY4E' 
alias py4e='cd ~/projects/PY4E' 

# Python################################################################################
alias python=/opt/homebrew/bin/python3
alias pip=/Library/Frameworks/Python.framework/Versions/3.11/bin/pip3
alias pyd='conda deactivate'
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
#__conda_setup="$('/opt/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
#if [ $? -eq 0 ]; then
#    eval "$__conda_setup"
#else
#    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
#        . "/opt/anaconda3/etc/profile.d/conda.sh"
#    else
#        export PATH="/opt/anaconda3/bin:$PATH"
#    fi
#fi
#unset __conda_setup
# <<< conda initialize <<<

# Goto Utilities #######################################################################
alias weather='curl wttr.in/Biloxi'
alias vim=nvim
alias runEB=runEB.zsh

# TMUX##################################################################################
#alias tas='tmux attach-session'
#alias tks='tmux kill-session'
#alias tls='tmux list-sessions'
function tos() {
    # List tmux sessions
    tmux list-sessions
    # Get session input to open
    echo -n "Enter Session to Open: "
    read response
    # Open session from input
    tmux attach-session -t $response
}
function tns() {
    # List tmux sessions
    tmux list-sessions
    # Get input for new session name
    echo -n "Enter New Session Name: "
    read response
    # Create new session with input name
    tmux new-session -s $response
}
function tks(){
    # List tmux sessions
    tmux list-sessions
    # Get input for new session name
    echo -n "Enter Session to Kill: "
    read response
    # Create new session with input name
    tmux kill-session -t $response

}
# MISC###############################################################################
eval "$(~/bin/rtx activate zsh)"

test -d "$HOME/.tea" && source <("$HOME/.tea/tea.xyz/v*/bin/tea" --magic=zsh --silent)

# SCRATCH###############################################################################
#function git.ac() {
#    # Step 1: git add .
#    git add .
#
#    # Step 2: git status
#    git status
#
#    # Step 3: Prompt to continue
#    read -p "Do you want to continue? (y/n) " response
#
#    if [[ "$response" == "y" ]]; then
#        # Step 4a: Ask for a commit message
#        read -p "Enter commit message: " commit_message
#
#        # Step 5: git commit
#        git commit -m "$commit_message"
#    elif [[ "$response" == "n" ]]; then
#        # Step 4b: git reset and exit
#        git reset
#        echo "Script aborted."
#    else
#        echo "Invalid response. Script aborted."
#    fi
#}

# Example usage:
# Type 'git-add-commit' in your terminal to run this script.



