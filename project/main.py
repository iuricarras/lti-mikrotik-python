import requests
from flask import Flask, request, jsonify, Blueprint, current_app
from flask_cors import CORS
from .config import routerip, authentication
import json
from . import db


main = Blueprint('main', __name__)

def apiRequest(url, method, body=None):
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "https://"+ routerip + url
    if method == 'GET':
        response = requests.get(api_url, auth=authentication, verify=False)
    elif method == 'POST':
        response = requests.post(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'}, verify=False)
    elif method == 'PUT':
        response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'}, verify=False)
    elif method == 'PATCH':
        response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'}, verify=False)
    elif method == 'DELETE':
        response = requests.delete(api_url, auth=authentication, verify=False)
        return '', response.status_code
    return response.json(), response.status_code

#Get all interfaces from the device
@main.get("/rest/interface")
def getInterfaces():
    responseJson, responseStatusCode = apiRequest("/rest/interface", "GET")
    return responseJson, responseStatusCode


#Get only the wireless interfaces
@main.get("/rest/interface/wireless")
def getWirelessInterfaces():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless", "GET")
    return responseJson, responseStatusCode


#CRUD - Bridge interfaces and respective ports
#Read
@main.get("/rest/interface/bridge")
def getBridges():
    responseJson, responseStatusCode = apiRequest("/rest/interface/bridge", "GET")
    return responseJson, responseStatusCode

#Create
@main.put("/rest/interface/bridge")
def putBridges():
    responseJson, responseStatusCode = apiRequest("/rest/interface/bridge", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Update
@main.patch("/rest/interface/bridge")
def patchBridges():
    id = request.args.get('id') 
    responseJson, responseStatusCode = apiRequest("/rest/interface/bridge/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode
    
#Delete
@main.delete("/rest/interface/bridge")
def deleteBridges():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/interface/bridge/"+id, "DELETE")
    return '', responseStatusCode



#Wireless interfaces

#Enable wireless interfaces
@main.post("/rest/interface/wireless/enable")
def enableWireless():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless/enable", "POST", request.get_json())
    return '', responseStatusCode

#Disable wireless interfaces
@main.post("/rest/interface/wireless/disable")
def disableWireless():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless/disable", "POST", request.get_json())
    return '', responseStatusCode

#Update
@main.patch("/rest/interface/wireless")
def patchWireless():    
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode


#CRUD - Port interfaces

#Read
@main.get("/rest/interface/bridge/port")
def getPorts():
    bridgeName = request.args.get('bridge');
    if(bridgeName != None):
        responseJson, responseStatusCode = apiRequest("/rest/interface/bridge/port?bridge="+bridgeName, "GET")
    else:
        responseJson, responseStatusCode = apiRequest("/rest/interface/bridge/port", "GET")
    return responseJson, responseStatusCode

#Create
@main.put("/rest/interface/bridge/port")
def insertPorts():
    responseJson, responseStatusCode = apiRequest("/rest/interface/bridge/port", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Delete
@main.delete("/rest/interface/bridge/port")
def deletePorts():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/interface/bridge/port/"+id, "DELETE")
    return '', responseStatusCode


#CRUD - Security profiles

#Read
@main.get("/rest/interface/wireless/security-profiles")
def getSecurityProfiles():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless/security-profiles", "GET")
    return responseJson, responseStatusCode

#Create
@main.put("/rest/interface/wireless/security-profiles")
def putSecurityProfiles():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless/security-profiles", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Update
@main.patch("/rest/interface/wireless/security-profiles")
def patchSecurityProfiles():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless/security-profiles/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode

#Delete
@main.delete("/rest/interface/wireless/security-profiles")
def deleteSecurityProfiles():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireless/security-profiles/"+id, "DELETE")
    return '' , responseStatusCode


#CRUD - Static routes

#Read
@main.get("/rest/ip/route")
def getStaticRoutes():
    responseJson, responseStatusCode = apiRequest("/rest/ip/route", "GET")
    return responseJson, responseStatusCode

#Create
@main.put("/rest/ip/route")
def putStaticRoutes():
    responseJson, responseStatusCode = apiRequest("/rest/ip/route", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Update
@main.patch("/rest/ip/route")
def patchStaticRoutes():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/route/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode

#Delete
@main.delete("/rest/ip/route")
def deleteStaticRoutes():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/route/"+id, "DELETE")
    return '', responseStatusCode


#CRUD - IP addresses

#Read
@main.get("/rest/ip/address")
def getAddresses():
    responseJson, responseStatusCode = apiRequest("/rest/ip/address", "GET")
    return responseJson, responseStatusCode

#Create
@main.put("/rest/ip/address")
def putAddresses():
    responseJson, responseStatusCode = apiRequest("/rest/ip/address", "PUT", request.get_json())
    return responseJson, responseStatusCode 

#Update
@main.patch("/rest/ip/address")
def patchAddresses():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/address/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode

#Delete
@main.delete("/rest/ip/address")
def deleteAddresses():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/address/"+id, "DELETE")
    return '', responseStatusCode


#CRUD - DHCP server

#Read
@main.get("/rest/ip/dhcp-server")
def getDHCPServer():
    responseJson, responseStatusCode = apiRequest("/rest/ip/dhcp-server", "GET")
    return responseJson, responseStatusCode


#Create
@main.put("/rest/ip/dhcp-server")
def putDHCPServer():
    responseJson, responseStatusCode = apiRequest("/rest/ip/dhcp-server", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Update
@main.patch("/rest/ip/dhcp-server")
def patchDHCPServer():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/dhcp-server/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode

#Delete
@main.delete("/rest/ip/dhcp-server")
def deleteDHCPServer():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/dhcp-server/"+id, "DELETE")
    return '', responseStatusCode

#CRUD - DHCP pools

#Read
@main.get("/rest/ip/pool")
def getDHCPPools():
    responseJson, responseStatusCode = apiRequest("/rest/ip/pool", "GET")
    return responseJson, responseStatusCode

#Create
@main.put("/rest/ip/pool")
def putDHCPPools():
    responseJson, responseStatusCode = apiRequest("/rest/ip/pool", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Update
@main.patch("/rest/ip/pool")
def patchDHCPPools():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/pool/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode


#Delete
@main.delete("/rest/ip/pool")
def deleteDHCPPools():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/pool/"+id, "DELETE")
    return '', responseStatusCode


#Activate/Deactivate/Configure DNS server

#Read
@main.get("/rest/ip/dns")
def getDNS():
    responseJson, responseStatusCode = apiRequest("/rest/ip/dns", "GET")
    return responseJson, responseStatusCode

#Update
@main.post("/rest/ip/dns/set")
def postDNS():
    responseJson, responseStatusCode = apiRequest("/rest/ip/dns/set", "POST", request.get_json())
    return responseJson, responseStatusCode


#Activate/Deactivate/Configure DNS static entries

#Read
@main.get("/rest/ip/dns/static")
def getDNSStatic():
    responseJson, responseStatusCode = apiRequest("/rest/ip/dns/static", "GET")
    return responseJson, responseStatusCode

#Create
@main.put("/rest/ip/dns/static")
def putDNSStatic():
    responseJson, responseStatusCode = apiRequest("/rest/ip/dns/static", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Update
@main.patch("/rest/ip/dns/static")
def patchDNSStatic():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/ip/dns/static/"+id, "PATCH", request.get_json())
    return responseJson, responseStatusCode


#Wireguard
#CRUD - Wireguard interfaces
#Get all wireguard interfaces
@main.get("/rest/interface/wireguard")
def getWireguardInterfaces():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireguard", "GET")
    return responseJson, responseStatusCode

#Create wireguard interfaces
@main.put("/rest/interface/wireguard")
def putWireguardInterfaces():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireguard", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Get Peers
@main.get("/rest/interface/wireguard/peers")
def getWireguardPeers():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireguard/peers", "GET")
    return responseJson, responseStatusCode

#Create Peers
@main.put("/rest/interface/wireguard/peers")
def putWireguardPeers():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireguard/peers", "PUT", request.get_json())
    return responseJson, responseStatusCode

#Update Peers
@main.patch("/rest/interface/wireguard/peers")
def patchWireguardPeers():
    id = request.args.get('id')
    returnedJson, responseStatusCode = apiRequest("/rest/interface/wireguard/peers/"+id, "PATCH", request.get_json())
    return returnedJson, responseStatusCode


#Delete Peers
@main.delete("/rest/interface/wireguard/peers")
def deleteWireguardPeers():
    id = request.args.get('id')
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireguard/peers/"+id, "DELETE")
    return '', responseStatusCode


#Download Peers
@main.post("/rest/interface/wireguard/peers/show-client-config")
def getWireguardPeersConfig():
    responseJson, responseStatusCode = apiRequest("/rest/interface/wireguard/peers/show-client-config", "POST", request.get_json())
    return responseJson, responseStatusCode