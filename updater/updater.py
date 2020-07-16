from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from updater import updaterApi

#Sets the updater to get smartqueue schedule every 30 minutes
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(updaterApi.update_smartqueue, 'interval', minutes=30)
    scheduler.start()