from apscheduler.schedulers.background import BlockingScheduler
import atexit
import steam_search
import database

def __crawler_job():
    try:
        print('Crawler has been started')
        print('Check database availability')
        if not database.check_connection():
            print('Database is unavailable, skip crawling session')
            return
        print('Database available, proceed with crawling')

        print('Trying to get games list from Steam')
        steam_games_list = steam_search.get_popular_games(10)

        print(f'Trying to parse received games. List size: {len(steam_games_list)}')
        for steam_game in steam_games_list:
            try:
                game_name, game_appid = steam_game['name'], steam_game['appid']

                print(f"Trying to parse game '{game_name}', appid '{game_appid}'")
                steam_game_info = steam_search.get_app_details(game_appid)  #TODO: use unified class with all fields, that will be passed across all the functions, which will partially fill its fields?
                if steam_game_info is not None:
                    print(f"Trying to write game with appid '{game_appid}' into a base")
                    database.update(steam_game_info)
                else:
                    print(f"Received empty game details for appid '{game_appid}', skip game")
            except Exception as e:
                print(f"Error: Failed to write a game with appid '{game_appid}' game\nError description: {e}")
    except Exception as e:
        print(f'Error: {e}')

def __shutdown_scheduler():
    try:
        print('Shutting down the scheduler')
        scheduler.shutdown()
    except Exception as e:
        print(f'Error: Scheduler is probably already offline\nError description: {e}')


scheduler = BlockingScheduler()
scheduler.add_job(func=__crawler_job, trigger="interval", hours=1, id='CRAWLER', replace_existing=True, max_instances=1)

# Guarantees that scheduler will be stopped on exit
atexit.register(__shutdown_scheduler)

try:
    print('Starting up the scheduler')
    #Crutch to start job on the startup
    __crawler_job()
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    __shutdown_scheduler()