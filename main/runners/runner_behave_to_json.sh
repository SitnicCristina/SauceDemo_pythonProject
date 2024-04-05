#!/bin/bash

#Run scenarios using behave and save the data in json file
behave ./features/saucedemo.feature -f json -o ./jsonLibrary/behaveResults.json