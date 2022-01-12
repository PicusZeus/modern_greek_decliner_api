poses = {'def_article': 'definite article',
         'ind_article': 'indefinite article',
         'conj': 'conjunction',
         'no_tag': 'not classified',
         'part': 'particle',
         'excl': 'exclamation',
         'noun': 'noun',
         'prep': 'preposition',
         'adv': 'adverb',
         'pron': 'pronoun',
         'verb': 'verb',
         'num': 'numeral',
         'properN': 'proper noun',
         'adj': 'adjective',
         'adv_adj': "adverb adjective",
         'pers_pron': 'personal pronoun',
         'pron_noun': 'pronoun noun',
         'adv_conj': ' conjunctive adverb',
         'acronym': 'acronym',
          'nd': 'not defined'
         }

secondary_poses = {

    'inf': 'infinitive',
    'imp': 'imperative',
    'imps': 'impersonal',
    'ind': 'indicative',
    'adj': 'adjective',


    'pant': 'adverbial past active participle',
    'pcon': 'adverbial present active participle',
    'prpas': 'present passive participle',
    'pact': 'present active participle',
    'ppas': 'past passive participle',
    'perfpart': 'perfect passive participle',
    'papart': 'past active participle',

    'comp': 'comparative',
    'superl': 'superlative',
    'adv': 'adverb',
    'comp_adv': 'comparative adverb',
    'superl_adv': 'superlative adverb',


    'card': 'cardinal numeral',
    'ord': 'ordinal numeral',
    'freq': 'frequency numeral adjective',
    'noun_num': 'noun numeral',
    
    'nakc': 'weak personal pronoun',
    'akc': 'strong personal pronoun',
    'nd': 'not defined',

    'surname': 'surname'
}

length_of_endings = {
    "1": [
        "ω",
        "ώ",
        "ά",
        "ς",
        "ν",
        "α",
        "ε"
    ],
    "2": [
        "ει",
        "άω",
        "ας",
        "άν",
        "εί",
        "με",
        "τε",
        "νε",
        "ες",
        "αν",
        "ου"
    ],
    "3": [
        "εις",
        "ετε",
        "ουν",
        "άει",
        "άμε",
        "άτε",
        "άνε",
        "ούν",
        "είς",
        "αμε",
        "ατε",
        "ανε"
    ],
    "4": [
        "ουμε",
        "ουνε",
        "ούμε",
        "ούνε",
        "είτε",
        "ομαι",
        "εσαι",
        "εται",
        "εστε",
        "άμαι",
        "άσαι",
        "άται",
        "άστε",
        "όταν",
        "είτο",
        "είσο"
    ],
    "5": [
        "ονται",
        "ιέμαι",
        "ιέσαι",
        "ιέται",
        "ιέστε",
        "ούμαι",
        "είσαι",
        "είται",
        "είστε",
        "όμουν",
        "όσουν",
        "ότανε",
        "ονταν",
        "ούντο",
        "ούμην",
        "είσθε"
    ],
    "6": [
        "όμαστε",
        "όσαστε",
        "ούμεθα",
        "ούνται",
        "όμουνα",
        "όσουνα",
        "ιόμουν",
        "ιόσουν",
        "ούμουν",
        "ούσουν",
        "ούνταν"
    ],
    "7": [
        "ιόμαστε",
        "ιόσαστε",
        "ιούνται",
        "ούμαστε",
        "όμασταν",
        "όσασταν",
        "ιόμουνα",
        "ιόσουνα",
        "ιούνταν",
        "ούσαστε"
    ],
    "8": [
        "όντουσαν",
        "ιόμασταν",
        "ιόσασταν",
        "ούμασταν",
        "ούσασταν"
    ]
}

pronouns= ['εγώ', 'εσύ', 'αυτός, αυτή, αυτό', 'εμείς', 'εσείς', 'αυτοί, αυτές, αυτά']



common_tenses = {'fin': 'present', 'past': 'past', 'fut': 'future', 'nd': 'not defined'}

# maps tenses with other data
greek_tenses = {
    'present': ['fin', 'imperf'],
    'continuous subjunctive': ['fin', 'imperf', 'να '],
    'continuous hortative': ['fin', 'imperf', 'ας '],
    'future continuous': ['fin', 'imperf', 'θα '],
    'continuous imperative': ['impt', 'imperf'],
    'simple subjunctive': ['fin', 'perf', 'να '],
    'simple future': ['fin', 'perf', 'θα '],
    'simple imperative': ['impt', 'perf'],
    'aorist': ['praet', 'perf'],
    'paratatikos': ['praet', 'imperf'],
    'perfect': ['aux_fin', 'perf'],
    'future perfect': ['aux_fin', 'perf', 'θα '],
    'past perfect': ['aux_praet', 'perf'],
    'dinitiki': ['praet', 'imperf', 'θα '],
    'optative_2': ['praet', 'imperf', 'να '],
    'first conditional': ['fin', 'perf', 'αν '],
    'second conditional': ['praet', 'imperf', 'αν '],
    'third conditional': ['aux_praet', 'perf', 'αν ']

}

cases = {'voc': 'vocative', 'gen': 'genitive', 'acc': 'accusative', 'nom': 'nominative', 'dat': 'dative', 'nd': 'not defined'}

persons = {'pri', 'sec', 'ter', 'impersonal', 'nd'}

genders = {'fem': 'feminine', 'masc': 'masculine', 'neut': 'neutral', 'nd': 'not defined'}
# will have to add some other genders specific to Polish language
numbers = {'sg', 'pl', 'dual', 'nd'}

aspects = {'imperf', 'perf', 'nd'}

voices = {'passive', 'active', 'middle', 'deponens', 'nd'}


