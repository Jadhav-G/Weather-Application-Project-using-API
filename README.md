Python Weather App

A simple desktop weather application built with Python's Tkinter library. It allows users to search for a city and get real-time weather information, including temperature, humidity, wind speed, and more. The application fetches data from the [OpenWeatherMap API](https://openweathermap.org/api).
     
          
        ![Image Alt](https://github.com/Jadhav-G/Weather-Application-Project-using-API/blob/e8ba98199c12fa9c6d389f6144d1c6717e0f56bc/Screenshot%202025-09-27%20200540.png)


 Features

  - Real-time Weather Data**: Get up-to-date weather information for any city in the world.
  - Search by City**: Simply type the name of a city and press the search button.
  - Detailed Information**: Displays key weather metrics:
      - Temperature (°C)
      - Humidity (%)
      - Pressure (hPa)
      - Wind Speed (m/s)
      - Weather description (e.g., "clear sky", "light rain").
  - Dynamic Icons**: The weather icon changes based on the current weather conditions.
  - Geolocation and Time**: Automatically detects and displays the local time, timezone, and geographical coordinates (latitude & longitude) of the searched city.
  - User-Friendly Interface**: A clean and intuitive graphical user interface (GUI) built with Tkinter.

-----

 Prerequisites

Before you begin, ensure you have the following installed on your system:

  * Python 3.x
  * pip (Python package installer)

-----

Setup and Installation

Follow these steps to get the application running on your local machine.

1. Clone the Repository**

```bash
git clone https://github.com/your-username/python-weather-app.git
cd python-weather-app
```

(If you are not using Git, you can simply download and extract the project files into a folder.)*

2. Create a `requirements.txt` file**
Create a file named `requirements.txt` in the project directory and add the following lines to it:

```
requests
geopy
timezonefinder
pytz
Pillow
```

3. Install Dependencies**
Open your terminal or command prompt in the project directory and run the following command to install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

4. Get an OpenWeatherMap API Key**
This application requires an API key from OpenWeatherMap to fetch weather data.

  - Go to the [OpenWeatherMap website](https://openweathermap.org/appid) and sign up for a free account.

  - After signing up, navigate to the "API keys" tab to find your default key.

  - Open the `weather.py` file and replace the placeholder API key with your own key.

    ```python
    Find this line in the getweather() function
    APIkey = "e700edd09e614b165ff236ec367ec86f" # <--- REPLACE THIS WITH YOUR KEY
    ```

5. Set Up Asset Folders**
The application requires specific images and icons to display correctly. Make sure you have the following folders and files in your project directory:

   A folder named `images/` containing:
      * `logo.png`
      * `Rounded Rectangle 1.png`
      * `Rounded Rectangle 2.png`
      * `Rounded Rectangle 2 copy.png`
      * `Rounded Rectangle 3.png`
      * `Layer 6.png`
      * `Layer 7.png`
   A folder named `icon/` containing the weather icon files (e.g., `01d@2x.png`, `02n@2x.png`, etc.). You can download these icons from the [OpenWeatherMap icon list](https://openweathermap.org/weather-conditions).

-----

How to Run

Once you have completed the setup, you can run the application with the following command from the project directory:

```bash
python weather.py
```

Enter a city name in the search box and click the search icon to get the weather details.

-----

Code Overview

  - weather.py: This is the main script that contains all the application logic.
      - Imports: Imports necessary libraries like `Tkinter` for the GUI, `requests` for API calls, `geopy` for coordinates, `timezonefinder` and `pytz` for time management, and `Pillow` for image handling.
      - `getweather()` function: This is the core function of the app.
        1.  It takes the city name from the input field.
        2.  Uses `geopy` to get the latitude and longitude of the city.
        3.  Uses `timezonefinder` to determine the local timezone.
        4.  Makes an API call to OpenWeatherMap using the coordinates.
        5.  Parses the JSON response to extract temperature, humidity, pressure, wind, and description.
        6.  Updates the Tkinter labels in the GUI to display the fetched data and the correct weather icon.
      - GUI Setup: The rest of the script is dedicated to building the application's window, frames, labels, buttons, and input fields using Tkinter.
   



