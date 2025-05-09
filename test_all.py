#!/usr/bin/python3
import sys
import time
import json
from autocorrect import Speller
from autocorrect.typos import Word

english = {
    "access": "acess",
    "accommodation": "accomodation|acommodation|acomodation",
    "arranged": "aranged|arrainged",
    "basically": "basicaly",
    "beginning": "begining",
    "benefit": "benifit",
    "benefits": "benifits",
    "between": "beetween",
    "biscuits": "biscits|biscuts|bisquits|buiscits|buiscuts",
    "built": "biult",
    "career": "carrer",
    "certain": "cirtain",
    "challenges": "chalenges|chalenges",
    "chapter": "chaper|chaphter|chaptur",
    "clerical": "clearical",
    "committee": "comittee",
    "completely": "completly",
    "consider": "concider",
    "considerable": "conciderable",
    "decide": "descide",
    "decided": "descided",
    "definition": "defenition",
    "definitions": "defenitions",
    "description": "discription",
    "different": "diffrent",
    "driven": "dirven",
    "establishing": "astablishing|establising",
    "extended": "extented",
    "extremely": "extreamly",
    "families": "familes",
    "february": "febuary",
    "gallery": "galery|gallary|gallerry|gallrey",
    "hierarchy": "hierchy",
    "inconvenient": "inconvienient|inconvient|inconvinient",
    "initial": "intial",
    "level": "leval",
    "levels": "levals",
    "literature": "litriture",
    "magnificent": "magnificnet|magificent|magnifcent|magnifecent",
    "management": "managment",
    "monitoring": "monitering",
    "necessary": "neccesary|necesary|neccesary|necassary|necassery",
    "parallel": "paralel|paralell|parrallel|parralell|parrallell",
    "particular": "particulaur",
    "perhaps": "perhapse",
    "position": "possition",
    "possible": "possable",
    "pronunciation": "pronounciation",
    "questionnaire": "questionaire",
    "receive": "recieve",
    "scarcely": "scarcly|scarecly|scarely",
    "scissors": "scisors|sissors",
    "singular": "singulaur",
    "someone": "somone",
    "southern": "southen",
    "special": "speaical|specail|specal|speical",
    "triangular": "triangulaur",
    "unexpected": "unexpcted|unexpeted|unexspected",
    "unfortunately": "unfortunatly",
    "unique": "uneque",
    "useful": "usefull",
    "valuable": "valubale|valuble",
    "variable": "varable",
    "variant": "vairiant",
    "various": "vairious",
    "visitors": "vistors",
    "voting": "voteing",
}

sentences = {
    "There is no coming to consciousness without pain.": "There is no comin to consiousnes without pain.",
    "Hey! Mr. Tambourine Man, play a song for me,": "Hey! Mr. Tambourime Man, play a ssong for me,",
    "I'm not sleepy and there is no place I'm going to.": "I'm not sleapy and tehre is no place I'm giong to.",
}

upper = {
    "USA": "USA",
    "camelCased": "camelCased",
    "I": "I",
}

only_replacements = {
    "other": "ather",
    "health": "heaith",
    "should": "shauld",
    "mental": "mentat",
    "also": "aiso",
    "order": "arder",
    "they": "thew",  # they, not the
    "here": "herw",  # here, not her
}

spanish_words_all_correct = {
    "hola": "hola",
    "hambre": "hanbre",
    "rabia": "ravia",
    "Fenómenos meteorológicos": "Fenomenos meteorologicos",
    "vamos": "vamo",
    "tipo": "tpio",
    "compromiso": "comppromiso",
    "conseguir": "conzeguir",
    "este": "ehte",
    "umbral": "unbral",
    "Estructura": "Extructura",
    "para": "praa",
}

italian_words_all_correct = {
    "male": "mlae",
    "partire": "paltile",
    "piatta": "paatta",
    "ordine": "oldine",
    "leggero": "lezgero",
    "cane": "canre",
    "salute": "slaute",
    "polipo": "popipo",
    "saltare": "saltale",
    "formaggio": "formazzio",
    "salto": "saulto",
}

french_words_all_correct = {
    "ordre": "oldre",
    "leger": "lezger",
    "cahier": "cnhier",
    "saut": "slaut",
    "vache": "vacne",
    "fromage": "fromae",
    "bisous": "biosus",
    "possible": "possable",
    "position": "posizion",
    "populaire": "popularie",
}

