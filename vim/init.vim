set colorcolumn=
set number


call plug#begin('~/.local/share/nvim/plugged')

" Tema
Plug 'dracula/vim', { 'as': 'dracula' }

" LSP per Python
Plug 'neovim/nvim-lspconfig'

" Completamento automatico
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'

" Snippet Engine
Plug 'L3MON4D3/LuaSnip'

" Treesitter (evidenziazione avanzata)
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}

" Debugging con DAP
Plug 'mfussenegger/nvim-dap'

call plug#end()

" Abilita colori e tema
syntax enable
set termguicolors
colorscheme dracula


" Attiva il supporto LSP per Python
lua << EOF
  require('lspconfig').pyright.setup{}
EOF
