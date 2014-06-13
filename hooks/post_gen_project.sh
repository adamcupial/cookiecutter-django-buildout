#!/bin/sh
echo
echo "************* Initializing GIT **************"
echo
command -v git >/dev/null 2>&1 && git init || { echo >&2 "git init is failed. Probably git is not installed. Install git if it's not installed."; exit 1; }
echo
echo "************* Build finished, start working! **************"
echo "Begin by going to your project's dir and running make install"
echo