single_typos_me = {
    "ae",
    "ame",
    "be",
    "bme",
    "ce",
    "cme",
    "de",
    "dme",
    "e",
    "ee",
    "em",
    "eme",
    "fe",
    "fme",
    "ge",
    "gme",
    "he",
    "hme",
    "ie",
    "ime",
    "je",
    "jme",
    "ke",
    "kme",
    "le",
    "lme",
    "m",
    "ma",
    "mae",
    "mb",
    "mbe",
    "mc",
    "mce",
    "md",
    "mde",
    "me",
    "mea",
    "meb",
    "mec",
    "med",
    "mee",
    "mef",
    "meg",
    "meh",
    "mei",
    "mej",
    "mek",
    "mel",
    "mem",
    "men",
    "meo",
    "mep",
    "meq",
    "mer",
    "mes",
    "met",
    "meu",
    "mev",
    "mew",
    "mex",
    "mey",
    "mez",
    "mf",
    "mfe",
    "mg",
    "mge",
    "mh",
    "mhe",
    "mi",
    "mie",
    "mj",
    "mje",
    "mk",
    "mke",
    "ml",
    "mle",
    "mm",
    "mme",
    "mn",
    "mne",
    "mo",
    "moe",
    "mp",
    "mpe",
    "mq",
    "mqe",
    "mr",
    "mre",
    "ms",
    "mse",
    "mt",
    "mte",
    "mu",
    "mue",
    "mv",
    "mve",
    "mw",
    "mwe",
    "mx",
    "mxe",
    "my",
    "mye",
    "mz",
    "mze",
    "ne",
    "nme",
    "oe",
    "ome",
    "pe",
    "pme",
    "qe",
    "qme",
    "re",
    "rme",
    "se",
    "sme",
    "te",
    "tme",
    "ue",
    "ume",
    "ve",
    "vme",
    "we",
    "wme",
    "xe",
    "xme",
    "ye",
    "yme",
    "ze",
    "zme",
}

