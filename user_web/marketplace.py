import webbrowser

def main():
    url = 'http://127.0.0.1:3001'
    
    webbrowser.get('chrome').open(url)
    print("Marketplace visited")

if __name__ == "__main__":
    main()
