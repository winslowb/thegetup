# Friday, Oct 27 2023 
Nice things for neovim is stuff configured for the edge2 when i fucking destroyed awsjson misc and other fuckin super neceessary stuff. i really fucked myself but was able to salvage stuff.
___

## lua stuff

    -- nvim  
        |-- init.lua
        |-- lazy-lock.json
        `-- lua
            |-- alpha-config.lua
            |-- bufferline-config.lua
            |-- gruvbox.lua.old
            |-- keymap.lua
            |-- lazy-config.lua
            |-- lsp-config.lua
            |-- lualine-config.lua
            |-- neorg-conf.lua
            |-- options.lua
            |-- plugins.lua
            |-- telescope-config.lua
            |-- toggleterm-config.lua
            |-- treesitter-config.lua
            `-- whichkey.lua
___

### init.lua

        vim.g.mapleader = "," -- set space as the leader key
        vim.g.maplocalleader = " " -- set comma as the local leader key

        -- Markdown folding
        vim.g.markdown_folding = 3
        -- Clipboard operations
        vim.api.nvim_set_keymap('n', '<Leader>c', '"+y', { noremap = true, silent = true })
        vim.api.nvim_set_keymap('n', '<Leader>p', '"+p', { noremap = true, silent = true })

        -- Misc stuff
        vim.opt.swapfile = false

        -- Set filetype to JSON and enable syntax folding
        --vim.api.nvim_set_keymap('n', '<leader>f', [[<Cmd>set filetype=json <bar> syntax on <bar> set fdm=syntax<CR>]], { noremap = true, silent = true })

        require "alpha-config"
        require "bufferline-config"
        require "keymap"
        require "lazy-config"
        require "lsp-config"
        require "lualine-config"
        require "options" 
        require "telescope-config"
        require "toggleterm-config"
        require "treesitter-config"
        require "whichkey"
        
        -- require "NERDTree-conf" 
        -- require "gruvbox"
        -- require "neorg-conf"
        -- require "nvim-cmp"
        -- require "vimwiki"

### lua config stuff
- for what ever reason the gruvbox theme stopped working and required shit ton of options in the *options.lua file*

--- Plugins.lua file  
return {
-- webdev icons
{
 	"nvim-tree/nvim-web-devicons",
 	},
-- Which-key Extension
{ 
	"folke/which-key.nvim",
      lazy = true,
	},
--Neo Tree
{
	"nvim-neo-tree/neo-tree.nvim"
	},
-- Colorscheme
 { 
 	"ellisonleao/gruvbox.nvim", 
 			priority = 1000, 
 	},
-- bufferline stuff...up at top
{
  "akinsho/bufferline.nvim",
-- 			dependencies = 'nvim-tree/nvim-web-devicons',
  },
--lua line stuff at the bottome
{
	"nvim-lualine/lualine.nvim",
--			dependencies = { 'nvim-tree/nvim-web-devicons' },
	}, 
--lsp 
{
	"neovim/nvim-lspconfig",
	},
-- lsp-zero for lsp  plugin			
{
	"VonHeikemen/lsp-zero.nvim",
	},
-- Alpha (Dashboard)
{
   "goolord/alpha-nvim",
			lazy = true,
	},
-- Telescope (Fuzzy Finder)
{
	"nvim-telescope/telescope.nvim",
			lazy = true,
			dependencies = {
					{'nvim-lua/plenary.nvim'},
			}
	},
-- Treesitter
{
	"nvim-treesitter/nvim-treesitter",
    	},
{
	"hrsh7th/nvim-cmp",
		},
-- Table Mode
{ 
	"dhruvasagar/vim-table-mode",
    	},
 -- vimwiki
{
	"vimwiki/vimwiki",
    	},
-- tpope's markdown stuff
{
	"tpope/vim-markdown"
	    },
-- Toggle Term
{
	"akinsho/toggleterm.nvim",
			version = "*",
			config = true
    },
-- Jack Mort ChatGPT
{
	"jackMort/ChatGPT.nvim",
			event = "VeryLazy",
			config = function()
				require("chatgpt").setup()
			end,
			dependencies = {
				"MunifTanjim/nui.nvim",
				"nvim-lua/plenary.nvim",
				"nvim-telescope/telescope.nvim"
			},
		},
{
	"nvim-neorg/neorg",
			build = ":Neorg sync-parsers",
			dependencies = { "nvim-lua/plenary.nvim" },
			config = function()
      require("neorg").setup {
									load = {
					-- [" " ] = {},
							["core.defaults"] = {}, -- Loads default behaviour
							["core.concealer"] = {}, -- 
							["core.autocommands"] = {}, --
							["core.completion"] = {}, -- works with completion
							["core.completion"] = {
								config = {
									engine = "nvim-cmp",
									},
								}, -- 
							["core.esupports.hop"] = {},
							["core.esupports.indent"] = {},
							["core.esupports.metagen"] = {},
							["core.export"] = {}, -- 
							["core.export.markdown"] = {}, -- core.integrations.treesitter
							["core.integrations.treesitter"] = {}, -- 
							["core.mode"] = {}, --  requirements for treesitter
							["core.highlights"] = {}, -- requirements for treesitter
							["core.summary"] = {}, -- 
							["core.dirman"] = { -- Manages Neorg workspaces
								config = {
									workspaces = {
										notes = "$HOME/norg",
										bill = "$HOME/norg/bill",
										work = "$HOME/norg/work",
								},
										default_workspace = "work"
							},
						},
					},
				}
			end,
		},
}

