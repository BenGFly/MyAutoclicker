@echo off
echo Instalando AutoClicker para Minecraft...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instala Python desde https://python.org
    pause
    exit /b 1
)

echo Python detectado correctamente
echo.

REM Instalar dependencias
echo Instalando dependencias...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    echo Intentando con pip3...
    pip3 install -r requirements.txt
)

echo.
echo ¡Instalación completada!
echo.
echo Para ejecutar el AutoClicker, usa:
echo python autoclicker.py
echo.
pause
