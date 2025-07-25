@echo off
echo.
echo ===============================================
echo ^|    🛠️  CREADOR DE EJECUTABLE (.exe)        ^|
echo ^|         AutoClicker para Minecraft         ^|
echo ===============================================
echo.

REM Verificar que PyInstaller esté instalado
python -c "import PyInstaller" >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ PyInstaller no está instalado
    echo 📦 Instalando PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo ❌ Error instalando PyInstaller
        pause
        exit /b 1
    )
)

echo ✅ PyInstaller detectado
echo.

echo 🔨 Creando ejecutable de AutoClicker Fácil...
echo ⏳ Esto puede tomar unos minutos...
echo.

REM Crear el ejecutable con PyInstaller
python -m PyInstaller --onefile --windowed --name="AutoClicker_Minecraft" autoclicker_facil.py

if %errorlevel% neq 0 (
    echo ❌ Error creando el ejecutable
    pause
    exit /b 1
)

echo.
echo ✅ ¡Ejecutable creado con éxito!
echo.
echo 📁 Tu archivo .exe está en:
echo    📂 dist\AutoClicker_Minecraft.exe
echo.
echo 📋 Para compartir con tu amigo:
echo    1. Copia el archivo AutoClicker_Minecraft.exe
echo    2. Tu amigo solo necesita ejecutar ese archivo
echo    3. ¡No necesita instalar Python ni nada más!
echo.

REM Verificar si el archivo se creó
if exist "dist\AutoClicker_Minecraft.exe" (
    echo 🎉 ¡LISTO! El archivo ejecutable está preparado
    echo.
    echo ¿Quieres abrir la carpeta donde está el .exe?
    set /p open="Presiona Y para abrir la carpeta: "
    if /i "%open%"=="Y" (
        explorer dist
    )
) else (
    echo ❌ No se encontró el archivo ejecutable
)

echo.
pause
