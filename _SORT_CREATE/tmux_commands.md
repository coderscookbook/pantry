# TMUX COMMANDS

## Command Line
All scripts in the '.scripts' command in the tmux section
tos	tmux open session
tns	tmux new session
tks	tmux kill session

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

## All Commands
attach-session       attach                   -- attach or switch to a session
bind-key             bind                     -- bind a key to a command
break-pane           breakp                   -- break a pane from an existing into a new window
capture-pane         capturep                 -- capture the contents of a pane to a buffer
choose-buffer                                 -- put a pane into buffer choice mode
choose-client                                 -- put a window into client choice mode
choose-tree                                   -- put a window into tree choice mode
clear-history        clearhist                -- remove and clear history for a pane
clock-mode                                    -- enter clock mode
command-prompt                                -- open the tmux command prompt in a client
confirm-before       confirm                  -- run a command but ask for confirmation before
copy-mode                                     -- enter copy mode
customize-mode                                -- enter customize mode
delete-buffer        deleteb                  -- delete a paste buffer
detach-client        detach                   -- detach a client from the server
display-menu         menu                     -- display a menu
display-message      display                  -- display a message in the status line
display-panes        displayp                 -- display an indicator for each visible pane
display-popup        popup                    -- display a popup box over a pane
find-window          findw                    -- search for a pattern in windows
has-session          has                      -- check and report if a session exists on the server
if-shell             if                       -- execute a tmux command if a shell-command succeeded
join-pane            move-pane  joinp  movep  -- split a pane and move an existing one into the new space
kill-pane            killp                    -- destroy a given pane
kill-server                                   -- kill clients, sessions and server
kill-session                                  -- destroy a given session
kill-window          killw                    -- destroy a given window
last-pane            lastp                    -- select the previously selected pane
last-window          last                     -- select the previously selected window
link-window          linkw                    -- link a window to another
list-buffers         lsb                      -- list paste buffers of a session
list-clients         lsc                      -- list clients attached to server
list-commands        lscm                     -- list supported sub-commands
list-keys            lsk                      -- list all key-bindings
list-panes           lsp                      -- list panes of a window
list-sessions        ls                       -- list sessions managed by server
list-windows         lsw                      -- list windows of a session
load-buffer          loadb                    -- load a file into a paste buffer
lock-client          lockc                    -- lock a client
lock-server          lock                     -- lock all clients attached to the server
lock-session         locks                    -- lock all clients attached to a session
move-window          movew                    -- move a window to another
new-session          new                      -- create a new session
new-window           neww                     -- create a new window
next-layout          nextl                    -- move a window to the next layout
next-window          next                     -- move to the next window in a session
paste-buffer         pasteb                   -- insert a paste buffer into the window
pipe-pane            pipep                    -- pipe output from a pane to a shell command
previous-layout      prevl                    -- move a window to the previous layout
previous-window      prev                     -- move to the previous window in a session
refresh-client       refresh                  -- refresh a client
rename-session       rename                   -- rename a session
rename-window        renamew                  -- rename a window
resize-pane          resizep                  -- resize a pane
resize-window        resizew                  -- resize a window
respawn-pane         respawnp                 -- reuse a pane in which a command has exited
respawn-window       respawnw                 -- reuse a window in which a command has exited
rotate-window        rotatew                  -- rotate positions of panes in a window
run-shell            run                      -- execute a command without creating a new window
save-buffer          saveb                    -- save a paste buffer to a file
select-layout        selectl                  -- choose a layout for a pane
select-pane          selectp                  -- make a pane the active one in the window
select-window        selectw                  -- select a window
send-keys            send                     -- send key(s) to a window
send-prefix                                   -- send the prefix key to a window
server-info          info                     -- show server information
set-buffer           setb                     -- set contents of a paster buffer
set-environment      setenv                   -- (un)set an environment variable
set-hook                                      -- set a hook to a command
set-option           set                      -- set a session option
set-window-option    setw                     -- set a window option
show-buffer          showb                    -- display the contents of a paste buffer
show-environment     showenv                  -- display the environment
show-hooks                                    -- show the global list of hooks
show-messages        showmsgs                 -- show client's message log
show-options         show                     -- show session options
show-window-options  showw                    -- show window options
source-file          source                   -- execute tmux commands from a file
split-window         splitw                   -- splits a pane into two
start-server         start                    -- start a tmux server
suspend-client       suspendc                 -- suspend a client
swap-pane            swapp                    -- swap two panes
swap-window          swapw                    -- swap two windows
switch-client        switchc                  -- switch the client to another session
unbind-key           unbind                   -- unbind a key
unlink-window        unlinkw                  -- unlink a window
wait-for             wait                     -- wait for an event or trigger it

