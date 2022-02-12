import asyncio
import time

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
import os


Scheduler = AsyncIOScheduler()
build_dir = os.path.abspath('../mcwzh-meme-web-builder-server/builds')


@Scheduler.scheduled_job(IntervalTrigger(seconds=5))
def delete_old_builds():
    for file in os.listdir(build_dir):
        file_path = os.path.join(build_dir, file)
        mtime = os.stat(file_path).st_mtime
        if mtime < (time.time() - (60 * 10)):
            os.remove(file_path)


Scheduler.start()
asyncio.get_event_loop().run_forever()
