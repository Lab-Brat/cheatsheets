### NvChad

#### NvChad Key Bindings
* `space -- t -- h` -> turn on built-in theme switcher
* `space -- f -- f` -> search all files in the project
* `space -- f -- b` -> search files in the buffer
* `space -- c -- h` -> open cheat sheats
* managing windows
  * `: -- vsp` -> open a new vertical window
  * `: -- sp` -> open a new horizontal window
  * `: -- q` -> close the window
* tabs
  * `Tab` -> navigate tabs
  * `Shift Tab` -> navigate tabs backwards
  * `space -- x` -> close tab
* terminal
  * `space -- v` -> vertical terminal
  * `space -- h` -> horizontal terminal


#### LunarVim Key Bindings
* `space -- e` -> file viewer
* `Ctrl -- \` -> terminal
* `Shift -- k` -> show object information
* `g -- l` -> show line error diagnostics


#### Nvim Advanced Features
* TreeSitter
  * `: -- TSInstall python` -> install treesitter syntax highliting for Python
  * `: -- TSInstallInfo` -> check all installed themes
* File viewer
  * `m` -> mark file
  * `d` -> delete file
  * `r` -> rename file
  * `c/p` -> copy/pase file
* LSP
  * `: -- LspSettings pyright` -> open (or create) pyright settings
* Trouble plugin
  * `: -- TroubleToggle` -> show all errors


#### Github Copilot
* `Alt -- l` -> accept suggestion
* `Alt -- [/]` -> previous/next suggestion
* `Ctrl -- ]` -> dismiss suggestion


#### Configuration
* `~/.config/nvim/lua/custom/` -> main configuration directory
  * `chardrc.lua` -> chad specific configurations
  * `init.lua` -> neovim configurations

