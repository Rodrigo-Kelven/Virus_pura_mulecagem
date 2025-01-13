import subprocess
import time
import winreg

def listar_programas_instalados():
    """Lista todos os programas instalados no Windows."""
    programas = []
    # Caminhos comuns no registro onde os programas instalados são listados
    caminhos = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for caminho in caminhos:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, caminho) as chave:
                for i in range(0, winreg.QueryInfoKey(chave)[0]):
                    try:
                        nome_programa = winreg.EnumValue(chave, i)[0]
                        caminho_programa = winreg.EnumValue(chave, i)[1]
                        # Adiciona o caminho do executável à lista
                        programas.append(caminho_programa)
                    except OSError:
                        continue
        except FileNotFoundError:
            continue

    return programas

def abrir_programas(programas):
    """Abre todos os programas na lista."""
    for programa in programas:
        try:
            subprocess.Popen(programa)
            time.sleep(0.1)  # Pequena pausa para evitar sobrecarga
        except Exception as e:
            print(f"Erro ao abrir {programa}: {e}")

if __name__ == "__main__":
    programas_instalados = listar_programas_instalados()
    abrir_programas(programas_instalados)
