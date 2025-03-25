import requests
# BeautifulSoup is used to parse/examine the HTML content
from bs4 import BeautifulSoup


 
url = "https://poki.com/"
filename = "games.txt"


def get_games():
    response = requests.get(url)
    # Code 200 means OK, we can consider anything else an error for this project
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Game titles and categories are saved in the <span> tag We will get a list of tags
        game_titles = soup.find_all("span")
        # Temp list to hold our game titles and categories
        cleaned_games = []
        for game in game_titles:
            # Getting the Text inside the <Span> tag which is the game titles and categories
            game = game.text.strip()
            # Since parsing by a tag is broad we will check for any blank items in the list
            if game != '':
                cleaned_games.append(game)
               
        return cleaned_games
    else:
        print("Request Failed")
        return []
    
# Saving the games to a file 
def save_games(games):
    with open(filename,"w") as file:
        for game in games:
            file.write(f"{game}\n")
            # file.write(game + "\n")
    

def load_games():
    # When the script is ran for the first time we will get an error
    try:
        with open(filename,'r') as file:
            games = []
            for line in file:
                # We added a new line with each title and need to remove it
                games.append(line.strip())
            return games
    except FileNotFoundError:
        print("First Run")
        return []
    

def check_games(old, current):
    new = []
    for game in current:
        if game not in old:
            new.append(game)
    return new
        
            
def run():
    current_games = get_games()
    old_games = load_games()
    
    new_games = check_games(old_games,current_games)
    # Show the new game if there are any using "-" as a bullet point
    if new_games:
        print("New games found:")
        for g in new_games:
            print("-",g)
    else:
        print("No new games found.")

run()