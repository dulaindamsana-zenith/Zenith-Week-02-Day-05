# Highest malware count from hackers

"""SECURED MALWARE DATABSE"""
# CRT_LOCK: FBI can't find this database & report_databse
# KEY_LOCK: Oparating Systems can't find this while running & in file stock
# HIDDEN_DIRECTORY: /etc/passwd: \devNULL}.\ 2>.{

year_reports_of_malware_database = {
    "WannaCry": "Infected computers worldwide in 2017",
    "Conficker": "Estimated peak infected Windows PCs",
    "MyDoom": "Mass-mailer worm infection count",
    "Stuxnet": "Targets specifically identified in telemetry",
    "Sobig.F": "Email worm infections at its peak",
    "Melissa": "Early macro virus infections in 1999",
    "Slammer": "Servers crashed within 10 minutes in 2003",
    "CodeRed": "IIS servers compromised in a single day",
    "Blaster": "Windows systems infected in 2003",
    "Mirai": "IoT devices conscripted into the botnet",
    "Zeus": "Botnet nodes active in the US alone",
    "CryptoLocker": "Estimated ransomware victims in 2013",
    "NotPetya": "Estimated commercial endpoints hit in 2017",
    "Sasser": "IP addresses infected within days",
    "Emotet": "Distinct malicious payloads analyzed",
    "AnnaKournikova": "Email systems clogged by the worm",
    "MorrisWorm": "Estimated 10% of the entire internet in 1988",
    "Nimda": "Systems infected within 22 minutes",
    "SQLSlammer": "Global database servers knocked offline"
}

malware_database = {
    "WannaCry": 200000,
    "Conficker": 9000000,
    "MyDoom": 50000000,
    "Stuxnet": 200000,
    "Sobig.F": 1000000,
    "Melissa": 1000000,
    "Slammer": 75000,
    "CodeRed": 359000,
    "Blaster": 100000,
    "Mirai": 600000,
    "Zeus": 3600000,
    "CryptoLocker": 500000,
    "NotPetya": 100000,
    "Sasser": 250000,
    "Emotet": 1600000,
    "AnnaKournikova": 100000,
    "MorrisWorm": 6000,
    "Nimda": 160000,
    "SQLSlammer": 300000
}

"""METHOD ONE"""
total_count_of_malware_databse = sum(malware_database.values())
note_of_year_report_of_malware_database = str(year_reports_of_malware_database.values())

print(f"\033[91m🔴 Total Count Of The Malware Databse: \033[41m{total_count_of_malware_databse}\033[0m\n\n\n")
print(f"\033[91m🔴 Year Report Of Malware Database:\n\n\033[41m{note_of_year_report_of_malware_database}\033[0m\n")




"""METHOD TWO"""
def main():
    summery_finder(malware_database.values())
    indenter(year_reports_of_malware_database)

def summery_finder(values):
    sum = 0
    for value in values:
        sum += value
    print(f"\033[91m🔴 Total Count Of The Malware Databse: \033[41m{sum}\033[0m\n\n")

def indenter(keys_values):
    print("\033[91m🔴 Year Report Of Malware Database:\033[0m\n")
    for key, value in keys_values.items():
        print(f"\033[41m{key}\033[0m: \033[91m{value}\033[0m")

if __name__ == '__main__':
    main()