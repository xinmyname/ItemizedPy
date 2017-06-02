"""Holds all infrastructure related items"""

import re

__UNCOUNTABLES = [
    "access", "accommodation", "adulthood", "advertising", "advice", "aggression",
    "aid", "air", "alcohol", "anger", "applause", "arithmetic", "art",
    "assistance", "athletics", "attention", "bacon", "baggage", "ballet",
    "beauty", "beef", "beer", "biology", "bison", "botany", "bread", "butter",
    "carbon", "cash", "chaos", "cheese", "chess", "childhood", "clothing",
    "coal", "coffee", "commerce", "compassion", "comprehension", "content",
    "corps", "corruption", "cotton", "courage", "cream", "currency", "dancing",
    "danger", "data", "deer", "delight", "dignity", "dirt", "distribution",
    "dust", "economics", "education", "electricity", "employment", "engineering",
    "envy", "equipment", "ethics", "evidence", "evolution", "faith", "fame",
    "fish", "flour", "flu", "food", "freedom", "fuel", "fun", "furniture",
    "garbage", "garlic", "genetics", "gold", "golf", "gossip", "grammar",
    "gratitude", "grief", "ground", "guilt", "gymnastics", "hair", "happiness",
    "hardware", "harm", "hate", "hatred", "health", "heat", "height", "help",
    "homework", "honesty", "honey", "hospitality", "housework", "humour",
    "hunger", "hydrogen", "ice", "importance", "inflation", "information",
    "injustice", "innocence", "iron", "irony", "jealousy", "jelly", "judo",
    "karate", "kindness", "knowledge", "labour", "lack", "laughter", "lava",
    "leather", "leisure", "lightning", "linguistics", "litter", "livestock",
    "logic", "loneliness", "luck", "luggage", "machinery", "magic", "management",
    "mankind", "marble", "mathematics", "mayonnaise", "means", "measles", "meat",
    "methane", "milk", "money", "moose", "mud", "music", "nature", "news",
    "nitrogen", "nonsense", "nurture", "nutrition", "obedience", "obesity",
    "oil", "oxygen", "passion", "pasta", "patience", "permission", "physics",
    "poetry", "pollution", "poverty", "power", "pronunciation", "psychology",
    "publicity", "quartz", "racism", "rain", "relaxation", "reliability",
    "research", "respect", "revenge", "rice", "rubbish", "rum", "salad",
    "satire", "scissors", "seaside", "series", "shame", "sheep", "shopping",
    "silence", "sleep", "smoke", "smoking", "snow", "soap", "software", "soil",
    "sorrow", "soup", "species", "speed", "spelling", "steam", "stuff",
    "stupidity", "sunshine", "swine", "symmetry", "tennis", "thirst", "thunder",
    "toast", "tolerance", "toys", "traffic", "transporation", "travel", "trust",
    "understanding", "unemployment", "unity", "validity", "veal", "vengeance",
    "violence"]

__RULES = [
    ("(th)is$", r"\1ese"),
    ("(th)at$", r"\1ose"),
    ("(millen)ium$", r"\1ia"),
    ("(l)eaf$", r"\1eaves"),
    ("(r)oof$", r"\1oofs"),
    ("(gen)us$", r"\1era"),
    ("(embarg)o$", r"\1oes"),
    ("arf$", "arves"),
    ("^(b|tabl)eau$", r"\1eaux"),
    ("^(append|matr)ix$", r"\1ices"),
    ("^(ind)ex$", r"\1ices"),
    ("^(a)pparatus$", r"\1pparatuses"),
    ("^(a)lumna$", r"\1lumnae"),
    ("^(alg|vertebr|vit)a$", r"\1ae"),
    ("^(d)ie$", r"\1ice"),
    ("(m|l)ouse$", r"\1ice"),
    ("^(p)erson$", r"\1eople"),
    ("^(o)x$", r"\1xen"),
    ("^(c)hild$", r"\1hildren"),
    ("(g)oose$", r"\1eese"),
    ("(t)ooth$", r"\1eeth"),
    ("lf$", "lves"),
    ("(f)oot$", r"\1eet"),
    ("^(wo|work|fire)man$", r"\1men"),
    ("(potat|tomat|volcan)o$", r"\1oes"),
    ("(criteri|phenomen)on$", r"\1a"),
    ("(nebul)a", r"\1ae"),
    ("oof$", "ooves"),
    ("ium$", "ia"),
    ("um$", "a"),
    ("oaf$", "oaves"),
    ("(thie)f$", r"\1ves"),
    ("fe$", "ves"),
    ("(buffal|carg|mosquit|torped|zer|vet|her|ech)o$", r"\1oes"),
    ("o$", "os"),
    ("ch$", "ches"),
    ("sis$", "ses"),
    ("(corp)us$", r"\1ora"),
    ("(cact|nucle|alumn|bacill|fung|radi|stimul|syllab)us$", r"\1i"),
    ("(ax)is", r"\1es"),
    ("(sh|zz|ss)$", r"\1es"),
    ("x$", "xes"),
    ("(t|sp|r|l|b)y$", r"\1ies"),
    ("s$", "ses"),
    ("$", "s")
]

def plural_of(word="", count=2):
    """Makes a singular word plurals"""

    if count == 1 or not word or __sorted_array_contains(__UNCOUNTABLES, word):
        return word

    for (pattern, repl) in __RULES:
        new_word = re.sub(pattern, repl, word)

        if new_word != word:
            return new_word

    return word

def __sorted_array_contains(array, item):
    first = 0
    last = len(array)-1
    while first <= last:
        mid = (first + last)//2
        if array[mid] == item:
            return True
        else:
            if item < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False
