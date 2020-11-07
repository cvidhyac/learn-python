import pyperclip, sys, webbrowser

# When invoked from a website with a copied value of address,
# or a system argv argument, then google maps site is opened for the corresponding address


def capture_address():
    address = ''
    if len(sys.argv) > 1:
      address = ' '.join(sys.argv[1:])
    else:
      address = pyperclip.paste()
    return address


def open_address():
    gmaps_url = "https://maps.google.com/maps/place/"
    address = capture_address()
    url_path = gmaps_url + address
    webbrowser.open(url_path)


open_address()

