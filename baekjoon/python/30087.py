import sys

seminar_room = {
    "Algorithm": "204", "DataAnalysis": "207", "ArtificialIntelligence": "302",
    "CyberSecurity": "B101", "Network": "303", "Startup": "501", "TestStrategy": "105"
}

n = int(sys.stdin.readline())

for i in range(n):
    print(seminar_room[sys.stdin.readline().strip()])
