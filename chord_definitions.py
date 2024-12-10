import re

y_chord = "KWH" # the 'y' in yet or the 'i' in genius
silent_linker = "KWR" # the 'linker' in genus


custom_alphabet = "*QSTKPWHRAO-eufrpblgtsdz"

keysymbol_shorthands = {
    """
    There will be groups of keysymbols that come up again and again,
    so I'll define them once here
    """
    "long a": "a i",
    "short vowels": " \[?(@|e5|I2|i7|e05|a|o|a5|e|@r)\]? ",
    "long vowels": " \[?(aa|y  uu|iy)\]? ",
    "any vowel": " \[?(a|ao|@|e5|i2|i7|e05|eir|o|a5)\]? ",
    "pasta vowel": " ao "
}

spelling_shorthands = {
    """
    There will be groups of letters that come up again and again,
    so I'll define them once here
    """
    "": "a i",
    "schwa": "@",
    "long a": " ee "
}


#regex logic for what must come before
#hopefully compiling it all here makes it run faster since they'll be used
NothingRegex = re.compile(r'')
AtLeastOneCharacterRegex = re.compile(r'.+')
skipsAnEUInTheVowels = re.compile(r'[AO][frpblgtsdz]+')
unavailable_e_no_r = re.compile(r'.*[QSTKPWHR][AO]*[eu]+fpblgtsdz]*')

A_to_s_yes_b_or_g = re.compile(r'.*[\-AOeufrp][bg][lgts]*')

ends_in_t = re.compile(r'.*t')

upToQ = re.compile(r'.*[/Q]')
upToS = re.compile(r'.*[/QS]')
upToT = re.compile(r'.*[/QST]')
upToK = re.compile(r'.*[/QSTK]')
upToP = re.compile(r'.*[/QSTKP]')
upToW = re.compile(r'.*[/QSTKPW]')
upToH = re.compile(r'.*[/QSTKPWH]')
upToR = re.compile(r'.*[/QSTKPWHR]')
first_stroke_upToR = re.compile(r'[/QSTKPWHR]+')

A_to_u = re.compile(r'.*[\-AOeu]')
A_to_f = re.compile(r'.*[\-AOeuf]')
A_to_r = re.compile(r'.*[\-AOeufr]')
A_to_p = re.compile(r'.*[\-AOeufrp]')
A_to_b = re.compile(r'.*[\-AOeufrpb]')
A_to_l = re.compile(r'.*[\-AOeufrpbl]')
A_to_g = re.compile(r'.*[\-AOeufrpblg]')
A_to_t = re.compile(r'.*[\-AOeufrpblgt]')
A_to_s = re.compile(r'.*[\-AOeufrpblgts]')
A_to_d = re.compile(r'.*[\-AOeufrpblgtsd]')
A_to_z = re.compile(r'.*[\-AOeufrpblgtsdz]')


A_to_z_no_pbs = re.compile(r'.*[\-AOeufr][lgtdz]+')
A_to_z_no_plt = re.compile(r'.*[\-AOeufr][bgsdz]+')


A_to_z_no_r = re.compile(r'.*[\-AOeuf][pblgtsdz]+')
A_to_z_no_p = re.compile(r'.*[\-AOeufr][blgtsdz]+')
A_to_z_no_b = re.compile(r'.*[\-AOeufrp][lgtsdz]+')
A_to_z_no_l = re.compile(r'.*[\-AOeufrpb][gtsdz]+')
A_to_z_no_g = re.compile(r'.*[\-AOeufrpbl][tsdz]+')
A_to_z_no_t = re.compile(r'.*[\-AOeufrpblg][sdz]+')
A_to_z_no_s = re.compile(r'.*[\-AOeufrpblgt][dz]+')
A_to_z_no_d = re.compile(r'.*[\-AOeufrpblgts][z]')

slash_to_u = re.compile(r'.*[/][QSTKPWHR]*[\-AOeu]+')
slash_to_f = re.compile(r'.*[/][QSTKPWHR]*[\-AOeuf]+')
slash_to_r = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufr]+')
slash_to_p = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrp]+')
slash_to_b = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpb]+')
slash_to_l = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpbl]+')
slash_to_g = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblg]+')
slash_to_t = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgt]+')
slash_to_s = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgts]+')
slash_to_d = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgtsd]+')
slash_to_z = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgtsdz]+')

