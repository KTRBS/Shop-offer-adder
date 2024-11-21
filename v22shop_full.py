import os
import json
import re

def get_file_path():
    base_path = "/storage/emulated/0/"
    file_path = input(f"ktr epock tool for v22 \ntool ver:V1\nEnter the file path where Classic Brawl server is located\n{base_path}")
    full_path = os.path.join(base_path, file_path, "shop.py")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path

def load_existing_offers(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            try:
                # Extract the offers list using regex
                offers_match = re.search(r"offers\s*=\s*(\[[\s\S]*?\])", content)
                if offers_match:
                    return json.loads(offers_match.group(1))
            except (json.JSONDecodeError, AttributeError):
                pass
    return []

def add_offer(data, shop_display, shop_type=None, title=None, id_val=None, cost=None, multiplier=None, timer=None, skin_id=None):
    offer = {
        "ID": id_val or 4,
        "OfferTitle": title or "no title",
        "Cost": cost or 0,
        "Multiplier": multiplier or 1,
        "SkinID": skin_id or 0,
        "ShopType": shop_type or 0,
        "ShopDisplay": shop_display,
        "Timer": timer or 99999
    }
    data.append(offer)

def main_menu():
    print("Menu:")
    print("1: Add normal offer")
    print("2: Add daily deals offer")
    print("3: Add skin offer")
    print("4: Add star coin offer")
    print("5: Exit")
    return input("Choose an option: ")

def sub_menu_normal():
    options = [
        {"name": "coins", "id": 1},
        {"name": "brawler", "id": 2},
        {"name": "star power", "id": 5},
        {"name": "brawl box", "id": 6},
        {"name": "tickets", "id": 7},
        {"name": "token doubler", "id": 9},
        {"name": "megabox", "id": 10},
        {"name": "power points", "id": 12},
        {"name": "bigbox", "id": 14},
        {"name": "gems", "id": 16},
    ]

    print("Choose what you want to add:")
    for i, opt in enumerate(options):
        print(f"{i}: {opt['name']}")

    choice = int(input("Enter the number: "))
    if 0 <= choice < len(options):
        return options[choice]["id"]
    else:
        print("Invalid choice. Please try again.")
        return sub_menu_normal()

def currency_menu():
    print("Choose currency:")
    print("0: FREE")
    print("1: Gems")
    print("2: Coins")
    print("3: Star points")
    return int(input("Enter the number: "))

def skin_menu():
    skins = {
        "Shelly": [
    {"SkinID": 29, "TID": "TID_SHOTGUN_BANDITA_SKIN", "DefaultCost": 29},
    {"SkinID": 52, "TID": "TID_SHOTGUN_STAR_SKIN", "DefaultCost": 0},
    {"SkinID": 122, "TID": "TID_SHELLY_WITCH_SKIN", "DefaultCost": 149}
],
"Nita": [
    {"SkinID": 15, "TID": "TID_SHAMAN_PANDA_SKIN", "DefaultCost": 29},
    {"SkinID": 60, "TID": "TID_NITA_REINDEER_SKIN", "DefaultCost": 149},
    {"SkinID": 79, "TID": "TID_SHAMAN_SHIBA_SKIN", "DefaultCost": 149}
],
"Colt": [
    {"SkinID": 2, "TID": "TID_GUNSLINGER_ROCKSTAR_SKIN", "DefaultCost": 29},
    {"SkinID": 69, "TID": "TID_SKIN_LUNAR_COLT", "DefaultCost": 149},
    {"SkinID": 103, "TID": "TID_COLT_OUTLAW_SKIN", "DefaultCost": 29}
],
"Bull": [
    {"SkinID": 25, "TID": "TID_BULL_HAIR_SKIN", "DefaultCost": 79},
    {"SkinID": 64, "TID": "TID_SKIN_FOOTBULL", "DefaultCost": 79},
    {"SkinID": 102, "TID": "TID_BULL_LINEBACKER_SKIN", "DefaultCost": 29}
],
"Jessie": [
    {"SkinID": 44, "TID": "TID_MECHANIC_KNIGHT_SKIN", "DefaultCost": 149},
    {"SkinID": 47, "TID": "TID_MECHANIC_SUMMER_SKIN", "DefaultCost": 79},
    {"SkinID": 123, "TID": "TID_JESSIE_DARK_KNIGHT_SKIN", "DefaultCost": 39}
],
"Brock": [
    {"SkinID": 5, "TID": "TID_ROCKET_BEACH_SKIN", "DefaultCost": 79},
    {"SkinID": 58, "TID": "TID_BROCK_BOOMBOX_SKIN", "DefaultCost": 79},
    {"SkinID": 72, "TID": "TID_SKIN_LUNAR_BROCK", "DefaultCost": 149},
    {"SkinID": 91, "TID": "TID_BROCK_HOTROD_SKIN", "DefaultCost": 149}
],
"Dynamike": [
    {"SkinID": 56, "TID": "TID_DYNAMIKE_SANTA_SKIN", "DefaultCost": 79},
    {"SkinID": 57, "TID": "TID_DYNAMIKE_CHEF_SKIN", "DefaultCost": 149},
    {"SkinID": 97, "TID": "TID_MIKE_ROBO_SKIN", "DefaultCost": 299}
],
"Bo": [
    {"SkinID": 94, "TID": "TID_BO_MECHA_SKIN", "DefaultCost": 299},
    {"SkinID": 98, "TID": "TID_BO_MECHA_LIGHT_SKIN", "DefaultCost": 49}
],
"Tick": [
    {"SkinID": 106, "TID": "TID_TICK_ROBO_SKIN", "DefaultCost": 149}
],
"8-bit": [
    {"SkinID": 109, "TID": "TID_8BIT_CLASSIC_SKIN", "DefaultCost": 29}
],
"Emz": [
    {"SkinID": 119, "TID": "TID_EMZ_TROLL_SKIN", "DefaultCost": 149}
],
"El Primo": [
    {"SkinID": 28, "TID": "TID_LUCHADOR_RUDO_SKIN", "DefaultCost": 79},
    {"SkinID": 30, "TID": "TID_LUCHADOR_KING_SKIN", "DefaultCost": 149},
    {"SkinID": 128, "TID": "TID_EL_PRIMO_BROWN_SKIN", "DefaultCost": 149}
],
"Barley": [
    {"SkinID": 27, "TID": "TID_BARKEEP_GOLD_SKIN", "DefaultCost": 29},
    {"SkinID": 59, "TID": "TID_BARLEY_WIZARD_SKIN", "DefaultCost": 0},
    {"SkinID": 90, "TID": "TID_BARLEY_MS_SKIN", "DefaultCost": 149},
    {"SkinID": 92, "TID": "TID_BARLEY_MAPLE_SKIN", "DefaultCost": 79},
    {"SkinID": 116, "TID": "TID_BARLEY_RED_WIZARD_SKIN", "DefaultCost": 29}
],
"Poco": [
    {"SkinID": 71, "TID": "TID_SKIN_VALENTINE_POCO", "DefaultCost": 149}
],
"Rosa": [
    {"SkinID": 111, "TID": "TID_ROSA_CALENDAR_SKIN", "DefaultCost": 149}
],
"Rico": [
    {"SkinID": 26, "TID": "TID_TRICKSHOT_GOLD_SKIN", "DefaultCost": 149},
    {"SkinID": 68, "TID": "TID_SKIN_POPCORN_RICO", "DefaultCost": 149}
],
"Darryl": [
    {"SkinID": 121, "TID": "TID_DARRYL_HOTROD_SKIN", "DefaultCost": 79}
],
"Penny": [
    {"SkinID": 119, "TID": "TID_PENNY_SANTA_SKIN", "DefaultCost": 79}
],
"Carl": [
    {"SkinID": 93, "TID": "TID_CARL_RR_SKIN", "DefaultCost": 79},
    {"SkinID": 104, "TID": "TID_CARL_HOG_RIDER_SKIN", "DefaultCost": 79}
],
"Piper": [
    {"SkinID": 65, "TID": "TID_PIPER_SNOW_SKIN", "DefaultCost": 79}
],
"Pam": [
    {"SkinID": 73, "TID": "TID_PAM_MIMI_SKIN", "DefaultCost": 149}
],
"Frank": [
    {"SkinID": 87, "TID": "TID_FRANK_DARK_SKIN", "DefaultCost": 149}
],
"Bibi": [
    {"SkinID": 108, "TID": "TID_BIBI_GOLDEN_SKIN", "DefaultCost": 149}
],
"Mortis": [
    {"SkinID": 50, "TID": "TID_UNDERTAKER_GREASER_SKIN", "DefaultCost": 149},
    {"SkinID": 63, "TID": "TID_UNDERTAKER_HAT_SKIN", "DefaultCost": 0},
    {"SkinID": 75, "TID": "TID_UNDERTAKER_NIGHTWITCH_SKIN", "DefaultCost": 149}
],
"Tara": [
    {"SkinID": 116, "TID": "TID_TARA_MYSTIC_SKIN", "DefaultCost": 149}
],
"Gene": [
    {"SkinID": 102, "TID": "TID_GENIE_ALADIN_SKIN", "DefaultCost": 149}
],
"Spike": [
    {"SkinID": 11, "TID": "TID_CACTUS_PINK_SKIN", "DefaultCost": 79},
    {"SkinID": 96, "TID": "TID_SPIKE_ROBO_SKIN", "DefaultCost": 149}
],
"Crow": [
    {"SkinID": 20, "TID": "TID_CROW_WHITE_SKIN", "DefaultCost": 79},
    {"SkinID": 49, "TID": "TID_CROW_PHEONIX_SKIN", "DefaultCost": 299},
    {"SkinID": 95, "TID": "TID_CROW_MECHA_SKIN", "DefaultCost": 299},
    {"SkinID": 100, "TID": "TID_CROW_MECHA_GOLD_SKIN", "DefaultCost": 49},
    {"SkinID": 101, "TID": "TID_CROW_MECHA_NIGHT_SKIN", "DefaultCost": 49}
],
"Leon": [
    {"SkinID": 110, "TID": "TID_LEON_SHARK_SKIN", "DefaultCost": 79},
    {"SkinID": 126, "TID": "TID_LEON_WEREWOLF_SKIN", "DefaultCost": 149}
],
"Sandy": [
    {"SkinID": 118, "TID": "TID_SANDY_SNOOZE_SKIN", "DefaultCost": 79},
    {"SkinID": 120, "TID": "TID_SANDY_NIGHT_SKIN", "DefaultCost": 149}
],
    }

    print("Select the character for which you want to add a skin:")
    for i, character in enumerate(skins.keys()):
        print(f"{i}: {character}")

    char_choice = int(input("Enter the number for the character: "))
    selected_character = list(skins.keys())[char_choice]

    print(f"\nSelected Character: {selected_character}")
    print("Available Skins:")
    for i, skin in enumerate(skins[selected_character]):
        print(f"{i}: {skin['TID']}, Default Cost: {skin['DefaultCost']}")

    skin_choice = int(input("Enter the number for the skin: "))
    selected_skin = skins[selected_character][skin_choice]

    print(f"\nSelected Skin - TID: {selected_skin['TID']}, Default Cost: {selected_skin['DefaultCost']}")
    price_choice = input("Do you want to set a custom price? (y/n): ").lower()

    if price_choice == 'y':
        custom_cost = int(input("Enter the custom price: "))
        selected_skin["Cost"] = custom_cost
    else:
        selected_skin["Cost"] = selected_skin["DefaultCost"]

    return selected_skin

def write_shop_py(file_path, data):
    template = f"""class Shop:
    
    offers = {json.dumps(data, indent=8, ensure_ascii=False)}
    
    gold = [
        {{
            'Cost': 20,
            'Amount': 150
        }},
        {{
            'Cost': 50,
            'Amount': 400
        }},
        {{
            'Cost': 140,
            'Amount': 1200
        }},
        {{
            'Cost': 280,
            'Amount': 2600
        }}
    ]
    
    tickets = [
        {{
            'Cost': 20,
            'Amount': 150
        }},
        {{
            'Cost': 50,
            'Amount': 400
        }},
        {{
            'Cost': 140,
            'Amount': 1200
        }},
        {{
            'Cost': 280,
            'Amount': 2600
        }}
    ]
    
    boxes = [
        {{
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 3
        }},
        {{
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 10
        }}
    ]
    
    token_doubler = {{
        'Cost': 50,
        'Amount': 1000
    }}
    
    def EncodeShopOffers(self):
        count = len(Shop.offers)
        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]

            self.writeVint(1)
            self.writeVint(item['ID'])  # ItemID
            self.writeVint(item['Multiplier'])  # Amount
            self.writeScId(0, item['SkinID'])
            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]
            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer'])  # Timer
            self.writeVint(1)
            self.writeVint(100)
            self.writeBoolean(False)  # is Offer Purchased
            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0)
            self.writeInt(0)
            self.write_string_reference(item['OfferTitle'])  # Offer's name
            self.writeBoolean(False)
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(template)

def main():
    file_path = get_file_path()
    data = load_existing_offers(file_path)

    while True:
        choice = main_menu()

        if choice == "1":
            shop_display = 0
            offer_id = sub_menu_normal()
            title = input("Set title: ")
            currency = currency_menu()
            cost = 0 if currency == 0 else int(input("Set price: "))
            shop_type = {1: 0, 2: 1, 3: 3}[currency] if currency > 0 else 0
            multiplier = int(input("Set items amount: "))
            timer = int(input("Set offer time (in seconds): "))
            add_offer(data, shop_display, shop_type, title, offer_id, cost, multiplier, timer)

        elif choice == "2":
            shop_display = 1
            offer_id = sub_menu_normal()
            title = input("Set title: ")
            currency = currency_menu()
            cost = 0 if currency == 0 else int(input("Set price: "))
            shop_type = {1: 0, 2: 1, 3: 3}[currency] if currency > 0 else 0
            multiplier = int(input("Set items amount: "))
            timer = int(input("Set offer time (in seconds): "))
            add_offer(data, shop_display, shop_type, title, offer_id, cost, multiplier, timer)

        elif choice == "3":
            shop_display = 2
            selected_skin = skin_menu()
            timer = int(input("Set offer time (in seconds): "))
            
            add_offer(data, shop_display, skin_id=selected_skin["SkinID"], cost=selected_skin["Cost"], title=selected_skin["TID"], timer=timer)

        elif choice == "4":
            shop_display = 0
            offer_id = sub_menu_normal()
            title = input("Set title: ")
            cost = int(input("Set price: "))
            multiplier = int(input("Set items amount: "))
            timer = int(input("Set offer time (in seconds): "))
            add_offer(data, shop_display, shop_type=3, title=title, id_val=offer_id, cost=cost, multiplier=multiplier, timer=timer)

        elif choice == "5":
            break

        write_shop_py(file_path, data)
        print("shop.py has been updated.\n\n")

if __name__ == "__main__":
    main()