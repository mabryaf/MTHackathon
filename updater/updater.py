from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from updater import updaterApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(updaterApi.update_smartqueue, 'interval', minutes=30)
    scheduler.start()