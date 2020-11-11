
                                     # ---- [KEYBINDINGS] ---- #
                                

               [< GO BACK](index.md)

# -- [ I3 ] -- #

| ------------------------ | ------------------------------------- | ---------------------------- | -------------------- |
<tb| I3                       |                                       | Client                       |                      |>
|--------------------------|---------------------------------------|------------------------------|----------------------|
|                          |                                       |                              |                      |
| Meta+x                   | Exit Menu                             | Meta+c                       | Kill Client          |
| Meta+Shift+r             | Reload Configuration                  | Meta+f                       | Fullscreen           |
| Print                    | Take Screenshot                       | Meta+q                       | Focus Parent         |
|                          |                                       | Meta+a                       | Focus Child          |
|                          |                                       |                              |                      |
| ------------------------ | ------------------------------------- | ---------------------------- | -------------------- |
<tb| Launcher                 |                                       | Screen                       |                      |>
| ------------------------ | ------------------------------------- | ---------------------------- | -------------------- |
|                          |                                       |                              |                      |
| Meta+Return              | Terminal                              | Meta+h                       | Focus Left           |
| Meta+d                   | Rofi run                              | Meta+l                       | Focus Right          |
| Meta+w                   | Rofi win                              | Meta+k                       | Focus Up             |
| Meta+Shift+F10           | Firefox PN                            | Meta+j                       | Focus Down           |
|                          |                                       | Meta+Shift+h                 | Previous Workspace   |
|                          |                                       | Meta+Shift+l                 | Next Workspace       |
|                          |                                       | Meta+[1-9]                   | Focus [1 - 9]        |
|                          |                                       |                              |                      |
| ------------------------ | ------------------------------------- | ---------------------------- | -------------------- |
<tb| Layout                   |                                       | Container                    |                      |>
| ------------------------ | ------------------------------------- | ---------------------------- | -------------------- |
|                          |                                       |                              |                      |
| Meta+s                   | Layout stacking                       | Meta+Shift+h                 | Move Left            |
| Meta+z                   | Layout tabbed                         | Meta+Shift+l                 | Move Right           |
| Meta+Shift+s             | Toggle Sticky when windows floating   | Meta+Shift+j                 | Move Down            |
| Meta+e                   | Toggle Split                          | Meta+Shift+k                 | Move Up              |
| Meta+Tab                 | Toggle Floating                       | Meta+Shift+[1-9]             | Move to WS[1-9]      |
| Meta+Space               | Swap                                  | Meta+Ctrl+Left               | Move to left Screen  |
|                          |                                       | Meta+Ctrl+Right              | Move to right screen |
|                          |                                       | Meta+h                       | Split horizontally   |
|                          |                                       | Meta+v                       | Split vertically     |
|                          |                                       | Meta+Escape                  | Switch back & forth  |
|                          |                                       | Meta+n                       | Move to scratchpad   |
|                          |                                       | Meta+Shift+n                 | Show Scratchpad      |
| ------------------------ | ------------------------------------- | ---------------------------- | -------------------- |

# -- [ VIM ] -- #

| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
<tb|        Action            |                                    |     Navigation                 |                                           |>
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
| g/text/                  | Show All lines with text           | h                              | Move left                                 |
| /pattern                 | Search forward pattern             | k                              | Move Up                                   |
| ?pattern                 | Search backward pattern            | j                              | Move Down                                 |
| *                        | Search words under the cursor      | l                              | Move Right                                |
| [I                       | Show lines with matching words     | w                              | Next word                                 |
| noh                      | Remove highlighting                | e                              | End of word                               |
| R / r                    | ReplaceMode / Replace char         | b / B                          | Previous word / WORD                      |
| > / <                    | Indent / Unindent                  | 0                              | Start of line                             |
| di(                      | Delete everything between ()       | $                              | End of line                               |
| Ctrl+r + (insert mode)   | Paste clipboard content            | gg/ G                          | Begin of file / End of file               |
| Ctrl+v                   | Visual Block                       | CTRL + ]                       | Jump to quickref help                     |
| 3p                       | Paste 3 Times                      | CTRL + O                       | Jump older location                       |
| ciw                      | Change Inner word                  | :vert help                     | Help in vertical mode                     |
| di                       | Delete everything in parenthesis   |                                |                                           |
| Yiw                      | Copy inner word                    |                                |                                           |
| :g/^#/d                  | Remove all commented lines         |                                |                                           |
| :g/^$/d                  | Remove all blank lines             |                                |                                           |
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
<tb|       Navigation         |                                    |        Tabs / Windows          |                                           |>
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
| (                        | Start of sentence                  | :tabnew <file>                 | Opening file in a new tab                 |
| )                        | End of sentence                    | :tabnext                       | Next Tab                                  |
| {                        | Start of paragraph                 | :tabprev                       | Previous Tab                              |
| }                        | End of paragraph                   | :tab h cmd                     | Open new help tab                         |
| H/L/M                    | Move to top/Bottom/Middle          | :vert help cmd                 | New help on vertical window               |
| %                        | Next bracket                       | Ctrl+ww                        | Switch window                             |
| :N                       | Goto N line                        | gt/gT/#gt                      | Tab Next/Prev/Tab#                        |
| Ctrl + e/y               | Go down / Go up                    |                                |                                           |
| zj / zk                  | Prev / Next fold                   |                                |                                           |
|                          |                                    |                                |                                           |
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
<tb|       Search             |                                    |        Marks                   |                                           |>
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
|                          |                                    |                                |                                           |
| %s/pattern/foo           | Change all pattern / foo           | m[a-z]                         | Create Mark                               |
| %s/pattern/foo/c         | Change all pattern / foo with conf | '[a-z]                         | Jump to Mark                              |
| %s/pattern/foo/g         | Change all occurence               | '[A-Z]                         | Jump to mark over the files               |
| n / N                    | Next Search Match /Prev Search     |                                |                                           |
|                          |                                    |                                |                                           |
|                          |                                    |                                |                                           |
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
<tb|       Fold               |                                    |        Other CMD               |                                           |>
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
|                          |                                    |                                |                                           |
| setlocal foldmethod=expr | Fold(hide)  Expr:syntax/indent/... | :htp                           | Show Runtimepath                          |
|                          |                                    | :ls                            | List all Buffer                           |
|                          |                                    | :tab h helpgrep conceal        | Summarize of conceal                      |
|                          |                                    | :!make -j8                     | execute Shell Command                     |
|                          |                                    | :set nornu                     | Disable relative number                   |
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
<tb|     Buffer               |                                    |        Other CMD               |                                           |>
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
|                          |                                    |                                |                                           |
| :buffer <nb>             | Switch to buffer <nb>              |                                | Show Runtimepath                          |
| :ls                      | List all buffer                    |                                | List all Buffer                           |
| :b <TAB>                 | Switch between buffer with TAB     |                                | Summarize of conceal                      |
| :bd                      | Delete Buffer                      |                                | execute Shell Command                     |
| :bw                      | Write buffer  and close            |                                |                                           |
| ------------------------ | ---------------------------------- | ------------------------------ | ----------------------------------------- |
                 
	 ## COMMANDS ##
		:scriptnames					List all scripts installed
    
# --[ W3M ]-- #

|----------------------|------------------------------------------------|-------------------------|----------------------------------|
<tb| Page / Cursor motion |                                                | Page / Cursor Motion    |                                  |>
|----------------------|------------------------------------------------|-------------------------|----------------------------------|
|                      |                                                |                         |                                  |
| ESC + t              | Select Tab                                     | Shift + t               | Open a new tab                   |
| Shift + b            | Go back                                        | s                       | Select buffer / historic         |
| Shift +h             | Help with keybinding                           | Shift + u               | Goto URL                         |
| ESC + l              | Popup linklist                                 | ESC+t                   | Popup Tab selection              |
| { / }                | Previous / Next tab                            | $,C-e                   | Go to the end of line            |
| Ctrl + q             | Close current Tab                              | w                       | Go to next word                  |
| Ctrl + t             | Open link in a new tab                         | W                       | Go to previous word              |
| h,C-b                | Cursor left                                    | >                       | Shift screen right               |
| j,C-n                | Cursor down                                    | <                       | Shift screen left                |
| k,C-p                | Cursor up                                      | .                       | Shift screen one column right    |
| J                    | Roll up one line                               | ,                       | Shift screen one column left     |
| K                    | Roll down one line                             | g,M-<                   | Go to the first line             |
| ^,C-a                | Go to the beginning of line                    | G,M->                   | Go to the last line              |
| ESC g                | Goto to specified line                         | Z / z                   | Move to center line / column     |
| TAB                  | Move to next Hyperlink                         | C-u / ESC TAB           | Move to previous hyperlink       |
| [ / ]                | Move to first hyperlink / end                  |                         |                                  |
|                      |                                                |                         |                                  |
| -------------------- | ---------------------------------------------- | ----------------------- | -------------------------------- |
<tb| Search               |                                                | Mark operation          |                                  |>
|----------------------|------------------------------------------------|-------------------------|----------------------------------|
|                      |                                                |                         |                                  |
| /,C-s                | Search forward                                 | C-SPC                   | Set/unset mark                   |
| ?,C-r                | Search backward                                | ESC p                   | Go to previous mark              |
| n                    | Search next                                    | ESC n                   | Go to next mark                  |
| N                    | Search previous                                | "                       | Mark by regular expression       |
| C-w                  | Toggle wrap search mode                        |                         |                                  |
|                      |                                                |                         |                                  |
|----------------------|------------------------------------------------|-------------------------|----------------------------------|
<tb| Hyperlink operation  |                                                | File / Stream operation |                                  |>
|----------------------|------------------------------------------------|-------------------------|----------------------------------|
|                      |                                                |                         |                                  |
| RET                  | Follow hyperlink                               | U                       | Open URL                         |
| a, ESC RET           | Save link to file                              | V                       | View new file                    |
| u                    | Peek link URL                                  | @                       | Execute shell command and load   |
| i                    | Peek image URL                                 | #                       | Execute shell command and browse |
| I                    | View inline image                              |                         |                                  |
| ESC I                | Save inline image to file                      |                         |                                  |
| :                    | Mark URL-like strings as anchors               | ESC b                   | Load bookmark                    |
| ESC :                | Mark Message-ID-like strings as news anchors   | ESC a                   | Add current to bookmark          |
| c                    | Peek current URL                               |                         |                                  |
| =                    | Display information about current document     |                         |                                  |
| C-g                  | Show current line number                       |                         |                                  |
| C-h                  | View history of URL                            |                         |                                  |
| F                    | Render frame                                   |                         |                                  |
| M                    | Browse current document using external browser |                         |                                  |
| ESC M                | Browse link using external browser             |                         |                                  |
|                      |                                                |                         |                                  |
| -------------------- | ---------------------------------------------- | ----------------------- | -------------------------------- |
<tb| Buffer operation     |                                                | Buffer selection mode   |                                  |>
|----------------------|------------------------------------------------|-------------------------|----------------------------------|
|                      |                                                |                         |                                  |
| B                    | Back to the previous buffer                    | k, C-p                  | Select previous buffer           |
| v                    | View HTML source                               | j, C-n                  | Select next buffer               |
| s                    | Select buffer                                  | D                       | Delect current buffer            |
| E                    | Edit buffer source                             | RET                     | Go to the selected buffer        |
| C-l                  | Redraw screen                                  |                         |                                  |
| R                    | Reload buffer                                  |                         |                                  |
| S                    | Save buffer                                    |                         |                                  |
| ESC s                | Save source                                    |                         |                                  |
| ESC e                | Edit buffer image                              |                         |                                  |
|                      |                                                |                         |                                  |
| -------------------- | ---------------------------------------------- | ----------------------- | -------------------------------- |

# -- [ VIMWIKI ] -- #
            
                    ## KEYBINDINGS ##

                        [[  :							Go to Previous header
                        ]]  :							Go to Next Header
                        [=  :							Go to Previous header which has the same level
                        ]=	:						Go to Next header which has the same level
                        \ww : 							Open default wiki index file
                        \wt :							Open default wiki in newtab
                        \ws : 							Select and open wiki indexfile
                        \wr : 							Delete wiki file
                        \wd :							Delete wiki file you are in
                        :VWS   <term to search>                                 Search term in all wiki pkages
                        :lopen                                                  See all results
                        <Tab> \ <Shift - Tab> :					Find Next wiki link / Previous link
                        {{local:Book/wxWidget.pdf}}                             Create Link for local file
                        
                   ## TODOLIST ##

                        1. [INSERT MODE]				Write - Your task
                        2. [NORMAL MODE]				CTRL + Space  Create Checkbox / Toggle ON/OFF
                        3. remove CheckBox				glSpace
                        4. Inc / Dec Percent				gln / glp
                         
                   ## LIST ## 

                        1. [INSERT MODE]				<t1Write 1.  Don't forget the space>
                        *								<t1You can create Buble list like this>
                          
                   ## TABLE ##

                                :VimwikiTable 5 3			<t1Create a table with 5 columnns and 3 rows>

                   ## LINKS ##
                   
                        1. [INSERT MODE] <Your Link Name>
                        2. [NORMAL MODE] <Enter> to create link

                   ## COMMANDS ###

                                :Vimwiki2HTML				<t1Convert current wiki link to HTML>
                                :VimwikiAll2HTML			<t1Convert all link to HTML>


                   ## INSERT CODE ##
                                ```cpp
                                ```sh
                                ```python
                                ```java
                                                Yourcode
                                ```

# -- [ QUTEBROWSER ] -- #
                
                yy                              Copy the current URL
                yT                              Copy the title 
                :config-source                  to update config file(theme) 
                f                               show link
                h/l                             Youtube 5s backward / forward
                m                               Add bookmark
                pp                              Open URL from clipboard
                Alt + num                       Go to tab n
                Ctrl + Tab                      Switch between two tabs
                Ctfl + f                        Scroll page down
                Ctrl + b                        Scroll page up
                wi                               Open Inspector
                
                :reload force (shift-R)         Reload page
        
# -- [ ROFI ] -- # 

        Switching in combi mode         ->              Ctrl + Tab
        Delete entry from history       ->              Shift + Del 
        
        
