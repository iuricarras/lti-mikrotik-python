import requests
from flask import Flask, request, jsonify, Blueprint, current_app
from flask_cors import CORS
from .config import routerip, authentication
import json
from . import db


main = Blueprint('main', __name__)

#Get all interfaces from the device
@main.get("/rest/interface")
def getInterfaces():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    print("routerip: ", routerip)
    api_url = "http://"+ routerip +"/rest/interface"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code


#Get only the wireless interfaces
@main.get("/rest/interface/wireless")
def getWirelessInterfaces():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/wireless"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code


#CRUD - Bridge interfaces and respective ports
#Read
@main.get("/rest/interface/bridge")
def getBridges():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/bridge"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/interface/bridge")
def putBridges():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/bridge"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'mainlication/json'})
    return response.json(), response.status_code

#Update
@main.patch("/rest/interface/bridge")
def patchBridges():
    id = request.args.get('id')
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')    
    api_url = "http://"+ routerip +"/rest/interface/bridge/*"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'mainlication/json'})
    return response.json(), response.status_code
    
#Delete
@main.delete("/rest/interface/bridge")
def deleteBridges():
    id = request.args.get('id')
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/bridge/"+id
    response = requests.delete(api_url, auth=authentication)
    return '', response.status_code



#Wireless interfaces

#Enable wireless interfaces
@main.post("/rest/interface/wireless/enable")
def enableWireless():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/wireless/enable"
    body = request.get_json()
    response = requests.post(api_url, auth=authentication, data=json.dumps(body), headers={'content-type':'application/json'})
    return '', response.status_code

#Disable wireless interfaces
@main.post("/rest/interface/wireless/disable")
def disableWireless():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    body = request.get_json()
    api_url = "http://"+ routerip +"/rest/interface/wireless/disable"
    response = requests.post(api_url, auth=authentication, data=json.dumps(body), headers={'content-type':'application/json'})
    return '', response.status_code

#Update
@main.patch("/rest/interface/wireless")
def patchWireless():    
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireless/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code


#CRUD - Port interfaces

#Read
@main.get("/rest/interface/bridge/port")
def getPorts():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    bridgeName = request.args.get('bridge');
    if(bridgeName != None):
        api_url = "http://"+ routerip +"/rest/interface/bridge/port?bridge="+bridgeName
    else:
        api_url = "http://"+ routerip +"/rest/interface/bridge/port"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/interface/bridge/port")
def insertPorts():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip + "/rest/interface/bridge/port"
    body = request.get_json()
    response = requests.put(api_url, auth=authentication, headers={'content-type':'application/json'}, data=json.dumps(body))
    return response.json(), response.status_code

#Delete
@main.delete("/rest/interface/bridge/port")
def deletePorts():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/bridge/port/"+id
    response = requests.delete(api_url, auth=authentication)
    return '', response.status_code


#CRUD - Security profiles

#Read
@main.get("/rest/interface/wireless/security-profiles")
def getSecurityProfiles():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/interface/wireless/security-profiles")
def putSecurityProfiles():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@main.patch("/rest/interface/wireless/security-profiles")
def patchSecurityProfiles():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@main.delete("/rest/interface/wireless/security-profiles")
def deleteSecurityProfiles():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireless/security-profiles/"+id
    response = requests.delete(api_url, auth=authentication)
    return '' , response.status_code


#CRUD - Static routes

#Read
@main.get("/rest/ip/route")
def getStaticRoutes():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/route"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/ip/route")
def putStaticRoutes():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/route"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@main.patch("/rest/ip/route")
def patchStaticRoutes():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/route/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@main.delete("/rest/ip/route")
def deleteStaticRoutes():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/route/"+id
    response = requests.delete(api_url, auth=authentication)
    return '', response.status_code


#CRUD - IP addresses

#Read
@main.get("/rest/ip/address")
def getAddresses():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/address"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/ip/address")
def putAddresses():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/address"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@main.patch("/rest/ip/address")
def patchAddresses():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/address/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@main.delete("/rest/ip/address")
def deleteAddresses():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/address/"+id
    response = requests.delete(api_url, auth=authentication)
    return '', response.status_code


#CRUD - DHCP server

#Read
@main.get("/rest/ip/dhcp-server")
def getDHCPServer():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/ip/dhcp-server")
def putDHCPServer():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@main.patch("/rest/ip/dhcp-server")
def patchDHCPServer():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@main.delete("/rest/ip/dhcp-server")
def deleteDHCPServer():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/dhcp-server/"+id
    response = requests.delete(api_url, auth=authentication)
    return '', response.status_code

#CRUD - DHCP pools

#Read
@main.get("/rest/ip/pool")
def getDHCPPools():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/pool"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/ip/pool")
def putDHCPPools():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/pool"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@main.patch("/rest/ip/pool")
def patchDHCPPools():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/pool/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Delete
@main.delete("/rest/ip/pool")
def deleteDHCPPools():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/pool/"+id
    response = requests.delete(api_url, auth=authentication)
    return '', response.status_code


#Activate/Deactivate/Configure DNS server

#Read
@main.get("/rest/ip/dns")
def getDNS():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/dns"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Update
@main.post("/rest/ip/dns/set")
def postDNS():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/dns/set"
    body = request.get_json()
    response = requests.post(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code
#Activate/Deactivate/Configure DNS static entries

#Read
@main.get("/rest/ip/dns/static")
def getDNSStatic():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/dns/static"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create
@main.put("/rest/ip/dns/static")
def putDNSStatic():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/ip/dns/static"
    body = request.get_json()
    response = requests.put(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code

#Update
@main.patch("/rest/ip/dns/static")
def patchDNSStatic():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/ip/dns/static/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication, headers={'content-type':'application/json'})
    return response.json(), response.status_code


#Wireguard

#Get Peers
@main.get("/rest/interface/wireguard/peers")
def getWireguardPeers():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/wireguard/peers"
    response = requests.get(api_url, auth=authentication)
    return response.json(), response.status_code

#Create Peers
@main.put("/rest/interface/wireguard/peers")
def putWireguardPeers():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip +"/rest/interface/wireguard/peers"
    body = request.get_json()
    print("body: ", body)
    response = requests.put(api_url, data=json.dumps(body), auth=authentication)
    return response.json(), response.status_code

#Update Peers
@main.patch("/rest/interface/wireguard/peers")
def patchWireguardPeers():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireguard/peers/"+id
    body = request.get_json()
    response = requests.patch(api_url, data=json.dumps(body), auth=authentication)
    return response.json(), response.status_code


#Delete Peers
@main.delete("/rest/interface/wireguard/peers")
def deleteWireguardPeers():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    id = request.args.get('id')
    api_url = "http://"+ routerip +"/rest/interface/wireguard/peers/"+id
    response = requests.delete(api_url, auth=authentication)
    return '', response.status_code


#Download Peers
@main.post("/rest/interface/wireguard/peers/show-client-config")
def getWireguardPeersConfig():
    routerip = current_app.config.get('ROUTER_IP')
    authentication = current_app.config.get('AUTHENTICATION')
    body = request.get_json()
    api_url = "http://"+ routerip +"/rest/interface/wireguard/peers/show-client-config"
    response = requests.post(api_url, data=json.dumps(body), auth=authentication)
    return response.json(), response.status_code