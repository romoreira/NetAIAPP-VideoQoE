import subprocess
import os
from datetime import datetime

# Lista de URLs ou fontes de streaming
streams = {
    "stream1": "http://example.com/stream1.m3u8",
    "stream2": "http://example.com/stream2.m3u8",
    "stream3": "http://example.com/stream3.m3u8",
}

# Diretório para armazenar os vídeos
output_dir = "captured_videos"
os.makedirs(output_dir, exist_ok=True)

# Duração máxima de captura para cada vídeo (em segundos)
capture_duration = 60  # 1 minuto

# Loop para processar cada stream
for name, url in streams.items():
    # Nome do arquivo de saída
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"{name}_{timestamp}.mp4")
    
    # Comando ffmpeg
    command = [
        "ffmpeg",
        "-i", url,                # URL do stream
        "-t", str(capture_duration),  # Duração de captura
        "-c:v", "copy",           # Copiar o codec de vídeo sem recodificar
        "-c:a", "copy",           # Copiar o codec de áudio sem recodificar
        output_file               # Arquivo de saída
    ]
    
    print(f"Capturando stream '{name}' e salvando em '{output_file}'...")
    subprocess.run(command, check=True)
    print(f"Stream '{name}' capturado com sucesso!")

print("Todos os streams foram capturados.")

