set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.

" plugin on GitHub repo
" Plugin 'tpope/vim-fugitive'

" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'

" Git plugin not hosted on GitHub
" Plugin 'git://git.wincent.com/command-t.git'

" git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'

" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
" Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}

" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

" PEP8 formatting for python files
Plugin 'Vimjas/vim-python-pep8-indent'

" Auto-formatting for many file types
Plugin 'Chiel92/vim-autoformat'

" Use eye-friendly colors
Plugin 'altercation/vim-colors-solarized'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line


" Highlight the search term when you search for it, but don't highlight
" just because we've sourced vimrc
set hlsearch
let @/ = ""

" Expand tabs into spaces on insert
set expandtab

" Set tabstop to be size 4
set ts=4

" Set shiftwidth to 4 to match tabstop
set sw=4

" Enable syntax highlighting
syntax on

" Show line numbers
set number

" Allow arrow keys to wrap around lines
set whichwrap+=<,>,[,]

" Always show statusline
set laststatus=2

" Use 256 colours (Use this setting only if your terminal supports 256 colours)
set t_Co=256

" Show when the leader key is active
set showcmd

" Automatically enter INSERT mode when opening a new file
autocmd BufNewFile * startinsert

" Automatically enter INSERT mode when editing a git commit message
autocmd BufReadPost *COMMIT_EDITMSG* startinsert

" use » to mark Tabs and ° to mark trailing whitespace. This is a
" non-obtrusive way to mark these special characters.
set list listchars=tab:»\ ,trail:°

" Remap shift-k to do nothing
nnoremap <s-k> <Nop>

" Explicitly set the Leader to comma. You can use '\' (the default),
" or anything else (some people like ';').
let mapleader=','

" Use Shift-Enter to toggle between normal and insert mode
inoremap <S-CR> <Esc>
nnoremap <S-CR> a

" Use semi-colon as an alternative to colon for commands
nmap ; :
vmap ; :

" Use a double semi-colon to get an actual semi-colon
noremap ;; ;

" Use F3 to initiate auto-formatting
noremap <F3> :Autoformat<CR>

" Use better contrast color scheme
" let g:solarized_termcolors=16
" let g:solarized_contrast="high"
set background=dark
" colorscheme solarized

