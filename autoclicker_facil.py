import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui
import keyboard

class AutoClickerFacil:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 AutoClicker FÁCIL para Minecraft")
        self.root.geometry("480x580")
        self.root.resizable(True, True)
        
        # Variables
        self.clicking = False
        self.click_position = (0, 0)
        self.click_count = 0
        
        self.setup_ui()
        
        # Configurar hotkey F6
        keyboard.add_hotkey('f6', self.toggle_clicking)
        
    def setup_ui(self):
        # Título grande
        title = tk.Label(self.root, text="🎮 AutoClicker FÁCIL", 
                        font=("Arial", 18, "bold"), fg="blue")
        title.pack(pady=10)
        
        subtitle = tk.Label(self.root, text="¡Solo 3 pasos para usar!", 
                           font=("Arial", 11), fg="gray")
        subtitle.pack(pady=2)
        
        # PASO 1
        paso1_frame = tk.Frame(self.root, bg="lightblue", relief="raised", bd=2)
        paso1_frame.pack(fill="x", padx=15, pady=5)
        
        tk.Label(paso1_frame, text="PASO 1: ⚙️ CONFIGURAR", 
                font=("Arial", 12, "bold"), bg="lightblue").pack(pady=3)
        
        config_frame = tk.Frame(paso1_frame, bg="lightblue")
        config_frame.pack(pady=3)
        
        tk.Label(config_frame, text="Velocidad:", font=("Arial", 10), bg="lightblue").pack(side="left")
        self.speed_var = tk.StringVar(value="normal")
        
        speeds = [("Lento (1s)", "lento"), ("Normal (0.1s)", "normal"), ("Rápido (0.05s)", "rapido")]
        for text, value in speeds:
            tk.Radiobutton(config_frame, text=text, variable=self.speed_var, 
                          value=value, bg="lightblue", font=("Arial", 9)).pack(side="left", padx=3)
        
        tipo_frame = tk.Frame(paso1_frame, bg="lightblue")
        tipo_frame.pack(pady=3)
        
        tk.Label(tipo_frame, text="Tipo:", font=("Arial", 10), bg="lightblue").pack(side="left")
        self.click_type = tk.StringVar(value="left")
        
        tk.Radiobutton(tipo_frame, text="🔨 Izquierdo (Minar)", variable=self.click_type, 
                      value="left", bg="lightblue", font=("Arial", 9)).pack(side="left", padx=3)
        tk.Radiobutton(tipo_frame, text="🧱 Derecho (Colocar)", variable=self.click_type, 
                      value="right", bg="lightblue", font=("Arial", 9)).pack(side="left", padx=3)
        
        # PASO 2
        paso2_frame = tk.Frame(self.root, bg="lightgreen", relief="raised", bd=2)
        paso2_frame.pack(fill="x", padx=15, pady=5)
        
        tk.Label(paso2_frame, text="PASO 2: 📍 SELECCIONAR POSICIÓN", 
                font=("Arial", 12, "bold"), bg="lightgreen").pack(pady=3)
        
        self.position_label = tk.Label(paso2_frame, text="❌ No seleccionada", 
                                      font=("Arial", 11, "bold"), fg="red", bg="lightgreen")
        self.position_label.pack(pady=2)
        
        pos_buttons = tk.Frame(paso2_frame, bg="lightgreen")
        pos_buttons.pack(pady=3)
        
        tk.Button(pos_buttons, text="🎯 Hacer Click en Pantalla", 
                 command=self.select_position, font=("Arial", 10, "bold"),
                 bg="orange", fg="white").pack(side="left", padx=3)
        
        tk.Button(pos_buttons, text="📍 Usar Posición Actual", 
                 command=self.use_current_position, font=("Arial", 10, "bold"),
                 bg="purple", fg="white").pack(side="left", padx=3)
        
        # PASO 3
        paso3_frame = tk.Frame(self.root, bg="lightyellow", relief="raised", bd=2)
        paso3_frame.pack(fill="x", padx=15, pady=5)
        
        tk.Label(paso3_frame, text="PASO 3: 🚀 ¡INICIAR!", 
                font=("Arial", 12, "bold"), bg="lightyellow").pack(pady=3)
        
        # Botón gigante de iniciar
        self.main_button = tk.Button(paso3_frame, text="🚀 HACER CLICK AUTOMÁTICO", 
                                    command=self.toggle_clicking, 
                                    font=("Arial", 14, "bold"), bg="green", fg="white",
                                    height=2)
        self.main_button.pack(pady=8, padx=15, fill="x")
        
        # Tecla alternativa
        tk.Label(paso3_frame, text="O presiona F6 en cualquier momento", 
                font=("Arial", 9), bg="lightyellow", fg="blue").pack(pady=2)
        
        # Estado
        self.status_frame = tk.Frame(self.root, bg="lightgray", relief="sunken", bd=2)
        self.status_frame.pack(fill="x", padx=15, pady=5)
        
        self.status_label = tk.Label(self.status_frame, text="🟢 Listo para usar", 
                                    font=("Arial", 11, "bold"), fg="green", bg="lightgray")
        self.status_label.pack(pady=3)
        
        self.counter_label = tk.Label(self.status_frame, text="Clicks realizados: 0", 
                                     font=("Arial", 9), bg="lightgray")
        self.counter_label.pack(pady=1)
        
    def get_interval(self):
        speeds = {"lento": 1.0, "normal": 0.1, "rapido": 0.05}
        return speeds[self.speed_var.get()]
    
    def select_position(self):
        self.status_label.config(text="🎯 Haz click donde quieras...", fg="orange")
        self.root.withdraw()  # Ocultar ventana
        
        # Esperar 1 segundo
        time.sleep(1)
        
        # Obtener posición al hacer click
        def on_click():
            x, y = pyautogui.position()
            self.click_position = (x, y)
            self.position_label.config(text=f"✅ Posición: ({x}, {y})", fg="green")
            self.status_label.config(text="✅ Posición guardada", fg="green")
            self.root.deiconify()  # Mostrar ventana
        
        # Simular selección de posición
        self.root.after(2000, on_click)  # Después de 2 segundos, usar posición actual
        
    def use_current_position(self):
        x, y = pyautogui.position()
        self.click_position = (x, y)
        self.position_label.config(text=f"✅ Posición: ({x}, {y})", fg="green")
        self.status_label.config(text="✅ Posición actual guardada", fg="green")
        
    def toggle_clicking(self):
        if self.click_position == (0, 0):
            messagebox.showwarning("⚠️ Falta configurar", 
                                  "Primero selecciona una posición en el PASO 2")
            return
            
        if not self.clicking:
            self.start_clicking()
        else:
            self.stop_clicking()
            
    def start_clicking(self):
        self.clicking = True
        self.main_button.config(text="⏹ DETENER AUTOCLICKER", bg="red")
        self.status_label.config(text="🔴 AUTOCLICKER ACTIVO", fg="red")
        
        # Iniciar en thread separado
        thread = threading.Thread(target=self.click_loop, daemon=True)
        thread.start()
        
    def stop_clicking(self):
        self.clicking = False
        self.main_button.config(text="🚀 HACER CLICK AUTOMÁTICO", bg="green")
        self.status_label.config(text="🟢 AutoClicker detenido", fg="green")
        
    def click_loop(self):
        while self.clicking:
            try:
                pyautogui.click(self.click_position[0], self.click_position[1], 
                               button=self.click_type.get())
                self.click_count += 1
                
                # Actualizar contador
                self.root.after(0, lambda: self.counter_label.config(
                    text=f"Clicks realizados: {self.click_count}"))
                
                time.sleep(self.get_interval())
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
                break
    
    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    app = AutoClickerFacil()
    app.run()
