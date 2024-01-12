#!/bin/bash
#Purpose: To automate cloning of repository from the gitolite server.
#

set -e

HOST=$1
PORT=$2
REPO=$3
USER="git"

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
	echo "Use case -- $0 HOST_IP PORT REPO_NAME"
else
	if [ ! -d "$REPO" ]; then

		git clone ssh://$USER@"$HOST:$PORT"/"$REPO"

		echo "Repo $REPO has been cloned."

	else
		echo "$REPO is an existing repository."

	fi
fi

exit 0
