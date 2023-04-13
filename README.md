# Vacation Itinerary Generator

Vacation Itinerary Generator is a web application that utilizes the OpenAI API to create personalized vacation itineraries based on user preferences. Users can input their destination, number of days, and interests, and the application will generate a detailed vacation itinerary.

## Features

- Custom itineraries tailored to users' preferences
- Easy-to-use web interface
- Powered by OpenAI's advanced language model

## Installation

To set up the Vacation Itinerary Generator locally, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/jyannes/itineraryGenerator.git

2. Install the required Python packages:

pip install flask openai python-dotenv


3. Create a `.env` file in the project's root directory and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

To run the Vacation Itinerary Generator locally, follow these steps:

1. Start the Flask development server:

python app.py

2. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

3. Enter your desired destination, number of days, and interests, then click "Generate Itinerary" to create your personalized vacation itinerary.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.




