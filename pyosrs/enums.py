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
    20: ("araxxor", "Araxxor"),
    21: ("artio", "Artio"),
    22: ("barrows_chests", "Barrows Chests"),
    23: ("bryophyta", "Bryophyta"),
    24: ("callisto", "Callisto"),
    25: ("cal_varion", "Calvarion"),
    26: ("cerberus", "Cerberus"),
    27: ("chambers_of_xeric", "Chambers of Xeric"),
    28: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    29: ("chaos_elemental", "Chaos Elemental"),
    30: ("chaos_fanatic", "Chaos Fanatic"),
    31: ("commander_zilyana", "Commander Zilyana"),
    32: ("corporeal_beast", "Corporeal Beast"),
    33: ("crazy_archaeologist", "Crazy Archaeologist"),
    34: ("dagannoth_prime", "Dagannoth Prime"),
    35: ("dagannoth_rex", "Dagannoth Rex"),
    36: ("dagannoth_supreme", "Dagannoth Supreme"),
    37: ("deranged_archaeologist", "Deranged Archaeologist"),
    38: ("duke_sucellus", "Duke Sucellus"),
    39: ("general_graardor", "General Graardor"),
    40: ("giant_mole", "Giant Mole"),
    41: ("grotesque_guardians", "Grotesque Guardians"),
    42: ("hespori", "Hespori"),
    43: ("kalphite_queen", "Kalphite Queen"),
    44: ("king_black_dragon", "King Black Dragon"),
    45: ("kraken", "Kraken"),
    46: ("kree_arra", "Kree'Arra"),
    47: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    48: ("lunar_chests", "Lunar Chests"),
    49: ("mimic", "Mimic"),
    50: ("nex", "Nex"),
    51: ("nightmare", "Nightmare"),
    52: ("phosanis_nightmare", "Phosani's Nightmare"),
    53: ("obor", "Obor"),
    54: ("phantom_muspah", "Phantom Muspah"),
    55: ("sarachnis", "Sarachnis"),
    56: ("scorpia", "Scorpia"),
    57: ("scurrius", "Scurrius"),
    58: ("skotizo", "Skotizo"),
    59: ("sol_heredit", "Sol Heredit"),
    60: ("spindel", "Spindel"),
    61: ("tempoross", "Tempoross"),
    62: ("the_gauntlet", "The Gauntlet"),
    63: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    64: ("the_leviathan", "The Leviathan"),
    65: ("the_whisperer", "The Whisperer"),
    66: ("theatre_of_blood", "Theatre of Blood"),
    67: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    68: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    69: ("tombs_of_amascut", "Tombs of Amascut"),
    70: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    71: ("tzkal_zuk", "TzKal-Zuk"),
    72: ("tztok_jad", "TzTok-Jad"),
    73: ("vardorvis", "Vardorvis"),
    74: ("venenatis", "Venenatis"),
    75: ("vet_ion", "Vet'ion"),
    76: ("vorkath", "Vorkath"),
    77: ("wintertodt", "Wintertodt"),
    78: ("zalcano", "Zalcano"),
    79: ("zulrah", "Zulrah"),
}
