#Exit now if this is not an interactive session
[ -z "$PS1" ] && return

function cd {
   builtin cd "$@" && ls -F
}
