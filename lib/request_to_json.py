import re
import json
import socket

#Squeeze the server parameters out of the GET request
def parameterSort(request):
    params = {}
    #Remove extra material from the request
    raw_var = ""
    start = request.find("?") + 1
    end = request.find("\\")
    request = request[start:end]
#     print ("Request: ", request)
    
    #Add requests to a dictionary and save dictionary for further use
    for i in range(len(request)):
        if request == " ":
            return
        if request[i] != "&":
            raw_var += request[i]
        if request[i] == "&":
            variable = raw_var.split('=')
            key = variable[0]
            value = variable[1]
            params[key] = value
            raw_var = ""
        if request[i] == "H" or i == len(request):
#             print("Parameters in parameterSort function: ",params)
            break
           
    return params

#Call saved dictionary from parameterSort function and convert to a json object and save to parameters.json
def saveVariables(new_parameters):
    if len(new_parameters) <=1:
        return
    parameters_json_object = json.dumps(new_parameters)
#     print("Parameters in json object: ", parameters_json_object)
    with open("/lib/parameters.json","w") as parameters_json:
        parameters_json.write(parameters_json_object)
        
#Call saved dictionary from parameterSort function and convert to a json object and save to parameters.json
def savePreviousVariables(new_parameters):
    if len(new_parameters) <=1:
        return
    parameters_json_object = json.dumps(new_parameters)
#     print("Parameters in json object: ", parameters_json_object)
    with open("/lib/previous_parameters.json","w") as parameters_json:
        parameters_json.write(parameters_json_object)
        
#Open and print parameters.json file
def printParameters():
    parameters_print = json.load(open("/lib/parameters.json"))
    print("Parameters in JSON: ", json.dumps(parameters_print))

#load the parameters from the parameters.json file
def loadParameters():
    parameters_loaded = json.load(open("/lib/parameters.json"))
    return parameters_loaded

#load the parameters from the previous_parameters.json file
def loadPreviousParameters():
    parameters_loaded = json.load(open("/lib/previous_parameters.json"))
    return parameters_loaded