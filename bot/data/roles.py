# Dotamind AI
# База ролей героев


HERO_ROLES = {


    "Anti-Mage": [
        "Carry"
    ],


    "Juggernaut": [
        "Carry"
    ],


    "Phantom Assassin": [
        "Carry"
    ],


    "Invoker": [
        "Mid",
        "Control"
    ],


    "Axe": [
        "Initiator",
        "Offlane"
    ],


    "Lion": [
        "Support",
        "Control"
    ],


    "Crystal Maiden": [
        "Support"
    ],


    "Shadow Demon": [
        "Support",
        "Save"
    ],


    "Earthshaker": [
        "Initiator",
        "Support"
    ]

}




def get_roles(hero_name):

    return HERO_ROLES.get(
        hero_name,
        [
            "Unknown"
        ]
    )