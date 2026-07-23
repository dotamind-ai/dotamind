# Dotamind AI
# База метаданных героев Dota 2


HEROES_META = {


    "Anti-Mage": {

        "attribute": "Agility",

        "roles": [
            "Carry"
        ],

        "difficulty": "Hard",

        "playstyle": [
            "Farm",
            "Split Push",
            "Late Game"
        ]

    },


    "Juggernaut": {

        "attribute": "Agility",

        "roles": [
            "Carry"
        ],

        "difficulty": "Medium",

        "playstyle": [
            "Fighting",
            "Safe Lane",
            "Scaling"
        ]

    },


    "Invoker": {

        "attribute": "Intelligence",

        "roles": [
            "Mid",
            "Support"
        ],

        "difficulty": "Very Hard",

        "playstyle": [
            "Magic Damage",
            "Control",
            "Combo"
        ]

    },


    "Phantom Assassin": {

        "attribute": "Agility",

        "roles": [
            "Carry"
        ],

        "difficulty": "Medium",

        "playstyle": [
            "Critical Damage",
            "Burst",
            "Late Game"
        ]

    }

}




def get_hero_meta(hero_name):

    return HEROES_META.get(
        hero_name,
        {
            "attribute": "Unknown",
            "roles": [],
            "difficulty": "Unknown",
            "playstyle": []
        }
    )