#!/bin/bash
set -m
# Navigate to the repository directory
cd "C:\Users\hassa\OneDrive\Desktop\gitpush"
printf -v mydate '%(%Y-%m-%d)T' -1
echo "date:${mydate}"

# Add the specific file to the staging area
git add "${mydate}.py"

# Commit the changes with a timestamp
git commit -m "Automatic commit on $mydate"

# Push the changes to the remote repository
git push origin main