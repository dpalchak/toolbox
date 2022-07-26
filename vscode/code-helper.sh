#!/bin/bash

if [[ -n ${VSCODE_IPC_HOOK_CLI} && -n ${VSCODE_HELPER_SCRIPT} ]]
then
  exec "${VSCODE_HELPER_SCRIPT}" $*
else
  exec /usr/bin/code $*
fi