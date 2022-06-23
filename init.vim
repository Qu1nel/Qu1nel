" СЕТЫ <@>----------------------------------------------------------------<@>
" Прочее
set mouse=a  " Включения манипулятора типа 'мышь'
set mousehide  " Спрятать курсор мыши когда набираем текст
set scrolloff=7  " Промежуток от курсора до краёв при листании
set number  " Нумерование строк
set t_vb=  " Не пищать!
set visualbell t_vb=  " Выключаем звук в vim
set novisualbell  " Не мигать
set showtabline=1  " Вырубаем черточки на табах
set backspace=indent,eol,start, whichwrap+=<,>,[,]  " Удобное поведение backspace
set undofile  " Сохранение изменений после перезагрузки

" Кодировки
set encoding=utf-8
set termencoding=utf-8  " Кодировка терминала
set fileencodings=utf8,cp1251

" Файлы
set fileformat=unix
set noswapfile  " Без временных файлов
set nobackup


" Отступы и Оформление @ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~@
" Таб 
set tabstop=4       " \
set shiftwidth=4    " \ стандарт отступа
set softtabstop=4   " \
set smarttab
set expandtab  " Ставим табы пробелами

" Автоотступ
set autoindent  " Автоотступ
filetype indent on " Включает отступы в файлых спец. типа

" BackSpace
set nowrap
set linebreak  " Перенос по словам, а не по буквам
set formatoptions-=cro  " Отключение автокоммента новой строки

" Перед сохранением вырезаем пробелы на концах (для .py .c .cpp .cc)
autocmd BufWritePre *.py :%s/\s\+$//e
autocmd BufWritePre *.c :%s/\s\+$//e
autocmd BufWritePre *.cpp :%s/\s\+$//e
autocmd BufWritePre *.cc :%s/\s\+$//e

" Включаем 'умные' отступы после ключевых слов (для .py .c .cpp .cc)
autocmd BufRead *.py set smartindent cinwords=if,elif,else,for,while,try,except,finally,der,class
autocmd BufRead *.c set smartindent cinwords=if,else,for,while
autocmd BufRead *.cpp set smartindent cinwords=if,else,for,while
autocmd BufRead *.cc set smartindent cinwords=if,else,for,while

" Прочее
set colorcolumn=79  " Полоса *ограничения на N столбце
syntax on  " Включить подсветку синтаксиса
let python_highlight_all = 1  " Включаем подсветку всего что горит
" @ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ @


" Цвета
set t_Co=256  " Поддержка 256 цетного терминала
highlight ColorColumn ctermbg=grey
set termguicolors

" Поиск
set ic  " Игнорировать регист при поиске
set is  " Использовать инкрементальный поиск
" <@>---------------------------------------------------------------------<@>



" ПЛАГИНЫ <@>-------------------------------------------------------------<@>
call plug#begin('~/.config/nvim/plugged/')  " Путь до папки, где будут лежать плагины

" Colorschemes
Plug 'morhetz/gruvbox' " gruvbox
Plug 'ayu-theme/ayu-vim'  " ayu
Plug 'sainnhe/sonokai'  " sonokai
Plug 'cocopon/iceberg.vim' " IciBerg

" Автокомплит и LSP
Plug 'neoclide/coc.nvim', {'branch': 'release', 'do': 'yarn install --frozen-lockfile'}

" Темы для строки состояния 
Plug 'vim-airline/vim-airline'

" Автопара ковычек/скобок
Plug 'jiangmiao/auto-pairs'

" Комментирование
Plug 'tpope/vim-commentary'

" Проводник
Plug 'preservim/nerdtree'

" Иконки для проводника
Plug 'ryanoasis/vim-devicons'

" Тегбар для классов, переменных, функций
Plug 'preservim/tagbar'  " sudo apt install exuberant-ctags

" Плавная прокрутка
Plug 'yuttie/comfortable-motion.vim'

" Отображение отступов
Plug 'nathanaelkane/vim-indent-guides'

" Тема в зависимости от типа файла
Plug 'caglartoklu/ftcolor.vim'

cal plug#end()
" <@>---------------------------------------------------------------------<@>



" НАСТРОЙКИ ДЛЯ ПЛАГИНОВ <@>----------------------------------------------<@>
" Мапы плагинов @ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ @
" Для 'nerdtree'
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>

" Для 'comfortable-motion'
nnoremap <silent> <C-j> :call comfortable_motion#flick(80)<CR>
nnoremap <silent> <C-k> :call comfortable_motion#flick(-80)<CR>
nnoremap <silent> <A-m> :call comfortable_motion#flick(120)<CR>
nnoremap <silent> <A-,> :call comfortable_motion#flick(-120)<CR>

" Для 'vim-commentary'
inoremap <C-.> gcc

" Для 'tagbar'
nmap <F8> :TagbarToggle<CR>

" Для 'coc.nvim'
nmap <silent> gd <Plug>(coc-definition)

" Для 'vim-indent-guides'
map <F5> :IndentGuidesToggle<CR>
" @ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ @


" Для 'AutoPairs'
au Filetype FILETYPE let b:AutoPairs = {"(": ")", "{": "}", "[": "]"}

" Для 'comfortable-motion'
let g:comfortable_motion_scroll_down_key = "j"
let g:comfortable_motion_scroll_up_key = "k"
let g:comfortable_motion_friction = 80.0
let g:comfortable_motion_air_drag = 5.0

" Для 'ftcolor.vim'
let g:ftcolor_redraw = 1
let g:ftcolor_default_color_scheme = 'sonokai'
let g:ftcolor_color_mappings = {}
let g:ftcolor_color_mappings.python = 'gruvbox'
let g:ftcolor_color_mappings.c = 'iceberg'
let g:ftcolor_color_mappings.cpp = 'ayu'

" Тема ayu-vim
let ayucolor="mirage"  " Варианты: light, mirage, dark

" Для 'coc.nvim'
set completeopt-=preview
" <@>---------------------------------------------------------------------<@>




" МАПЫ и ГОРЯЧИЕ КЛАВИШИ <@>----------------------------------------------<@>
inoremap kj <ESC>
nnoremap ,<space> :nohlsearch<CR>
nnoremap <C-v> <ESC>"+pa <ESC>
vnoremap <C-c> "+y
inoremap <C-z> <ESC>"+ua
" <@>---------------------------------------------------------------------<@>



