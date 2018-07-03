
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
setopt appendhistory autocd extendedglob

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/usr/local/google/home/palchak/.zshrc'

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


#Bindkeys based on $EDITOR
bindkey -v

# Who doesn't want home and end to work?
bindkey '\e[1~' beginning-of-line
bindkey '\e[4~' end-of-line

# Use standard ctrl+R for history search
bindkey '^R' history-incremental-search-backward


export MAKEFLAGS="-j"


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

setopt rm_start_silent

autoload add-zsh-hook

launch_autols() {
  eval ls
}

add-zsh-hook chpwd launch_autols