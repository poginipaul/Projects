#!/bin/bash
# Purpose: Send remote commands to multiple servers.
# OS: Ubuntu

set -e

SERVERS="REMOTE_SERVERS.txt"
INSTALL_SCRIPT="nginx-pkg-install.sh"
USER="paul"
CMDS=("ls /tmp/\"$INSTALL_SCRIPT\"" "chmod +x /tmp/\"$INSTALL_SCRIPT\"")

#Check servers status.
for server in $(cat "$SERVERS"); do

    # Send icmp to the server if reachable.
    if ping "$server" -c 1 > /dev/null; then
        echo "#----------#"
        echo "SERVER $server"
        echo "#----------#"
        echo "$server -> server ok"

        # Execute nginx package script. 
        if scp "$INSTALL_SCRIPT" $USER@$server:/tmp; then
            ssh $USER@$server ls /tmp/"$INSTALL_SCRIPT" | grep nginx
            ssh $USER@$server chmod +x /tmp/"$INSTALL_SCRIPT"
            ssh $USER@$server sudo bash /tmp/"$INSTALL_SCRIPT"
            ssh $USER@$server rm /tmp/"$INSTALL_SCRIPT"
            curl -X GET "$server"
            echo
        fi
    else
        echo "$server -> server unreachable"
    fi
done

exit 0

