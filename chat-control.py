from functions import *

# create chatbot
assistant_bot = create_bot('Rajiv')

# train all data
train_all_data(assistant_bot)

# check identity
identity = input("State your identity please: ")

# rules for responding to different identities
if identity == "Rajiv":
    print("Welcome, Rajiv. Happy to have you at home.")

else:
    print("Your access is denied here.")
    exit()

# custom data
weather_data = [
    "What is the weather like today?",
    "Weather is going to be cloudy with scattered showers"
]
custom_train(assistant_bot, weather_data)

house_owner = [
    "Who is the owner of this house?",
    "Rajiv Kumar is the owner of this house."
]
custom_train(assistant_bot, house_owner)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Rajiv
if identity == 'Rajiv':
    city_born = [
        "Where was I born?",
        "Rajiv, you were born in Seattle."
    ]
    custom_train(assistant_bot, city_born)

# start chatbot
start_chatbot(assistant_bot)
