# 🎮 AutoClicker para Minecraft

<div align="center">

![AutoClicker](https://img.shields.io/badge/AutoClicker-Minecraft-green?style=for-the-badge&logo=minecraft)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge&logo=windows)

**Un autoclicker avanzado y fácil de usar, especialmente diseñado para Minecraft y otros juegos.**

[📥 Descargar .exe](#-descarga-directa) • [🚀 Instalación](#-instalación-rápida) • [📖 Guía de uso](#-uso-para-minecraft) • [🤝 Contribuir](#-contribuir)

</div>

---

## ✨ Características

- 🖥️ **Interfaz gráfica intuitiva** con configuración visual
- 🖱️ **Múltiples tipos de click**: Izquierdo, derecho y medio
- ⏱️ **Control de velocidad preciso**: Desde 0.01 hasta 5 segundos entre clicks
- 🔄 **Dos modos de operación**: Infinito o cantidad específica de clicks
- 📍 **Selección de posición**: Click manual o posición actual del mouse
- ⌨️ **Hotkey configurable**: F6-F12 para iniciar/detener sin cambiar ventana
- 📊 **Contador de clicks en tiempo real**
- 🛡️ **Seguridad integrada**: Failsafe para detener moviendo mouse a esquina
- 📦 **Versión ejecutable**: No requiere instalación de Python

## 📥 Descarga Directa

### Opción 1: Archivo Ejecutable (Recomendado)
**¡Descarga y usa inmediatamente!**
- 📁 [AutoClicker_Minecraft.exe](dist/AutoClicker_Minecraft.exe) (13.5 MB)
- ✅ No requiere Python ni instalaciones
- ✅ Funciona en cualquier Windows
- ✅ Interfaz súper fácil de usar

### Opción 2: Código Fuente
```bash
git clone https://github.com/TU_USUARIO/MyAutoclicker.git
cd MyAutoclicker
```

## 🚀 Instalación Rápida

### Opción 1: Instalación Automática
1. Ejecuta `install.bat` como administrador
2. Ejecuta `run.bat` para iniciar el autoclicker

### Opción 2: Instalación Manual
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el autoclicker
python autoclicker.py
```

## 🎯 Uso para Minecraft

### Configuraciones Recomendadas:

**Para minar rápido:**
- Intervalo: 0.05-0.1 segundos
- Tipo: Click Izquierdo
- Modo: Infinito

**Para colocar bloques:**
- Intervalo: 0.1-0.2 segundos
- Tipo: Click Derecho
- Modo: Cantidad específica

**Para pescar (AFK Fishing):**
- Intervalo: 0.5-1.0 segundos
- Tipo: Click Derecho
- Modo: Infinito

### Pasos de uso:
1. **Abre Minecraft** y ve a la ubicación donde quieres hacer click
2. **Abre el AutoClicker** ejecutando `run.bat`
3. **Configura el intervalo** según tu necesidad
4. **Selecciona el tipo de click** (izquierdo para minar, derecho para colocar)
5. **Elige la posición**:
   - "Seleccionar Posición": Haz click donde quieres que actúe
   - "Usar Posición Actual": Usa donde esté el mouse ahora
6. **Regresa a Minecraft** y presiona **F6** para iniciar
7. **Presiona F6 nuevamente** para detener

## ⌨️ Controles

- **F6**: Iniciar/Detener autoclicker (configurable)
- **Botones en interfaz**: Control manual
- **Mouse a esquina superior izquierda**: Detención de emergencia

## ⚙️ Configuración Avanzada

### Intervalos Recomendados:
- **0.01-0.05s**: Clicking muy rápido (cuidado con anti-cheat)
- **0.1-0.2s**: Velocidad normal para juegos
- **0.5-1.0s**: Velocidad conservadora
- **1.0s+**: Para tareas que requieren paciencia

### Tipos de Click:
- **Izquierdo**: Minar, atacar, seleccionar
- **Derecho**: Colocar bloques, usar items, abrir inventarios
- **Medio**: Funciones especiales

## 🛡️ Seguridad y Consideraciones

### Anti-Cheat:
- **Usa intervalos variables** si el servidor tiene anti-cheat
- **No uses velocidades extremas** (menos de 0.05s puede ser detectado)
- **Toma descansos** para parecer más humano

### Seguridad del Sistema:
- El programa incluye un **failsafe**: mueve el mouse a la esquina superior izquierda para detener todo
- **No requiere permisos de administrador** para uso básico
- **Código abierto**: Puedes revisar todo el código

## 🐛 Solución de Problemas

### Error: "No module named 'pyautogui'"
```bash
pip install pyautogui pynput
```

### Error: "Permission denied"
- Ejecuta como administrador
- Verifica que tu antivirus no esté bloqueando el programa

### El autoclicker no funciona en el juego
- Asegúrate de que el juego esté en **modo ventana** o **ventana sin bordes**
- Verifica que la posición seleccionada sea correcta
- Prueba con intervalos más largos

### Hotkey no responde
- Cambia la tecla de F6 a otra (F7, F8, etc.)
- Asegúrate de que ningún otro programa use la misma tecla

## 📝 Notas Importantes

⚠️ **Uso Responsable**: 
- Úsalo solo en servidores que permitan autoclickers
- No lo uses para hacer trampa en servidores competitivos
- Respeta las reglas de cada servidor

⚠️ **Términos de Servicio**:
- Algunos servidores prohíben autoclickers
- Úsalo bajo tu propia responsabilidad
- Lee las reglas del servidor antes de usar

## 🔧 Personalización

El código está comentado y es fácil de modificar. Puedes:
- Cambiar los intervalos por defecto
- Añadir más tipos de click
- Modificar la interfaz
- Agregar patrones de click más complejos

## � Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. 🍴 Fork el proyecto
2. 🌟 Crea tu rama de feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la rama (`git push origin feature/AmazingFeature`)
5. 🔄 Abre un Pull Request

## ⭐ Soporte

Si este proyecto te ayudó, ¡dale una estrella! ⭐

Para reportar bugs o solicitar features, abre un [issue](../../issues).

## 📞 Contacto

- 💬 Discord: [Tu Discord]
- 📧 Email: [Tu Email]
- 🐙 GitHub: [@BenGFly](https://github.com/BenGFly)

---

<div align="center">

**¡Disfruta tu experiencia mejorada en Minecraft! 🎮⛏️**

![Minecraft](https://img.shields.io/badge/Made%20for-Minecraft-brightgreen?style=flat&logo=minecraft)

</div>
