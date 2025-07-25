@echo off
title AutoClicker para Minecraft - Launcher
color 0A

echo.
echo     =====================================================
echo     ^|                                                   ^|
echo     ^|        🎮 AutoClicker para Minecraft 🎮           ^|
echo     ^|                                                   ^|
echo     ^|              Creado especialmente para            ^|
echo     ^|              mejorar tu experiencia               ^|
echo     ^|                  en Minecraft                     ^|
echo     ^|                                                   ^|
echo     =====================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python no detectado
    echo.
    echo 📥 Por favor instala Python desde:
    echo    https://python.org/downloads/
    echo.
    echo ⚠️  Asegúrate de marcar "Add Python to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)

echo ✅ Python detectado correctamente
echo.

REM Verificar dependencias
echo 🔍 Verificando dependencias...
python -c "import pyautogui, pynput" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Dependencias no encontradas, instalando...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ❌ Error instalando dependencias
        echo 💡 Intenta ejecutar como administrador
        pause
        exit /b 1
    )
    echo ✅ Dependencias instaladas correctamente
) else (
    echo ✅ Todas las dependencias están instaladas
)

echo.
echo 🚀 ¿Qué versión quieres usar?
echo.
echo [1] 🎯 AutoClicker SÚPER FÁCIL (Para principiantes)
echo [2] 🔧 Configurador para Minecraft (Recomendado)
echo [3] � AutoClicker Completo (Interfaz avanzada)
echo [4] 📝 AutoClicker Simple (Solo consola)
echo [5] 📖 Ver README con instrucciones
echo [6] 🚪 Salir
echo.

set /p choice="Elige una opción (1-6): "

if "%choice%"=="1" (
    echo.
    echo 🎯 Iniciando AutoClicker SÚPER FÁCIL...
    python autoclicker_facil.py
) else if "%choice%"=="2" (
    echo.
    echo 🎯 Iniciando Configurador para Minecraft...
    python minecraft_setup.py
) else if "%choice%"=="3" (
    echo.
    echo 🔧 Iniciando AutoClicker Completo...
    python autoclicker.py
) else if "%choice%"=="4" (
    echo.
    echo 📝 Iniciando AutoClicker Simple...
    python autoclicker_simple.py
) else if "%choice%"=="5" (
    echo.
    echo 📖 Abriendo README...
    start README.md
) else if "%choice%"=="6" (
    echo.
    echo 👋 ¡Hasta luego!
    timeout /t 2 >nul
    exit /b 0
) else (
    echo.
    echo ❌ Opción no válida
    timeout /t 2 >nul
    goto menu
)

echo.
echo 🎮 ¡Disfruta tu AutoClicker!
echo.
pause
