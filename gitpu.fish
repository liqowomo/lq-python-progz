#!/bin/fish 
echo "This will execute the following commands"
echo " git commit -a = Add all files and then open a commit window"
echo " git push = This will push it up to your branch"
git add . 
git commit -a
git push