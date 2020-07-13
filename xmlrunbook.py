from nornir import InitNornir
from nornir.plugins.tasks.networking import netconf_get
from rich import print
from xml.dom import minidom
import itertools

nr = InitNornir(config_file="config.yaml")

def ipvzero(task):
    result = task.run(task=netconf_get, path="interfaces//statistics[in-unicast-pkts > 0]")
    resulter = result.result
    unicasts = minidom.parseString(resulter).getElementsByTagName("in-unicast-pkts")
    inter = minidom.parseString(resulter).getElementsByTagName("name")
    for x,y in zip(unicasts, inter):
        packets = x.firstChild.nodeValue
        namers = y.firstChild.nodeValue
        print(f"[green]{task.host}:[/green] Interfaces receiving packets: [u]{namers}[/u] (total:{packets})\n")

nr.run(task=ipvzero)
