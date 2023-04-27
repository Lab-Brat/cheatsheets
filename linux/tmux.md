### tmux

#### Basic Key Bindings
`prefix` is usually `Ctrl + b`, 
but can be changed to anything else (`Ctrl + Space` in my case).

* sessions
  * `tmux` -> create and enter a new session
  * `tmux new -s new-session` -> create a named session
  * `tmux ls` -> list current sessions
  * `tmux attach` -> attach most recent session
  * `tmux attach -t test-session` -> attach a specified session
  * `prefix -- d` -> detach session
  * `prefix -- s` -> list all sessions from within a session
  * `prefix -- w` -> preview session windows
* windows
  * `prefix -- c` -> launch a new window
  * `prefix -- <window number>` -> switch windows
  * `prefix -- n` -> next window
  * `prefix -- p` -> previous window
  * `prefix -- &` -> close window
* panes
  * `prefix -- %` -> split vertically
  * `prefix -- "` -> split horizontally
  * `prefix -- <v^>` -> use arrows to switch between panes
  * `prefix -- q` -> show pane numbers
  * `prefix -- z` -> zoom selected pane
  * `prefix -- x` -> close pane
* misc
  * `prefix -- I` -> install tmux plugins

