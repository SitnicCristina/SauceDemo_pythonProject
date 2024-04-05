#!/bin/bash

#Run scenarios using behave and save the data in json file
behave /Users/cristina.sitnic/PycharmProjects/SauceDemo_pythonProject/features/saucedemo.feature -f json -o ./jsonLibrary/behaveResults.json