###
--  options.lua
*line 253 starts the options the the gruvbox theme*

local opt = vim.opt
opt.autowrite = true -- Enable auto write
opt.breakindent = true
opt.clipboard = "unnamedplus" -- Sync with system clipboard
opt.completeopt = "menu,menuone,noselect"
opt.conceallevel = 2 -- Hide * markup for bold and italic
opt.confirm = true -- Confirm to save changes before exiting modified buffer
opt.cursorline = true -- Enable highlighting of the current line
opt.expandtab = false
opt.expandtab = true -- Use spaces instead of tabs
opt.formatoptions = "jcroqlnt" -- tcqj
opt.grepformat = "%f:%l:%c:%m"
opt.grepprg = "rg --vimgrep"
opt.ignorecase = true
opt.inccommand = "nosplit" -- preview incremental substitute
opt.incsearch = true
opt.laststatus = 0
opt.linebreak = true
opt.list = false -- Show some invisible characters (tabs...
opt.mouse = "" -- Enable mouse mode
opt.number = true -- Print line number
opt.paste = true
opt.pumblend = 10 -- Popup blend
opt.pumheight = 10 -- Maximum number of entries in a popup
opt.relativenumber = true
opt.relativenumber = true -- Relative line numbers
opt.scrolloff = 5 -- Lines of context
opt.sessionoptions = { "buffers", "curdir", "tabpages", "winsize" }
opt.shiftround = true -- Round indent
opt.shiftwidth = 2
opt.shortmess:append { W = true, I = true, c = true }
opt.showmode = false -- Dont show mode since we have a statusline
opt.sidescrolloff = 8 -- Columns of context
opt.signcolumn = "yes" -- Always show the signcolumn, otherwise it would shift the text each time
opt.smartcase = true -- Don't ignore case with capitals
opt.smartindent = true
opt.smartindent = true -- Insert indents automatically
opt.spelllang = { "en" }
opt.splitbelow = true -- Put new windows below current
opt.splitright = true -- Put new windows right of current
opt.tabstop = 2 -- Number of spaces tabs count for
opt.termguicolors = true -- True color support
opt.timeoutlen = 150
opt.undofile = true
opt.undolevels = 10000
opt.updatetime = 200 -- Save swap file and trigger CursorHold
opt.wildmode = "longest:full,full" -- Command-line completion mode
opt.winminwidth = 5 -- Minimum window width
opt.wrap = true

-- Fix markdown indentation settings
vim.g.markdown_recommended_style = 0

vim.o.background = 'dark'
-- Default options:
require("gruvbox").setup({
  terminal_colors = true, -- add neovim terminal colors
  undercurl = true,
  underline = true,
  bold = true,
  italic = {
    strings = true,
    emphasis = true,
    comments = true,
    operators = false,
    folds = true,
  },
  strikethrough = true,
  invert_selection = false,
  invert_signs = false,
  invert_tabline = false,
  invert_intend_guides = false,
  inverse = true, -- invert background for search, diffs, statuslines and errors
  contrast = "", -- can be "hard", "soft" or empty string
  palette_overrides = {},
  overrides = {},
  dim_inactive = false,
  transparent_mode = false,
})
vim.cmd("colorscheme gruvbox")


-- a function to save buffers w/o file names to a temp directory, until the buffer is written to a file
-- vim.api.nvim_exec([[
--  function! AutoSaveToTempDir()
--    if @% == ""
--      write! $HOME/unsaved_buffer/buffer
--    else
--      write
--    endif
--  endfunction

 -- autocmd CursorHold,CursorHoldI * call AutoSaveToTempDir()
--]], false)

### whichkey.lua
-- whichkey.lua
-- i truncated all the stuff before...but this was the working whichkey configgg
}

