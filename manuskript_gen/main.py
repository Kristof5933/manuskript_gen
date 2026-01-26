# -*- coding: utf-8 -*-

from prompt_toolkit.shortcuts import radiolist_dialog
from config import ConfigLoader, Config
from util import FakeService
from data import Characters

def menu():
    profiles = ConfigLoader().listAvailableConfigurations()

    result = radiolist_dialog(
        title="Manuskript generator",
        text="Select an option:",
        values=profiles
    ).run()

    return result

def generateNovel(profileName: str):
    print(f"Generating novel for the profile {profileName}")

    config: Config = ConfigLoader().loadConfig(profileName)

    print(config)

    characters = Characters(config)
    characters.debug()


def run():
    ConfigLoader("../config.json")

    choice = menu()

    if choice is None or choice == "quit":
        print("Goodbye!")
    else:
        FakeService(locale="en_US")
        generateNovel(choice)
