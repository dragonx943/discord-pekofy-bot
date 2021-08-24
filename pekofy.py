from discord import Embed
import regex

jp_regex = regex.compile("[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf}]")
discord_regex = regex.compile(r"<(?:@[!&]?|#)\d+>")
url_regex = regex.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")

is_japanese = lambda text: jp_regex.search(text)
is_mention = lambda text: discord_regex.search(text)
is_url = lambda text: url_regex.search(text)

en_punctuation_list = ['.', '?', '!', '\]']
jp_punctuation_list = ['。', '？', '！', '」', '・', '”', '】', '』', '；']
punctuation_list = en_punctuation_list + jp_punctuation_list + ['\n']

def pekofy(input_text):
    """
    Since the previous pekofy function was written in the thought of Reddit message formatting,
    I decided to rewrite it, to avoid Discord mentions and be more pythonic.
    (sorry that it took months for me to do something)
    """
    corrected = input_text.replace("\n", "\n ")
    words = corrected.split(" ")
    length = len(words)

    print(words)
    for index, word in enumerate(words):
        if is_japanese(word):
            keyword = "ぺこ"
        else:
            keyword = " peko"
        
        if is_mention(word) or is_url(word):
            continue

        for punctuation in punctuation_list:
            if punctuation in word:
                #print(words)
                words[index] = word.replace(punctuation, keyword + punctuation) 
                break
            elif index + 1 == length:
                words[index] = word + keyword

    pekofied = " ".join(words)
    return pekofied.replace("\n ", "\n") 

def embed_pekofy(embed):
    pekoembed = embed.to_dict()

    if pekoembed.get("title"):
        pekoembed["title"] = pekofy(pekoembed["title"])
    
    if pekoembed.get("description"):
        pekoembed["description"] = pekofy(pekoembed["description"])
    
    if pekoembed.get("author"):
        if pekoembed["author"].get("name"):
            pekoembed["author"]["name"] = pekofy(pekoembed["author"]["name"])

    return Embed.from_dict(pekoembed)
