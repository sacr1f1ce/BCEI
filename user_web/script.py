import webbrowser

def main():
    url = 'http://127.0.0.1:3000'
    webbrowser.get('chrome').open(url)
    print("Minus one visit")

if __name__ == "__main__":
    main()
