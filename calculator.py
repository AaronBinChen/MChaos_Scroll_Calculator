# Importing the built-in SQLite library in Python
import sqlite3 as sl
# Import modules for CGI handling
import cgi, cgitb

# Connection object
con = sl.connect('maplestory_items.db')

# Creating Database Table that holds information about the maple items
with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS ITEMS (
            id INTEGER NOT NULL,
            item_set VARCHAR (255) NOT NULL,
            item_category VARCHAR (255) NOT NULL,
            item_name VARCHAR (255) NOT NULL,
            class VARCHAR (255),
            level_requirement INTEGER,
            all_stats INTEGER,
            weapon_attack INTEGER,
            magic_attack INTEGER,
            PRIMARY KEY ("id")
        );
    """)

# Inserting Records
sql = 'INSERT OR IGNORE INTO ITEMS (id, item_set, item_category, item_name, class, level_requirement, all_stats, weapon_attack, magic_attack) values (?, ?, ?, ?, ?, ?, ?, ?, ?)'

data = [
    # Solid Gollux Set
    (1, 'Solid Gollux', 'Earrings', 'Solid Gollux Earrnings', 'All', 130, 10, 5, 5),
    (2, 'Solid Gollux', 'Ring', 'Solid Gollux Ring', 'All', 130, 6, 4, 4),
    (3, 'Solid Gollux', 'Pendant', 'Solid Engraved Gollux Pendant', 'All', 130, 19, 3, 3),
    (4, 'Solid Gollux', 'Belt', 'Solid Engraved Gollux Belt', 'All', 130, 10, 10, 10),
    
    # Scarlet Set
    (5, 'Scarlet', 'Ring', 'Scarlet Ring', 'All', 135, 4, 1, 1),
    
    # Meister Set
    (6, 'Meister', 'Ring', 'Meister Ring', 'All', 140, 5, 1, 1),
    
    # Reinforced Gollux Set
    (7, 'Reinforced Gollux', 'Earrings', 'Reinforced Gollux Earrings', 'All', 140, 12, 6, 6),
    (8, 'Reinforced Gollux', 'Ring', 'Reinforced Gollux Ring', 'All', 140, 8, 5, 5),
    (9, 'Reinforced Gollux', 'Pendant', 'Reinforced Engraved Gollux Pendant', 'All', 140, 23, 3, 3),
    (10, 'Reinforced Gollux', 'Belt', 'Reinforced Engraved Gollux Belt', 'All', 140, 30, 20, 20),
    
    # Superior Gollux Set
    (11, 'Superior Gollux', 'Earrings', 'Superior Gollux Earrings', 'All', 150, 15, 10, 10),
    (12, 'Superior Gollux', 'Ring', 'Superior Gollux Ring', 'All', 150, 10, 8, 8),
    (13, 'Superior Gollux', 'Pendant', 'Superior Engraved Gollux Pendant', 'All', 150, 28, 5, 5),
    (14, 'Superior Gollux', 'Belt', 'Superior Engraved Gollux Belt', 'All', 150, 60, 35, 35),

    # Outlaw Heart
    (15, 'Outlaw', 'Heart', 'Outlaw Heart', 'All', 150, 5, 0, 0),

    # Chaos Root Abyss Set - Warriors
    (16, 'CRA', 'Hat', 'Royal Warrior Helm', 'Warrior', 150, 40, 2, 0),   
    (17, 'CRA', 'Top', 'Eagle Eye Warrior Armor', 'Warrior', 150, 30, 2, 0),
    (18, 'CRA', 'Bottom', 'Trixter Warrior Pants', 'Warrior', 150, 30, 2, 0),
    (19, 'CRA', 'Weapon', 'Fafnir Mercy', 'Warrior', 150, 40, 171, 0),
    (20, 'CRA', 'Weapon', 'Fafnir Death Bringer', 'Warrior', 150, 40, 171, 0),
    (21, 'CRA', 'Weapon', 'Fafnir Mistilteinn', 'Warrior', 150, 40, 164, 0),
    (22, 'CRA', 'Weapon', 'Fafnir Twin Cleaver', 'Warrior', 150, 40, 164, 0),
    (23, 'CRA', 'Weapon', 'Fafnir Guardian Hammer', 'Warrior', 150, 40, 164, 0),
    (24, 'CRA', 'Weapon', 'Fafnir Penitent Tears', 'Warrior', 150, 40, 171, 0),
    (25, 'CRA', 'Weapon', 'Fafnir Battle Cleaver', 'Warrior', 150, 40, 171, 0),
    (26, 'CRA', 'Weapon', 'Fafnir Lightning Striker', 'Warrior', 150, 40, 171, 0),
    (27, 'CRA', 'Weapon', 'Fafnir Brionak', 'Warrior', 150, 40, 171, 0),
    (28, 'CRA', 'Weapon', 'Fafnir Moon Glaive', 'Warrior', 150, 40, 171, 0),
    (29, 'CRA', 'Weapon', 'Fafnir Raven Ring', 'Warrior', 150, 40, 171, 0),
    (30, 'CRA', 'Weapon', 'Fafnir Big Mountain', 'Warrior', 150, 40, 171, 0),

    # Chaos Root Abyss Set - Magician
    (31, 'CRA', 'Hat', 'Royal Dunwitch Hat', 'Magician', 150, 40, 0, 2),   
    (32, 'CRA', 'Top', 'Eagle Eye Dunwitch Robe', 'Magician', 150, 30, 0, 2),
    (33, 'CRA', 'Bottom', 'Trixter Dunwitch Pants', 'Magician', 150, 30, 0, 2), 
    (34, 'CRA', 'Weapon', 'Fafnir Mandle Cradle', 'Magician', 150, 40, 119, 201),
    (35, 'CRA', 'Weapon', 'Fafnir Scepter', 'Magician', 150, 40, 119, 201),
    (36, 'CRA', 'Weapon', 'Fafnir Psy-limiter', 'Magician', 150, 40, 119, 201),
    (37, 'CRA', 'Weapon', 'Fafnir Lucent Gauntlet', 'Magician', 150, 40, 119, 201),
    (38, 'CRA', 'Weapon', 'Fafnir Mana Taker', 'Magician', 150, 40, 119, 201),
    (39, 'CRA', 'Weapon', 'Fafnir Mana Crown', 'Magician', 150, 40, 126, 204),
    (40, 'CRA', 'Weapon', 'Fafnir Indigo Flash', 'Magician', 150, 40, 126, 204),

    # Chaos Root Abyss Set - Bowman
    (41, 'CRA', 'Hat', 'Royal Ranger Beret', 'Bowman', 150, 40, 2, 0),   #No MA so it'll be null
    (42, 'CRA', 'Top', 'Eagle Eye Ranger Cowl', 'Bowman', 150, 30, 2, 0),
    (43, 'CRA', 'Bottom', 'Trixter Ranger Pants', 'Bowman', 150, 30, 2, 0),
    (44, 'CRA', 'Weapon', 'Fafnir Wind Chaser', 'Bowman', 150, 40, 160, 0),
    (45, 'CRA', 'Weapon', 'Fafnir Windwing Shooter', 'Bowman', 150, 40, 164, 0),
    (46, 'CRA', 'Weapon', 'Fafnir Dual Windwing', 'Bowman', 150, 40, 160, 0),
    (47, 'CRA', 'Weapon', 'Fafnir Ancient Bow', 'Bowman', 150, 40, 160, 0),

    # Chaos Root Abyss Set - Thief 
    (48, 'CRA', 'Hat', 'Royal Assassin Hood', 'Thief', 150, 40, 2, 0),
    (49, 'CRA', 'Top', 'Eagle Eye Assassin Shirt', 'Thief', 150, 30, 2, 0),
    (50, 'CRA', 'Bottom', 'Trixter Assassin Pants', 'Thief', 150, 30, 2, 0),
    (51, 'CRA', 'Weapon', 'Fafnir Split Edge', 'Thief', 150, 40, 128, 0),
    (52, 'CRA', 'Weapon', 'Fafnir Chain', 'Thief', 150, 40, 160, 0),
    (53, 'CRA', 'Weapon', 'Fafnir Dragon Ritual Fan', 'Thief', 150, 40, 160, 0),
    (54, 'CRA', 'Weapon', 'Fafnir Damascus', 'Thief', 150, 40, 160, 0),
    (55, 'CRA', 'Weapon', 'Fafnir Ciel Claire', 'Thief', 150, 40, 164, 0),
    (56, 'CRA', 'Weapon', 'Fafnir Risk Holder', 'Thief', 150, 40, 86, 0),

    # Chaos Root Abyss Set - Pirate
    (57, 'CRA', 'Hat', 'Royal Wanderer Hat', 'Pirate', 150, 40, 2, 0),
    (58, 'CRA', 'Top', 'Eagle Eye Wanderer Coat', 'Pirate', 150, 30, 2, 0),
    (59, 'CRA', 'Bottom', 'Trixter Wanderer Pants', 'Pirate', 150, 30, 2, 0),
    (60, 'CRA', 'Weapon', 'Fafnir Angelic Shooter', 'Pirate', 150, 40, 128, 0),
    (61, 'CRA', 'Weapon', 'Fafnir Split Edge', 'Pirate', 150, 40, 128, 0),
    (62, 'CRA', 'Weapon', 'Fafnir Perry Talon', 'Pirate', 150, 40, 128, 0),
    (63, 'CRA', 'Weapon', 'Fafnir Zeliska', 'Pirate', 150, 40, 125, 0),
    (64, 'CRA', 'Weapon', 'Fafnir Lost Cannon', 'Pirate', 150, 40, 175, 0),

    # Sweetwater Set
    (65, 'Sweetwater', 'Face Accessory', 'Sweetwater Tattoo', 'All', 160, 5, 0, 0),
    (66, 'Sweetwater', 'Eye Accessory', 'Sweetwater Monocle', 'All', 160, 10, 0, 0),
    #  Absolab Set- Warrior
    (65, 'Absolab', 'Gloves', 'Absolab Knight Gloves', 'Warrior', 160, 20, 5, 0),
    (66, 'Absolab', 'Shoulder', 'Absolab Knight Shoulder', 'Warrior', 160, 14, 10, 10),

    # Absolab Set - Magician
    (67, 'Absolab', 'Gloves', 'Absolab Mage Gloves', 'Magician', 160, 20, 0, 5),
    (68, 'Absolab', 'Shoulder', 'Absolab Mage Shoulder', 'Magician', 160, 14, 10, 10),

    # Absolab Set - Bowman
    (69, 'Absolab', 'Gloves', 'Absolab Archer Gloves', 'Bowman', 160, 20, 5, 0),
    (70, 'Absolab', 'Shoulder', 'Absolab Archer Shoulder', 'Bowman', 160, 14, 10, 10),

    # Absolab Set - Thief
    (71, 'Absolab', 'Gloves', 'Absolab Bandit Gloves', 'Thief', 160, 20, 5, 0),
    (72, 'Absolab', 'Shoulder', 'Absolab Bandit Shoulder', 'Thief', 160, 14, 10, 10),

    # Absolab Set - Pirate
    (73, 'Absolab', 'Gloves', 'Absolab Pirate Gloves', 'Pirate', 160, 20, 5, 0),
    (74, 'Absolab', 'Shoulder', 'Absolab Pirate Shoulder', 'Pirate', 160, 14, 10, 10),

    # Arcane Umbra Set - Warriors
    (75, 'arc', 'Hat', 'Arcane Umbra Knight Hat', 'Warrior', 200, 65, 7, 0),   
    (76, 'arc', 'Shoes', 'Arcane Umbra Knight Shoes', 'Warrior', 200, 40, 9, 0),
    (77, 'arc', 'Gloves', 'Arcane Umbra Knight Gloves', 'Warrior', 200, 40, 9, 0),
    (78, 'arc', 'Cape', 'Arcane Umbra Knight Cape', 'Warrior', 200, 35, 6, 6),
    (79, 'arc', 'Shoulder', 'Arcane Umbra Knight Shoulder', 'Warrior', 200, 35, 20, 20),
    (80, 'arc', 'Weapon', 'Arcane Umbra Bladecaster', 'Warrior', 200, 100, 295, 0),
    (81, 'arc', 'Weapon', 'Arcane Umbra Desperado', 'Warrior', 200, 100, 295, 0),
    (82, 'arc', 'Weapon', 'Arcane Umbra Saber', 'Warrior', 200, 100, 283, 0),
    (83, 'arc', 'Weapon', 'Arcane Umbra Axe', 'Warrior', 200, 100, 283, 0),
    (84, 'arc', 'Weapon', 'Arcane Umbra Hammer', 'Warrior', 200, 100, 283, 0),
    (85, 'arc', 'Weapon', 'Arcane Umbra Two-handed Sword', 'Warrior', 200, 100, 195, 0),
    (86, 'arc', 'Weapon', 'Arcane Umbra Two-handed Axe', 'Warrior', 200, 100, 295, 0),
    (87, 'arc', 'Weapon', 'Arcane Umbra Two-handed Hammer', 'Warrior', 200, 100, 295, 0),
    (88, 'arc', 'Weapon', 'Arcane Umbra Spear', 'Warrior', 200, 100, 295, 0),
    (89, 'arc', 'Weapon', 'Arcane Umbra Polearm', 'Warrior', 200, 100, 264, 0),
    (90, 'arc', 'Weapon', 'Arcane Umbra Katana', 'Warrior', 200, 100, 283, 0),
    (91, 'arc', 'Weapon', 'Arcane Umbra Ellaha', 'Warrior', 200, 100, 221, 0),

    # Arcane Umbra Set - Magician
    (92, 'arc', 'Hat', 'Arcane Umbra Mage Hat', 'Magician', 200, 65, 0, 7),   
    (93, 'arc', 'Shoes', 'Arcane Umbra Mage Shoes', 'Magician', 200, 40, 0, 9),
    (94, 'arc', 'Gloves', 'Arcane Umbra Mage Gloves', 'Magician', 200, 40, 0, 9), 
    (95, 'arc', 'Cape', 'Arcane Umbra Mage Cape', 'Magician', 200, 35, 6, 6),
    (96, 'arc', 'Shoulder', 'Arcane Umbra Mage Shoulder', 'Magician', 200, 35, 20, 20),
    (97, 'arc', 'Weapon', 'Arcane Umbra Shining Rod', 'Magician', 200, 100, 206, 347),
    (98, 'arc', 'Weapon', 'Arcane Umbra Scepter', 'Magician', 200, 100, 206, 347),
    (99, 'arc', 'Weapon', 'Arcane Umbra Psy-limiter', 'Magician', 200, 100, 206, 347),
    (100, 'arc', 'Weapon', 'Arcane Umbra Lucent Gauntlet', 'Magician', 200, 100, 206, 347),
    (101, 'arc', 'Weapon', 'Arcane Umbra Wand', 'Magician', 200, 100, 206, 347),
    (102, 'arc', 'Weapon', 'Arcane Umbra Staff', 'Magician', 200, 100, 218, 353),
    (103, 'arc', 'Weapon', 'Arcane Umbra Fan', 'Magician', 200, 100, 206, 347),

    # Arcane Umbra Set - Bowman
    (104, 'arc', 'Hat', 'Arcane Umbra Archer Hat', 'Bowman', 200, 65, 7, 0),   #No MA so it'll be null
    (105, 'arc', 'Shoes', 'Eagle Eye Ranger Cowl', 'Bowman', 200, 40, 9, 0),
    (106, 'arc', 'Gloves', 'Trixter Ranger Pants', 'Bowman', 200, 40, 9, 0),
    (107, 'arc', 'Cape', 'Arcane Umbra Archer Cape', 'Bowman', 200, 35, 6, 6),
    (108, 'arc', 'Shoulder', 'Arcane Umbra Archer Shoulder', 'Bowman', 200, 35, 20, 20),
    (109, 'arc', 'Weapon', 'Arcane Umbra Bow', 'Bowman', 200, 100, 276, 0),
    (110, 'arc', 'Weapon', 'Arcane Umbra Crossbow', 'Bowman', 200, 100, 283, 0),
    (111, 'arc', 'Weapon', 'Arcane Umbra Dual Bowguns', 'Bowman', 200, 100, 276, 0),
    (112, 'arc', 'Weapon', 'Arcane Umbra Ancient Bow', 'Bowman', 200, 100, 276, 0),

    # Arcane Umbra Set - Thief 
    (113, 'arc', 'Hat', 'Arcane Umbra Thief Hat', 'Thief', 200, 65, 7, 0),
    (114, 'arc', 'Shoes', 'Arcane Umbra Thief Shoes', 'Thief', 200, 40, 9, 0),
    (115, 'arc', 'Gloves', 'Arcane Umbra Thief Gloves', 'Thief', 200, 40, 9, 0),
    (116, 'arc', 'Cape', 'Arcane Umbra Thief Cape', 'Thief', 200, 35, 6, 6),
    (117, 'arc', 'Shoulder', 'Arcane Umbra Thief Shoulder', 'Thief', 200, 35, 20, 20),
    (118, 'arc', 'Weapon', 'Arcane Umbra Energy Chain', 'Thief', 200, 100, 221, 0),
    (119, 'arc', 'Weapon', 'Arcane Umbra Chain', 'Thief', 200, 100, 276, 0),
    (120, 'arc', 'Weapon', 'Arcane Umbra Super Ritual Fan', 'Thief', 200, 100, 276, 0),
    (121, 'arc', 'Weapon', 'Arcane Umbra Dagger', 'Thief', 200, 100, 276, 0),
    (122, 'arc', 'Weapon', 'Arcane Umbra Cane', 'Thief', 200, 100, 283, 0),
    (123, 'arc', 'Weapon', 'Arcane Umbra Guards', 'Thief', 200, 100, 149, 0),

    # Arcane Umbra Set - Pirate
    (124, 'arc', 'Hat', 'Arcane Umbra Pirate Hat', 'Pirate', 200, 65, 7, 0),
    (125, 'arc', 'Shoes', 'Arcane Umbra Pirate Shoes', 'Pirate', 200, 40, 9, 0),
    (126, 'arc', 'Gloves', 'Arcane Umbra Pirate Gloves', 'Pirate', 200, 40, 9, 0),
    (127, 'arc', 'Cape', 'Arcane Umbra Pirate Cape', 'Pirate', 200, 35, 6, 6),
    (128, 'arc', 'Shoulder', 'Arcane Umbra Pirate Shoulder', 'Pirate', 200, 35, 20, 20),
    (129, 'arc', 'Weapon', 'Arcane Umbra Soul Shooter', 'Pirate', 200, 100, 221, 0),
    (130, 'arc', 'Weapon', 'Arcane Umbra Energy Chain', 'Pirate', 200, 100, 221, 0),
    (131, 'arc', 'Weapon', 'Arcane Umbra Knuckle', 'Pirate', 200, 100, 221, 0),
    (132, 'arc', 'Weapon', 'Arcane Umbra Pistol', 'Pirate', 200, 100, 216, 0),
    (133, 'arc', 'Weapon', 'Arcane Umbra Siege Gun', 'Pirate', 200, 100, 302, 0)
]

# Inserting Sample Rows into the Table now
with con:
    con.executemany(sql, data)

# Extracting data that is needed
# with con:
#     data = con.execute("SELECT * FROM ITEMS WHERE item_set == 'arc'")
#     for row in data:
#         print(row)

# Create instance of Field Storage
form = cgi.FieldStorage()

# Get data from fields
item_name = form.getvalue('item_name')
num_of_stars = form.getvalue('number_of_stars')
num_of_scrolls = form.getvalue('number_of_scrolls')

return((item_name, num_of_stars, num_of_scrolls))