import requests
import json
from datetime import datetime

def get_games():
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    '''
    GetAppList
    GET https://api.steampowered.com/ISteamApps/GetAppList/v2/
    
    Получает полный список общедоступных приложений.
    Этот вызов не имеет дополнительных параметров.
    
    Ответ:
    applist
        apps - список с приложениями.
            appid - uint32 - AppID данного приложения.
            name - string - название данного приложения.
    '''

    try:
        response = requests.get(url)
        if response.status_code == 200:
            app_list = response.json().get('applist', {}).get('apps', [])
            filtered_app_list = [
                {'name': app['name'], 'appid': app['appid']}
                for app in app_list
                if app.get('name')
            ]
            return filtered_app_list
        return []
    except Exception as e:
        print(f'Error: {e}')

def get_app_details(app_id, country='RU'):
    url = "https://store.steampowered.com/api/appdetails"
    params = {
        'appids': app_id,
        'cc': country,
        'l': 'russian'
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()

            if data.get(str(app_id)).get('success'):
                details = data.get(str(app_id)).get('data')
                price_overview = details.get('price_overview')
                price = price_overview.get('final') / 100 if price_overview else None
                return {
                    'name': details.get('name'),
                    'brief_description': details.get('short_description'),
                    'description': details.get('detailed_description'),
                    'image_url': details.get('header_image'),
                    'type': details.get('type'),
                    'price': price,
                    'source': 'steam',
                    'datetime': datetime.now()
                }
    except Exception as e:
        print(f"Error: {e}")

    print(f"Couldn`t retrieve game details by apppid: '{app_id}'")
    return None
