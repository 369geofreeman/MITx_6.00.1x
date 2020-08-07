# import math
# import numpy as np
# import os
import string

# print(int(((2+4*6) % 4)*1+6//7+912*3*22*math.sqrt(4) +
#           int(np.array([3])+os.system("echo 2 > /dev/null"))))





a = '123'
b = '123123'
c = '123123123'


print(c.replace('1', ''))








# set nocompatible              " required
# filetype off                  " required

# " set the runtime path to include Vundle and initialize
# set rtp+=~/.vim/bundle/Vundle.vim
# call vundle#begin()

# " alternatively, pass a path where Vundle should install plugins
# "call vundle#begin('~/some/path/here')

# " let Vundle manage Vundle, required
# Plugin 'gmarik/Vundle.vim'

# " add all your plugins here (note older versions of Vundle
# " used Bundle instead of Plugin)

# " ...

# " All of your Plugins must be added before the following line
# call vundle#end()            " required
# filetype plugin indent on    " required

# au BufNewFile,BufRead *.py
#     \ set tabstop=4
#     \ set softtabstop=4
#     \ set shiftwidth=4
#     \ set textwidth=79
#     \ set expandtab
#     \ set autoindent
#     \ set fileformat=unix

# au BufNewFile,BufRead *.js, *.html, *.css
#     \ set tabstop=2
#     \ set softtabstop=2
#     \ set shiftwidth=2

# set encoding=utf-8

# au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

# let g:ycm_autoclose_preview_window_after_completion=1
# map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

# "python with virtualenv support
# py3 3
# py3 << EOF
# import os
# import sys
# if 'VIRTUAL_ENV' in os.environ:
#   project_base_dir = os.environ['VIRTUAL_ENV']
#   activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
#   execfile(activate_this, dict(__file__=activate_this))
# EOF

# let python_highlight_all=1
# syntax on

# if has('gui_running')
#   set background=dark
#   colorscheme solarized
# else
#   colorscheme slate
# endif
# set backspace=indent,eol,start
# set nu
# set clipboard=unnamed

# Plugin 'vim-scripts/indentpython.vim'
# Plugin 'vim-syntastic/syntastic'
# Plugin 'nvie/vim-flake8'
# Plugin 'altercation/vim-colors-solarized'
# Plugin 'scrooloose/nerdtree'
# Plugin 'jistr/vim-nerdtree-tabs'
# Plugin 'tpope/vim-fugitive'
# Plugin 'kien/ctrlp.vim'
# Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
# Bundle 'Valloric/YouCompleteMe'
