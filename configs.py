# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
This is the Permanent Files Store Bot for [Moviez Café™](https://t.me/moviezcafe38)

😎 **Developed By** [W∆LT3R](https://t.me/ritwikRG)

👥 **Support Group:** [Moviez Café™ Discussion](https://t.me/moviez_cafe_38)

📢 **Channel:** [Moviez Café™](https://t.me/moviezcafe38)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @AbirHasan2005

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot** For [Moviez Café™](https://t.me/moviezcafe38)

Owened By [W∆LT3R](https://t.me/ritwikRG) 😎

Check **About Bot** Button.
"""
