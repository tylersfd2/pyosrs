from enum import Enum
from typing import Dict, Final, Tuple


class GAME_MODE(Enum):  # noqa
    MAIN: str = "hiscore_oldschool"
    IRONMAN: str = "hiscore_oldschool_ironman"
    HARDCORE: str = "hiscore_oldschool_hardcore_ironman"
    ULTIMATE: str = "hiscore_oldschool_ultimate"
    DEADMAN: str = "hiscore_oldschool_deadman"
    SEASONAL: str = "hiscore_oldschool_seasonal"
    TOURNAMENT: str = "hiscore_oldschool_tournament"
    FRESH_START: str = "hiscore_oldschool_fresh_start"


SKILLS_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    0: ("overall", "Overall"),
    1: ("attack", "Attack"),
    2: ("defence", "Defence"),
    3: ("strength", "Strength"),
    4: ("hitpoints", "Hitpoints"),
    5: ("ranged", "Ranged"),
    6: ("prayer", "Prayer"),
    7: ("magic", "Magic"),
    8: ("cooking", "Cooking"),
    9: ("woodcutting", "Woodcutting"),
    10: ("fletching", "Fletching"),
    11: ("fishing", "Fishing"),
    12: ("firemaking", "Firemaking"),
    13: ("crafting", "Crafting"),
    14: ("smithing", "Smithing"),
    15: ("mining", "Mining"),
    16: ("herblore", "Herblore"),
    17: ("agility", "Agility"),
    18: ("thieving", "Thieving"),
    19: ("slayer", "Slayer"),
    20: ("farming", "Farming"),
    21: ("runecrafting", "Runecrafting"),
    22: ("hunter", "Hunter"),
    23: ("construction", "Construction"),
}

MINIGAMES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    0: ("league_points", "League Points"),
    1: ("deadman_points", "Deadman Points"),
    2: ("bounty_hunter_hunter", "Bounty Hunter - Hunter"),
    3: ("bounty_hunter_rogue", "Bounty Hunter - Rogue"),
    4: ("bounty_hunter_hunter_legacy", "Bounty Hunter (Legacy) - Hunter"),
    5: ("bounty_hunter_rogue_legacy", "Bounty Hunter (Legacy) - Rogue"),
    13: ("lms", "LMS"),
    14: ("pvp_arena", "PvP Arena"),
    15: ("soul_wars", "Soul Wars Zeal"),
    16: ("rifts_closed", "Rifts Closed"),
    17: ("colosseum_glory", "Colosseum Glory"),
}

CLUES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    6: ("all", "Clue Scrolls (all)"),
    7: ("beginner", "Clue Scrolls (beginner)"),
    8: ("easy", "Clue Scrolls (easy)"),
    9: ("medium", "Clue Scrolls (medium)"),
    10: ("hard", "Clue Scrolls (hard)"),
    11: ("elite", "Clue Scrolls (elite)"),
    12: ("master", "Clue Scrolls (master)"),
}

BOSSES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    18: ("abyssal_sire", "Abyssal Sire"),
    19: ("alchemical_hydra", "Alchemical Hydra"),
    20: ("amoxliatl", "Amoxliatl"),
    21: ("araxxor", "Araxxor"),
    22: ("artio", "Artio"),
    23: ("barrows_chests", "Barrows Chests"),
    24: ("bryophyta", "Bryophyta"),
    25: ("callisto", "Callisto"),
    26: ("cal_varion", "Calvarion"),
    27: ("cerberus", "Cerberus"),
    28: ("chambers_of_xeric", "Chambers of Xeric"),
    29: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    30: ("chaos_elemental", "Chaos Elemental"),
    31: ("chaos_fanatic", "Chaos Fanatic"),
    32: ("commander_zilyana", "Commander Zilyana"),
    33: ("corporeal_beast", "Corporeal Beast"),
    34: ("crazy_archaeologist", "Crazy Archaeologist"),
    35: ("dagannoth_prime", "Dagannoth Prime"),
    36: ("dagannoth_rex", "Dagannoth Rex"),
    37: ("dagannoth_supreme", "Dagannoth Supreme"),
    38: ("deranged_archaeologist", "Deranged Archaeologist"),
    39: ("duke_sucellus", "Duke Sucellus"),
    40: ("general_graardor", "General Graardor"),
    41: ("giant_mole", "Giant Mole"),
    42: ("grotesque_guardians", "Grotesque Guardians"),
    43: ("hespori", "Hespori"),
    44: ("kalphite_queen", "Kalphite Queen"),
    45: ("king_black_dragon", "King Black Dragon"),
    46: ("kraken", "Kraken"),
    47: ("kree_arra", "Kree'Arra"),
    48: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    49: ("lunar_chests", "Lunar Chests"),
    50: ("mimic", "Mimic"),
    51: ("nex", "Nex"),
    52: ("nightmare", "Nightmare"),
    53: ("phosanis_nightmare", "Phosani's Nightmare"),
    54: ("obor", "Obor"),
    55: ("phantom_muspah", "Phantom Muspah"),
    56: ("sarachnis", "Sarachnis"),
    57: ("scorpia", "Scorpia"),
    58: ("scurrius", "Scurrius"),
    59: ("skotizo", "Skotizo"),
    60: ("sol_heredit", "Sol Heredit"),
    61: ("spindel", "Spindel"),
    62: ("tempoross", "Tempoross"),
    63: ("the_gauntlet", "The Gauntlet"),
    64: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    65: ("the_hueycoatl", "The Hueycoatl"),
    66: ("the_leviathan", "The Leviathan"),
    67: ("the_whisperer", "The Whisperer"),
    68: ("theatre_of_blood", "Theatre of Blood"),
    69: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    70: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    71: ("tombs_of_amascut", "Tombs of Amascut"),
    72: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    73: ("tzkal_zuk", "TzKal-Zuk"),
    74: ("tztok_jad", "TzTok-Jad"),
    75: ("vardorvis", "Vardorvis"),
    76: ("venenatis", "Venenatis"),
    77: ("vet_ion", "Vet'ion"),
    78: ("vorkath", "Vorkath"),
    79: ("wintertodt", "Wintertodt"),
    80: ("zalcano", "Zalcano"),
    81: ("zulrah", "Zulrah"),
}
