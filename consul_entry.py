import subprocess
import json
from base64 import b64decode

from configs import DEFAULT_KV_ENDPOINT

def PutKv(key, val):
    try:
        url = "curl -s -k --request PUT --data " + val + " " + DEFAULT_KV_ENDPOINT + key
        returnval = subprocess.Popen(url, shell=True, stdout=subprocess.PIPE).stdout
    except:
        print("Error occured")
        raise

    print(key, ":" ,val, "successfully put")

def GetKv(key, recurse=False):
    try:
        url = "curl -s -k " + DEFAULT_KV_ENDPOINT + key
        url = url + "?recurse=true" if recurse else url
        returnval = subprocess.Popen(url , shell=True, stdout=subprocess.PIPE) #+ "/\?recurse=true" if recurse else ""
        val = returnval.stdout.read()
        if "?keys" == key:
            return val
        ret_val = json.loads(val.decode("utf-8"))
        print ({x['Key']:b64decode(x['Value']).decode('utf-8') for x in ret_val})
    except:
        print(key, ": Key not found!, please retry")


def DeleteKv(key, recurse=False):
    try:
        url = "curl -s -k --request DELETE " + DEFAULT_KV_ENDPOINT + key
        url = url + "?recurse=true" if recurse else url
        returnval = subprocess.Popen(url, shell=True, stdout=subprocess.PIPE).stdout
        print(returnval)
    except:
        print("invalid key!")
        raise

    print(key, "deleted!")
    #print(returnval)

def printList():
    print("******************************************\n")
    print("press 1 to put key-val")
    print("press 2 to get val")
    print("press 3 to delete a key-val pair")
    print("******************************************\n")

    choice = int(input())
    Switch(choice)

def Switch(argument):
    switcher = {
        1: PutKv,
        2: GetKv,
        3: DeleteKv,

    }
    #function call
    switcher[argument]()


if __name__ == "__main__":
    while True:
        printList()