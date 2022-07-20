
#
# .zshrc is sourced in interactive shells.
# It should contain commands to set up aliases,
# functions, options, key bindings, etc.
#

source "${HOME}/.zshrc_common"


# Note that 'path' is intentionally lower-case, as it is an array (not a string)
path=("/usr/local/opt/llvm/bin" "${HOME}/Library/Android/sdk/platform-tools" "/usr/local/opt/coreutils/libexec/gnubin/" $path)
export PATH

export HOMEBREW_NO_AUTO_UPDATE=1

alias ls="ls -FG"
alias ll="ls -lFGh"
alias la="ls -laFGh"

alias kate="kate 2>&1 1>/dev/null"

alias xpra_c="Xpra attach --dpi=120 --encoding=rgb --title=@title@ --ssh=\"ssh\" --desktop-scaling=off \"ssh://palchak.mtv.corp.google.com/:42\""
