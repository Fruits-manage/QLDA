@echo off
echo ========================================
echo    INSTALLING PYTHON DEPENDENCIES
echo ========================================
echo.

echo Installing dependencies for Admin portal...
cd /d "d:\IT\summer-2\QLDA\admin"
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install admin dependencies
    pause
    exit
)
echo.




echo Installing dependencies for Customer portal...
cd /d "d:\IT\summer-2\QLDA\customer"
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install customer dependencies
    pause
    exit
)
echo.

echo Installing dependencies for Farmer portal...
cd /d "d:\IT\summer-2\QLDA\farmer"
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install farmer dependencies
    pause
    exit
)
echo.

echo ========================================
echo All dependencies installed!
echo.
echo Next steps:
echo 1. Make sure XAMPP MySQL is running
echo 2. Run setup_databases.bat
echo 3. Run start_all_portals.bat
echo ========================================
pause
