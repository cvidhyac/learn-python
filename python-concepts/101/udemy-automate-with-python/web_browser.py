import webbrowser


def open_site(url, address):
    url_path = url + address
    webbrowser.open(url_path)


def demo():
    url = "https://maps.google.com/maps/place/"
    open_site(url, "111 Richmond Street West")


demo()
