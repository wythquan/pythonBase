import webbrowser

def decorator(func):
    def wrapper(url):
        if "https://" in url:
            func(url)
        else:
            print("Invalid URL")

    return wrapper

@decorator
def open_url(url):
    webbrowser.open(url)

open_url("https://google.com")