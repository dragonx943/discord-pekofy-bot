import random

no_change = [
    "Sorry, I couldn\'t pekofy the message for some reason peko. So here\'s a clip of Pekora saying [{}]({}) instead peko.".format(title, link) \
    for title, link in {
        "naww": "https://www.youtube.com/watch?v=JNgCFHbPARg",
        "motherf*cker": "https://www.youtube.com/watch?v=57ToRyDoTAE",
        "oh no jesus": "https://www.youtube.com/watch?v=MwCNEySMNWg",
        "yolo": "https://www.youtube.com/watch?v=MSUckSO-Dsw",
        "ogey rrat": "https://www.youtube.com/watch?v=JacN1MzyeKo",
        "rrat simulator rrrra": "https://www.youtube.com/watch?v=Xr_pKdyeIJo",
        "wao wao waoo!":"https://www.youtube.com/watch?v=O9s_HLql2YM",
        "pardun?":"https://www.youtube.com/watch?v=a3DpRlWdnDw",
        "holy sheet":"https://www.youtube.com/watch?v=yo0_m34o6Mg",
        "motherf*cker": "https://www.youtube.com/watch?v=4q1B06m4_Lk", # korone roll
        "god bless you": "https://streamable.com/1w8pbx",
        "hi honey": "https://www.youtube.com/watch?v=n8psYwqS544"
    }.items()
]

no_reference = [
    "Ah peko, you need to reply to a message that you want to pekofy!",
    "You need to reply to a message that you want to be pekofied peko!"
]
limit_reached = "Sorry, but I can't pekofy it any further to prevent spam peko. Thank you for your understanding peko."

hey_moona = "Hey Moona!"
pain_peko = "pain-peko. https://usagi.bemxio.xyz/painpeko.webp"
insult_me_peko = "insult me peko"
pekorat = "pekorat"

cant_dm = "I can't send stuff in your DMs, peko!\nPlease enable `User Settings > Privacy & Safety > Allow direct messages from server members`, if you want me to get into your DMs."
unexpected_error = """
Oops, something went wrong peko! 

Please make an issue about this on the GitHub repo, 
or message my developer (@bemxio on Discord or u/bemxioo on Reddit) including the text below:
```
{}
```
"""
command_cooldown = "You all are going too fast peko~! Please wait {} seconds before typing this command again!"
message_too_long = "This message is toooo long peko~!!! I can't send the pekofied version of it!"

gacha_win = [
    "Congratuttrasyon! You won {} pekos! {}".format(pekos, link) 
    for pekos, link in {
        "100": "https://www.youtube.com/shorts/xuFSlfznFzU",
        "2000": "https://i.redd.it/jnknro1eysg51.jpg",
        "1 morbillion": "https://youtu.be/ANUYB8q5PsE"
    }.items()
]

gacha_lose = [
    "Oh no! You lost {} pekos! {}".format(pekos, link) 
    for pekos, link in {
        "100": "https://i.kym-cdn.com/photos/images/original/002/241/259/1c1.png",
        "1000": "https://www.youtube.com/shorts/ljxEIQZyjGo",
        "ALL of your": "https://www.youtube.com/watch?v=vHpFuQPtE_U"
    }.items()
]
