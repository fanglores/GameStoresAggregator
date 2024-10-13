import requests
import json
from datetime import datetime

def get_popular_games(limit=100):
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
            return app_list[:limit]
        return []
    except:
        print('ERROR')

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
            if str(app_id) in data and data[str(app_id)]['success']:
                details = data[str(app_id)]['data']
                price_overview = details.get('price_overview')
                price = price_overview.get('final') / 100 if price_overview else None
                return {
                    'name': details.get('name'),
                    'price': price,
                    'source': 'steam',
                    'datetime': datetime.now()
                }
        else:
            print(f"Не удалось получить детали для app_id {app_id}")
    except Exception as e:
        print(f"Ошибка при получении цены для app_id {app_id}: {e}")
    finally:
        return None, None