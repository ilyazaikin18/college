# В исходном текстовом файле (radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).

import re

with open('radio_stations.txt', 'r', encoding='UTF-8') as file:
    radio_stations = file.read()
    a = re.findall(r'//\w+.\w+.\w+:', radio_stations)
    print(set(a))   # альтернатива print(a)

