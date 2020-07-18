from dotenv import load_dotenv
import os

load_dotenv()


def load_bot_token():
    return os.getenv("DISCORD_TOKEN")


def load_db_password():
    return os.getenv("POSTGRESQL_PASSWORD")


def load_db_host():
    return os.getenv("POSTGRESQL_HOST")


def load_db_port():
    return os.getenv("POSTGRESQL_PORT")


def load_openweather_token():
    return os.getenv("OPENWEATHER_TOKEN")


def load_topgg_token():
    return os.getenv("TOPGG_TOKEN")
