import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    
    for game_obj in json_data:
        game = test_data.Game()
        game.platform = test_data.Platform()
        game.platform.launch_year = game_obj['platform']['launch year']
        game.platform.name = game_obj['platform']['name']
        game.title = game_obj['title']
        game.year = game_obj['year']
        game_library.add_game(game)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###

#Open the file specified by input_json_file
#Use the json module to load the data from the file
with open(input_json_file, 'r') as file:
    json_data = json.load(file)
    print(json_data)
    # Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
    game_library = make_game_library_from_json(json_data)
    print(game_library)

### End Add Code Here ###