local mappings = {

		["d"] = { "<cmd>:put =strftime('* %A, %b %d %Y ')<CR>", "Named day and date"},
		["k"] = { "<cmd>bdelete<CR>", "Kill Buffer" },  -- Close current file
		["p"] = { "<cmd>Lazy<CR>", "Plugin Manager" },  -- Invoking plugin manager
		["r"] = { "<cmd>luafile ~/.config/nvim/init.lua<CR>", "Reload lua Config" },
	 	["V"] = { "<cmd>VimwikiIndex<CR>", "Vimwiki" },
	 	["h"] = { "<cmd>bp<CR>", "Move to previous buffer" },
	 	["l"] = { "<cmd>bn<CR>", "Move to to buffer" },
		["N"] = { "<cmd>Neotree<CR>", "Neo tree" }, -- File Manager
		["T"] = { "<cmd>Telescope find_files<CR>", "Telescope"},

-- Toggle Tem
    B = {
      name = "Terminal",
        b = { "<cmd>ToggleTerm direction=float<cr>", "Float" }, -- Floating Terminal
        n = { "<cmd>lua _NODE_TOGGLE()<cr>", "Node" }, -- NodeJS Terminal
        p = { "<cmd>lua _PYTHON_TOGGLE()<cr>", "Python" }, -- Python Terminal

        -- Play with size according to your needs.
        h = { "<cmd>ToggleTerm size=10 direction=horizontal<cr>", "Horizontal" }, -- Horizontal Terminal,
        v = { "<cmd>ToggleTerm size=80 direction=vertical<cr>", "Vertical" }, -- Vertical Terminal
    },

-- Chatgpt jack mort stuff
		c = {
			name = "ChatGPT",
				a = { "<cmd>ChatGPTRun add_tests<CR>", "Add Tests", mode = { "n", "v" } },
				c = { "<cmd>ChatGPT<CR>", "ChatGPT" },
				d = { "<cmd>ChatGPTRun docstring<CR>", "Docstring", mode = { "n", "v" } },
				e = { "<cmd>ChatGPTEditWithInstruction<CR>", "Edit with instruction", mode = { "n", "v" } },
				f = { "<cmd>ChatGPTRun fix_bugs<CR>", "Fix Bugs", mode = { "n", "v" } },
				g = { "<cmd>ChatGPTRun grammar_correction<CR>", "Grammar Correction", mode = { "n", "v" } },
				k = { "<cmd>ChatGPTRun keywords<CR>", "Keywords", mode = { "n", "v" } },
				l = { "<cmd>ChatGPTRun code_readability_analysis<CR>", "Code Readability Analysis", mode = { "n", "v" } },
				o = { "<cmd>ChatGPTRun optimize_code<CR>", "Optimize Code", mode = { "n", "v" } },
				r = { "<cmd>ChatGPTRun roxygen_edit<CR>", "Roxygen Edit", mode = { "n", "v" } },
				s = { "<cmd>ChatGPTRun summarize<CR>", "Summarize", mode = { "n", "v" } },
				t = { "<cmd>ChatGPTRun translate<CR>", "Translate", mode = { "n", "v" } },
				x = { "<cmd>ChatGPTRun explain_code<CR>", "Explain Code", mode = { "n", "v" } },
		},

-- neorg stuff
	o = {
			name = "Neorg Stuff",
				j = {"<cmd>Neorg journal today<CR>", "Add a daily or go to the curent journal"},
				J = {"<cmd>execute 'normal! i* *Journal* - ' . strftime('%A, %b %d %Y ')<CR>", "Insert journal header"},
				k = {"<cmd>Neorg keybind<CR>", "Show chose module keybinds"},  
				l = {"<cmd>normal! i{::}<CR>", "Insert link"},
				T = {"<cmd>normal! i - ( )<CR>", "Insert to-do"},
				m = {"<cmd>Neorg inject-metadata <CR>", "Add meta header"},
				n = {"<cmd>Neorg keybind norg core.dirman.new.note<CR>", "Create new note"},  
				M = {"<cmd>execute 'normal! i* *Meeting* - _/ /_ ' . strftime('%A, %b %d %Y ')<CR>", "Insert Meeting header"},
				N = {"<cmd>execute 'normal! i* *Note* - _/ /_ ' . strftime('%A, %b %d %Y ')<CR>", "Insert Note header"},
				O = {"<cmd>execute 'normal! i** *1o1* - _/ /_ ' . strftime('%A, %b %d %Y ')<CR>", "Insert 1o1 header"},
				S = {"<cmd>execute 'normal! i** *Sync* - _/ /_ ' . strftime('%A, %b %d %Y ')<CR>", "Insert Sync header"},
				t = {"<cmd>Neorg toggle-concealer<CR>", "Toggle conceasl"},
				y = {"<cmd>Neorg journal yesterday<CR>", "Go to the yesterdays journal"},

				},

-- Toggle Mode stuff
	t	= {
			name = 'Toggle Mode Stuff',
				h = { "<cmd>nohl<CR>", "Turn off highliting "}, --  no hl stuff
				n = { "<cmd>set number! relativenumber!<CR>", "Turn off line number"}, -- Turn off line numbers
				t = {"<cmd>TableModeToggle<CR>", "TableMode On/Off" }, -- Toggle Mode on/off
				r = { "<cmd>TableModeRealign<CR>", "TableMode Re-Align" }, -- TableMode Re-Align
				s = { "<cmd>TableModeRealign<CR>", "TableModeSort" }, -- TableMode sort 
				c = { "<cmd>if &conceallevel == 0 | set conceallevel=3 | else | set conceallevel=0 | endif<CR>", "Toggle conceal level" },
				m = { 
					name = "wait...theres more!",
						v = { "<cmd>luafile $HOME/.config/nvim/init.lua<CR>", "Reload neovim" }, -- reload neovim
		},
	},

-- quit and write stuff
	q = {
			name = 'quit or save stuff', 
				q = { "<cmd>q!<CR>", "Quit w/o save" }, -- Hard quit
				w = { "<cmd>w!<CR>", "Save" }, -- Write current file
				x = { "<cmd>x!<CR>", "Save" }, -- Save and quit
		},

-- vim stuff...move windows
	v = {
			name = "Vime stuff",
				W = { "<cmd>horizontal resize +10!<CR>:wincmd w<CR>", "Increase window width" }, -- increase window width
				w = { "<cmd>horizontal resize -5!<CR>:wincmd w<CR>", " Decrease window width" }, -- decrease window width
				I = { "<cmd>vertical resize +10!<CR>:wincmd w<CR>", "Increase window height" }, -- increase window height
				i = { "<cmd>vertical resize -5!<CR>:wincmd w<CR>", "Decrease window height" }, -- decrease window width
				j = { "<cmd>wincmd J<cr>", "Move window down"}, 
				k = { "<cmd>wincmd K<cr>", "Move window up"}, 
				l = { "<cmd>wincmd R<cr>", "Move window to the right"},
				h = { "<cmd>wincmd H<cr>", "Move window to the left"}, 
			},
}


which_key.setup(setup)
which_key.register(mappings, opts)

