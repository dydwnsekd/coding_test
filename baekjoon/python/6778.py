import sys

TroyMartian = {"antenna": 3, "eyes": 4}
VladSaturnian = {"antenna": 6, "eyes": 2}
GraemeMercurian = {"antenna": 2, "eyes": 3}

antenna = int(sys.stdin.readline())
eyes = int(sys.stdin.readline())

if antenna >= TroyMartian["antenna"] and eyes <= TroyMartian["eyes"]:
    print("TroyMartian")
if antenna <= VladSaturnian["antenna"] and eyes >= VladSaturnian["eyes"]:
    print("VladSaturnian")
if antenna <= GraemeMercurian["antenna"] and eyes <= GraemeMercurian["eyes"]:
    print("GraemeMercurian")
