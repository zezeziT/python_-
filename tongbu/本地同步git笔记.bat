@echo off
cd /d "E:\python\official_docs" || (
  echo Path not found. Please check if the directory is correct!
  pause
  exit /b
)

echo Adding all changes...
git add .

:: Get current date in YYYY-MM-DD format (works in most Windows environments)
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do (
    set today=%%c-%%a-%%b
)

echo Committing with today's date...
git commit -m "Update study notes - %today%"

echo Pushing to GitHub...
git push

echo Sync complete!
pause
