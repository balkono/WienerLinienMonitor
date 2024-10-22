import requests,re
from datetime import datetime

def get_data(divas):
    print("Getting available WienerLinien monitoring data via DIVA numbers...\n")
    url="https://www.wienerlinien.at/ogd_realtime/monitor?stopId=0&diva="
    datalist=[]
    for e in divas:
        datalist.insert(0,requests.get(url+e).json())
    return datalist

def get_options(datlst):
    i=0
    for entry in datlst:
        print(str(i)+": "+get_name(entry))
        i=i+1

def get_name(entry):
    try:
        name = entry["data"]["monitors"][0]["locationStop"]["properties"]["title"]
    except KeyError:
        return "station not available now - closed"
    return name

def sel_entry():
    return input("Which station's departures shall be shown? Enter number of entry or \"q\" to exit!")

def get_time(raw):
    try:
        tim=raw["timeReal"]
    except KeyError:
        try:
            tim=raw["timePlanned"]
        except KeyError:
            return "no time available"
    x=re.findall(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}",tim)
    d= datetime.fromisoformat(x[0])
    return d.strftime("%H:%M:%S, %d.%m.%y")