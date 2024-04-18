import webview

if __name__ == '__main__':
    # Create a browser window with the specified URL
    webview.create_window("Comfort Airlines", "http://127.0.0.1/comfort-airlines", fullscreen=True)

    # Run the GUI event loop
    webview.start()
    