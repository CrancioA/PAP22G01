"""
Extend existing functionality in of app1 class SystemInformation to support
- getting available memory (total, used, free)
- getting routing table and displaying it as a table
"""

import os
import re
from itertools import islice
from tabulate import tabulate

class SystemInformation:
    @staticmethod
    def ip_getter():
        result = os.popen('ipconfig')
        for line in result.readlines():
            pattern = 'IPv4 Address.*:(?P<IP>.*)'
            match = re.search(pattern, line)
            if match:
                print(match.group("IP"))

    @staticmethod
    def cp_usage():
        result = os.popen('wmic cpu get loadpercentage')
        for line in result.readlines():
            pattern = "(?P<CP_Usage>\d+)"
            match = re.search(pattern, line)
            if match:
                print(f"CPU Load percentage is {match.group('CP_Usage')}")

    @staticmethod
    def available_memory():
        result = os.popen('systeminfo')
        for line in result.readlines():
            pattern = "Virtual Memory: Max Size:(?P<total>.*)"
            match = re.search(pattern, line)
            if match:
                print(f"Total Virtual Memory:{match.group('total')}")
        result1 = os.popen('systeminfo')
        for line1 in result1.readlines():
            pattern1 = "Virtual Memory: Available:(?P<free>.*)"
            match1 = re.search(pattern1, line1)
            if match1:
                print(f"Free Virtual Memory:{match1.group('free')}")
        result2 = os.popen('systeminfo')
        for line2 in result2.readlines():
            pattern2 = "Virtual Memory: In Use:(?P<used>.*)"
            match2 = re.search(pattern2, line2)
            if match2:
                print(f"Used Virtual Memory:{match2.group('used')}")

        print(50 * "#")

        result = os.popen('systeminfo')
        for line in result.readlines():
            pattern = "Total Physical Memory:(?P<total>.*)"
            match = re.search(pattern, line)
            if match:
                print(f"Total Physical Memory:{match.group('total')}")
                max_memory = match.group('total')
        result1 = os.popen('systeminfo')
        for line1 in result1.readlines():
            pattern1 = "Available Physical Memory:(?P<free>.*)"
            match1 = re.search(pattern1, line1)
            if match1:
                print(f"Free Physical Memory:{match1.group('free')}")
                available_memory = match1.group('free')
                used_memory = str(
                    int(max_memory[:-3].replace(',', '')) - int(available_memory[:-3].replace(',', '')))
                print(f"Used Physical Memory: {used_memory} MB")

    @staticmethod
    def routing_table():
        result = os.popen('route print').read()
        pattern = r"IPv4 Route Table\n(?P<routing_table>[^\r\n]+((\r|\n|\r\n)[^\r\n]+)*=)"  # regex-ul l-am luat de la Bogdan ca efectiv nu imi mergea nici un regex facut de mine
        match = re.search(pattern, result)
        if match:
            table = str(match.group("routing_table")).split()  # am transformat string-ul intr-o lista cu un singur element
            # print(table)
            length_to_split = [3, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # am impartit lista cu un singur element in subliste cu lungimi diferite
            inputt = iter(table)
            new_table = [list(islice(inputt, elem)) for elem in length_to_split]
            # print(new_table)
            new_table.pop(0) # am eleminat sublistele de care nu aveam nevoie
            new_table.pop(0)
            new_table.pop(11)
            # print(new_table)
            print(tabulate(new_table, headers=["Network Destination", "Netmask", "Gateway", "Interface", "Metric"]))


# SystemInformation.ip_getter()
# SystemInformation.cp_usage()
SystemInformation.available_memory()
SystemInformation.routing_table()

