#!/bin/bash

#Run scenarios using behave and save the data in json file
behave ./features/saucedemo.feature -f json -o ./jsonLibrary/behaveResults.json

#run the streamlit app to read data from json and display fancy
streamlit run ./main/app.py