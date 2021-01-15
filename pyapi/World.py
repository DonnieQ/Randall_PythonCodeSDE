import Enemies
import random

#parent class for tiles
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #dummy checks
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
       return """
       ***********************************************************************************************
        You awaken inside Chad's class classroom, dust and decayed wallpaper telling their own stories.
        You see four possible paths, each emitting their own dangers.
        ************************************************************************************************
        """

#randomly presents enemy to player
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = Enemies.Zombie()
            self.alive_text = """
            ***********************************************************
            A Zombie comes running towards you! Is that a classmate?
            ***********************************************************
                              """
            self.dead_text = """
            ***************************************************************
            The zombie of ur classmate lies motionless, what happened here?
            ***************************************************************
                             """
        elif r < 0.80:
            self.enemy = Enemies.PhantomGina()
            self.alive_text = """
            **************************************
            Oh No! Gina has become a loust soul!!!
            **************************************
            """
            self.dead_text = """
            ************************************************************
            The spirit of Gina floats away, she smiles as she fades away
            ************************************************************
            """
        elif r < 0.95:
            self.enemy = Enemies.AbelColony()
            self.alive_text = """
            *************************************************************************************
            You hear a squeaking noise growing louder...suddenly you are surrounded of gouls!
            *************************************************************************************
                              """
            self.dead_text = """
            *************************************************
            Dozens of dead Abels are scattered on the ground.
            ************************************************"""
        else:
            self.enemy = Enemies.DustinZombie()
            self.alive_text = """
            *******************************************************
            Suddenly, a huge green giant blocks your path! Dustin??
            *******************************************************
                              """
            self.dead_text = """
            *************************************************************
            Defeated, your old friend lies at your feet. Rest well Dustin
            *************************************************************
                             """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    #allows players player base stats to be manipulated
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("""
            **********************************************
            Enemy does {} damage. You have {} HP remaining.
            **********************************************
            """.
                  format(self.enemy.damage, player.hp))

# class PracticeTile(MapTile):
#     def intro_text(self):
#         return """
#         This is to see if all this works.
#         """


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        **********************************************************************
        You've reached the main doors, Chad lies in agony on the floor...
        ... You give him a sensu bean, and he unlocks the main doors for you!
        Congrats!! Victory is yours!!
        **********************************************************************
        """

#random tile to grant player additional health
class ChargeTile(MapTile):
    def __init__(self, x, y):
        self.hp = random.randint(1, 50)
        self.health_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.health_claimed:
            self.health_claimed = True
            player.hp = player.hp + self.hp
            print("+{} health added.".format(self.hp))

    def intro_text(self):
        if self.health_claimed:
            return """
            **************************************************************
            The room vibrates with your aurua, but there is nothing here.
            You must forge onward....
            **************************************************************
            """
        else:
            return """
            *****************************************************************************
            You remember your Sayain Spirit!
            You charge your Ki, and let your screams send tingles down your enemies spines.                                                   
                                           ██                                  
                                           ██                            
                                    ██    ████                      
                                    ██    ██████                            
                                    ▓▓    ▓▓██  ██████    ▓▓                      
                                    ██    ████  ████████                 
                                        ████████████████  ██                  
                                        ██████████▓▓████  ██                
                                  ▓▓  ████████▓▓▓▓████▓▓██▓▓              
                                  ████▓▓██▓▓██▓▓▓▓██████████              
                                  ██████▓▓▓▓▓▓▓▓▓▓▓▓████████                
                                  ██████▓▓▓▓▓▓▓▓  ▓▓▓▓██████                
                                    ████▓▓▓▓▓▓    ▓▓▓▓▓▓████                  
                                      ████▓▓        ▓▓▓▓████                  
                                      ████▓▓▓▓      ▓▓████                      
                                        ░░  ░░      ░░  ░░       
            ******************************************************************************
            """


class BreatheTile(MapTile):
    def intro_text(self):
        return """
        *********************************************************
        You meditate, for the road before you lingers with Danger
        *********************************************************
        """
#domain specific languages. ("creating your own lane in Python")
#use dsl to define map, then python to interpret dsl and then turn into world_map variable
world_dsl = """
|EN|EN|VT|EN|EN|
|EN|  |  |  |EN|
|EN|FG|EN|  |BT|
|BT|  |ST|FG|EN|
|FG|  |EN|  |FG|
"""
#each new line of the string is a row, each row is seperated by a |
#if there is no tile, there are two pipes next to each other
#counts number of occurrences of substring in string
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines() #breaks apart multiline string and returns list of lines.
    lines = [l for l in lines if l]#list of comprehension to filter empty lines/ if l short for if l!=".
    pipe_counts = [line.count("|") for line in lines] #LOC to count number of pipes/check each row is the same
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True
#maps dsl abbreviations to tile types
tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": ChargeTile,
                  "BT": BreatheTile,
                  "  ": None}


world_map = []

start_tile_location = None

#parse dsl. 
def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
    
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]#line by line
    
    #iterate over dsl
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|") #splt line into abbreviations
        dsl_cells = [c for c in dsl_cells if c]#cell by cell
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]#look up abbreviation in dictionary
            if tile_type == StartTile:
                global start_tile_location #global variable
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)#f dict returned valid, create tile and pass x-y

        world_map.append(row)

#locates tile at a coordinate
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x] #world_map[y] selects the row of the map, [x] selects the cell in that row
    except IndexError: # will handle coords being greater than my map...like outofbounds
        return None
