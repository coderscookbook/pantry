# TMUX COMMANDS

## Sessions
tmux
tmux new -s SESSION_NAME
tmux attach #
tmux aattach -t SESSION_NAME
tmux ls 
exit or Ctrl+D
tmux kill-session -t SESSION_NAME
tmux list-sessions

## Windows (<prefix> + __)
- c = new window
- w = list windows
- n = next window
- p = previous window
- f = find window
- , = create/edit a window's name
- & = close window
- d = detach session

## Panes
- % = split pane vertically
- " = split pane horizontally
- q = show pane's number
- arrow key or o = switch panes
- x = delete pane and then confirm with Y or N
- Alt/Opt + arrow keys = resize pane

## Workflow
- tmux attach-session -t SESSION_NAME
- tmux switch-client -t SESSION_NAME
