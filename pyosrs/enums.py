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
    18: ("collections_logged", "Collections Logged"),
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
    19: ("abyssal_sire", "Abyssal Sire"),
    20: ("alchemical_hydra", "Alchemical Hydra"),
    21: ("amoxliatl", "Amoxliatl"),
    22: ("araxxor", "Araxxor"),
    23: ("artio", "Artio"),
    24: ("barrows_chests", "Barrows Chests"),
    25: ("bryophyta", "Bryophyta"),
    26: ("callisto", "Callisto"),
    27: ("cal_varion", "Calvarion"),
    28: ("cerberus", "Cerberus"),
    29: ("chambers_of_xeric", "Chambers of Xeric"),
    30: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    31: ("chaos_elemental", "Chaos Elemental"),
    32: ("chaos_fanatic", "Chaos Fanatic"),
    33: ("commander_zilyana", "Commander Zilyana"),
    34: ("corporeal_beast", "Corporeal Beast"),
    35: ("crazy_archaeologist", "Crazy Archaeologist"),
    36: ("dagannoth_prime", "Dagannoth Prime"),
    37: ("dagannoth_rex", "Dagannoth Rex"),
    38: ("dagannoth_supreme", "Dagannoth Supreme"),
    39: ("deranged_archaeologist", "Deranged Archaeologist"),
    40: ("duke_sucellus", "Duke Sucellus"),
    41: ("general_graardor", "General Graardor"),
    42: ("giant_mole", "Giant Mole"),
    43: ("grotesque_guardians", "Grotesque Guardians"),
    44: ("hespori", "Hespori"),
    45: ("kalphite_queen", "Kalphite Queen"),
    46: ("king_black_dragon", "King Black Dragon"),
    47: ("kraken", "Kraken"),
    48: ("kree_arra", "Kree'Arra"),
    49: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    50: ("lunar_chests", "Lunar Chests"),
    51: ("mimic", "Mimic"),
    52: ("nex", "Nex"),
    53: ("nightmare", "Nightmare"),
    54: ("phosanis_nightmare", "Phosani's Nightmare"),
    55: ("obor", "Obor"),
    56: ("phantom_muspah", "Phantom Muspah"),
    57: ("sarachnis", "Sarachnis"),
    58: ("scorpia", "Scorpia"),
    59: ("scurrius", "Scurrius"),
    60: ("skotizo", "Skotizo"),
    61: ("sol_heredit", "Sol Heredit"),
    62: ("spindel", "Spindel"),
    63: ("tempoross", "Tempoross"),
    64: ("the_gauntlet", "The Gauntlet"),
    65: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    66: ("the_hueycoatl", "The Hueycoatl"),
    67: ("the_leviathan", "The Leviathan"),
    68: ("the_royal_titans", "The Royal Titans"),
    69: ("the_whisperer", "The Whisperer"),
    70: ("theatre_of_blood", "Theatre of Blood"),
    71: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    72: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    73: ("tombs_of_amascut", "Tombs of Amascut"),
    74: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    75: ("tzkal_zuk", "TzKal-Zuk"),
    76: ("tztok_jad", "TzTok-Jad"),
    77: ("vardorvis", "Vardorvis"),
    78: ("venenatis", "Venenatis"),
    79: ("vet_ion", "Vet'ion"),
    80: ("vorkath", "Vorkath"),
    81: ("wintertodt", "Wintertodt"),
    82: ("zalcano", "Zalcano"),
    83: ("zulrah", "Zulrah"),
}
