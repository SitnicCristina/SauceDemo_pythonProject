import streamlit as st
import json


def main():
    # Load JSON data
    with open("/Users/cristina.sitnic/PycharmProjects/SauceDemo_pythonProject/jsonLibrary/behaveResults.json", "r") as f:
        json_data = json.load(f)

    # Display the JSON data
    st.title("Fancy JSON Data Viewer")

    for scenario in json_data:
        st.subheader(f"Feature: {scenario['name']}")
        st.write(f"Status: {scenario['status']}")

        for step in scenario['elements']:
            st.subheader(f"Scenario: {step['name']}")
            st.write(f"Status: {step['status']}")
            st.write(f"Type: {step['type']}")
            st.write(f"Keyword: {step['keyword']}")


if __name__ == "__main__":
    main()
