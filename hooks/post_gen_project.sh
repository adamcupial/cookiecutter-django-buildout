#!/bin/sh
echo
echo "************* Initializing GIT **************"
echo
command -v git >/dev/null 2>&1 && git init || { echo >&2 "git init is failed. Probably git is not installed. Install git if it's not installed."; exit 1; }
echo
echo "************* Build finished, start working! **************"
echo "1. cd to your project dir"
echo "2. cp local.cfg-dist to local.cfg (git-ignored by default)"
echo "3. edit local.cfg and change / set your settings"
echo "4. make install (or install_prod)"
echo
