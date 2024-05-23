import webview
import threading
import subprocess
import os
import time
import requests

def start_server():
    # Change current directory to the folder where the script resides
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Bind to a specific loopback address to avoid port overlap
    subprocess.Popen(["python3", "-m", "http.server", "-b", "127.0.0.2"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def check_server():
    # Check if the server is up and running
    while True:
        try:
            response = requests.get("http://127.0.0.2:8000")
            if response.status_code == 200:
                # Server is running, create the browser window
                webview.create_window("Comfort Airlines", "http://127.0.0.2:8000", fullscreen=True)
                break
        except requests.ConnectionError:
            # Server not yet running, wait and try again
            time.sleep(0.5)

if __name__ == '__main__':
    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    
    # Check if the server is running and create the window once it is
    check_server()

    # Run the GUI event loop
    webview.start()
