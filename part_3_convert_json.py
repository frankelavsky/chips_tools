import cc_dat_utils
import cc_classes
import json

def make_chip_levels_from_json( json_data ):
    # Convert JSON data to CCLevelPack
    game_data = cc_classes.CCLevelPack()

    for level_data in json_data:
        # Initialize a new level
        game_level = cc_classes.CCLevel()

        # add basic data
        game_level.level_number = level_data["Number"]
        game_level.num_chips = level_data["Chip Count"]
        game_level.time = level_data["Time Limit"]
        game_level.lower_layer = [0] * 1024
        
        # convert our list of lists of ints into a long list of ints
        game_level.upper_layer = []
        for slice in level_data["Upper Layer"]:
            for cell in slice:
                game_level.upper_layer.append(cell)

        # loop over our fields, map those to proper field classes before adding to game level
        for field_data in level_data["Fields"]:
            # not sure if we need to initialize this here or not, like this?
            # field = cc_classes.CCField()

            # check each human-readable field, convert into proper class
            # note: the classes seem to already create their "type" (assign the number they need)
            if (field_data["type"] == "title"): 
                field = cc_classes.CCMapTitleField(field_data["value"])
            elif (field_data["type"] == "password"):
                field = cc_classes.CCEncodedPasswordField(field_data["value"])
            elif (field_data["type"] == "hint"): 
                field = cc_classes.CCMapHintField(field_data["value"])
            elif (field_data["type"] == "monsters"): 
                coordinates = []
                for coord_data in field_data["value"]:
                    coord = cc_classes.CCCoordinate(coord_data[0],coord_data[1])
                    coordinates.append(coord)
                field = cc_classes.CCMonsterMovementField(coordinates)

            # add field!
            game_level.add_field(field)

        # add level!
        game_data.add_level(game_level)

    # done!
    return game_data

#Part 3
#Load your custom JSON file
input_json_file = "data/fje_cc1.json"

with open(input_json_file, 'r') as file:
    json_data = json.load(file)
    print(json_data)
    # Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
    game_data = make_chip_levels_from_json(json_data)
    # Save converted data to DAT file
    print(game_data.__str__())
    cc_dat_utils.write_cc_level_pack_to_dat(game_data, "data/fje_cc1.dat")


