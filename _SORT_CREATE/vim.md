# VIM COMMANDS CHEAT SHEET

### Random Useful
:put=expand('%:p'): get filepath of current buffer, copy and paste into buffer

### Navigating Code Block
ctrl-e: move viewport down one line
ctrl-y: move viewport up one line
ctrl-f: move viewport down a page
ctrl-b: move viewport up a page
H: move cursor to the top of the viewport
L: move cursor to the bottom of the viewport
zz: centers the current line on the screen
}: Move to the beginning of the next paragraph or code block.
%: Jump between matching opening and closing parentheses, brackets, or braces.
[[: Jump to the previous section of code (e.g., function definition, class declaration).
]]: Jump to the next section of code.
[m: Jump to the beginning of the previous C-style code block (e.g., if statement, loop).
]m: Jump to the end of the next C-style code block.
[(: Move to the beginning of the current function block.
]): Move to the end of the current function block.
[/: Move to the beginning of the current C-style block (e.g., block comment).
]/: Move to the end of the current C-style block.
:help motion.txt: Access the Vim documentation to explore more motion commands related to code blocks

### Code Folding
zc - Close the fold at the current cursor position.
zC - Close all folds recursively, including nested folds.
zM - Close all folds in the current buffer.
zR - Open all folds in the current buffer.
zo - Open the fold at the current cursor position.
zO - Open all folds recursively below the current cursor position.
zr - Reduce the fold level by one.
zR - Increase the fold level by one.

### TRICKS
z   q + "key" - create macro, stop recording macro
:set number!  - toggle relative line numbers

### Modes

    i - Insert mode (insert text)
    v - Visual mode (select text)
    V - Visual line mode (select entire lines)
    ctrl-v - Visual block mode (select rectangular blocks)
    : - Command-line mode (enter commands)

### Navigation

    h, j, k, l - Navigate left, down, up, right
    w, b - Navigate forward or backward by word
    0, ^, $ - Navigate to the beginning, first non-space character, or end of the line
    gg, G - Navigate to the first or last line
    :n - Navigate to line number n (eg., :42)

### Editing

    x - Delete the character under the cursor
    X - Delete the character before the cursor
    dd - Delete the current line
    D - Delete from the cursor position to the end of the line
    yy - Copy (yank) the current line
    w would 
    p, P - Paste after or before the cursor
    u - Undo the last change
    ctrl-r - Redo the last undone change
    . - Repeat the last command
    > - Shift selected text to the right (indent)
    < - Shift selected text to the left (unindent)
    

FIND: insert multiple cursors

### Search and Replace
    /pattern - Search forward for the pattern
    ?pattern - Search backward for the pattern
    n, N - Go to the next or previous match
    :%s/pattern/replacement/g - Replace all occurrences of the pattern with the replacement
    :%s/pattern/replacement/gc - Replace occurrences with confirmation
    :s/pattern/replacement - Replace the first occurrence in the current line
    :s/pattern/replacement/g - Replace all occurrences in the current line
    :g/variable_name/normal! I - Insert text at the beginning of each pattern that matches
    :%s/@.*//g - Remove all characters from the @ symbol to the end of the line for each line in file
	- :%s - substitute command for each line in the file
	- @.* pattern to match (@ is itself; .* part matches any number of chars)
	- // = reaplace the matched pattern with nothing (ie. delete it)
	- g = flag that means global
Practice Line: 
|||||||||| <<<<buffy<<<<<<<<<<<<<<<>>>>buffy>>>>>>>>>>>>>>>buffybuffy 

### Files and Buffers

    :e filename - Open a file
    :w - Save the current file
    :w filename - Save the current file as a new file
    :q - Quit Vim (fails if there are unsaved changes)
    :q! - Quit Vim without saving changes
    :wq or :x - Save and quit Vim
    :e! - Revert to the last saved version of the file
    :bn, :bp - Go to the next or previous buffer
    :bd - Close the current buffer

### Split Windows

    :sp, :vs - Split the window horizontally or vertically
    ctrl-w h, ctrl-w j, ctrl-w k, ctrl-w l - Navigate between split windows
    ctrl-w s, ctrl-w v - Split the current window horizontally or vertically

### SORTING
    :'<,'>sort	    - sort highlighted lines alphabetically based on first char of each line
    :'<,'>sort i    - sort as above but ignore case of first char
    :'<,'>sort!	    - same as above but sort reverse order 
    :'<,'>sort n    - sort numerically
    Practice:
	H
	O
	X
	122231
	848
	43
	20

	
