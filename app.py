import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
routerip = "" # "192.168.20.176"
auth = ("","")  #('admin','ubuntu')


#Set login credentials
@app.post('/login')
def login():
    global routerip
    global auth
    body = request.get_json()
    routerip = body['ip']
    auth = (body['username'], body['password'])
    return jsonify({"status": "success"}), 200

#Get all interfaces from the device
@app.get("/rest/interface")
def getInterfaces():
     api_url = "http://"+ routerip +"/rest/interface"
     response = requests.get(api_url, auth=auth)
     return response.json(), response.status_code


#Get only the wireless interfaces
@app.get("/rest/interface/wireless")
def getWirelessInterfaces():
    api_url = "http://"+ routerip +"/rest/interface/wireless"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code


#CRUD - Bridge interfaces and respective ports
#Read
@app.get("/rest/interface/bridge")
def getBridges():
    api_url = "http://"+ routerip +"/rest/interface/bridge"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/interface/bridge")
def putBridges():
    api_url = "http://"+ routerip +"/rest/interface/bridge"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@app.patch("/rest/interface/bridge")
def patchBridges():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/bridge/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code
    
#Delete
@app.delete("/rest/interface/bridge")
def deleteBridges():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/bridge/"+id
    response = requests.delete(api_url, auth=auth)
    return '', response.status_code


#Wireless interfaces

#Enable wireless interfaces
@app.post("/rest/interface/wireless/enable")
def enableWireless():
    api_url = "http://"+ routerip +"/rest/interface/wireless/enable"
    body = request.get_json()
    response = requests.post(api_url, auth=auth, data=json.dumps(body), headers={'content-type':'application/json'})
    return '', response.status_code

#Disable wireless interfaces
@app.post("/rest/interface/wireless/disable")
def disableWireless():
    body = request.get_json()
    api_url = "http://"+ routerip +"/rest/interface/wireless/disable"
    response = requests.post(api_url, auth=auth, data=json.dumps(body), headers={'content-type':'application/json'})
    return '', response.status_code

#Update
@app.patch("/rest/interface/wireless")
def patchWireless():    
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireless/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code


#CRUD - Port interfaces

#Read
@app.get("/rest/interface/bridge/port")
def getPorts():
    bridgeName = request.args.get('bridge');
    if(bridgeName != None):
        api_url = "http://"+ routerip +"/rest/interface/bridge/port?bridge="+bridgeName
    else:
        api_url = "http://"+ routerip +"/rest/interface/bridge/port"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/interface/bridge/port")
def insertPorts():
    api_url = "http://"+ routerip + "/rest/interface/bridge/port"
    body = request.get_json()
    response = requests.put(api_url, auth=auth, headers={'content-type':'application/json'}, data=json.dumps(body))
    return response.json(), response.status_code

#Delete
@app.delete("/rest/interface/bridge/port")
def deletePorts():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/bridge/port/"+id
    response = requests.delete(api_url, auth=auth)
    return '', response.status_code


#CRUD - Security profiles

#Read
@app.get("/rest/interface/wireless/security-profiles")
def getSecurityProfiles():
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/interface/wireless/security-profiles")
def putSecurityProfiles():
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@app.patch("/rest/interface/wireless/security-profiles")
def patchSecurityProfiles():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@app.delete("/rest/interface/wireless/security-profiles")
def deleteSecurityProfiles():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles/"+id
    response = requests.delete(api_url, auth=auth)
    return '' , response.status_code


#CRUD - Static routes

#Read
@app.get("/rest/ip/route")
def getStaticRoutes():
    api_url = "http://"+ routerip +"/rest/ip/route"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/ip/route")
def putStaticRoutes():
    api_url = "http://"+ routerip +"/rest/ip/route"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@app.patch("/rest/ip/route")
def patchStaticRoutes():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/route/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@app.delete("/rest/ip/route")
def deleteStaticRoutes():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/route/"+id
    response = requests.delete(api_url, auth=auth)
    return '', response.status_code


#CRUD - IP addresses

#Read
@app.get("/rest/ip/address")
def getAddresses():
    api_url = "http://"+ routerip +"/rest/ip/address"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/ip/address")
def putAddresses():
    api_url = "http://"+ routerip +"/rest/ip/address"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@app.patch("/rest/ip/address")
def patchAddresses():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/address/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@app.delete("/rest/ip/address")
def deleteAddresses():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/address/"+id
    response = requests.delete(api_url, auth=auth)
    return '', response.status_code


#CRUD - DHCP server

#Read
@app.get("/rest/ip/dhcp-server")
def getDHCPServer():
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/ip/dhcp-server")
def putDHCPServer():
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@app.patch("/rest/ip/dhcp-server")
def patchDHCPServer():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@app.delete("/rest/ip/dhcp-server")
def deleteDHCPServer():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server/"+id
    response = requests.delete(api_url, auth=auth)
    return '', response.status_code

#CRUD - DHCP pools

#Read
@app.get("/rest/ip/pool")
def getDHCPPools():
    api_url = "http://"+ routerip +"/rest/ip/pool"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/ip/pool")
def putDHCPPools():
    api_url = "http://"+ routerip +"/rest/ip/pool"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@app.patch("/rest/ip/pool")
def patchDHCPPools():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/pool/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@app.delete("/rest/ip/pool")
def deleteDHCPPools():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/pool/"+id
    response = requests.delete(api_url, auth=auth)
    return '', response.status_code


#Activate/Deactivate/Configure DNS server

#Read
@app.get("/rest/ip/dns")
def getDNS():
    api_url = "http://"+ routerip +"/rest/ip/dns"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Update
@app.post("/rest/ip/dns/set")
def postDNS():
    api_url = "http://"+ routerip +"/rest/ip/dns/set"
    body = request.get_json()
    response = requests.post(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code
#Activate/Deactivate/Configure DNS static entries

#Read
@app.get("/rest/ip/dns/static")
def getDNSStatic():
    api_url = "http://"+ routerip +"/rest/ip/dns/static"
    response = requests.get(api_url, auth=auth)
    return response.json(), response.status_code

#Create
@app.put("/rest/ip/dns/static")
def putDNSStatic():
    api_url = "http://"+ routerip +"/rest/ip/dns/static"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@app.patch("/rest/ip/dns/static")
def patchDNSStatic():
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/dns/static/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=auth, headers={'content-type':'application/json'})
    return response.json(), response.status_code