slash_to_r = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufr]')

slash_to_z_no_r = re.compile(r'.*[/][QSTKPWHR]*[\-AOeuf]+[pblgtsdz]+')
slash_to_z_no_p = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufr]+[blgtsdz]+')
slash_to_z_no_b = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrp]+[lgtsdz]+')
slash_to_z_no_l = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpb]+[gtsdz]+')
slash_to_z_no_g = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpbl]+[tsdz]+')
slash_to_z_no_t = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblg]+[sdz]+')
slash_to_z_no_s = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgt]+[dz]+')
slash_to_z_no_d = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgts]+[z]')

"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {

    "": [
        #{"description": "silent e",
        # "spelling": "e",
        # "pronunciation": "",
        # "ambiguity": 1, #maid/made
        # "what must come before": ".*[/QSTKPWHR]\*?([AOeu])[*frpblgtsdz]+",
        # "steno theory": "WSI"},
         
        #{"description": "droppable e",
        # "spelling": "e",
        # "pronunciation": keysymbol_shorthands["short vowels"],
        # "ambiguity": 1,
        # "what must come before": ".*[/QSTKPWHR]\*?([AOeu]+)[*frpblgtsdz]+",
        # "steno theory": "I don't know"},
         
        #{"description": "droppable a",
        # "spelling": "a",
        # "pronunciation": keysymbol_shorthands["short vowels"],
        # "ambiguity": 1,
        # "what must come before": ".*[/QSTKPWHR]\*?([AOeu]+)[*frpblgtsdz]+",
        # "steno theory": "I don't know"},

        {"description": "drop short vowel",
         "spelling": "[aeiou]",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 2,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"},


        {"description": "drop long vowel",
         "spelling": "[aeiou]",
         "pronunciation": keysymbol_shorthands["long vowels"],
         "ambiguity": 3,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"},

        {"description": "ignoring a suffix border",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 1,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"}],

    "/Q": [
        {"description": "^ for initial short a",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix)) " + keysymbol_shorthands["any vowel"],
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "Josiah"},
         
        {"description": "^ for initial long a",
         "spelling": "a",
         "pronunciation": " (starting_)?((root)|(prefix))  ee ",
         "ambiguity": 1,
         "what must come before": NothingRegex,
         "steno theory": "Josiah"}],

    "/S": [
        {"description": "S for initial s",
         "spelling": "ss?",
         "pronunciation": " (starting_)?((root)|(prefix))  s ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "S for linking s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "S for linking vowel + s",
         "spelling": "[aeiouy]ss?",
         "pronunciation": keysymbol_shorthands["short vowels"] + " s ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/S*": [
        {"description": "S* for initial s of a compound word",
         "spelling": "ss?",
         "pronunciation": " compound  s ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "S": [
        {"description": "S for s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"}],

    "/SR": [
        {"description": "SR for linker v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/SO*pb": [
        {"description": "SO*PB for 'son' where the o is silent",
         "spelling": "son",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/S-pb": [
        {"description": "S-PB for 'son' where the o is silent",
         "spelling": "son",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/T": [
        {"description": "T for initial t",
         "spelling": "t",
         "pronunciation": " (starting_)?((root)|(prefix))  t ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "T for linker t",
         "spelling": "tt?",
         "pronunciation": "( (root)|(prefix)|(suffix) )? t ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/T*": [
        {"description": "T for compound linker t",
         "spelling": "t",
         "pronunciation": " compound  t ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwings"}],

    "T": [
        {"description": "T for t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],

    "/TK":[
        {"description": "TK for initial d",
         "spelling": "d",
         "pronunciation": " (starting_)((root)|(prefix)|(suffix))  d ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TK for linking d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "TK for linking d whilst ignoring boundaries",
         "spelling": "d",
         "pronunciation": " d  (suffix) ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "TK":[
        {"description": "TK for d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TKPW": [
        {"description": "TKPW for initial g",
         "spelling": "g",
         "pronunciation": " (starting_)?((root)|(prefix))  g ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TKPW for linker g",
         "spelling": "gg?",
         "pronunciation": "( (root)|(prefix)|(suffix) )? g ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/TKPW*": [
        {"description": "TKPW for compound linker g",
         "spelling": "g",
         "pronunciation": " compound  g ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "TKPW": [
        {"description": "TKPW for g",
         "spelling": "gg?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TP": [
        {"description": "TP for initial f",
         "spelling": "f",
         "pronunciation": " (starting_)?((root)|(prefix))  f ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TP for linker f",
         "spelling": "ff?",
         "pronunciation": "( (root)|(prefix)|(suffix) )? f ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/TP*": [
        {"description": "TP for compound linker f",
         "spelling": "f",
         "pronunciation": " compound  f ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "TP": [
        {"description": "T for f",
         "spelling": "ff?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TPH": [
        {"description": "TPH for initial n",
         "spelling": "n",
         "pronunciation": " (starting_)((root)|(prefix)|(suffix))  n ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TPH for linking n",
         "spelling": "nn?",
         "pronunciation": "( (root)|(prefix)|(suffix) )? n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "TPH": [
        {"description": "TPH for n",
         "spelling": "nn?",
         "pronunciation": " n ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TH": [
        {"description": "TH for initial th",
         "spelling": "th",
         "pronunciation": " (starting_)((root)|(prefix)|(suffix))  th ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TH for linking th",
         "spelling": "th",
         "pronunciation": "( (root)|(prefix)|(suffix) )? th ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"}],

    "/K": [
        {"description": "K for initial k",
         "spelling": "k",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

         {"description": "K for initial hard c",
         "spelling": "c",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 1,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "K for linking ch that sounds like k",
         "spelling": "ch",
         "pronunciation": "( (root)|(prefix)|(suffix) )? k ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "K for linking c that sounds like k",
         "spelling": "c",
         "pronunciation": "( (root)|(prefix)|(suffix) )? k ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "K": [
        {"description": "K for k",
         "spelling": "kk?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": upToT,
         "steno theory": "WSI"},

        {"description": "K for hard c",
         "spelling": "c",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToT,
         "steno theory": "WSI"},

        {"description": "K for ch that sounds like k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToT,
         "steno theory": "WSI"}],


    "/KWH": [
        {"description": "KWH for linking y",
         "spelling": "y",
         "pronunciation": "( (root)|(prefix)|(suffix) )? iy ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"},

        {"description": "KWH for linking i",
         "spelling": "i",
         "pronunciation": "( (root)|(prefix)|(suffix) )? ii ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/KWR": [
        {"description": "KWR for silent suffix linker",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "I think StenEd?"},

        {"description": "KWR for silent linker",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/KWReu/KWRe": [
        {"description": "KWREU/KWRE for ie",
         "spelling": "ie",
         "pronunciation": "( suffix )? iy ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "I think StenEd?"}],

    "/P": [
        {"description": "P for initial p",
         "spelling": "p",
         "pronunciation": " (starting_)?((root)|(prefix))  p ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "P for linker p",
         "spelling": "pp?",
         "pronunciation": "( (root)|(prefix)|(suffix) )? p ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/P*": [
        {"description": "P for compound linker p",
         "spelling": "p",
         "pronunciation": " compound  p ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwings"}],

    "P": [
        {"description": "P for p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "WSI"}],

    "/PW*": [
        {"description": "PW* for joining a compound word with b",
         "spelling": "b",
         "pronunciation": " compound  b ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],


    "/PW": [
        {"description": "PW for initial b",
         "spelling": "b",
         "pronunciation": " (starting_)((root)|(prefix))  b ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "Lapwing"},

        {"description": "PW for linking b",
         "spelling": "bb?",
         "pronunciation": "( (root)|(prefix) )* b ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "PW": [
        {"description": "PW for b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/W": [
        {"description": "W for initial w",
         "spelling": "w",
         "pronunciation": " (starting_)?((root)|(prefix))  w ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "W for linker w",
         "spelling": "ww?",
         "pronunciation": "( (root)|(prefix)|(suffix) )? w ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/W*": [
        {"description": "W for compound linker w",
         "spelling": "w",
         "pronunciation": " compound  w ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "W": [
        {"description": "W for w",
         "spelling": "ww?",
         "pronunciation": " w ",
         "ambiguity": 0,
         "what must come before": upToP,
         "steno theory": "WSI"}],


    "/WA": [
        {"description": "WA for linking oir sound",
         "spelling": "oire?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri's Accent"}],
    
    "WA": [
        {"description": "WA for oir sound",
         "spelling": "oir?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 0,
         "what must come before": upToP,
         "steno theory": "Harri's Accent"},


        {"description": "WA for oir sound",
         "spelling": "oire?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 1,
         "what must come before": upToP,
         "steno theory": "Harri's Accent"}],



    "/H": [
        {"description": "H for linking h",
         "spelling": "h",
         "pronunciation": "( (root)|(prefix) )* h ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "H": [
        {"description": "H for h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "what must come before": upToW,
         "steno theory": "WSI"}],

    "/HR*": [
        {"description": "HR* for joining a compound word with l",
         "spelling": "l",
         "pronunciation": " compound  l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "/HR": [
        {"description": "HR for suffix linker l",
         "spelling": "ll?",
         "pronunciation": " suffix  l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "HR for linker l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "HR for vowel then suffix linker l",
         "spelling": "ll?",
         "pronunciation": keysymbol_shorthands["short vowels"] + " suffix  l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],


    "HR": [
        {"description": "HR for l",
         "spelling": "l",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": upToW,
         "steno theory": "WSI"},


        {"description": "HR for ll",
         "spelling": "ll",
         "pronunciation": " l ",
         "ambiguity": 1, #Alan Allan
         "what must come before": upToW,
         "steno theory": "WSI"}],

    "/R": [
        {"description": "R for initial r",
         "spelling": "r",
         "pronunciation": " (starting_)?((root)|(prefix))  r ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "R for linker r",
         "spelling": "rr?",
         "pronunciation": "( (root)|(prefix)|(suffix) )? r ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/R*": [
        {"description": "R for compound linker r",
         "spelling": "r",
         "pronunciation": " compound  r ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "R": [
        {"description": "R for r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": upToH,
         "steno theory": "WSI"}],

    "/A": [

        {"description": "A for initial a",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix))  a ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "A for initial schwa",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix)) " + keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "A for the initial pasta vowel",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix)) " + keysymbol_shorthands["pasta vowel"],
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "Harri's accent"},


        {"description": "A for the initial drama vowel",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  aa ",
         "ambiguity": 1,
         "what must come before": NothingRegex,
         "steno theory": "drama is a short vowel"}],

    "A": [
        {"description": "A for short a",
         "spelling": "a",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"}],



    "AOe": [

        {"description": "AOE for long e spelt ee",
         "spelling": "ee",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I don't know"},

        {"description": "AOE for long e spelt e",
         "spelling": "e",
         "pronunciation": " ii ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I don't know"},
        
        {"description": "AOE for long e spelt ea",
         "spelling": "ea",
         "pronunciation": " ii ",
         "ambiguity": 2,
         "what must come before": upToR,
         "steno theory": "I don't know"}],

    "AOeu": [
        {"description": "AOEU for long i",
         "spelling": "i",
         "pronunciation": " ae ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"}],


    "AOu": [
        {"description": "AOU for long u",
         "spelling": "u",
         "pronunciation": "( y )? (uu|UU) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I don't know"}],


    "Ae": [
        {"description": "AE for long e spelt ea, but only if it's the first stroke",
         "spelling": "ea",
         "pronunciation": " ii ",
         "ambiguity": 1,
         "what must come before": first_stroke_upToR,
         "steno theory": " I don't know"},

        {"description": "AE for long a spelt a_e, but only if it's the first stroke",
         "spelling": "a",
         "pronunciation": " ee ",
         "ambiguity": 2,
         "what must come before": first_stroke_upToR,
         "steno theory": " I don't know"}],

    "/Aeu": [
        {"description": "AEU for initial long a",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  (ee|ei|eir) ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"}],

    "Aeu": [
        {"description": "AEU for long a",
         "spelling": "aa?",
         "pronunciation": " (ee|ei|eir) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"}],


    "/Au": [
        {"description": "AU for the initial drama vowel",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  aa ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "drama is a long vowel"},

        {"description": "AU for the initial daughter vowel",
         "spelling": "a(a|u)",
         "pronunciation": " (starting_)?((root)|(prefix))  oo ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "daughter is a long vowel"},

        {"description": "AU for initial al in false",
         "spelling": "all?",
         "pronunciation": " (starting_)?((root)|(prefix))  oo  l ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "false is AUL"}],

    "Au": [
        {"description": "AU for the daughter vowel",
         "spelling": "a(a|u)",
         "pronunciation": " oo ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "daughter is a long vowel"},

        {"description": "AU for al in false",
         "spelling": "all?",
         "pronunciation": " oo  l ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "false is AUL"}],


    "/Ar": [

        {"description": "AR for initial long a followed by r",
         "spelling": "aa?re?",
         "pronunciation": " starting_((root)|(prefix))  ar  r ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "Lapwing"}],

    "Ar": [
        {"description": "AR for long a followed by r",
         "spelling": "aa?re?",
         "pronunciation": " ar  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "Lapwing"}],


    "Oe": [
        {"description": "OU for o said like owe",
         "spelling": "o",
         "pronunciation": " ou ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "Lapwing?"}],

    "O": [
        {"description": "O for o",
         "spelling": "o",
         "pronunciation": " (O|o|@|@r) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"}],

        #{"description": "O for o, even though it's not pronounced",
        # "spelling": "o",
        # "pronunciation": "",
        # "ambiguity": 1,
        # "what must come before": upToR,
        # "steno theory": "WSI"}],

    "Ou": [
        {"description": "OU for ow said like ow",
         "spelling": "ow",
         "pronunciation": " ow ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "OU for ou said like ow",
         "spelling": "ou",
         "pronunciation": " ow ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "WSI"}],

    "Or": [
        {"description": "OR for long o followed by r",
         "spelling": "ore?",
         "pronunciation": " or  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "Lapwing"}],


    "e": [
        {"description": "E for unstressed e",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

         {"description": "E for long e spelt just e", #abalone
          "spelling": "e",
          "pronunciation" : " iy ",
          "ambiguity": 1,
          "what must come before": upToR,
          "steno theory": "I don't know"}],

    "eu": [
        {"description": "EU for y said like long e",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"},

        {"description": "EU for i",
         "spelling": "i",
         "pronunciation": " i ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"},
        
        {"description": "EU for y said like uh",
         "spelling": "y",
         "pronunciation": " I2 ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

    "er": [
        {"description": "ER for er",
         "spelling": "er",
         "pronunciation": " @r  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "folding ER for suffix er when E is free",
         "spelling": "er",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 1,
         "what must come before": skipsAnEUInTheVowels, #replaced the logic ".*[AO](?!.*(.).*\1)[fpblgtsdz]*\*?"
         "steno theory": "Harri"}],

    "u": [

        {"description": "U for u",
         "spelling": "u",
         "pronunciation": " (@|uh) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "U for ou said like country",
         "spelling": "ou",
         "pronunciation": " uh ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "WSI"}],

    "ur": [
        {"description": "UR for ur",
         "spelling": "ure?",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"}],

    "f":[
        {"description": "-F for f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"},
         
        {"description": "-F for v",
         "spelling": "f",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"},

        #{"description": "-F for s",
        # "spelling": "s",
        # "pronunciation": " (s|z) ",
        # "ambiguity": 1,
        # "what must come before": A_to_u,
        # "steno theory": "I think StenEd?"},

        {"description": "-F for v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"},

        #{"description": "folding -F for s",
        # "spelling": "s",
        # "pronunciation": " s ",
        # "ambiguity": 2,
        # "what must come before": ".*[AOeu]r?p?b?l?g?t?s?d?z?#\*?",
        # "steno theory": "I think StenEd?"},

         {"description": "-F for gh",
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I don't know"}],



    #"fr":[
    #    {"description": "-FR for m",
    #     "spelling": "m",
    #     "pronunciation": " m ",
    #     "ambiguity": 2,
    #     "what must come before": A_to_u,
    #     "steno theory": "I think StenEd?"}],

    "frp":[
        {"description": "-FRP for mp",
         "spelling": "mp",
         "pronunciation": " m  p ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"}],

    "frpblg": [
        {"description": "-FRPBG for nkl",
         "spelling": "n(c|k)le?",
         "pronunciation": " ng  k  l ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"}],

    "frpbg": [
        {"description": "-FRPBG for nk",
         "spelling": "n(c|k)",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"}],

    "frb":[
        {"description": "-FRB for mb",
         "spelling": "mb",
         "pronunciation": " m  b ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"}],

    "ft":[
        {"description": "-FT for ft",
         "spelling": "ft",
         "pronunciation": " f  t ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"},

        {"description": "-FT for st",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "WSI"}],

    "plt":[
        {"description": "-F for s then -PLT for suffix -ment",
         "spelling": "sement",
         "pronunciation": " s suffix  m  e5  n  t ",
         "ambiguity": 1,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_u,
         "steno theory": "I don't know"}],

    "fb":[
        {"description": "-FB for v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "Josiah?"}],

    "fg":[
        {"description": "-FG for gh",
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "Harri"}],

    "r": [
        {"description": "-R for r",
         "spelling": "re?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": A_to_f,
         "steno theory": "WSI"},


        {"description": "folding R for suffix er when E is unavailable",
         "spelling": "er",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 2,
         "what must come before": unavailable_e_no_r,
         "steno theory": "Harri"}],

    "rb": [
        {"description": "-RB for sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": A_to_f,
         "steno theory": "I don't know"}],

    "p": [
        {"description": "-P for p",
         "spelling": "pp?e?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": A_to_r, #".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "steno theory": "WSI"}],

    "pb": [
        {"description": "-PB for n",
         "spelling": "(e|o)?nn?e?",
         "pronunciation": " n ",
         "ambiguity": 0,
         "what must come before": A_to_r,
         "steno theory": "WSI"}],

    "/-pbs": [
        {"description": "-PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "I think StenEd?"},

        {"description": "-PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|I2)  suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "I think StenEd?"}],


    "pbs": [
        {"description": "-PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": A_to_r,
         "steno theory": "I think StenEd?"},


         {"description": "-PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|I2)  suffix  n  E5  s ",
         "ambiguity": 2,
         "what must come before": A_to_r,
         "steno theory": "I think StenEd?"},

        {"description": "folding -PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_pbs,
         "steno theory": "I think StenEd?"},

        {"description": "folding -PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|I2)  suffix  n  E5  s ",
         "ambiguity": 2,
         "what must come before": A_to_z_no_pbs,
         "steno theory": "I think StenEd?"}],

    "pl": [
        {"description": "-PL for m",
         "spelling": "mm?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r,
         "steno theory": "WSI"}],

    "*pz": [
        {"description": "*PZ for h",
         "spelling": "h",
         "pronunciation": "( h )?",
         "ambiguity": 0,
         "what must come before": slash_to_r,
         "steno theory": "Josiah"}],


    "/-plt":[
        {"description": "-PLT for suffix -ment",
         "spelling": "ment",
         "pronunciation": " suffix  m  e5  n  t ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "plt":[
        {"description": "-PLT for suffix -ment",
         "spelling": "ment",
         "pronunciation": " suffix  m  e5  n  t ",
         "ambiguity": 1,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_r,
         "steno theory": "I don't know"},

         {"description": "folding -PLT for suffix -ment",
         "spelling": "ment",
         "pronunciation": " suffix  m  e5  n  t ",
         "ambiguity": 1,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_z_no_plt,
         "steno theory": "I don't know"}],


    "b": [
        {"description": "-B for b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": A_to_p,
         "steno theory": "WSI"}],

    "bg": [
        {"description": "-BG for k",
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p,
         "steno theory": "WSI"},

        {"description": "-BG for ck",
         "spelling": "ck",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p,
         "steno theory": "WSI"},

        {"description": "-BG for k sound spelt ch",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p,
         "steno theory": "WSI"}],

    "l":[
        {"description": "-L for l",
         "spelling": "ll?e?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_b,
         "steno theory": "WSI"},

        {"description": "folding -L for l",
         "spelling": "ll?e?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_z_no_l,
         "steno theory": "I don't know"},

        {"description": "-L for -ly",
         "spelling": "ly",
         "pronunciation": " suffix  l  iy ",
         "ambiguity": 2,
         "what must come before": A_to_b,
         "steno theory": "I don't know"},

        {"description": "folding -L for -ly",
         "spelling": "ly",
         "pronunciation": " suffix  l  iy ",
         "ambiguity": 2,
         "what must come before": A_to_z_no_l,
         "steno theory": "I don't know"}],

    "/-ls":[
        {"description": "-LS for -less",
         "spelling": "less",
         "pronunciation": " suffix  l  E5  s ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/-g":[
        {"description": "-G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "g":[
        {"description": "-G for g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": A_to_l,
         "steno theory": "WSI"},

        {"description": "-G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_l,
         "steno theory": "WSI"},

        {"description": "folded -G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_g,
         "steno theory": "WSI"}],

    "gs":[
        {"description": "-GS for shion",
         "spelling": "(sh|te)ion",
         "pronunciation": " sh  suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_l,
         "steno theory": "I think StenEd?"}],

    "t":[
        {"description": "-T for t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": A_to_g,
         "steno theory": "WSI"}],

    "*t":[
        {"description": "*T for th",
         "spelling": "the?",
         "pronunciation": " th ",
         "ambiguity": 0,
         "what must come before": slash_to_g,
         "steno theory": "Lapwing"}],

    #"/-s":[
    #    {"description": "-S for plurals",
    #     "spelling": "s",
    #     "pronunciation": "( (suffix) ) z ",
    #     "ambiguity": 1,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],
        
    "s":[

        {"description": "-S for unvoiced s",
         "spelling": "ss?e?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_t,
         "steno theory": "WSI"},

        {"description": "-S for unvoiced c",
         "spelling": "ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": A_to_t,
         "steno theory": "WSI"},

        #{"description": "-S for voiced s",
        # "spelling": "ss?e?",
        # "pronunciation": " z ",
        # "ambiguity": 1,
        # "what must come before": A_to_t,
        # "steno theory": "WSI"},

        {"description": "-S for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) ) (s|z) ",
         "ambiguity": 1,
         "what must come before": ends_in_t,
         "steno theory": "WSI"}],

    "*s":[
        {"description": "*S for 's",
         "spelling": "'s",
         "pronunciation": " suffix  (s|z) ",
         "ambiguity": 2,
         "what must come before": slash_to_t,
         "steno theory": " Josiah"},

        {"description": "*S for voiced s",
         "spelling": "ss?e?",
         "pronunciation": " z ",
         "ambiguity": 0,
         "what must come before": slash_to_t,
         "steno theory": "Harri?"},
         
        {"description": "*S for suffix -ise",
         "spelling": "ise",
         "pronunciation": " suffix  ae  z ",
         "ambiguity": 1,
         "what must come before": slash_to_t,
         "steno theory": "Harri?"}],

    "/-d": [
        {"description": "-D for -ed",
         "spelling": "ed",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "d": [
        {"description": "-D for d",
         "spelling": "de?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": A_to_s,
         "steno theory": "WSI"},

        {"description": "-D for -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 1,
         "what must come before": A_to_s,
         "steno theory": "WSI"},

        {"description": "folding -D for -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_d,
         "steno theory": "WSI"}],

    "*d": [
        {"description": "*D for y",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": slash_to_s,
         "steno theory": "Harri"},

        {"description": "*D for dy",
         "spelling": "dy",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "what must come before": slash_to_s,
         "steno theory": "HelloChap? I can't remember"}],

    "dz": [
        {"description": "-DZ for suffix ing when G is taken",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": A_to_s_yes_b_or_g,
         "steno theory": "WSI"}],

    #"/-z":[
    #    {"description": "-Z for plurals",
    #     "spelling": "e?s",
    #     "pronunciation": "( (suffix) )( i7 )? (s|#z) ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],

    "z":[
        {"description": "-Z for plurals",
         "spelling": "e?s",
         "pronunciation": "( (suffix) )( i7 )? (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_d,
         "steno theory": "WSI"},

        #{"description": "-Z for voiced s",
         #"spelling": "e?s",
         #"pronunciation": " (z) ",
         #"ambiguity": 1,
         #"what must come before": A_to_d,
         #"steno theory": "WSI"}
         
         ],
    
    

}
