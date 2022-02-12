import random
from discord_webhook import DiscordWebhook
import signal
import sys
import time

# !{sys.executable} -m pip install discord_webhook # comment this line out if your not using jupyter

url = 'https://discord.com/api/webhooks/940924706188587038/dirnj8YZZwSoZQy4ezEyaLiQklxVeCpVfY_7htiU71vEQpLBq8lNsfn88ZI3Ab2XJnex'
#url = "https://discord.com/api/webhooks/940976812555661363/YYVDSDAHyVL4inSYEO-91UeQsNyyg-n1Pt6-SnEijJd4uMfr3He_p-gcJ_wla9Ysp8Yg"
contents = ["pann big clown", "pann :clown::camera_with_flash:", "pann big noob", "pann :skull:",
            "https://tenor.com/view/dont-care-didnt-ask-cope-_ratio-skill-issue-canceled-gif-24148064",
            "https://media.discordapp.net/attachments/919845936904171572/937547816669184080/377C081C-7250-469E-A0E6-53CAFCF58FD0.gif",
            "https://media.discordapp.net/attachments/721723269107023974/932828709646393364/spinning-skeleton-skeleton_1.gif",
            "https://cdn.discordapp.com/emojis/915411270272966676.webp?size=128&quality=lossless\nhttps://cdn.discordapp.com/emojis/917946997741350932.webp?size=128&quality=lossless",
            ":/", "\\\:", "bruh", "stop this bot", "skill issue", "pann cope", "shutup", "stfu",
            "https://cdn.discordapp.com/emojis/915146986171273246.webp?size=128&quality=lossless",
            "pann big clown", "pann :clown::camera_with_flash:", "pann big noob", "pann :skull:",
            "https://tenor.com/view/dont-care-didnt-ask-cope-_ratio-skill-issue-canceled-gif-24148064",
            "https://media.discordapp.net/attachments/919845936904171572/937547816669184080/377C081C-7250-469E-A0E6-53CAFCF58FD0.gif",
            "https://media.discordapp.net/attachments/721723269107023974/932828709646393364/spinning-skeleton-skeleton_1.gif",
            "https://cdn.discordapp.com/emojis/915411270272966676.webp?size=128&quality=lossless\nhttps://cdn.discordapp.com/emojis/917946997741350932.webp?size=128&quality=lossless",
            ":/", "\\\:", "bruh", "stop this bot", "skill issue", "pann cope", "shutup", "stfu",
            "https://cdn.discordapp.com/emojis/915146986171273246.webp?size=128&quality=lossless",
            "pann big clown", "pann :clown::camera_with_flash:", "pann big noob", "pann :skull:",
            "https://tenor.com/view/dont-care-didnt-ask-cope-_ratio-skill-issue-canceled-gif-24148064",
            "https://media.discordapp.net/attachments/919845936904171572/937547816669184080/377C081C-7250-469E-A0E6-53CAFCF58FD0.gif",
            "https://media.discordapp.net/attachments/721723269107023974/932828709646393364/spinning-skeleton-skeleton_1.gif",
            "https://cdn.discordapp.com/emojis/915411270272966676.webp?size=128&quality=lossless\nhttps://cdn.discordapp.com/emojis/917946997741350932.webp?size=128&quality=lossless",
            ":/", "\\\:", "bruh", "stop this bot", "skill issue", "pann cope", "shutup", "stfu",
            "https://cdn.discordapp.com/emojis/915146986171273246.webp?size=128&quality=lossless",
            "pann big clown", "pann :clown::camera_with_flash:", "pann big noob", "pann :skull:",
            "https://tenor.com/view/dont-care-didnt-ask-cope-_ratio-skill-issue-canceled-gif-24148064",
            "https://media.discordapp.net/attachments/919845936904171572/937547816669184080/377C081C-7250-469E-A0E6-53CAFCF58FD0.gif",
            "https://media.discordapp.net/attachments/721723269107023974/932828709646393364/spinning-skeleton-skeleton_1.gif",
            "https://cdn.discordapp.com/emojis/915411270272966676.webp?size=128&quality=lossless\nhttps://cdn.discordapp.com/emojis/917946997741350932.webp?size=128&quality=lossless",
            ":/", "\\\:", "bruh", "stop this bot", "skill issue", "pann cope", "shutup", "stfu",
            "https://cdn.discordapp.com/emojis/915146986171273246.webp?size=128&quality=lossless", "@everyone"]


def signal_handler(signal, frame):
    webhook1 = DiscordWebhook(url, rate_limit_retry=True, content="Exiting!")
    response1 = webhook.execute()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

while True:
    webhook = DiscordWebhook(url, rate_limit_retry=True, content=contents[random.randint(0, 68)])
    response = webhook.execute()
    time.sleep(random.randint(5, 10))
