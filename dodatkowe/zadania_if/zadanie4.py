"""4. Standardowe limity prędkość wynoszą odpowiednio:
na autostradzie – 140 km/h,
na drodze ekspresowej dwujezdniowej – 120 km/h,
na drodze ekspresowej jednojezdniowej – 100 km/h,
na drodze jednojezdniowej dwukierunkowej – 90 km/
w terenie zabudowanym - 50 km/h
Poproś użytkownika o podanie dowolnej prędkości, a następnie wyświetl na jakiej drodze na pewno się nie porusza (zgodnie z prawem).

Np. input: 112
Nie znajduje się po terenie zabudowany
Nie znajduje się po drodze dwujezdniowej
Nie znajduje się na drodze ekspresowej jednojezdniowej """
limits = {
    140: "autostrada",
    120: "droga ekspresowa dwujezdniowa",
    100: "droga ekspresowa jedno jezdniowa",
    90: "droga jedno jezdniowa dwukierunkowa",
    50: "teren zabudowany"
}
try:
    speed = int(input("Podaj prędkość pojazdu [km/h]"))
except ValueError:
    print("Prędkość w złym formacie")
    speed = 0
for k, v in limits.items():
    if speed > k:
        print("--nie znajduje się na", v)