import requests
from datetime import datetime

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Please try again later.")
        return None


def get_weather_data_for_date(date):
    weather_data = get_weather_data()
    if not weather_data:
        return

    input_date = datetime.strptime(date, "%Y-%m-%d")
    closest_date_data = None
    min_time_difference = float('inf')

    for data in weather_data["list"]:
        data_date = datetime.strptime(data["dt_txt"], "%Y-%m-%d %H:%M:%S")
        time_difference = abs((data_date - input_date).total_seconds())
        if time_difference < min_time_difference:
            min_time_difference = time_difference
            closest_date_data = data

    if closest_date_data:
        return closest_date_data
    else:
        print("No weather data available for the specified date.")


def get_option():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    return input("Enter your choice: ")


def main():
    while True:
        option = get_option()

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            data = get_weather_data_for_date(date)
            if data:
                print(f"Temperature on {date}: {data['main']['temp']}°C")

        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            data = get_weather_data_for_date(date)
            if data:
                print(f"Wind Speed on {date}: {data['wind']['speed']} m/s")

        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            data = get_weather_data_for_date(date)
            if data:
                print(f"Pressure on {date}: {data['main']['pressure']} hPa")

        elif option == "0":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
