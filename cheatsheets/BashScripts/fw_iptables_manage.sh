#!/bin/bash

rules=(
"INPUT -s 192.168.56.0/24 -p tcp -m tcp --dport 22 -j ACCEPT"
"INPUT -p tcp --dport 22 -j DROP"
"INPUT -s 192.168.56.0/24 -p tcp -m tcp --dport 5432 -j ACCEPT"
"INPUT -p tcp --dport 5432 -j DROP"
)

rule_exists() {
    local rule="${1}"
    sudo iptables -C $rule > /dev/null 2>&1
}

all_rules_exist=true
for rule in "${rules[@]}"; do
    if ! rule_exists "${rule}"; then
        all_rules_exist=false
        break
    fi
done

if [ $# -eq 0 ]; then
    if "${all_rules_exist}"; then
        echo "All rules exist."
    else
        echo "Warning: Not all rules exist."
    fi
    exit 0
fi

if [ "${1}" == "add-rules" ]; then
    if "${all_rules_exist}"; then
        echo "All rules already exist."
    else
        echo "Adding rules..."
        for rule in "${rules[@]}"; do
            sudo iptables -A $rule
        done
    fi

elif [ "${1}" == "remove-rules" ]; then
    if "${all_rules_exist}"; then
        echo "Removing rules..."
        for rule in "${rules[@]}"; do
            sudo iptables -D $rule
        done
    else
        echo "Warning: Not all rules exist. No actions will be performed."
    fi
else
    echo "Invalid argument. Please use 'add-rules' or 'remove-rules'."
fi
