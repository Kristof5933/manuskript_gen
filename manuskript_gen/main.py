#!/usr/bin/env python
# --!-- coding: utf8 --!--

from prompt_toolkit.shortcuts import radiolist_dialog
from util import FakeService
from data import Manuskript
from config import ConfigLoader

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

    manuskript = Manuskript("../output", profileName)
    manuskript.save()

def run():
    ConfigLoader("../config.json")

    choice = menu()

    if choice is None or choice == "quit":
        print("Goodbye!")
    else:
        FakeService(locale="en_US")
        generateNovel(choice)
