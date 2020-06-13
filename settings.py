#from dotenv import load_dotenv
import os

#load_dotenv()


def load_bot_token():
    return os.environ["DISCORD_TOKEN"]
    #return os.getenv("DISCORD_TOKEN")


def load_openweather_token():
    return os.environ["OPENWEATHER_TOKEN"]
    #return os.getenv("OPENWEATHER_TOKEN")


def load_googletranslate_token():
    return os.environ["GOOGLETRANSLATE_TOKEN"]
    #return os.getenv("GOOGLETRANSLATE_TOKEN")
