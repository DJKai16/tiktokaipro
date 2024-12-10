from rich import print
from rich.panel import Panel
from rich.console import Console
import os
import yt_dlp

console = Console()

def descargar_video_tiktok(url):
    opciones = {
        'outtmpl': 'video_tiktok.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        archivo = "video_tiktok.mp4"
        if os.path.exists(archivo) and os.path.getsize(archivo) < 1024 * 100:
            os.remove(archivo)
            return None, "[bold red]El archivo descargado es demasiado pequeño. Descarga fallida.[/bold red]"
        else:
            return archivo, "[bold green]¡Video descargado exitosamente![/bold green]"
    except Exception as e:
        return None, f"[bold red]Error al descargar el video: {e}[/bold red]"

def main():
    # Título con colores y marco
    print(Panel("[bold green]Descargador de Videos de TikTok[/bold green]", expand=False))

    # Entrada del usuario
    url = console.input("[cyan]Ingresa la URL del video de TikTok: [/cyan] ")

    if not url.strip():
        print("[bold red]Error: La URL no puede estar vacía.[/bold red]")
        return

    # Mensaje de progreso
    print(Panel("[yellow]Descargando el video, por favor espera...[/yellow]", expand=False))

    # Llamada a la función para descargar
    archivo, mensaje = descargar_video_tiktok(url)

    # Mensaje final
    print(mensaje)
    if archivo:
        print(f"[bold magenta]El video se guardó como:[/bold magenta] [underline]{archivo}[/underline]")

if __name__ == "__main__":
    main()