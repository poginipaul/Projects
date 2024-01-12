#!/bin/bash
#Purpose: Using git commands to the repository.
#

set -e

REPO=${1%/}
TODAY=$(date +%Y-%m-%d)
BACKUP_DST="gilt-backup"

##
# Check if argument is present.
##
if [ -z "$REPO" ]; then
	echo "Use case $0 <REPOSITORY_NAME>"

else
	##
	# Check if the files that are modified and new.
	##

	FILES_UPDATED=false

	for files in "$REPO"/*
	do
		if [[ $(stat -c "%y %n" "$files" | grep -oE "$TODAY") == "$TODAY" ]]; then

			stat -c "%y %n" "$files"

			FILES_UPDATED=true
		fi
	done

	if [ "$FILES_UPDATED" = true ]; then
		cd "$REPO"

		GIT_STAT=$(git status)

		if [[ "$GIT_STAT" =~ "Untracked files" ]] || [[ "$GIT_STAT" =~ "Changes not staged for commit" ]]; then
			git add --all
			git commit -m "Committing files."
			git push origin master

			cd ..

			#mkdir "$BACKUP_DST"/"$REPO.$TODAY"

			gilt --debug overlay

			tar -cvf "../gitolite-archive/$REPO.$TODAY.tar" "$REPO"
		else
			echo "No changes."

			tar -cvf "../gitolite-archive/$REPO.$TODAY.old.tar" "$REPO"
		fi

	else
		# Backup updated files to the backup directory.

		echo "Files for $REPO is updated or $REPO hasn't commited."


		cd "$REPO"

		git status

		#mkdir "../$BACKUP_DST"/"$REPO.$TODAY"

		git add --all
		git commit -m "Committing files."
		git push origin master

		cd ..

		gilt --debug overlay

		ls "$BACKUP_DST"
	fi
fi
