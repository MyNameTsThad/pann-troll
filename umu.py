import random

import urllib3
from discord_webhook import DiscordWebhook
import signal
import sys
import time

# !{sys.executable} -m pip install discord_webhook # comment this line out if your not using jupyter

url = 'https://discord.com/api/webhooks/940954938429808660/0tYFZU3ZXTIkUfqUrV90Ua90XxGaofpGGTApZ-LG-1-UqrI_rcbvPlNICW-9byi_VduG'
umusSent = 0


def signal_handler(signal, frame):
    sys.exit(0)


def tryRespond(wh):
    try:
        response1 = webhook.execute()
        return response1
    except:
        tryRespond(wh)


signal.signal(signal.SIGINT, signal_handler)

while True:
    webhook = DiscordWebhook(url, rate_limit_retry=True, content="umu")
    response = tryRespond(webhook)
    umusSent += 1
    print(umusSent, "umu's sent", end='\r')
    time.sleep(random.randint(1, 3))
