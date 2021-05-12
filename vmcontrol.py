import requests
import json
import urllib3
import re

baseURL = "http://127.0.0.1:8697/api/"
username = "student"
password = "Bloempot1!"
valid_cert = False
appformat = "application/vnd.vmware.vmw.rest-v1+json"
headers = {"content-type": appformat, "accept": appformat}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def GetVMs():
    uri = "vms"

    try:
        r = requests.get(baseURL + uri, headers=headers, auth=(username, password), verify=valid_cert)

        if r.status_code == 200:
            response = json.dumps(r.json())
            data = json.loads(response)
            return(data)
    except:
        print("Failed")

def VMOperation(vmList,powerState):
    uri = "/power"
    baseURL = "http://127.0.0.1:8697/api/vms/"
    vmId = vmList["id"]
    vmNameList = vmList["path"]

    vmCompile = re.compile("CSR[0-9][0-9]")
    vmNameSearch = vmCompile.findall(vmNameList)
    vmName = set(vmNameSearch)

    try:
        r = requests.put(baseURL + vmId + uri, headers=headers, auth=(username, password), verify=valid_cert, data=powerState)

        if r.status_code == 200:
            if powerState == "on":
                print("Powerd On: " + str(vmName))
            if powerState == "off":
                print("Powerd Off: " + str(vmName))
            if powerState == "suspend":
                print("Suspended: " + str(vmName))
        else:
            return ("Request failed: " + r.status_code)
    
    except:
        return print("Failed")

def main():
    vmList = GetVMs()
    print(vmList)

if __name__ == '__main__':
    main()