@echo off
title FRUIT MANAGEMENT SYSTEM - Complete Setup
color 0B
echo.
echo =================================================
echo         FRUIT MANAGEMENT SYSTEM
echo            Complete Setup Wizard
echo =================================================
echo.
echo This script will:
echo 1. Install Python dependencies
echo 2. Setup XAMPP MySQL databases  
echo 3. Run database migrations
echo 4. Test all connections
echo 5. Start all portals
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul

:: Step 1: Install dependencies
echo.
echo 📦 Step 1/5: Installing Python dependencies...
call install_dependencies.bat
if %errorlevel% neq 0 (
    echo ❌ Dependency installation failed!
    pause
    exit /b 1
)

:: Step 2: Setup databases
echo.
echo 🗄️ Step 2/5: Setting up MySQL databases...
call setup_databases.bat
if %errorlevel% neq 0 (
    echo ❌ Database setup failed!
    pause
    exit /b 1
)

:: Step 3: Run migrations
echo.
echo 🚀 Step 3/5: Running database migrations...
call run_migrations.bat
if %errorlevel% neq 0 (
    echo ❌ Migration failed!
    pause
    exit /b 1
)

:: Step 4: Test connections
echo.
echo 🔧 Step 4/5: Testing database connections...
python test_database_connections.py
if %errorlevel% neq 0 (
    echo ❌ Connection test failed!
    pause
    exit /b 1
)

:: Step 5: Start all portals
echo.
echo 🌐 Step 5/5: Starting all portals...
echo.
echo Press any key to launch all portals...
pause >nul

call start_all_portals.bat

echo.
echo =================================================
echo ✅ FRUIT MANAGEMENT SYSTEM SETUP COMPLETE!
echo =================================================
echo.
echo 🌐 Portal URLs:
echo - Admin Portal:    http://localhost:8000/
echo - Customer Portal: http://localhost:8001/
echo - Farmer Portal:   http://localhost:8002/
echo.
echo 🔑 Default Login Credentials:
echo - Admin: admin / admin123
echo - Customer: customer_admin / customer123
echo - Farmer: farmer_admin / farmer123
echo.
echo 📚 Documentation available in docs/ folder
echo 🔧 API testing available via test_api_integration.py
echo.
pause
