import time

from items import Beer

f = open('hillary.txt','r')
picture = f.read()
f.close()

rooms = {
    "Tavern": {
        "description": "You're in a cozy tavern warmed by an open fire.",
        "exits": { "outside": "Taglon Village", "narnia": "Narnia", "teleporter": "Teleporter"},
        "items": { "beer": str(Beer())} ,
    },
    "Narnia": {
        "description": "You find yourself in an enchanted realm, far far from everything you know",
        "exits": {"teleporter": "Teleporter", "tavern": "Tavern"},
        "items": {"broken branches": "Hmm..Evidence of a recent struggle.", "sleigh": "A means to travel quickly?"}
    },
    "Taglon Village": {
        "description": "You're standing outside and there is a tavern to your right and a mansion down the street. It's raining.",
        "exits": { "tavern": "Tavern", "mansion": "Mansion", "bloodridge": "Bloodridge" },
        "items": {"barrel": "An old whisky barrel.", "bloody spoon": "A possible murder weapon, but who uses a spoon? Honestly?"}
    },
    "Teleporter": {
        "description": "you are standing inside the teleporter room. Here you can go to the many different worlds.",
        "exits": {"tavern": "Tavern", "holly": "Holly", "isabella": "Isabella", "max": "Max"},
        "items": {"candle": "This could be useful..", "chair": "A lonely chair.", "map": "Ummmm you might need this later on"},
    },
    "Bloodridge": {
        "description": "You're in the ancient town of Bloodridge. Home of the elder daemons.",
        "exits": { "taglon village": "Taglon Village"},
        "items": {"daemon blade": "A rustic blade. Looks evil."}
    },
    "Mansion": {
        "description": "You're on the first floor of a creepy four-story mansion.",
        "exits": {"outside": "Taglon Village", "floor2": "Floor 2"},
        "items": {"candle": "This could be useful..", "chair": "A lonely chair.", "suit of armor": "Oooh shiny."}
    },
    "Floor 2": {
        "description": "You're on the second floor and filled with self doubt.",
        "exits": {"floor1": "mansion", "floor3": "Floor 3"},
        "items": {"light switch": "What the hell is this thing on the wall? Seems out of place.", "crooked picture": "picture"}
    },
    "Floor 3": {
        "description": "You're now on floor three and have serious doubts about this place.",
        "exits": {"floor2": "Floor 2", "floor4": "Floor 4"},
        "items": {"nothing here": "nothing here"}
    },
    "Floor 4": {
        "description": "You're now on the top floor. A nightmarish phantom is approaching.",
        "exits": {"floor3": "Floor 3", "floor5": "Floor 5"},
        "items": {"sword": "Now this is what I need!!", "knife": "Uhhh not sure if this would be very useful.."}
    },
    "Floor 5": {
        "description": "You're now on the top floor. A nightmarish phantom is approaching.",
        "exits": {"floor4": "Floor 4", "service elevator": "Mansion"},
        "items": {"coffee": "I need to stay awake!", "brown pants": "hmm... i might need a change of clothes if i get scared"}
    },   
    "Holly":{
        "description": "you are standing inside a small warehouse, it's dark and cold inside, filled with strange smell that you may never want to know what its source is.",
        "exits": {"tavern": "Tavern", "teleporter": "Teleporter"},
        "items": {"newspaper": "Too dark to read, but there is something sticky on the pages", "flashlight": "Lucky you, it's broken"}
    },

    "Kitchen": {
        "description": "Here is a modern kitchen, there are pots setting up and meats on the table",
        "exits": {"tavern": "Tavern", "mansion": "Mansion", "bloodridge": "Bloodridge"},
        "items": {"pot": "a boiled pot, there are some meat and bones inside, for some bones, it looks like some part of bones from human legs and arms",
                  "cupboard": "A piece of cloth felt off as you opened the cupboard, with blood.", "knife":"a knife for cutting meat lying on the floor","cookbook":"Cookbook for cooking soup, the first page came into your eyes is a page with blood fingerprint on it "}
    },

    "Whiteroom":{
        "description": "you are standing inside a small room, all the walls are painted white, as you step inside the room, you heard someone's screaming, echoing inside the room.",
        "exits": {"tavern": "Tavern", "Teleporter": "Teleporter"},
        "items": {"MP3":"a small MP3 is placed at the edge of the room, without battery, not the source for the screaming sound" }
    },
    "Max": {
        "description": "you are laying on the floor of the mortuary, corpses are every where.",
        "exits": {"tavern": "Tavern", "teleporter": "Teleporter","outside": "Taglon Village", "narnia": "Narnia"},
        "items": {"a scalpel": "Be careful... It's sharp", "sickbed": "A white tidy bed...", "beaker": "Ummmmmm I'm wondering about what does it used to held before"}
    },
    "Warehouse": {
        "description": "you are standing inside the warehouse.",
        "exits": {"tavern": "Tavern", "teleporter": "Teleporter","outside": "Taglon Village", "narnia": "Narnia"},
        "items": {"a telescope": "It will be useful in the future, believe me.", "A skeleton": "evidence of some one has been killed...", "jacket": "keep in warm is very important"},
    },
    "Basement": {
        "description": "you are standing in a basement. Which is super cold.",
        "exits": {"tavern": "Tavern", "teleporter": "Teleporter","outside": "Taglon Village", "narnia": "Narnia"},
        "items": {"a waterbottle": "It seems it have not been used for a long time...", "a flashlight": "An important tool", "a 3D printer": "The printer is still working..."}
    },
    "Isabella": {
        "description": "You're standing inside the restroom and there is a village down the street. It's raining",
        "exits": {"taglon village": "Taglon Village" },
        "items": {"hand washing sink": "Blood is coming out of the tap", "mirror": "It seems like something is behind the mirror, looks like a dead body."}
    },
    "School": {
        "description": "You're standing inside the school and it is next to the Taglon Village. It's raining",
        "exits": {"taglon village": "Taglon Village"},
        "items": {"chemistry lab": "It looks messy.", "library": "Books are everywhere","locker":"All are locked and covered with blood.","playground":"Dead bodies are everywhere."}
    },
     "Taglon Village Country Club": {
        "description": "You're standing inside the Taglon Village Country Club and Taglon Village is down the street. It's raining",
        "exits": {"taglon village": "Taglon Village"},
        "items": {"vip lounge": "Free long island ice tea is provided.", "racecourse": "Ponies are training","restaurant":"Sponge fingers are today's special. Someone said it tastes like real man's finger.","changing room":"Haven't been cleaned for a long time, there are blood stains on the wall."}
    },
     "Tony's house": {
        "description": "You're standing inside Tony's house and the Taglon Village Country Club is next to it. It's raining",
        "exits": { "taglon village": "Taglon Village", "taglon village country club": "Taglon Village Country Club"},
        "items": {"tony's room": "Too messy, clothes are everywhere", "kitchen": "Knives are covered with blood, and the smell is disgusting.","attic":"There are some dirty giant teddy bears, even an adult male can hide in it.","Bathroom":"The water in the tub is bubbling"}
    }

}
