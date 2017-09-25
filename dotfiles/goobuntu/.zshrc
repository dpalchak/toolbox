
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

#Bindkeys based on $EDITOR
bindkey -e

# Who doesn't want home and end to work?
bindkey '\e[1~' beginning-of-line
bindkey '\e[4~' end-of-line

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

export MAKEFLAGS="-j"


alias ls="ls -F --color=auto"
alias ll="ls -lFh --color=auto"
alias la="ls -laFh --color=auto"

alias cd..="cd .."
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

alias kate="kate 2>&1 1>/dev/null"

alias lsdfu="dfu-util -l"
alias lscoppa="lsusb -d 18d1:"


autoload add-zsh-hook

launch_autols() {
  eval ls
}

add-zsh-hook chpwd launch_autols
