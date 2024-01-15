#!/bin/bash
# Purpose: Installation of nginx to the remote servers.
# OS: Ubuntu

PKG="nginx"
ROOT_DIR="/var/www/html/test"


function service(){
    if ! systemctl list-units --full -all | grep "$PKG.service"; then
        echo
        echo "No package "$PKG""
        #sudo -i
        sudo -n apt-get install "$PKG" -y > /dev/null
        systemctl status "$PKG"
        echo "#----------#"
    
    else
        systemcl status "$PKG"
    fi
}

service



