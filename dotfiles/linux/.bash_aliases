#Exit now if this is not an interactive session
[ -z "$PS1" ] && return

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

alias g2="cd ~/GEN2"
alias envsetup="source ~/GEN2/build/envsetup.sh"

