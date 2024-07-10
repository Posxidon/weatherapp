# WeatherApp

WeatherApp is a web application that provides current weather information for a given city. It utilizes the OpenWeatherMap API to fetch real-time weather data and displays it to the user.

## Technologies and Libraries Used

The following technologies and libraries are utilized in this project:

- Django: The web application is built using the Django framework, which provides a robust foundation for developing web applications.

- OpenWeatherMap API: The OpenWeatherMap API is used to retrieve weather data based on the user's input.

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/Posxidon/weatherapp.git

2. Install the required dependencies using pip:
pip install requests 

3. Obtain an API key from OpenWeatherMap by signing up at their website (https://openweathermap.org/) and generating an API key.

4. In the `weatherApp/views.py` file, replace `'YOUR_API_KEY'` with your actual API key.

5. Run the Django development server:
python manage.py runserver

6. Access the WeatherApp in your web browser at `http://localhost:8000`.

## Usage

- Enter the name of a city in the search field and click the "Search" button.

- The application will fetch the current weather information for the specified city and display it on the page.

- The weather information includes the temperature, pressure, humidity, and a brief description of the weather condition.

- You can search for weather information for different cities by entering their names in the search field.