optional_language_tests = {
    "en": {
        "forbidden": "forbiden",
        "decisions": "deciscions|descisions",
        "supposedly": "supposidly",
        "embellishing": "embelishing",
        "technique": "tecnique",
        "permanently": "perminantly",
        "confirmation": "confermation",
        "appointment": "appoitment",
        "progression": "progresion",
        "accompanying": "acompaning",
        "applicable": "aplicable",
        "regained": "regined",
        "guidelines": "guidlines",
        "surrounding": "serounding",
        "titles": "tittles",
        "unavailable": "unavailble",
        "advantageous": "advantageos",
        "brief": "brif",
        "appeal": "apeal",
        "consisting": "consisiting",
        "clerk": "cleark|clerck",
        "component": "componant",
        "favourable": "faverable",
        "separation": "seperation",
        "search": "serch",
        "receive": "recieve",
        "employees": "emploies",
        "prior": "piror",
        "resulting": "reulting",
        "suggestion": "sugestion",
        "opinion": "oppinion",
        "cancellation": "cancelation",
        "criticism": "citisum",
        "useful": "usful",
        "humour": "humor",
        "anomalies": "anomolies",
        "would": "whould",
        "doubt": "doupt",
        "examination": "eximination",
        "therefore": "therefoe",
        "recommend": "recomend",
        "separated": "seperated",
        "successful": "sucssuful|succesful",
        "apparent": "apparant",
        "occurred": "occureed",
        "particular": "paerticulaur",
        "pivoting": "pivting",
        "announcing": "anouncing",
        "challenge": "chalange",
        "arrangements": "araingements",
        "proportions": "proprtions",
        "organized": "oranised",
        "accept": "acept",
        "dependence": "dependance",
        "unequalled": "unequaled",
        "numbers": "numbuers",
        "sense": "sence",
        "conversely": "conversly",
        "provide": "provid",
        "arrangement": "arrangment",
        "responsibilities": "responsiblities",
        "fourth": "forth",
        "ordinary": "ordenary",
        "description": "desription|descvription|desacription",
        "inconceivable": "inconcievable",
        "data": "dsata",
        "register": "rgister",
        "supervision": "supervison",
        "encompassing": "encompasing",
        "negligible": "negligable",
        "allow": "alow",
        "operations": "operatins",
        "executed": "executted",
        "interpretation": "interpritation",
        "hierarchy": "heiarky",
        "indeed": "indead",
        "years": "yesars",
        "through": "throut",
        "committee": "committe",
        "inquiries": "equiries",
        "before": "befor",
        "continued": "contuned",
        "permanent": "perminant",
        "choose": "chose",
        "virtually": "vertually",
        "correspondence": "correspondance",
        "eventually": "eventully",
        "lonely": "lonley",
        "profession": "preffeson",
        "they": "thay",
        "now": "noe",
        "desperately": "despratly",
        "university": "unversity",
        "adjournment": "adjurnment",
        "possibilities": "possablities",
        "stopped": "stoped",
        "mean": "meen",
        "weighted": "wagted",
        "adequately": "adequattly",
        "shown": "hown",
        "matrix": "matriiix",
        "profit": "proffit",
        "encourage": "encorage",
        "collate": "colate",
        "disaggregate": "disaggreagte|disaggreaget",
        "receiving": "recieving|reciving",
        "proviso": "provisoe",
        "umbrella": "umberalla",
        "approached": "aproached",
        "pleasant": "plesent",
        "difficulty": "dificulty",
        "appointments": "apointments",
        "base": "basse",
        "conditioning": "conditining",
        "earliest": "earlyest",
        "beginning": "begining",
        "universally": "universaly",
        "unresolved": "unresloved",
        "length": "lengh",
        "exponentially": "exponentualy",
        "utilized": "utalised",
        "set": "et",
        "surveys": "servays",
        "families": "familys",
        "system": "sysem",
        "approximately": "aproximatly",
        "their": "ther",
        "scheme": "scheem",
        "speaking": "speeking",
        "repetitive": "repetative",
        "inefficient": "ineffiect",
        "geneva": "geniva",
        "exactly": "exsactly",
        "immediate": "imediate",
        "appreciation": "apreciation",
        "luckily": "luckeley",
        "eliminated": "elimiated",
        "believe": "belive",
        "appreciated": "apreciated",
        "readjusted": "reajusted",
        "were": "wer|where",
        "feeling": "fealing",
        "and": "anf",
        "false": "faulse",
        "seen": "seeen",
        "interrogating": "interogationg",
        "academically": "academicly",
        "relatively": "relativly|relitivly",
        "traditionally": "traditionaly",
        "studying": "studing",
        "majority": "majorty",
        "build": "biuld",
        "aggravating": "agravating",
        "transactions": "trasactions",
        "arguing": "aurguing",
        "sheets": "sheertes",
        "successive": "sucsesive|sucessive",
        "segment": "segemnt",
        "especially": "especaily",
        "later": "latter",
        "senior": "sienior",
        "dragged": "draged",
        "atmosphere": "atmospher",
        "drastically": "drasticaly",
        "particularly": "particulary",
        "visitor": "vistor",
        "session": "sesion",
        "continually": "contually",
        "availability": "avaiblity",
        "busy": "buisy",
        "parameters": "perametres",
        "surroundings": "suroundings|seroundings",
        "employed": "emploied",
        "adequate": "adiquate",
        "handle": "handel",
        "means": "meens",
        "familiar": "familer",
        "between": "beeteen",
        "overall": "overal",
        "timing": "timeing",
        "committees": "comittees|commitees",
        "queries": "quies",
        "econometric": "economtric",
        "erroneous": "errounous",
        "decides": "descides",
        "reference": "refereence|refference",
        "intelligence": "inteligence",
        "edition": "ediion|ediition",
        "are": "arte",
        "apologies": "appologies",
        "thermawear": "thermawere|thermawhere",
        "techniques": "tecniques",
        "voluntary": "volantary",
        "subsequent": "subsequant|subsiquent",
        "currently": "curruntly",
        "forecast": "forcast",
        "weapons": "wepons",
        "routine": "rouint",
        "neither": "niether",
        "approach": "aproach",
        "available": "availble",
        "recently": "reciently",
        "ability": "ablity",
        "nature": "natior",
        "commercial": "comersial",
        "agencies": "agences",
        "however": "howeverr",
        "suggested": "sugested",
        "career": "carear",
        "many": "mony",
        "annual": "anual",
        "according": "acording",
        "receives": "recives|recieves",
        "interesting": "intresting",
        "expense": "expence",
        "relevant": "relavent|relevaant",
        "table": "tasble",
        "throughout": "throuout",
        "conference": "conferance",
        "sensible": "sensable",
        "described": "discribed|describd",
        "union": "unioun",
        "interest": "intrest",
        "flexible": "flexable",
        "refered": "reffered",
        "controlled": "controled",
        "sufficient": "suficient",
        "dissension": "desention",
        "adaptable": "adabtable",
        "representative": "representitive",
        "irrelevant": "irrelavent",
        "unnecessarily": "unessasarily",
        "applied": "upplied",
        "apologised": "appologised",
        "these": "thees|thess",
        "choices": "choises",
        "will": "wil",
        "procedure": "proceduer",
        "shortened": "shortend",
        "manually": "manualy",
        "disappointing": "dissapoiting",
        "excessively": "exessively",
        "comments": "coments",
        "containing": "containg",
        "develop": "develope",
        "credit": "creadit",
        "government": "goverment",
        "acquaintances": "aquantences",
        "orientated": "orentated",
        "widely": "widly",
        "advise": "advice",
        "difficult": "dificult",
        "investigated": "investegated",
        "bonus": "bonas",
        "conceived": "concieved",
        "nationally": "nationaly",
        "compared": "comppared|compased",
        "moving": "moveing",
        "necessity": "nessesity",
        "opportunity": "oppertunity|oppotunity|opperttunity",
        "thoughts": "thorts",
        "equalled": "equaled",
        "variety": "variatry",
        "analysis": "analiss|analsis|analisis",
        "patterns": "pattarns",
        "qualities": "quaties",
        "easily": "easyly",
        "organization": "oranisation|oragnisation",
        "the": "thw|hte|thi",
        "corporate": "corparate",
        "composed": "compossed",
        "enormously": "enomosly",
        "financially": "financialy",
        "functionally": "functionaly",
        "discipline": "disiplin",
        "announcement": "anouncement",
        "progresses": "progressess",
        "except": "excxept",
        "recommending": "recomending",
        "mathematically": "mathematicaly",
        "source": "sorce",
        "combine": "comibine",
        "input": "inut",
        "careers": "currers|carrers",
        "resolved": "resoved",
        "demands": "diemands",
        "unequivocally": "unequivocaly",
        "suffering": "suufering",
        "immediately": "imidatly|imediatly",
        "accepted": "acepted",
        "projects": "projeccts",
        "necessary": "necasery|nessasary|nessisary|neccassary",
        "journalism": "journaism",
        "unnecessary": "unessessay",
        "night": "nite",
        "output": "oputput",
        "security": "seurity",
        "essential": "esential",
        "beneficial": "benificial|benficial",
        "explaining": "explaning",
        "supplementary": "suplementary",
        "questionnaire": "questionare",
        "employment": "empolyment",
        "proceeding": "proceding",
        "decision": "descisions|descision",
        "per": "pere",
        "discretion": "discresion",
        "reaching": "reching",
        "analysed": "analised",
        "expansion": "expanion",
        "although": "athough",
        "subtract": "subtrcat",
        "analysing": "aalysing",
        "comparison": "comparrison",
        "months": "monthes",
        "hierarchal": "hierachial",
        "misleading": "missleading",
        "commit": "comit",
        "auguments": "aurgument",
        "within": "withing",
        "obtaining": "optaning",
        "accounts": "acounts",
        "primarily": "pimarily",
        "operator": "opertor",
        "accumulated": "acumulated",
        "extremely": "extreemly",
        "there": "thear",
        "summarys": "sumarys",
        "analyse": "analiss",
        "understandable": "understadable",
        "safeguard": "safegaurd",
        "consist": "consisit",
        "declarations": "declaratrions",
        "minutes": "muinutes|muiuets",
        "associated": "assosiated",
        "accessibility": "accessability",
        "examine": "examin",
        "surveying": "servaying",
        "politics": "polatics",
        "annoying": "anoying",
        "again": "agiin",
        "assessing": "accesing",
        "ideally": "idealy",
        "scrutinized": "scrutiniesed",
        "simular": "similar",
        "personnel": "personel",
        "whereas": "wheras",
        "when": "whn",
        "geographically": "goegraphicaly",
        "gaining": "ganing",
        "requested": "rquested",
        "separate": "seporate",
        "students": "studens",
        "prepared": "prepaired",
        "generated": "generataed",
        "graphically": "graphicaly",
        "suited": "suted",
        "variable": "varible|vaiable",
        "building": "biulding",
        "required": "reequired",
        "necessitates": "nessisitates",
        "together": "togehter",
        "profits": "proffits",
    },
    "pl": {
        "gżegżółka": "grzegżółka",
        "pszczoła": "przczoua",
        "marazm": "marasm",
        "kosodrzewina": "kosodzewima",
        "zabrzmiało": "zabrzmialo",
        "wybór": "wybor",
        "jesteś": "jestes",
        "potomstwo": "potostwo",
        "dotknął": "dotknal",
        "służącej": "słóżącej",
        "Paul": "paul",
        "koń": "kon",
        "Warszawa": "warszawa",
        "zacisnęła": "zacisnela",
        "zagłodzonych": "zaglodzonych",
        "zgiń": "zgin",
        "świerzb": "świeżb",
        "żyto": "rzyto",
        "chuligan": "huligan",
        "prószyć": "pruszyć",
        "wehikuł": "wechikuł",
        "humorzasty": "chumorzasty",
        "sufrażystki": "sufrarzystki",
        "zastrzeżenie": "zastrzerzenie",
        "rozprężenie": "rozpręrzenie",
        "higroskopijny": "chigroskopijny",
        "błahostka": "błachostka",
        "pszenica": "przenica",
        "zżymać": "zrzymać",
        "strużka": "strurzka",
        "rzeżucha": "rzerzucha",
        "ówczesny": "uwczesny",
        "uśmiechnięta": "usmiechnieta",
        "podnieta": "podgnieta",
        "drzwi": "drzwu",
        "bezkształtnej": "bezksztaltnej",
        "przepadnij": "przepadmi",
        "oczy": "ocxy",
        "Manaam": "manaam",
        "Skłodowska": "skłodowska",
    },
    "tr": {
        "yanlış": "yanlş|yanls",
        "gidiyor": "gidiyr|gidiyro",
        "geleceğim": "gelecegim",
        "yapacak": "yapıcak",
        "sevecek": "sevicek",
        "muhakkak": "muhakak|muakkak|muakak",
        "yapacağım": "yapacagim",
        "yapacaktık": "yapacaktik",
        "yapılacaktı": "yapılcaktı",
        "salgın": "salgin",
        "komisyonu": "komidyonu|komilyonu",
        "kelimesinin": "kelmesinin",
        "bilgisini": "bilgiini|bilgisin",
        "tarafından": "tarafndan|tarafindan",
        "işgal": "şigal",
        "taraf": "teraf",
        "ekonomik": "ekonomk",
        "sıkıntılar": "sıkıntıler",
        "anlaşılacağı": "anlaşlacağı",
        "ettirdi": "ettird",
    },
    "ru": {
        "убийства": "убийста",
        "американские": "америкнские",
        "приговорённый": "пргговорённый",
        "председательствовавший": "председательствовавши",
        "Разработана": "Разработаа",
        "широкий": "ширркий",
        "тридцать": "тридцатьь",
        "удерживала": "удержииала",
        "возглавила": "вззглавила",
        "написанной": "напссанной",
    },
    "uk": {
        "положення": "положеннн",
        "міжконтинентальної": "міжконтннентальноi|мїxконтинентальної",
        "журналу": "xурналу",
        "Боснію": "Босніo",
        "письменник": "письмениик",
        "повсякденного": "повсякденноо",
        "алегоричні": "алегоринні",
        "сцени": "сценн|сцеии",
        "названий": "названйй",
        "культуролог": "культуролг",
    },
    "es": {
        "hola": "hola",
        "hambre": "hanbre",
        "rabia": "ravia",
        "Fenómenos meteorológicos": "Fenomenos meteorologicos",
        "vamos": "vamo",
        "tipo": "tpio",
        "compromiso": "comppromiso",
        "conseguir": "conzeguir",
        "este": "ehte",
        "umbral": "unbral",
        "Acción": "Accion",
        "Comunicación": "Comunicacion",
        "Estructura": "Extructura",
        "Abanderar": "Habanderar|Avanderar|Havanderar",
        "para": "praa",
        "camión": "cambión",
    },
    "pt": {
        "contigo": "contgio",
        "Comida": "Conida",
        "namorada": "nanorada",
        "corrida": "corida",
        "computador": "computadr",
        "estadunidense": "estaunidense",
        "decidiu": "drcidiu",
        "oportunidades": "oportuniidades",
        "atualmente": "atualmentef",
        "descoberto": "descoverto",
        "indicado": "indixado",
        "arrepende": "arepende",
        "declara": "declada",
    },
    "el": {
        "άκρη": "άκρι",
        "άνθρωποι": "άνθρωπει",
        "άνθρωπος": "ανθροπος|άθρωπος|άνθρωποσ|άνθροπος",
        "άρρωστος": "άρρωςτος|άρωστος",
        "αισθανθεί": "εσθανθεί",
        "ασθένεια": "ασθένια",
        "γεια": "γειαα",
        "διάγνωση": "διάγνοση",
        "διαχείριση": "διαχίρηση",
        "είμαι": "ειμε",
        "είσαι": "εισε",
        "επιχείρηση": "επιχείριση",
        "ευχαριστώ": "εφχαριστω",
        "κάποιον": "κάπιον",
        "κέφι": "κέφυ",
        "καί": "κε",
        "καιρό": "κερό",
        "κοντά": "κωντά",
        "μεσημέρη": "μεσημέρει",
        "ξέρεις": "ξέρις",
        "ξεκινάς": "ξεκηνάς",
        "παιδί": "πεδί",
        "παρατηρούν": "παρατιρούν",
        "ποδόσφαιρο": "ποδόσφερο",
        "ποτάμι": "ποτάμυ",
        "προτείνεις": "προτίνεις",
        "πρωί": "πρωή",
        "ρώτησε": "ρώτησαι",
        "σπίτι": "σπίτη",
        "σπουδαίο": "σπουδέο",
        "συμβαίνει": "συμβαίνη",
        "συνέχεια": "συνέχια",
        "συναρπαστικό": "σιυναρπαστικό",
        "ταξίδι": "ταξήδι",
        "φορά": "φωρά",
        "όλα": "ώλα",
        "κεφάλι": "κεφάλυ|κεφάλη",
        "λιμάνι": "λιμάνη",
        "κρεβάτι": "κρεβάτη",
        "φιστίκυ": "φιστίκι",
        "λουλούδι": "λουλούδη",
        "παππούς": "παπούς",
        "παίζω": "πέζω",
        "παιχνίδι": "πεχνίδι",
        "μητέρα": "μυτέρα",
        "πατέρας": "παττέρας",
        "πρωίνος": "πρωίνοσ",
        "στυλό": "στυλός",
        "πορτοκάλι": "πορτοκάλλι",
        "μήλο": "μείλο",
        "φράουλα": "ράουλα",
        "μπανάνα": "πανάνα",
        "καφές": "καφέσ",
        "γραφείο": "γραφίο",
        "Επικοινωνία": "Επικοινονία",
        "Ερώτηση": "Ερώτηςη",
        "απορία": "Απορεία",
        "Ορισμός": "Οροισμός",
        "λεξικό": "λεξξικό",
        "Γερμανικά": "Γερμανικκά",
        "μετάφραση": "μετάφαση",
    },
    "cs": {
        "celé": "ďelé",
        "jedny": "jedáy",
        "lingvistiku": "lingviskiku",
        "Větví": "Větďť",
        "nepřestaneme": "iepřestaneme",
        "vlna": "vlwi",
        "natož": "nabož",
        "této": "típo",
        "směr": "sjmr",
        "neobejdou": "nkqbejdou",
        "kosila": "kwsila",
        "Stroj": "ntroj",
        "dravost": "drapost",
        "cípu": "cípť",
        "archeolog": "arcůexlog",
        "mozku": "můzkw",
        "otřesů": "otresů",
        "Délky": "Drlgy",
        "blíž": "běíž",
        "zbytky": "úbytby",
        "mobily": "čobily",
        "sebe": "sefe",
        "vystěhování": "vystěhotání",
        "poctivé": "kocxivé",
        "hradiště": "hrkdiště",
        "slabí": "slaví",
        "unikátní": "unikdtní",
        "pomoc": "ažmoc",
        "číst": "číht",
        "hladině": "hladins",
        "odhadů": "ížhadů",
        "valounů": "valopnů",
        "různá": "růsná",
        "vývojovou": "vývsjovou",
        "zájmy": "ťájmy",
        "kdybyste": "kdybystň",
        "spatřovali": "spstřovali",
        "obklady": "obkladí",
        "cestana": "cástana",
        "rozeznají": "rozemnají",
        "zimující": "zimojícp",
        "nýbrž": "nýfre",
        "objevila": "objemila",
        "historkám": "histozkám",
        "kruhu": "kruůu",
        "bylo": "uylo",
        "chybí": "chňbx",
        "Loňskému": "Loňňkémp",
        "středisku": "střediůku",
        "vysoká": "šysoká",
        "objeveny": "fbéeveny",
        "potřebu": "ýotřhbu",
        "slabého": "alcbého",
        "dostaly": "aqstaly",
        "působil": "půsočik",
        "Cestě": "Cežtě",
        "fakulty": "falulty",
        "češi": "debi",
        "uveřejněném": "uveřejngném",
        "obsahem": "objahem",
        "rekordům": "nekorčům",
        "Davida": "Davýdó",
        "sporty": "sporťy",
        "duhový": "dqúový",
        "říkat": "říkmt",
        "virulentní": "viruleitní",
        "praxi": "traxe",
        "rozvojem": "áozěojem",
        "něco": "nýěo",
        "někdo": "nějdo",
        "vajíčka": "vajíčua",
        "dostal": "dostďl",
        "Této": "Txto",
        "miliardy": "mileardy",
        "advokáti": "jžvokáti",
        "nalezených": "nalezpných",
        "evoluci": "evobuci",
        "zrnko": "zrnqú",
        "přichází": "přqcháyí",
        "mapy": "maxy",
        "trubek": "aribek",
        "průvodu": "provodk",
        "opačně": "čpačně",
        "odhalil": "čdhalil",
        "všeobecné": "všeýbecné",
        "tváře": "óváře",
        "drak": "drao",
        "našli": "ntšli",
        "dánského": "ňánského",
        "adrenalin": "adrěnalin",
        "Ožije": "Ožijě",
        "chvíli": "hhvílš",
        "bouřlivý": "boířřivý",
        "motýly": "motýčy",
        "starověkého": "starověéého",
        "zástupci": "zástuhcď",
        "vydat": "vfdat",
        "expanze": "expaněe",
        "smetánka": "soetánka",
        "ležící": "ůežícč",
        "tahy": "taey",
        "druh": "ťrdh",
        "přehlídky": "pšehlídkg",
        "republice": "rečublice",
        "park": "áark",
        "nastěhovali": "nastihovali",
        "center": "cenber",
        "Slavný": "Sčavaý",
        "chlapců": "célapců",
        "přicházejí": "přichávejř",
        "poznat": "poznzt",
        "přednost": "lřednosv",
        "vědeckou": "věteckeu",
        "jich": "ěiih",
        "lyžařského": "lyáařského",
        "proslulou": "prosluloq",
        "horská": "horskz",
        "charisma": "vharismy",
        "řekl": "řwkl",
        "sítě": "šítě",
        "silou": "siuou",
        "koncentracích": "konceitracích",
        "nežádoucí": "žežádoucé",
        "obejít": "ozejžt",
        "měla": "měaa",
        "mírnějšími": "mírnějjísi",
        "její": "řfjí",
        "Jednoho": "Jednohó",
        "vystoupit": "hystoupió",
        "brázdil": "ůrázdil",
        "větru": "sětmu",
        "bouře": "bžuře",
        "přišly": "ařišln",
        "francouzské": "francouesžé",
        "filosofa": "felosofa",
        "regionu": "rcgionu",
        "neumějí": "neuměpí",
        "položený": "poloýený",
        "kmen": "kťen",
        "Pódia": "qóóia",
        "zemětřesení": "zemětřeaení",
        "popsat": "pžůsat",
        "vděčili": "vdščili",
        "staveb": "stakwb",
        "trénují": "tíénují",
        "liší": "lišk",
        "uplyne": "uúlyne",
        "vrcholku": "vrcholkú",
        "britští": "britště",
        "Rusku": "Ručíu",
        "pronikání": "proóikáří",
        "slona": "slvna",
        "víno": "vířo",
        "nemocem": "nevocem",
        "šílená": "vílená",
        "jader": "jaámr",
        "stalo": "staso",
        "rozpoznat": "rťzpnznat",
        "multikulturním": "mulýikulturním",
        "nadace": "xasace",
        "americký": "americkl",
        "vykreslují": "vykreslijí",
        "polarizovaný": "polarbzovaný",
        "jezdí": "jefdí",
        "zaledněné": "zalednulé",
        "děti": "dětú",
        "emise": "emiře",
        "vyvozují": "vyvozusí",
        "národní": "nárbdní",
        "naplaveninách": "nwplaveninách",
    },
    "it": {
        "ciao": "ciap",
        "nera": "nela",
        "mamma": "mamna",
        "dimenticare": "dimelticare",
        "assaggiare": "assaggiale|assaggiael",
        "portare": "poltare",
        "voglio": "vollio",
        "niente": "nente",
        "però": "pelò",
        "medaglia": "medagla|mdeaglia",
        "annegare": "annegale",
        "fare": "fale",
        "polmone": "pormone",
        "eseguire": "eseugire|esegurie",
        "mangiare": "mamgiare",
        "dormire": "dolmire|dirmire",
        "cara": "cala",
        "serpente": "selpente|serepnte",
        "noia": "nioa",
        "carne": "carme",
        "salame": "saalme",
        "chitarra": "chitalra|chitalla|chitara|kitarra",
        "giovane": "giovnae",
        "cavallo": "cavatlo",
        "poltrona": "poltrola",
    },
    "fr": {
        "disparu": "disparue",
        "atteint": "atteind",
        "croient": "croyent",
        "cicogne": "cygogne",
        "electronique": "électronique",
        "bien": "bein",
        "connexion": "connection",
        "galerie": "gallerie",
        "meilleur": "meiileur",
        "obnubiler": "obnibuler",
        "oculaire": "ocualire",
        "télescope": "teiescope",
        "valeur": "vaelur",
        "vertu": "veltu",
        "salade": "saiade",
        "renommer": "renomner",
        "sibyllin": "sibuliin",
        "successeur": "succaszeur",
        "écologie": "ecoiogie",
        "éloge": "elogie",
        "emménager": "ennenager",
        "cheval": "clreval",
        "permis": "pennis",
        "recueillir": "recuelilir",
        "martel": "manel",
        "veux": "vuex",
        "emploi": "emnloi",
        "pôle": "pole",
        "qui": "uui",
        "experience": "escpehience",
    },
    "vi": {
        "hiếu": "hiéu",
        "hiền": "hién",
        "châu": "chau",
        "cho": "chò|chõ|chọ|chỏ",
        "đường": "duong",
        "biển": "bien|biẻn",
        "tranh": "trảnh",
        "điện": "điẹn",
        "tuổi": "tuỏi",
        "nhân": "khân",
        "nghĩa": "nghia",
        "trường": "truồng",
        "phóng": "phống",
        "tuyển": "tuyể",
        "ghẹ": "chẹ",
        "bún": "bứn",
        "thuê": "thue",
        "giầy": "glầy",
        "thâu": "thău",
        "ngoại": "ngbại",
        "khỏe": "khôe",
        "chuẩn": "chuân",
        "thiên": "triên",
        "tôn": "tón|tòn|tõn",
        "thuế": "thuể",
        "liếm": "liễm",
        "ngọc": "vgạc",
        "giầy": "giay",
        "miễn": "miển|mien",
        "gói": "gới",
        "thực": "thọc",
        "mọi": "mội",
        "nông": "nong",
        "sạch": "sach",
        "ho": "hợ",
        "nội": "nọi",
        "ngõ": "ngỗ",
        "bông": "bônh",
        "tờ": "tở",
        "sỹ": "sý",
        "nữ": "nũ",
        "loan": "loán",
        "tối": "tói",
        "gội": "gậi",
        "xét": "xết",
        "ép": "ếp",
        "kiểu": "riểu",
        "hạn": "hạh",
        "họp": "hop",
        "kim": "kỉm",
        "chỉnh": "chỉng",
        "trịnh": "tgịnh",
        "quốc": "quộc",
        "nhựa": "nhụa",
        "thuốc": "thuóc",
        "toàn": "toan",
        "giãn": "giăn",
        "mau": "mảu",
    },
}


