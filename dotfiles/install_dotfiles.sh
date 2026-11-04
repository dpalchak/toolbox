#!/bin/bash

if [[ `uname` == "Linux" ]]; then
    OS_DIR="linux"
elif [[ `uname` == "Darwin" ]]; then
    OS_DIR="osx"
else
    echo "Unsupported OS"
    exit 1
fi

LINK="ln -s -v -r -f -t"

mkdir -p ${HOME}/.ssh
$LINK ${HOME}/.ssh common/.ssh/*

$LINK ${HOME} ${OS_DIR}/.z*
$LINK ${HOME} common/.[a-zA-Z]*

