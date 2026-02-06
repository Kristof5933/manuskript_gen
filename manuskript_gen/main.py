#!/usr/bin/env python
# --!-- coding: utf8 --!--

from prompt_toolkit.shortcuts import radiolist_dialog
from util.fakeService import FakeService
from util.references import References
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

    references = References()
    FakeService(references, locale="en_US")
    manuskript = Manuskript("../output", profileName)
    manuskript.save()

def run():
    ConfigLoader("../config.json")

    choice = menu()

    if choice is None or choice == "quit":
        print("Goodbye!")
    else:
        generateNovel(choice)
