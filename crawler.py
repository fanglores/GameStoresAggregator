from apscheduler.schedulers.background import BackgroundScheduler
import steam_search

scheduler = BackgroundScheduler()
scheduler.add_job(func=__crawler_job, trigger="interval", hours=1, id='CRAWLER_UPDATER', replace_existing=True, max_instances=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

def __crawler_job():
    try:
        steam_games_list = steam_search.get_popular_games()

        for steam_game in steam_games_list:
            steam_game_info = steam_search.get_app_details(steam_game['appid'])
            database_update(steam_game_info)
    except:
        print('ERROR')