#!/bin/bash

ACCESS_DIR="/dir/with/many/old/files"
AGE=60
LOGFILE="/var/log/cron_cleaner.log"

find $ACCESS_DIR -mtime +$AGE -type f -print | while read file; do
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "$TIMESTAMP deleting $file" >> $LOGFILE
    rm -rf "$file"
done
