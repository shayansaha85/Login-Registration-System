import json

backendDataFile = open("Backend.db", "r")
backendDataUnfiltered = backendDataFile.read()
backendDataFile.close()
backendDataUnfiltered = backendDataUnfiltered.replace("'", '"')
backendData = json.loads(backendDataUnfiltered)

def nextUserSerial():
    numberOfUsers = len(list(backendData[0].keys()))
    return "user" + str(numberOfUsers+1)

# print(nextUserSerial())

def fetchAllUserName():
    listOfUserNames = []
    listOfUsers = []
    users = list(backendData[0].keys())
    for user in users:
        listOfUserNames.append(backendData[0][user]["username"])

    return listOfUserNames

def fetchCreds():
    users = list(backendData[0].keys())
    credentials = {}
    for user in users:
        credentials[backendData[0][user]["username"]] = backendData[0][user]["password"]

    return credentials

def enterData(firstName, username, password, email):
    noOfNewEntry = nextUserSerial()
    backendData[0][noOfNewEntry] = {
        "firstname" : firstName,
        "username" : username,
        "password" : password,
        "email" : email
    }
    contentOfBackendFile = str(backendData)
    fileUpdate = open("Backend.db", "w")
    fileUpdate.write(contentOfBackendFile)
    fileUpdate.close()
    print("File updated successfully")

