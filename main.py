# Imported modules that would help me with web scraping to get the images url and show the image
# Found this on stackoverflow after trying multiple times
from PIL import Image
import requests
from io import BytesIO
import random  # Think we all know what this does

# made a dictionary of the countries ill be using, I named the countries in keys all lower case for a reason you'll see
# later below.
countries = {
    "turkey": "https://tolerance-homes.com/storage/images/pages/qP0fv1mqZpQwoJDnLJSeaxis4WhOye64LrbNaPet.jpeg",
    "mexico": "https://cdn.britannica.com/73/2573-004-29818847/Flag-Mexico.jpg",
    "albania": "https://cdn.britannica.com/00/6200-004-42B7690E/Flag-Albania.jpg",
    "japan": "https://cdn.vox-cdn.com/uploads/chorus_asset/file/8935439/1_T9y2zj-bx2ugH7b6BjAJQQ.0.jpeg",
    "barbados": "https://cdn.vox-cdn.com/uploads/chorus_asset/file/8935451/1_7mr-X-_9PnLWkZZ0lzZH6w.0.jpeg",
    "montenegro": "https://cdn.vox-cdn.com/uploads/chorus_asset/file/8935461/1_VQAJa4odNHfOuugIH9kxxQ.0.jpeg",
    "argentina": "https://cdn.britannica.com/69/5869-004-7D75CD05/Flag-Argentina.jpg",
    "algeria": "https://cdn.britannica.com/34/3034-004-1A765B57/Flag-Algeria.jpg",
    "morocco": "https://cdn.britannica.com/39/3039-004-52B064C7/Flag-Morocco.jpg",
    "uruguay": "https://cdn.britannica.com/74/4874-004-50846A53/Flag-Uruguay.jpg",
    "qatar": "https://cdn.britannica.com/76/5776-004-54A070FA/Flag-Qatar.jpg",
    "bahrain": "https://cdn.britannica.com/67/5767-004-E0FF7201/Flag-Bahrain.jpg",
    "kazakhstan": "https://cdn.britannica.com/39/7239-004-1BEC6C20/Flag-Kazakhstan.jpg",
    "latvia": "https://cdn.britannica.com/49/6249-004-D8906A92/Flag-Latvia.jpg",
    "austria": "https://cdn.britannica.com/73/6073-004-B0B9EBEE/Flag-Austria.jpg",
    "bhutan": "https://cdn.britannica.com/79/6479-004-BDDD1FE1/flag-dragon-image-Bhutan-design.jpg",
    "colombia": "https://cdn.britannica.com/68/7668-004-08492AB7/Flag-Colombia.jpg",
    "venezuela": "https://cdn.britannica.com/04/4904-004-EBEFDE35/Flag-Venezuela.jpg",
    "australia": "https://cdn.britannica.com/78/6078-004-77AF7322/Flag-Australia.jpg",
    "new zealand": "https://cdn.britannica.com/17/3017-004-DCC13F9D/Flag-New-Zealand.jpg"
}


random_country = random.choice(list(countries.keys()))  # Gets a random country, y using keys(), you obtain a sequence,
# we convert the keys into a list, which can then be used as a sequence for random selection.
# By using keys(), you obtain a sequence of country codes. Randomly selecting a country code allows you to easily,
# access the corresponding URL from the dictionary using.


def get_image():  # Get image function I got from modules that I found in stackoverflow
    response = requests.get(random_country)  # Uses the random country variable
    img = Image.open(BytesIO(response.content))
    img.show()


def show_image(used_countries):  # Show image function with parameter uses_countries because I realized that the same,
    global random_country        # image was showing up more than once and that's not what I wanted.

    new_country = random.choice(list(countries.keys()))  # In order to get a new country I couldn't use the same var,
    while new_country in used_countries:                 # random_country that was already used before, so using a new,
        new_country = random.choice(list(countries.keys()))  # new_country in the function reassures me of a new flag.
#  In the while loop ^ it checks if the new country is already in used countries then the call the random.choice again.
    random_country = countries[new_country]  # Random country = a random.choice country that was assign to new country,
    get_image()                              # that gets random image from dic countries.
    used_countries.append(new_country)       # We append that random country to used countries, so it won't show again.


key_random_country = None  # Realized that in order to check the input of the user I had to get the key which is the
# name of the flag and compare to the user's input. Which we will see down below in a function to check the answer.


def check_answer(lives, correct_answer):  # Check answer function to check user's input with two parameter to keep track
    global key_random_country             # of the user's lives and answers he got correct.

    for key, value in countries.items():  # For loop that will iterate over both keys and values.
        if value == random_country:       # If value is equal to random country,
            key_random_country = key      # then we assign that key from that value to key_random_country, so that way
            break                         # we can use it to check users input.

    print(f"You have {lives} lives left, {correct_answer} Correct answers.")  # Shows users he lives and correct answers
    guess_input = input("Guess the country of this flag: ").lower()  # Used lower to avoid any uppercase or lowercase,
# problems which why I made the keys starting letter all lower.
    if guess_input == key_random_country:  # Checks the users input with the random key we got above in the for loop.
        print("Correct answer!")
        correct_answer += 1  # Add/Assign 1 to correct answers which its default was at 0
    else:
        print("Wrong answer")
        lives -= 1  # Subtract/Assign 1 to lives which default was 3

    return lives, correct_answer  # Pass these variables as arguments and return their updated values from the function


continue_playing = True  # If user wants to continue to play
play = input("Play? Press ENTER or type 'No': ").lower()
if play == 'no':
    continue_playing = False  # If user types no then continue playing i False and while won't run
# All these three variables down below are defaults we talked about above
lives_left = 3
correct_answers = 0
countries_used = []

while continue_playing:
    show_image(countries_used)
    lives_left, correct_answers = check_answer(lives_left, correct_answers)

    if lives_left == 0:  # If lives == 0 then game is over and user lost,
        print("Game Over! You lost")
        continue_playing = False

    if correct_answers == 3:  # If he got three right then he won and game ends.
        print("You Won!")
        continue_playing = False
