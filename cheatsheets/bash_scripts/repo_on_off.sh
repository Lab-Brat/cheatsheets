#!/bin/bash

# Get a list of repositories
repos=$(yum repolist all | grep enabled | awk '{print $1}')

echo "The following repositories are currently enabled:"
echo "$repos"

# Ask the user for input
read -p "Would you like to enable, disable these repositories or restore them? (enable/disable/restore): " action

if [[ "$action" == "enable" ]]; then
    # enable repositories in the list
    for repo in $repos; do
        sudo yum-config-manager --enable $repo
        echo "Enabled $repo"
    done
elif [[ "$action" == "disable" ]]; then
    # disable repositories in the list and back them up
    for repo in $repos; do
        sudo yum-config-manager --disable $repo
        echo "Disabled $repo"
        echo $repo >> disabled_repos.txt
    done
elif [[ "$action" == "restore" ]]; then
    # enable backed-up repositories
    if [ -f disabled_repos.txt ]; then
        while IFS= read -r repo; do
            sudo yum-config-manager --enable $repo
            echo "Restored $repo"
        done < disabled_repos.txt
    else
        echo "No repositories to restore."
    fi
else
    echo "Invalid input. Please enter either 'enable', 'disable' or 'restore'."
fi
