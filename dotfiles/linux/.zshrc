
#
# .zshrc is sourced in interactive shells.
# It should contain commands to set up aliases,
# functions, options, key bindings, etc.
#
source "${HOME}/.zshrc_common"

alias ls="ls -CF --color=auto"
alias ll="ls -lFh --color=auto"
alias la="ls -laFh --color=auto"

alias owns="dpkg -S"
alias ccalc="wine \"c:\Program Files (x86)\Console Calculator\CCalc.exe\""

# gnome-terminal generates some annoying console spew, so silence it
alias gnome-terminal="gnome-terminal 2>/dev/null"

alias xpra-mtv="xpra attach --ssh=\"ssh -q\" ssh:palchak@palchak.mtv.corp.google.com:42"

# Enable EE CAD tools (go/ee-cad)
export CDSHOME="${HOME}/wearables/ecad"
# source profile like .bashrc
if [ -f ${HOME}/wearables/ecad/scripts/edatools-deb-palchak ]; then
	source ${HOME}/wearables/ecad/scripts/edatools-deb-palchak
fi

# Enable use of fig and g4
if [[ -f "/etc/bash_completion.d/hgd" ]]; then
	source /etc/bash_completion.d/hgd
fi

if [[ -f "/etc/bash_completion.d/g4d" ]]; then
	source /etc/bash_completion.d/g4d
fi

export MGLS_LICENSE_FILE="${HOME}/.lattice/license.dat"
export MODELSIM_TCL="${HOME}/toolbox/dotfiles/linux/modelsim.tcl"

# Activate a default Python virtual environment
VIRTUAL_ENV_DISABLE_PROMPT=1
if [[ -f ~/.venv/palchak/bin/activate ]]; then
	source ~/.venv/palchak/bin/activate
fi

unset VIRTUAL_ENV_DISABLE_PROMPT
