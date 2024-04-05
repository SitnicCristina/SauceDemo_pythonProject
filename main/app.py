import sys

import streamlit as st
import json
import subprocess


def main():
    # Load JSON data
    with open("./jsonLibrary/behaveResults.json", "r") as f:
        json_data = json.load(f)

    # Display the JSON data
    st.title("Fancy JSON Data Viewer")

    for scenario in json_data:
        st.subheader(f"Feature: :blue[{scenario['name']}]")
        st.write(f"Status: {scenario['status']}")

        for step in scenario['elements']:
            st.divider()
            st.subheader(f"Scenario: {step['name']}")

            if step['status'] == "passed":
                st.write(f"Status: :green[{step['status']}]")
            elif step['status'] == "failed":
                st.write(f"Status: :red[{step['status']}]")
            else:
                st.write(f"Status: :{step['status']}")

            st.write(f"Type: {step['type']}")
            st.write(f"Keyword: {step['keyword']}")

if __name__ == "__main__":

    # Display the Project Details
    st.title("Sauce Demo Automation testing.")
    st.write("Please click the button to start running the scenarios")

    button_run_scenarios = st.button("Run scenarios")
    if button_run_scenarios:
        p = subprocess.run([f"{sys.executable}", "./main/script.py"])
        main()
