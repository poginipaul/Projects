#!/bin/bash
#Purpose: Adding a repository to the gitolite configuration.
#

set -e

REPO=$1
USERS=$2
GITOLITE_CONF_DIR="gitolite-admin/conf/gitolite.conf"
SRC_DIR="my-codes/"

#Create new repository.
function add_repository_name() {
	echo -e "\nrepo $REPO\n    RW+     =   $USERS" >> "$GITOLITE_CONF_DIR"
}

#Check the script args is not empty.
if [ -z "$1" ] || [ -z "$2" ]; then
	clear

	echo "Use case $0 <REPOSITORY_NAME> <USER>"

else
	#Create a repository and add a user.
	if ! cat gitolite-admin/conf/gitolite.conf | grep "repo $1"; then
		echo "No Available Repository"

		clear

		add_repository_name

		date

		cat gitolite-admin/conf/gitolite.conf
	else
		date

		cat gitolite-admin/conf/gitolite.conf | grep "repo $1"

		echo "Available Repository"
	fi
fi

exit 0
