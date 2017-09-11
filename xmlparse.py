from urllib import request
import xml.etree.ElementTree as ET


file = request.urlopen('http://netapps-web.ucsd.edu/maildb/expiring-users.xml')

tree = ET.parse(file)

file.close()

root = tree.getroot()

sscf_depts ={"Anthropology": [],
            "Cognitive Science": [],
            "Communication": [],
            "Economics": [],
            "Education Studies": [],
            "Trio Outreach Programs": [],
            "Ethnic Studies": [],
            "Linguistics": [],
            "Political Science": [],
            "Psychology": [],
            "Sociology": []}

for row in root.iter('row'):
    x = row.find('department').text
    if x in sscf_depts:
        sscf_depts[x].append(row.find('mailname').text)

for key in sscf_depts:
        if sscf_depts[key]:
            filename = key + "expired.txt"
            with open(filename, 'w') as log:
                for uname in sscf_depts[key]:
                    log.write('{}\n'.format(uname))

input("Press enter to close")