def spelltest(speller, tests, verbose=2):
    n, bad = 0, 0
    for target, incorrect_spellings in tests.items():
        for incorrect_spelling in incorrect_spellings.split("|"):
            n += 1
            w = speller(incorrect_spelling)
            if w != target:
                bad += 1
                if verbose >= 2:
                    print(f"spell({incorrect_spelling}) => {w}; should be {target}")
    if verbose >= 1:
        print(f"bad: {bad}/{n}")
    return bad


def benchmark(name, speller, tests, repetitions=20):
    current_min = float("inf")
    for _ in range(repetitions):
        start = time.time()
        spelltest(speller, tests, verbose=0)
        duration = time.time() - start
        current_min = min(duration, current_min)
    print(f"{name:<24} {current_min:.3f}s    ", end="")
    spelltest(speller, tests, verbose=1)


spell = Speller("en")


def test_english_words():
    assert spelltest(spell, english) == 0


def test_sentences():
    assert spelltest(spell, sentences) == 0


def test_uppercase():
    assert spelltest(spell, upper) == 0


def test_replacements():
    spell_replace = Speller(only_replacements=True)
    assert spelltest(spell_replace, only_replacements) == 0


def test_empty():
    spell.autocorrect_word("")


def test_single_typos():
    word = Word("me", "en")
    assert set(word.typos()) == single_typos_me


