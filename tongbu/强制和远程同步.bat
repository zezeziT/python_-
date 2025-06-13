@echo off
cd /d "E:\python\official_docs" 

echo Syncing remote changes to local repo...
git fetch origin
git reset --hard origin/main
git clean -fd

echo Done syncing.
pause
