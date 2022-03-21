from django.shortcuts import render
from django.http import JsonResponse
import requests
from requests.api import request
import aiohttp
import asyncio
import json
#from rest_framework.response import Response


def get_total_players():
    pass

def get_current_event():
    data = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    jdata = json.loads(data.text)
    events = jdata["events"]
    current_event = 0
    for event in events:
        if event["is_current"] == True:
            current_event = event["id"]
    return current_event

def get_golies():
    players = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    jdata = json.loads(players.text)
    elements = jdata["elements"]
    goalies = {}
    for i in elements:
        keeperId = i["id"]
        if i["element_type"] == 1:
            goalies[keeperId] = i["event_points"]
    return goalies  

def get_defenders():
    players = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    jdata = json.loads(players.text)
    elements = jdata["elements"]
    total_players = len(elements)
    defenders = {}
    for i in elements:
        defenderId = i["id"]
        if i["element_type"] == 2:
            defenders[defenderId] = i["event_points"]
    return defenders  


def get_midfielders():
    players = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    jdata = json.loads(players.text)
    elements = jdata["elements"]
    total_players = len(elements)
    midfielders = {}
    for i in elements:
        midfielderId = i["id"]
        if i["element_type"] == 3:
            midfielders[midfielderId] = i["event_points"]
    return midfielders  


def get_forwards():
    players = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    jdata = json.loads(players.text)
    elements = jdata["elements"]
    forwards = {}
    for i in elements:
        forwardId = i["id"]
        if i["element_type"] == 4:
            forwards[forwardId] = i["event_points"]
    return forwards  

def get_players(request, player_id):
    players = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    jdata = json.loads(players.text)
    elements = jdata["elements"]
    player_score = 0
    for i in elements:
        if i["id"] == player_id:
            player_score = i["event_points"]
            
    return JsonResponse(player_score, safe=False)  


def event(request):
    return JsonResponse(
        {
            "GW": get_current_event()
        }
    )

def goal(request):
    return JsonResponse(get_golies(), safe=False)

def defender(request):
    return JsonResponse(get_defenders(), safe=False)

def midfield(request):
    return JsonResponse(get_midfielders(), safe=False)

def forward(request):
    return JsonResponse(get_forwards(), safe=False)

