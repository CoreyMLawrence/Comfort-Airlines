import webview
import threading
import subprocess
import os

def start_server():
    # Bind to a specific loopback address to avoid port overlap
    subprocess.Popen(["python3", "-m", "http.server", "-b", "127.0.0.2"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    
    # Create a browser window with the specified URL
    webview.create_window("Comfort Airlines", "http://127.0.0.2:8000", fullscreen=True)

    # Run the GUI event loop
    webview.start()
