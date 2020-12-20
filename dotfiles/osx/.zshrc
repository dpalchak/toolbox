
#
# .zshrc is sourced in interactive shells.
# It should contain commands to set up aliases,
# functions, options, key bindings, etc.
#


# source profile like .bashrc
if [ -f /etc/profile ]; then
	source /etc/profile
fi


# Lines configured by zsh-newuser-install
HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt appendhistory autocd extendedglob no_share_history
unsetopt share_history

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/Users/palchak/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

# Customize to your needs...

prompt sorin

# This way the completion script does not have to parse Bazel's options
# # repeatedly.  The directory in cache-path must be created manually.
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache
zstyle ':completion:*' users
zstyle ':completion:*' completer _complete _match
setopt auto_list nolist_ambiguous nomenu_complete glob_complete


#Bindkeys based on $EDITOR
bindkey -v

# Who doesn't want home and end to work?
bindkey '\e[1~' beginning-of-line
bindkey '\e[4~' end-of-line

# Use standard ctrl+R for history search
bindkey '^R' history-incremental-search-backward


export MAKEFLAGS="-j"
export CMAKE_GENERATOR="Ninja"

alias ls="ls -FG"
alias ll="ls -lFGh"
alias la="ls -laFGh"

alias cd..="cd .."
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

alias kate="kate 2>&1 1>/dev/null"

alias lsdfu="dfu-util -l"
alias lscoppa="lsusb -d 18d1:"

setopt rm_star_silent
setopt clobber

autoload add-zsh-hook

launch_autols() {
  eval ls
}

findreplace() {
  if (( $# != 2 )) then
    echo usage: findreplace FILE_GLOB REGEX
  fi
  cmd="find -L . -type f -name \"$1\" -print0 | xargs -0 -t sed -i -e '$2'"
  echo "'${cmd}'"  
  eval ${cmd}
}

add-zsh-hook chpwd launch_autols

# Note that 'path' is intentionally lower-case, as it is an array (not a string)
path=('/Users/palchak/.local/bin' '/Users/palchak/Library/Android/sdk/platform-tools' '/Users/palchak/Library/Python/3.6/bin' $path)
export PATH

export ADB_VENDOR_KEYS='/Users/palchak/firmware/android/adb_keys'

# Tell the terminal about the current working directory at each prompt.

if [ -z "$INSIDE_EMACS" ]; then
    update_terminal_title() {
        printf '\033]0;%s\007' "${PWD//${HOME}/~}"
    }

    # Register the function so it is called at each prompt.
    autoload add-zsh-hook
    add-zsh-hook precmd update_terminal_title
fi
