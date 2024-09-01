from enum import Enum
from typing import Dict, Final, Tuple


class GAME_MODE(Enum):
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
    24: ("league_points", "League Points"),
    25: ("deadman_points", "Deadman Points"),
    26: ("bounty_hunter_hunter", "Bounty Hunter - Hunter"),
    27: ("bounty_hunter_rogue", "Bounty Hunter - Rogue"),
    28: ("bounty_hunter_hunter_legacy", "Bounty Hunter (Legacy) - Hunter"),
    29: ("bounty_hunter_rogue_legacy", "Bounty Hunter (Legacy) - Rogue"),
    37: ("lms", "LMS"),
    38: ("pvp_arena", "PvP Arena"),
    39: ("soul_wars", "Soul Wars Zeal"),
    40: ("rifts_closed", "Rifts Closed"),
    41: ("colosseum_glory", "Colosseum Glory"),
}

CLUES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    30: ("all", "Clue Scrolls All"),
    31: ("beginner", "Clue Scrolls Beginner"),
    32: ("easy", "Clue Scrolls Easy"),
    33: ("medium", "Clue Scrolls Medium"),
    34: ("hard", "Clue Scrolls Hard"),
    35: ("elite", "Clue Scrolls Elite"),
    36: ("master", "Clue Scrolls Master"),
}

BOSSES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    42: ("abyssal_sire", "Abyssal Sire"),
    43: ("alchemical_hydra", "Alchemical Hydra"),
    44: ("araxxor", "Araxxor"),
    45: ("artio", "Artio"),
    46: ("barrows_chests", "Barrows Chests"),
    47: ("bryophyta", "Bryophyta"),
    48: ("callisto", "Callisto"),
    49: ("cal_varion", "Calvarion"),
    50: ("cerberus", "Cerberus"),
    51: ("chambers_of_xeric", "Chambers of Xeric"),
    52: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    53: ("chaos_elemental", "Chaos Elemental"),
    54: ("chaos_fanatic", "Chaos Fanatic"),
    55: ("commander_zilyana", "Commander Zilyana"),
    56: ("corporeal_beast", "Corporeal Beast"),
    57: ("crazy_archaeologist", "Crazy Archaeologist"),
    58: ("dagannoth_prime", "Dagannoth Prime"),
    59: ("dagannoth_rex", "Dagannoth Rex"),
    60: ("dagannoth_supreme", "Dagannoth Supreme"),
    61: ("deranged_archaeologist", "Deranged Archaeologist"),
    62: ("duke_sucellus", "Duke Sucellus"),
    63: ("general_graardor", "General Graardor"),
    64: ("giant_mole", "Giant Mole"),
    65: ("grotesque_guardians", "Grotesque Guardians"),
    66: ("hespori", "Hespori"),
    67: ("kalphite_queen", "Kalphite Queen"),
    68: ("king_black_dragon", "King Black Dragon"),
    69: ("kraken", "Kraken"),
    70: ("kree_arra", "Kree'Arra"),
    71: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    72: ("lunar_chests", "Lunar Chests"),
    73: ("mimic", "Mimic"),
    74: ("nex", "Nex"),
    75: ("nightmare", "Nightmare"),
    76: ("phosanis_nightmare", "Phosani's Nightmare"),
    77: ("obor", "Obor"),
    78: ("phantom_muspah", "Phantom Muspah"),
    79: ("sarachnis", "Sarachnis"),
    80: ("scorpia", "Scorpia"),
    81: ("scurrius", "Scurrius"),
    82: ("skotizo", "Skotizo"),
    83: ("sol_heredit", "Sol Heredit"),
    84: ("spindel", "Spindel"),
    85: ("tempoross", "Tempoross"),
    86: ("the_gauntlet", "The Gauntlet"),
    87: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    88: ("the_leviathan", "The Leviathan"),
    89: ("the_whisperer", "The Whisperer"),
    90: ("theatre_of_blood", "Theatre of Blood"),
    91: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    92: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    93: ("tombs_of_amascut", "Tombs of Amascut"),
    94: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    95: ("tzkal_zuk", "TzKal-Zuk"),
    96: ("tztok_jad", "TzTok-Jad"),
    97: ("vardorvis", "Vardorvis"),
    98: ("venenatis", "Venenatis"),
    99: ("vet_ion", "Vet'ion"),
    100: ("vorkath", "Vorkath"),
    101: ("wintertodt", "Wintertodt"),
    102: ("zalcano", "Zalcano"),
    103: ("zulrah", "Zulrah"),
}

HISCORE_RESPONSE_LEN: Final[int] = (
    len(SKILLS_INDEX) + len(MINIGAMES_INDEX) + len(CLUES_INDEX) + len(BOSSES_INDEX)
)
