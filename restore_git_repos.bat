
REM Repository: projects/_trash/termtools
echo Restoring: projects/_trash/termtools
if exist "projects\_trash\termtools\.git" (
    echo   Directory already exists, skipping...
) else (
    REM Create parent directory if needed
    if not exist "projects\_trash" mkdir "projects\_trash"
    
    REM Clone the repository
    git clone "git@github.com:yasserfarouk/termtools.git" "projects\_trash\termtools"
    if errorlevel 1 (
        echo   Failed to clone
    ) else (
        echo   Successfully cloned
        
        REM Checkout the original branch if not already on it
        cd "projects\_trash\termtools"
        git checkout "master" 2>nul
        if errorlevel 1 (
            echo   Could not checkout branch: master
        ) else (
            echo   Checked out branch: master
        )
        cd ..\..
    )
)
echo.


REM Repository: projects/_trash/termtools
echo Restoring: projects/_trash/termtools
if exist "projects\_trash\termtools\.git" (
    echo   Directory already exists, skipping...
) else (
    REM Create parent directory if needed
    if not exist "projects\_trash" mkdir "projects\_trash"
    
    REM Clone the repository
    git clone "git@github.com:yasserfarouk/termtools.git" "projects\_trash\termtools"
    if errorlevel 1 (
        echo   Failed to clone
    ) else (
        echo   Successfully cloned
        
        REM Checkout the original branch if not already on it
        cd "projects\_trash\termtools"
        git checkout "master" 2>nul
        if errorlevel 1 (
            echo   Could not checkout branch: master
        ) else (
            echo   Checked out branch: master
        )
        cd ..\..
    )
)
echo.

