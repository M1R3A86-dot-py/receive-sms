import requests
import json

def receive():
    #get old number
    number = open('number.txt', 'r')
    number = number.read()
    number = number.replace('n', '')
    print(number)

    #requests
    url = 'https://receive-sms.com/newmessages/' + number + '/12016457276'
    r = requests.get(url=url)
    print(r.text)

    #check
    if r.text == '[]':
        receive()
    else:
        #get new number
        idnumber = r.text
        idnumber = idnumber.replace('[', '')
        idnumber = idnumber.replace(']', '')
        print(idnumber)
        idnumber = json.loads(idnumber)["id"]
        #write number in number.txt
        number = open('number.txt', 'w')
        number.write(idnumber)
        number.close()
        #add json
        result = r.text
        rsult = result.replace('[', '')
        rsult = result.replace(']', '')
        resultfile = open('result.json', 'w+')
        resultread = resultfile.read()
        resultread = result.replase(']', '')
        resultfile.write(resultread + ',' + result + ']')
receive()