def test_spanish():
    spell_es = Speller("es")
    assert spelltest(spell_es, spanish_words_all_correct) == 0


def test_italian():
    spell_it = Speller("it")
    assert spelltest(spell_it, italian_words_all_correct) == 0


def test_french():
    spell_fr = Speller("fr")
    assert spelltest(spell_fr, french_words_all_correct) == 0


if __name__ == "__main__":
    command = sys.argv[1]

    with open("data/cess_esp_word_count.json", "r", encoding="utf-8") as file:
        nlp_data = json.load(file)

    if command == "quality":
        # this doesn't have to pass 100%, they check the accuracy of correction
        print("\nquality:")
        for lang, test in optional_language_tests.items():
            print(lang + "  ", end="")
            spell = Speller(lang, nlp_data=nlp_data)
            spelltest(spell, test, verbose=1)
    elif command == "benchmark":
        print("\nbenchmarks:")
        spell = Speller("en")
        benchmark("english sentences", spell, sentences)
        spell = Speller("en", fast=True)
        benchmark("english sentences fast", spell, sentences)
        spell = Speller("es", nlp_data=nlp_data)
        benchmark("spanish words", spell, optional_language_tests["es"])
        spell = Speller("it")
        benchmark("italian words", spell, optional_language_tests["it"])
        spell = Speller("fr")
        benchmark("french words", spell, optional_language_tests["fr"])
    elif command == "find_threshold":
        lang = sys.argv[2]
        test = optional_language_tests[lang]
        for i in range(6, 30):
            threshold = int(1.2**i) - 2
            spell = Speller(lang, threshold=threshold, nlp_data=nlp_data)
            bad = spelltest(spell, test, verbose=0)
            print(f"threshold: {threshold:3},   bad: {bad:3}")
    else:
        print("bad option, use:")
        print("./test_all.py [quality | benchmark | find_threshold [lang]]")
