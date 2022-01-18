DEF_ARTICLE = 'def_article'
IND_ARTICLE = 'ind_article'
CONJ = 'conj'
NO_TAG = 'no_tag'
PART = 'part'
EXCL = 'excl'
NOUN = 'noun'
PREP = 'prep'
ADV = 'adv'
PRON = 'pron'
VERB = 'verb'
NUM = 'num'
PROPER_N = 'properN'
ADJ = 'adj'
ADV_ADJ = 'adv_adj'
PERS_PRON = 'pers_pron'
PRON_NOUN = 'pron_noun'
ADV_CONJ = 'adv_conj'
ACRONYM = 'acronym'
ND = 'nd'


INF = 'inf'
IMP = 'imp'
IMPS = 'imps'
IND = 'ind'
SUBJ = 'subj'

PANT = 'pant'
PCON = 'pcon'
PRPAS = 'prpas'
PACT = 'pact'
PPAS = 'ppas'
PERFPART = 'perfpart'
PAPART = 'papart'

COMP = 'comp'
SUPERL = 'superl'
COMP_ADV = 'comp_adv'
SUPERL_ADV = 'superl_adv'

CARD = 'card'
ORD = 'ord'
FREQ = 'freq'
NOUN_NUM = 'noun_num'

NAKC = 'nakc'
AKC = 'akc'


SURNAME = 'surname'

PRES = 'pres'
PAST = 'past'
AOR = 'aor'
FUT = 'fut'
PARAT = 'parat'


IMPERF = 'imperf'
IMPT = 'impt'
PERF = 'perf'
AUX_PRES = 'aux_pres'
AUX_PAST = 'aux_past'

NA = 'να'
AS = 'ας'
THA = 'θα'
AN = 'αν'
MAKARI = 'μακάρι'
DEN = 'δεν'
MHN = 'μην'

NOM = 'nom'
GEN = 'gen'
DAT = 'dat'
ACC = 'acc'
VOC = 'voc'



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


PRIM = 'prim'
SEC = 'sec'
TER = 'ter'
IMPERS = 'impers'

FEM = 'fem'
MASC = 'masc'
NEUT = 'neut'

SG = 'sg'
PL = 'pl'
DUAL = 'dual'

PASS = 'pass'
ACT = 'act'
MED = 'med'
DEPON = 'depon'
