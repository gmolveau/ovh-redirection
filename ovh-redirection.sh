#!/usr/bin/env sh
# this needs to be a script because a .bashrc (or .zshrc) function
# will change your current virtualenv if you're using one

cd /Users/gregou/dev/ovh-redirection
# we need to cd because the script needs to access the local file ovh.conf
source venv/bin/activate
python3 ovh_client/cli.py "$@"