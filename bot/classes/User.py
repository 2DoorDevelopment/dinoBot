import discord

from datetime import datetime, timedelta


class User:
    def __init__(self, discord_id: discord.Member):
        self.member = discord_id

    def new_user(self):
        time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

        return {
            "discord_id": self.member.id,
            "time_sold": time,
            "fossil_type": "",  # Insert Starting Fossil Type
            "balance": 0,
            "fossil_quality": 1,
            "fossil_yield": 1,
            "dig_speed": 1,
            "quadrants": 1,
            "excavators": 1,
            "heli_total": 1,
            "heli_capacity": 1,
        }
