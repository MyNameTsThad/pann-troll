import random

from discord_webhook import DiscordWebhook
import signal
import sys
import time

# !{sys.executable} -m pip install discord_webhook # comment this line out if your not using jupyter

url = 'https://discord.com/api/webhooks/940976812555661363/YYVDSDAHyVL4inSYEO-91UeQsNyyg-n1Pt6-SnEijJd4uMfr3He_p-gcJ_wla9Ysp8Yg'


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
    webhook = DiscordWebhook(url, rate_limit_retry=True, content=".")
    response = tryRespond(webhook)
    time.sleep(float(random.randint(2, 10)) / float(10))
