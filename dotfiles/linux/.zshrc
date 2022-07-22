
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


# Enable EE CAD tools (go/ee-cad)
export CDSHOME="${HOME}/wearables/ecad"
# source profile like .bashrc
if [ -f ${HOME}/wearables/ecad/scripts/edatools-deb-palchak ]; then
	source ${HOME}/wearables/ecad/scripts/edatools-deb-palchak
fi

export MGLS_LICENSE_FILE="${HOME}/.lattice/radiant/2.2/license/license.dat"
export MODELSIM_TCL="${HOME}/.config/modelsim.tcl"
