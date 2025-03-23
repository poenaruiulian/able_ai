import streamlit as st
import json
from streamlit_js_eval import streamlit_js_eval

def get_geolocation():
    # This JavaScript code returns a promise that resolves with the geolocation data.
    js_code = """
    new Promise((resolve, reject) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    resolve({
                        lat: position.coords.latitude,
                        lon: position.coords.longitude
                    });
                },
                (error) => {
                    reject('Error getting geolocation: ' + error.message);
                }
            );
        } else {
            reject('Geolocation is not supported by this browser.');
        }
    });
    """

    # Run the JavaScript and capture the result.
    try:
        geolocation_data = streamlit_js_eval(js_expressions=js_code)
        # Display the JSON data in the app
        return geolocation_data
    except Exception as e:
        st.error(f"An error occurred: {e}")
