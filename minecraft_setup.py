import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

class MinecraftAutoClickerSetup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 Configurador AutoClicker para Minecraft")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Título
        title_label = tk.Label(self.root, text="⛏️ AutoClicker para Minecraft", 
                              font=("Arial", 18, "bold"), fg="green")
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(self.root, text="Configuraciones predefinidas para diferentes actividades", 
                                 font=("Arial", 10), fg="gray")
        subtitle_label.pack(pady=5)
        
        # Frame de actividades
        activities_frame = ttk.LabelFrame(self.root, text="Selecciona tu actividad en Minecraft", padding=15)
        activities_frame.pack(fill="x", padx=20, pady=10)
        
        self.activity = tk.StringVar(value="mining")
        
        activities = [
            ("⛏️ Minar bloques rápido", "mining", "0.05 segundos, Click Izquierdo"),
            ("🧱 Colocar bloques", "building", "0.15 segundos, Click Derecho"),
            ("🎣 Pescar AFK", "fishing", "1.0 segundos, Click Derecho"),
            ("⚔️ Combate/Atacar", "combat", "0.1 segundos, Click Izquierdo"),
            ("🌾 Farmear cultivos", "farming", "0.3 segundos, Click Izquierdo"),
            ("🔧 Craftear en masa", "crafting", "0.2 segundos, Click Izquierdo"),
            ("⚙️ Configuración personalizada", "custom", "Elige tus propios valores")
        ]
        
        for text, value, description in activities:
            frame = tk.Frame(activities_frame)
            frame.pack(fill="x", pady=2)
            
            ttk.Radiobutton(frame, text=text, variable=self.activity, value=value).pack(anchor="w")
            tk.Label(frame, text=f"  → {description}", font=("Arial", 9), fg="blue").pack(anchor="w")
        
        # Frame de configuración personalizada
        self.custom_frame = ttk.LabelFrame(self.root, text="Configuración Personalizada", padding=10)
        self.custom_frame.pack(fill="x", padx=20, pady=10)
        
        self.custom_interval = tk.DoubleVar(value=0.1)
        self.custom_click_type = tk.StringVar(value="left")
        
        # Intervalo personalizado
        tk.Label(self.custom_frame, text="Intervalo (segundos):").pack(anchor="w")
        interval_frame = tk.Frame(self.custom_frame)
        interval_frame.pack(fill="x", pady=2)
        
        tk.Scale(interval_frame, from_=0.01, to=2.0, resolution=0.01, 
                orient="horizontal", variable=self.custom_interval).pack(side="left", fill="x", expand=True)
        tk.Entry(interval_frame, textvariable=self.custom_interval, width=8).pack(side="right")
        
        # Tipo de click personalizado
        tk.Label(self.custom_frame, text="Tipo de click:").pack(anchor="w", pady=(10,0))
        click_frame = tk.Frame(self.custom_frame)
        click_frame.pack(fill="x")
        
        ttk.Radiobutton(click_frame, text="Izquierdo", variable=self.custom_click_type, value="left").pack(side="left")
        ttk.Radiobutton(click_frame, text="Derecho", variable=self.custom_click_type, value="right").pack(side="left")
        ttk.Radiobutton(click_frame, text="Medio", variable=self.custom_click_type, value="middle").pack(side="left")
        
        # Frame de instrucciones
        instructions_frame = ttk.LabelFrame(self.root, text="📋 Instrucciones", padding=10)
        instructions_frame.pack(fill="x", padx=20, pady=10)
        
        instructions_text = """1. Selecciona la actividad que vas a realizar
2. Haz click en "Lanzar AutoClicker"
3. En Minecraft, posiciona el mouse donde necesites
4. Presiona F6 para iniciar/detener el autoclicker

⚠️ Importante:
• Asegúrate de que Minecraft esté en modo ventana
• Algunos servidores prohíben autoclickers
• Usa velocidades moderadas para evitar detección"""
        
        tk.Label(instructions_frame, text=instructions_text, justify="left", 
                font=("Arial", 9)).pack(anchor="w")
        
        # Botones
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", padx=20, pady=20)
        
        launch_button = tk.Button(button_frame, text="🚀 Lanzar AutoClicker", 
                                 command=self.launch_autoclicker, 
                                 bg="green", fg="white", font=("Arial", 12, "bold"))
        launch_button.pack(side="left", fill="x", expand=True, padx=2)
        
        simple_button = tk.Button(button_frame, text="📝 Versión Simple", 
                                 command=self.launch_simple, 
                                 bg="blue", fg="white", font=("Arial", 12, "bold"))
        simple_button.pack(side="left", fill="x", expand=True, padx=2)
        
        # Estado
        self.status_label = tk.Label(self.root, text="Listo para configurar", 
                                    fg="green", font=("Arial", 10, "bold"))
        self.status_label.pack(pady=5)
        
    def get_config_for_activity(self):
        """Retorna la configuración para la actividad seleccionada"""
        configs = {
            "mining": (0.05, "left"),
            "building": (0.15, "right"),
            "fishing": (1.0, "right"),
            "combat": (0.1, "left"),
            "farming": (0.3, "left"),
            "crafting": (0.2, "left"),
            "custom": (self.custom_interval.get(), self.custom_click_type.get())
        }
        return configs.get(self.activity.get(), (0.1, "left"))
    
    def launch_autoclicker(self):
        """Lanza el autoclicker principal con configuración"""
        try:
            interval, click_type = self.get_config_for_activity()
            
            # Crear archivo de configuración temporal
            config_content = f"""# Configuración automática para {self.activity.get()}
INTERVAL = {interval}
CLICK_TYPE = "{click_type}"
ACTIVITY = "{self.activity.get()}"
"""
            
            with open("minecraft_config.py", "w") as f:
                f.write(config_content)
            
            self.status_label.config(text="Iniciando AutoClicker...", fg="blue")
            self.root.update()
            
            # Ejecutar autoclicker
            subprocess.Popen([sys.executable, "autoclicker.py"])
            
            self.status_label.config(text="AutoClicker iniciado con éxito!", fg="green")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el autoclicker:\n{e}")
            
    def launch_simple(self):
        """Lanza la versión simple del autoclicker"""
        try:
            self.status_label.config(text="Iniciando AutoClicker Simple...", fg="blue")
            self.root.update()
            
            subprocess.Popen([sys.executable, "autoclicker_simple.py"])
            
            self.status_label.config(text="AutoClicker Simple iniciado!", fg="green")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el autoclicker simple:\n{e}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MinecraftAutoClickerSetup()
    app.run()
