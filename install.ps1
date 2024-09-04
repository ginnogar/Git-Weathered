# Crear un entorno virtual si no existe
if (-not (Test-Path "venv")) {
    python -m venv venv
}

# Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Instalar las dependencias si requirements.txt existe
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
}