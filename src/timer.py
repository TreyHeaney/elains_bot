from time import time
from datetime import datetime
from discord.ext import tasks, commands


class Timer(commands.Cog):
    def __init__(self):
        self.index = 0
        self.timer.start()
        self.last_sent = datetime.now()

    def cog_unload(self):
        self.timer.cancel()

    @tasks.loop(seconds=1.14)
    async def timer(self):
        now = datetime.now()
        current_day = now.day
        current_hour = now.hour
        
        last_day = self.last_sent.day
        last_hour = self.last_sent.hour

        if last_day == 1 or current_day > last_day:
            if current_hour == 10:
                await self.send_message('Happy New Year!')