from discord import Embed

pekora_noises = {
    "naww": "https://www.youtube.com/watch?v=JNgCFHbPARg",
    "motherf*cker": "https://www.youtube.com/watch?v=1OjQVMiyUMg",
    "oh no jesus": "https://www.youtube.com/watch?v=MwCNEySMNWg",
    "yolo": "https://www.youtube.com/watch?v=MSUckSO-Dsw",
    "ogey rrat": "https://www.youtube.com/watch?v=JacN1MzyeKo",
    "rrat simulator rrrra": "https://www.youtube.com/watch?v=Xr_pKdyeIJo",
    "wao wao waoo!":"https://www.youtube.com/watch?v=O9s_HLql2YM",
    "pardun?":"https://www.youtube.com/watch?v=a3DpRlWdnDw"
}

nothing_changed_reply_list = []
for title, link in pekora_noises.items():
    nothing_changed_reply_list.append("Sorry, I couldn't pekofy the message for some reason peko. "	
                                      "So here's a video of Pekora saying {} instead peko.\n{}".format(title, link))

no_recursion_reply = "no\nhttps://www.youtube.com/watch?v=3FOe-KNUwb4"
pain_peko_reply = "pain-peko.\nhttps://preview.redd.it/dvk3bft2a9l51.jpg?auto=webp&s=d5e53605dc0e99ed55884fc00c9b965c7dd38e7c"
hey_moona_reply = "Hey Moona!"
limit_reached_reply = "Sorry peko, but I can't pekofy it any further to prevent spam peko. Thank you for your understanding peko."
bot_score_abuse_reply = "Sorry peko, can't pekofy that due to potential bot score abuse peko."
confused_reply = "eh?"

# some of them are repeated to increase chance
thanks = ["Thank you peko", "Thank you peko!", "Thank you peko~", "Arigatou peko!", "Thank you peko!",
          "Thank you peko~", "Arigatou peko!", "Arigatou peko~", "ありがとうぺこ～", "ありがとうぺこ！",
          "Thank you peko!", "Thank you peko~", "Ehehe", "Ehehe", "Ehehe",
          "Arigatou peko da ne! peko~\nhttps://www.youtube.com/watch?v=zOUPxaA6mBM",
          "Arigatou peko.\nhttps://www.youtube.com/watch?v=swGNEJ56EFI"]

sorrys = ["Sorry peko ; ;", "Sorry peko...", "G-Gomen peko.", "ごめんぺこ・・・"]

insults = ["Bakatare ga!", "Bakatare ga!", "Bakatare ga!", "Bakatare ga!", "Anta wa baka nano?", "バカたれが！",
           "ばかたれが！", "あんたはバカなの？", "ぺっ", "Go peko yourself!",
           "Disgusting.\nhttps://streamable.com/6ntf2g"]

loves = ["Thank you guys. Don't cheat on me, okay? Peko~\nhttps://streamable.com/8gagri",
         "Love you too peko!\nhttps://streamable.com/dbzfxj", "I love you too peko!", "Love you too peko~"]

cutes = ["You're cute too peko!", "You're also cute peko!", "You're cute too peko~", "You're also cute peko~", "Ehehe", "あなたもかわいいぺこ！"]

cursed_pekopasta = "So as a joke, I went to my friend's house wearing Pekora's wig and clothes. I could barely stop" \
                   " my laughter as he went as red as a tomato and looked at me from head to toe with a bit of drool" \
                   " in his mouth. The way he stared made me feel a bit funny too, but I decided to tease him more " \
                   "by taking off my clothes. He asked me, \"Are you serious?\" and I said \"Yep peko.\"\nHe went" \
                   " silent for what seemed like forever, so I asked him, \"What's the matter peko?\" He said he's " \
                   "confused, but then his boner got really hard, which made me take off his clothes. I expected him " \
                   "to scream, \"Stop!\" as I kissed him and stroked his cock, but he instead shouted \"Oh God, " \
                   "Pekora!\" which made me get a boner myself. Before I knew it, I was blowing him for the first time" \
                   " till he came.\nHis semen was so thick, it got stuck inside my throat no matter how hard I " \
                   "swallowed. He then said, \"I want to fuck you now!\" and seeing that we've already gone that far " \
                   "and we were both naked, I obliged. A few hours later, the jerk went all pale and said to me \"Why " \
                   "did we do that? Now I'm not fucking straight.\" But he still looked so cute all confused like " \
                   "that, so I took pity on him and reassured while wiping his cum off my face, \"Let's just pretend " \
                   "I'm still Pekora.\""

cursed_pekopasta_censored = "So as a joke, I went to my friend's house wearing Pekora's wig and clothes. I could barely stop" \
                   " my laughter as he went as red as a tomato and looked at me from head to toe with a bit of drool" \
                   " in his mouth. The way he stared made me feel a bit funny too, but I decided to tease him more " \
                   "by taking off my clothes. He asked me, \"Are you serious?\" and I said \"Yep peko.\"\nHe went" \
                   " silent for what seemed like forever, so I asked him, \"What's the matter peko?\" He said he's " \
                   "confused, but then his b\\*ner got really hard, which made me take off his clothes. I expected him " \
                   "to scream, \"Stop!\" as I kissed him and stroked his c\\*ck, but he instead shouted \"Oh God, " \
                   "Pekora!\" which made me get a b\\*ner myself. Before I knew it, I was blowing him for the first time" \
                   " till he came.\nHis s\\*men was so thick, it got stuck inside my throat no matter how hard I " \
                   "swallowed. He then said, \"I want to f\\*ck you now!\" and seeing that we've already gone that far " \
                   "and we were both n\\*ked, I obliged. A few hours later, the jerk went all pale and said to me \"Why " \
                   "did we do that? Now I'm not f\\*cking straight.\" But he still looked so cute all confused like " \
                   "that, so I took pity on him and reassured while wiping his c\\*m off my face, \"Let's just pretend " \
                   "I'm still Pekora.\""

found_myself = "Sorry peko, I sent this message! I can't pekofy it!"
status_content = "Commiting war crimes peko | !helpeko"
invite = "https://discord.com/api/oauth2/authorize?client_id=817481976797069383&permissions=67472384&scope=bot"

helpeko = Embed(
    title = "pekofy_bot commands:",
    description = "If you have any problems, feel free to contact the creator on Discord (bemxio#5847) or on Reddit (u/bemxioo) peko!"
)

helpeko.add_field(
    name = "!pekofy",
    value = "pekofies a message that is replied"
)
helpeko.add_field(
    name = "!pekopasta",
    value = "sends a Pekora cosplay copypasta"
)
helpeko.add_field(
    name = "!helpeko",
    value = "sends this help message"
)
helpeko.add_field(
    name = "!credits",
    value = "shows credits of all things that made pekofy_bot exist"
)
helpeko.add_field(
    name = "insult me peko",
    value = "insults you"
)
helpeko.add_field(
    name = "!invite",
    value = "sends an invite for adding the bot"
)
helpeko.add_field(
    name = "!pekodebug",
    value = "shows debug stuff about the bot (bot owner only)"
)

credits = "Thank you so much, denki, for helping with the verification of me peko!\n" \
        "I am made in Python (with discord.py), and hosted on Heroku!\n" \
        "Check out the original Reddit bot made by esmo-c! https://github.com/emso-c/pekofy-bot"

pekodebug_template = "Server count: **{0}**\n" \
                     "Ping: **{1} ms**"

no_reply = "You need to reply to a message you want to be pekofy'd peko!"
cooldown_msg = "You all are going too fast peko! Please wait {0} seconds to type this command!"