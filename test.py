# import math
# import numpy as np
# import os
import string

# print(int(((2+4*6) % 4)*1+6//7+912*3*22*math.sqrt(4) +
#           int(np.array([3])+os.system("echo 2 > /dev/null"))))




class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def addNode(self,node):
        newNode = Node(node)
        currNode = self.head
        while currNode.next!=None:
            currNode = currNode.next
        currNode.next = newNode

    def display(self):
        currNode = self.head
        res = []
        while currNode.next!=None:
            currNode = currNode.next
            res.append(currNode.data)
        return res

    def delNode(self,index):
        count = 0
        currNode = self.head
        if index<0:
            print('No node at index')
            return None
        while currNode.next!=None:
            if count>index:
                print('no node at index')
                return None
            prevNode = currNode
            if count==index:
                prevNode = currNode.next
                currNode = prevNode
            else:
                currNode = prevNode.next

    def revList(self):
        currNode = self.head
        prev = None
        while currNode:
            next = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = next
        self.head = prev
        return self.head

    def getNode(self,index):
        currNode = self.head
        count = 0
        if index<0:
            print('No node at index')
            return None
        while count<index:
            currNode = currNode.next
            count+=1
        return currNode.data


myList = LinkedList()
myList.addNode('abc')
myList.addNode(23)
myList.addNode('hello')
myList.addNode([1,2,3])
myList.addNode(369)

print(myList.display())

myList.delNode(2)

print(myList.display())

print(myList.getNode(2))

myList.revList()

print(myList.display())





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
