import pyautogui
import time
import keyboard

print("🎮 AutoClicker Simple para Minecraft")
print("=" * 40)

# Configuración básica
click_interval = float(input("Intervalo entre clicks (segundos, ej: 0.1): ") or 0.1)
click_type = input("Tipo de click (left/right/middle): ") or "left"

print(f"\nConfiguración:")
print(f"- Intervalo: {click_interval} segundos")
print(f"- Tipo: {click_type}")
print(f"- Hotkey: F6 para iniciar/detener")

print("\n📍 Posiciona tu mouse donde quieres hacer click")
print("Presiona ENTER cuando esté listo...")
input()

# Capturar posición actual
x, y = pyautogui.position()
print(f"Posición guardada: ({x}, {y})")

print("\n🎯 Presiona F6 para iniciar el autoclicker")
print("🛑 Presiona F6 nuevamente para detener")
print("🚨 Mueve el mouse a la esquina superior izquierda para emergencia")

clicking = False
click_count = 0

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print(f"\n✅ AutoClicker INICIADO - Haciendo click en ({x}, {y})")
    else:
        print(f"\n⏹️ AutoClicker DETENIDO - Total de clicks: {click_count}")

# Configurar hotkey
keyboard.add_hotkey('f6', toggle_clicking)

try:
    while True:
        if clicking:
            try:
                pyautogui.click(x, y, button=click_type)
                click_count += 1
                if click_count % 100 == 0:  # Mostrar progreso cada 100 clicks
                    print(f"Clicks realizados: {click_count}")
                time.sleep(click_interval)
            except pyautogui.FailSafeException:
                print("🚨 Detención de emergencia activada!")
                break
        else:
            time.sleep(0.1)  # Pequeña pausa cuando no está clickeando
            
except KeyboardInterrupt:
    print(f"\n👋 Programa terminado - Total de clicks: {click_count}")
except Exception as e:
    print(f"\n❌ Error: {e}")
finally:
    print("Gracias por usar AutoClicker Simple! 🎮")
