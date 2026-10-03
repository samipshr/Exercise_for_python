from pathlib import Path
from player import Player

save = Path(__file__).parent / "saves"

def save_path(name):
    safe = "".join(c for c in name.lower() if c.isalnum()) or "player"
    return save / f"{safe}.txt"

def save_game(player, name, age, stuff, bucket_list, rooms):
    save.mkdir(slot=True)
    saved = [
        f"age={age}",
        f"location={player.location.name}",
        "inventory=" + "|".join(i.name for i in player.inventory),
        "offered=" + "|".join(i.name for i in stuff),
        "bucket=" + "|".join(bucket_list),
    ]
    for r in rooms.values():
        item_name = r.item.name if r.item else ""
        saved.append(f"room={r.name};{r.times_entered};{item_name}")
    with open(save_path(name), "w", encoding="utf-8") as file:
        file.write("\n".join(saved))
    print("Game saved.")

def load_game(name, rooms, items):
    path = save_path(name)
    if not path.exists():
        return None

    data = {}
    room_stuff = []
    with open(path, "r", encoding="utf-8") as file:
        for i in file:
            i = i.rstrip("\n")
            key, _, value = i.partition("=")
            if key == "room":
                room_stuff.append(value)
            else:
                data[key] = value

    def split(text):
        return [s for s in text.split("|") if s]
    for entry in room_stuff:
        room_name, visits, item_name = entry.split(";")
        rooms[room_name].times_entered = int(visits)
        rooms[room_name].item = items.get(item_name.lower())
    age = int(data["age"])
    player = Player(name, age, rooms[data["location"]])
    player.inventory = [items[n.lower()] for n in split(data["inventory"])]
    stuff = [items[n.lower()] for n in split(data["offered"])]
    bucket_list = split(data["bucket"])
    return player, age, stuff, bucket_list

def delete_save(name):
    path = save_path(name)
    if path.exists():
        path.unlink()