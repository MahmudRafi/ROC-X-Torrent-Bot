import os

TOKEN = os.environ.get("BOT_TOKEN")
API_HASH = os.environ.get("API_HASH")
API_ID = int(os.environ.get("API_ID"))
START_MESSAGE = os.environ.get("START_MESSAGE", f"<b>@RootOfCyber</b>")
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", f"@RootOfCyber")
TORRENTS = {}
