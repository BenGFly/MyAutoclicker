import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import pyautogui
from pynput import mouse, keyboard
from pynput.mouse import Button, Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener

class AutoClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoClicker para Minecraft - v1.0")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # Variables de control
        self.clicking = False
        self.click_thread = None
        self.click_position = (0, 0)
        self.hotkey_listener = None
        
        # Variables de configuración
        self.click_interval = tk.DoubleVar(value=0.1)
        self.click_type = tk.StringVar(value="left")
        self.click_mode = tk.StringVar(value="infinite")
        self.click_count = tk.IntVar(value=100)
        self.hotkey = tk.StringVar(value="F6")
        
        self.setup_ui()
        self.start_hotkey_listener()
        
    def setup_ui(self):
        # Título principal
        title_label = tk.Label(self.root, text="🎮 AutoClicker para Minecraft", 
                              font=("Arial", 16, "bold"), fg="blue")
        title_label.pack(pady=10)
        
        # Frame para configuración de clicks
        click_frame = ttk.LabelFrame(self.root, text="Configuración de Clicks", padding=10)
        click_frame.pack(fill="x", padx=10, pady=5)
        
        # Intervalo de clicks
        ttk.Label(click_frame, text="Intervalo entre clicks (segundos):").pack(anchor="w")
        interval_frame = tk.Frame(click_frame)
        interval_frame.pack(fill="x", pady=2)
        
        self.interval_scale = tk.Scale(interval_frame, from_=0.01, to=5.0, 
                                      resolution=0.01, orient="horizontal",
                                      variable=self.click_interval, length=200)
        self.interval_scale.pack(side="left")
        
        interval_entry = tk.Entry(interval_frame, textvariable=self.click_interval, width=8)
        interval_entry.pack(side="left", padx=(10, 0))
        
        # Tipo de click
        ttk.Label(click_frame, text="Tipo de click:").pack(anchor="w", pady=(10, 0))
        click_type_frame = tk.Frame(click_frame)
        click_type_frame.pack(fill="x")
        
        ttk.Radiobutton(click_type_frame, text="Click Izquierdo", 
                       variable=self.click_type, value="left").pack(side="left")
        ttk.Radiobutton(click_type_frame, text="Click Derecho", 
                       variable=self.click_type, value="right").pack(side="left")
        ttk.Radiobutton(click_type_frame, text="Click Medio", 
                       variable=self.click_type, value="middle").pack(side="left")
        
        # Modo de click
        ttk.Label(click_frame, text="Modo de click:").pack(anchor="w", pady=(10, 0))
        mode_frame = tk.Frame(click_frame)
        mode_frame.pack(fill="x")
        
        ttk.Radiobutton(mode_frame, text="Infinito", 
                       variable=self.click_mode, value="infinite").pack(side="left")
        ttk.Radiobutton(mode_frame, text="Cantidad específica", 
                       variable=self.click_mode, value="count").pack(side="left")
        
        count_frame = tk.Frame(click_frame)
        count_frame.pack(fill="x", pady=2)
        ttk.Label(count_frame, text="Cantidad de clicks:").pack(side="left")
        count_entry = tk.Entry(count_frame, textvariable=self.click_count, width=8)
        count_entry.pack(side="left", padx=(10, 0))
        
        # Frame para posición
        position_frame = ttk.LabelFrame(self.root, text="Posición del Click", padding=10)
        position_frame.pack(fill="x", padx=10, pady=5)
        
        self.position_label = tk.Label(position_frame, text="Posición: No seleccionada", 
                                      fg="red", font=("Arial", 10))
        self.position_label.pack(pady=2)
        
        position_buttons = tk.Frame(position_frame)
        position_buttons.pack(fill="x")
        
        ttk.Button(position_buttons, text="Seleccionar Posición", 
                  command=self.select_position).pack(side="left", padx=2)
        ttk.Button(position_buttons, text="Usar Posición Actual", 
                  command=self.use_current_position).pack(side="left", padx=2)
        
        # Frame para controles
        control_frame = ttk.LabelFrame(self.root, text="Controles", padding=10)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        # Hotkey
        hotkey_frame = tk.Frame(control_frame)
        hotkey_frame.pack(fill="x", pady=2)
        ttk.Label(hotkey_frame, text="Tecla de activación:").pack(side="left")
        hotkey_combo = ttk.Combobox(hotkey_frame, textvariable=self.hotkey, width=8,
                                   values=["F6", "F7", "F8", "F9", "F10", "F11", "F12"])
        hotkey_combo.pack(side="left", padx=(10, 0))
        hotkey_combo.bind("<<ComboboxSelected>>", self.update_hotkey)
        
        # Botones de control
        button_frame = tk.Frame(control_frame)
        button_frame.pack(fill="x", pady=10)
        
        self.start_button = tk.Button(button_frame, text="🚀 INICIAR AUTOCLICKER", 
                                     command=self.start_clicking, bg="green", 
                                     fg="white", font=("Arial", 14, "bold"),
                                     height=2)
        self.start_button.pack(side="left", padx=2, fill="x", expand=True)
        
        self.stop_button = tk.Button(button_frame, text="⏹ DETENER", 
                                    command=self.stop_clicking, bg="red", 
                                    fg="white", font=("Arial", 14, "bold"), 
                                    state="disabled", height=2)
        self.stop_button.pack(side="left", padx=2, fill="x", expand=True)
        
        # Frame de estado
        status_frame = ttk.LabelFrame(self.root, text="Estado", padding=10)
        status_frame.pack(fill="x", padx=10, pady=5)
        
        self.status_label = tk.Label(status_frame, text="Listo para usar", 
                                    fg="green", font=("Arial", 10, "bold"))
        self.status_label.pack()
        
        self.clicks_counter = tk.Label(status_frame, text="Clicks realizados: 0", 
                                      font=("Arial", 9))
        self.clicks_counter.pack()
        
        # Información de ayuda
        help_frame = ttk.LabelFrame(self.root, text="Ayuda", padding=10)
        help_frame.pack(fill="x", padx=10, pady=5)
        
        help_text = f"""🎯 CÓMO USAR EL AUTOCLICKER:

1. ⚙️ Configura el intervalo y tipo de click
2. 📍 Selecciona dónde hacer click:
   • "Seleccionar Posición" → Haz click en pantalla
   • "Usar Posición Actual" → Usa posición del mouse
3. 🚀 INICIAR:
   • Botón verde "INICIAR AUTOCLICKER"
   • O presiona '{self.hotkey.get()}' (más cómodo)
4. ⏹ DETENER:
   • Botón rojo "DETENER" 
   • O presiona '{self.hotkey.get()}' nuevamente
   • O mueve mouse a esquina superior izquierda

⚠️ Para Minecraft: 
• Usa 0.05-0.1 segundos para click rápido
• Click izquierdo para romper bloques
• Click derecho para colocar bloques"""
        
        help_label = tk.Label(help_frame, text=help_text, justify="left", 
                             font=("Arial", 9), fg="dark blue")
        help_label.pack(anchor="w")
        
    def select_position(self):
        """Permite al usuario seleccionar una posición haciendo click"""
        self.status_label.config(text="Haz click en la posición deseada...", fg="orange")
        self.root.withdraw()  # Ocultar ventana
        
        def on_click(x, y, button, pressed):
            if pressed:
                self.click_position = (x, y)
                self.position_label.config(text=f"Posición: ({x}, {y})", fg="green")
                self.status_label.config(text="Posición seleccionada", fg="green")
                self.root.deiconify()  # Mostrar ventana
                return False  # Detener listener
        
        # Crear listener temporal para capturar click
        with MouseListener(on_click=on_click):
            time.sleep(0.1)  # Pequeña pausa
            while self.status_label.cget("text") == "Haz click en la posición deseada...":
                time.sleep(0.1)
                
    def use_current_position(self):
        """Usa la posición actual del mouse"""
        x, y = pyautogui.position()
        self.click_position = (x, y)
        self.position_label.config(text=f"Posición: ({x}, {y})", fg="green")
        self.status_label.config(text="Posición actual guardada", fg="green")
        
    def start_clicking(self):
        """Inicia el autoclicker"""
        if self.click_position == (0, 0):
            messagebox.showwarning("Advertencia", "Por favor selecciona una posición primero")
            return
            
        if self.clicking:
            return
            
        self.clicking = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.status_label.config(text="AutoClicker ACTIVO", fg="red")
        
        # Iniciar thread de clicking
        self.click_thread = threading.Thread(target=self.click_loop, daemon=True)
        self.click_thread.start()
        
    def stop_clicking(self):
        """Detiene el autoclicker"""
        self.clicking = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.status_label.config(text="AutoClicker DETENIDO", fg="green")
        
    def click_loop(self):
        """Loop principal de clicking"""
        click_count = 0
        max_clicks = self.click_count.get() if self.click_mode.get() == "count" else float('inf')
        
        while self.clicking and click_count < max_clicks:
            try:
                # Realizar click en la posición especificada
                pyautogui.click(self.click_position[0], self.click_position[1], 
                               button=self.click_type.get())
                click_count += 1
                
                # Actualizar contador en la UI
                self.root.after(0, lambda: self.clicks_counter.config(
                    text=f"Clicks realizados: {click_count}"))
                
                # Esperar el intervalo especificado
                time.sleep(self.click_interval.get())
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Error en clicking: {e}"))
                break
                
        # Auto-detener si se completó el conteo
        if click_count >= max_clicks:
            self.root.after(0, self.stop_clicking)
            
    def start_hotkey_listener(self):
        """Inicia el listener para la tecla de activación"""
        def on_press(key):
            try:
                if hasattr(key, 'name') and key.name.lower() == self.hotkey.get().lower():
                    if self.clicking:
                        self.root.after(0, self.stop_clicking)
                    else:
                        self.root.after(0, self.start_clicking)
            except AttributeError:
                pass
                
        self.hotkey_listener = KeyboardListener(on_press=on_press)
        self.hotkey_listener.daemon = True
        self.hotkey_listener.start()
        
    def update_hotkey(self, event=None):
        """Actualiza la tecla de activación"""
        if self.hotkey_listener:
            self.hotkey_listener.stop()
        self.start_hotkey_listener()
        
    def run(self):
        """Ejecuta la aplicación"""
        try:
            self.root.mainloop()
        finally:
            if self.hotkey_listener:
                self.hotkey_listener.stop()

if __name__ == "__main__":
    # Configurar pyautogui
    pyautogui.FAILSAFE = True  # Mover mouse a esquina superior izquierda para detener
    pyautogui.PAUSE = 0.01
    
    app = AutoClicker()
    app.run()
