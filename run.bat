@echo off
echo Iniciando AutoClicker para Minecraft...
echo.

REM Verificar si el archivo existe
if not exist autoclicker.py (
    echo ERROR: No se encuentra autoclicker.py
    echo Asegúrate de estar en el directorio correcto
    pause
    exit /b 1
)

REM Ejecutar el autoclicker
python autoclicker.py

if %errorlevel% neq 0 (
    echo.
    echo Si hay errores de dependencias, ejecuta install.bat primero
    pause
)
