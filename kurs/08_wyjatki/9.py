""" Sprawdź jak wygląda kod modułu antigravity. Korzystając z tego samego sposobu otwarcia dowolnego url
 pozwól użytkownikowi podać adres www.
Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się:
https://
http://
www
bez www
Może się kończyć za pomocą:
.pl
.com
Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy."""
import webbrowser
from urllib.error import URLError


def open_url(a):
    if a[0:8] == 'https://' or a[0:7] == 'http://' or a[0:3] == 'www':
        webbrowser.open(a)
    elif a[-3:] == '.pl' or a[-4:] == ".com":
        webbrowser.open(a)
    else:
        raise URLError('błędny adres')


url = input("Podaj adres www")

try:
    open_url(url)
except URLError as ue:
    print("błędny adres", ue)