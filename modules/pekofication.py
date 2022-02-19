from discord import Embed
import regex

# regex patterns for filtering out stuff
japanese = regex.compile("[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf}]")
url = regex.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")

# punctuation list with EN and JP marks to know where to put 'peko'
en_punctuation_list = ['.', ',', '?', '!', ':', ';', '\]']
jp_punctuation_list = ['。', '？', '！', '」', '・', '”', '】', '』', '；']
punctuation_list = en_punctuation_list + jp_punctuation_list + ['\n']

async def pekofy(input_text):
    corrected = input_text.replace("\n", "\n ")
    words = corrected.split(" ")
    length = len(words)
    
    pekotimes = 0 # number of times 'peko' has occured

    for index, word in enumerate(words):
        if japanese.match(word):
            keyword = "ぺこ"
        else:
            keyword = " peko"
        
        if url.match(word):
            continue

        if word.isupper():
            keyword = keyword.upper()

        # checking how many times peko has occured
        if word == keyword.strip():
            pekotimes += 1

            if pekotimes > 3:
                return "TOO_MANY_PEKOS"
        else:
            pekotimes = 0
        
        for punctuation in punctuation_list:
            if word.endswith(punctuation):
                words[index] = word.replace(punctuation, keyword + punctuation)
                break
            elif index + 1 == length:
                words[index] = word + keyword

    pekofied = " ".join(words)
    return pekofied.replace("\n ", "\n") 

async def pekofy_embed(embed):
    pekoembed = embed.to_dict()

    if pekoembed.get("title"):
        pekoembed["title"] = pekofy(pekoembed["title"])
    
    if pekoembed.get("description"):
        pekoembed["description"] = pekofy(pekoembed["description"])
    
    if pekoembed.get("author"):
        if pekoembed["author"].get("name"):
            pekoembed["author"]["name"] = pekofy(pekoembed["author"]["name"])

    return Embed.from_dict(pekoembed)
