from resource_data.variables import *

poses = {DEF_ARTICLE: 'definite article',
         IND_ARTICLE: 'indefinite article',
         CONJ: 'conjunction',
         NO_TAG: 'not classified',
         PART: 'particle',
         EXCL: 'exclamation',
         NOUN: 'noun',
         PREP: 'preposition',
         ADV: 'adverb',
         PRON: 'pronoun',
         VERB: 'verb',
         NUM: 'numeral',
         PROPER_N: 'proper noun',
         ADJ: 'adjective',
         ADV_ADJ: "adverb adjective",
         PERS_PRON: 'personal pronoun',
         PRON_NOUN: 'pronoun noun',
         ADV_CONJ: ' conjunctive adverb',
         ACRONYM: 'acronym',
         ND: 'not defined'
         }


secondary_poses = {

    IMPS: 'impersonal',

    ADJ: 'adjective',
    PANT: 'adverbial past active participle',
    PCON: 'adverbial present active participle',
    PRPAS: 'present passive participle',
    PACT: 'present active participle',
    PPAS: 'past passive participle',
    PERFPART: 'perfect passive participle',
    PAPART: 'past active participle',

    COMP: 'comparative',
    SUPERL: 'superlative',
    ADV: 'adverb',
    COMP_ADV: 'comparative adverb',
    SUPERL_ADV: 'superlative adverb',

    CARD: 'cardinal numeral',
    ORD: 'ordinal numeral',
    FREQ: 'frequency numeral adjective',
    NOUN_NUM: 'noun numeral',

    NAKC: 'weak personal pronoun',
    AKC: 'strong personal pronoun',
    ND: 'not defined',

    SURNAME: 'surname'
}



pronouns = ['εγώ', 'εσύ', 'αυτός, αυτή, αυτό', 'εμείς', 'εσείς', 'αυτοί, αυτές, αυτά']

common_tenses = {PRES: 'present', PAST: 'past', FUT: 'future', ND: 'not defined'}

moods = {IND: 'indicative', SUBJ: 'subjunctive', IMPT: 'imperative', INF: 'infinitive'}

# maps tenses with other data
particles = {NA, AN, AS, MAKARI, DEN, THA, MHN}

greek_tenses = {
    'present': [PRES, IND, IMPERF, None],
    'continuous subjunctive': [PRES, SUBJ, IMPERF, NA],
    'continuous hortative': [PRES, SUBJ, IMPERF, AS],
    'future continuous': [PRES, SUBJ, IMPERF, THA],
    'continuous imperative': [PRES, IMPT, IMPERF, None],
    'simple subjunctive': [PRES, SUBJ, PERF, NA],
    'simple future': [PRES, SUBJ, PERF, THA],
    'simple imperative': [PRES, IMPT, PERF, None],
    'aorist': [PAST, IND, PERF, None],
    'paratatikos': [PAST, IND, IMPERF, None],
    'perfect': [AUX_PRES, IND, PERF, None],
    'future perfect': [AUX_PRES, SUBJ, PERF, THA],
    'past perfect': [AUX_PAST, IND, PERF, None],
    'dinitiki': [PAST, IND, IMPERF, THA],
    'optative_2': [PAST, IND, IMPERF, NA],
    'first conditional': [PRES, SUBJ, PERF, AN],
    'second conditional': [PAST, IND, IMPERF, AN],
    'third conditional': [AUX_PAST, IND, PERF, AN]

}

cases = {VOC: 'vocative', GEN: 'genitive', ACC: 'accusative', NOM: 'nominative', DAT: 'dative',
         ND: 'not defined'}

persons = {PRIM: 'first', SEC: 'second', TER: 'third', IMPERS: 'impersonal', ND: 'not defined'}

genders = {FEM: 'feminine', MASC: 'masculine', NEUT: 'neutral', ND: 'not defined'}
# will have to add some other genders specific to Polish language
numbers = {SG: 'singular', PL: 'plural', DUAL: 'dual', ND: 'not defined'}

aspects = {IMPERF: 'imperfective', PERF: 'perfective', ND: 'not defined'}

voices = {PASS: 'passive', ACT: 'active', MED: 'middle', DEPON: 'deponens', ND: 'not defined'}
