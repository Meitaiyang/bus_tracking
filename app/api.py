import requests
import json
from flask import jsonify

app_id = 'shrek473-b2142b35-f284-4f3a'
app_key = 'b03f7216-1d9f-4f04-ab5d-bcde430f0362'

auth_url="https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        content_type = 'application/x-www-form-urlencoded'
        grant_type = 'client_credentials'

        return{
            'content-type' : content_type,
            'grant_type' : grant_type,
            'client_id' : self.app_id,
            'client_secret' : self.app_key
        }

class data():

    def __init__(self, app_id, app_key, auth_response):
        self.app_id = app_id
        self.app_key = app_key
        self.auth_response = auth_response

    def get_data_header(self):
        auth_JSON = json.loads(self.auth_response.text)
        access_token = auth_JSON.get('access_token')

        return{
            'authorization': 'Bearer '+access_token
        }

def call_api(bus_number):

    Estimated_url = f"https://tdx.transportdata.tw/api/basic/v2/Bus/EstimatedTimeOfArrival/City/Taipei/{bus_number}?%24format=JSON"
    Route_url = f"https://tdx.transportdata.tw/api/basic/v2/Bus/Route/City/Taipei/{bus_number}?%24format=JSON"
    Stop_url = f"https://tdx.transportdata.tw/api/basic/v2/Bus/DisplayStopOfRoute/City/Taipei/{bus_number}?%24format=JSON"

    try:
        d = data(app_id, app_key, auth_response)
        data_response = requests.get(Estimated_url, headers=d.get_data_header())
    except:
        a = Auth(app_id, app_key)
        auth_response = requests.post(auth_url, a.get_auth_header())
        d = data(app_id, app_key, auth_response)
        Estimated = requests.get(Estimated_url, headers=d.get_data_header()).json()   
        Route = requests.get(Route_url, headers=d.get_data_header()).json()
        Stop = requests.get(Stop_url, headers=d.get_data_header()).json()

    result = list()

    if not Route or not Estimated or not Stop:
        return result

    for route in Route:
        bus_num = route["RouteName"]["Zh_tw"]
        for direction in [0, 1]:
            stops_for_route_direction = [stop for stop in Stop if stop["RouteID"] == route["RouteID"] and stop["Direction"] == direction]
            # If no stops found for this direction, continue
            if not stops_for_route_direction:
                continue
            
            if direction == 0:
                direction_name = route["DestinationStopNameZh"]
            else:
                direction_name = route["DepartureStopNameZh"]

            schedule = []
            for stop_entry in stops_for_route_direction:
                for stop in stop_entry["Stops"]:
                    stop_id = stop["StopID"]
                    stop_name = stop["StopName"]["Zh_tw"]
                    estimated_time = None

                    # Find the estimated time for the stop
                    for estimate in Estimated:
                        if "EstimateTime" in estimate and estimate["RouteID"] == route["RouteID"] and estimate["StopID"] == stop_id:
                            estimated_time = estimate["EstimateTime"]
                            break

                    # If estimated time is not found, set it as -1 (indicating 'Not Available')
                    if estimated_time is None:
                        estimated_time = "Not Available"

                    schedule.append({"station_name": stop_name, "arrival_time": estimated_time})

            result.append({"bus_number": bus_num, "direction": direction_name, "schedule": schedule})

    return result