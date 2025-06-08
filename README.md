# Foodie Day Tour Generator

## Overview

This project is a Python script that creates a personalized, narrative-style foodie day tour for any city you choose.  
It combines **real-time weather data** and the power of **OpenAI's GPT-4** to recommend whether to eat indoors or outdoors, suggest iconic local dishes, and generate a breakfast-lunch-dinner itinerary with cultural context.

**Why?**  
Travelers and foodies often want a quick, fun way to plan a day of eating in a new city, tailored to the weather and local cuisine. This tool automates that process using AI!

---

## Features

- Fetches live weather for your chosen cities.
- Uses GPT-4 to:
  - Recommend indoor/outdoor dining based on weather.
  - Suggest 3 iconic local dishes.
  - Generate a full, story-like foodie itinerary.
- Saves all results to `foodie_tours.txt` for easy sharing.

---

## How It Works

1. **Weather Fetching:**  
   The script uses [wttr.in](https://wttr.in) to get a quick weather summary for each city.

2. **AI-Powered Planning:**  
   It sends prompts to OpenAI's GPT-4 to:
   - Decide if you should eat indoors or outdoors.
   - List 3 must-try dishes for the city.
   - Write a fun, narrative itinerary for breakfast, lunch, and dinner, including cultural context.

3. **Output:**  
   All results are printed to the console and saved to a text file.

---

## Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/prasathsd/Last_minute_Planner.git
   cd Last_minute_Planner
   ```

2. **Install dependencies:**
   ```bash
   pip install openai requests
   ```

3. **Set your OpenAI API key as an environment variable:**
   - **Windows (PowerShell):**
     ```powershell
     $env:OPENAI_API_KEY="sk-proj-yourkeyhere"
     ```
   - **Mac/Linux (bash):**
     ```bash
     export OPENAI_API_KEY=sk-proj-yourkeyhere
     ```

4. **Run the script:**
   ```bash
   python foodie_agent.py
   ```

---

## Usage

- When prompted, enter city names separated by commas (e.g., `Paris, Tokyo, Mumbai`).
- The script will fetch weather, ask GPT-4 for recommendations, and print/save the results.

---

## Example


==================================================
FOODIE TOUR: Shimla
==================================================

Weather: Shimla: ☀️   +28°C
Dining Recommendation: We should recommend outdoor dining today. The weather in Shimla is sunny and 28°C, which is quite pleasant and warm. This is a good temperature to enjoy a meal outside.
Iconic Dishes:
- Sidu
- Chha Gosht
- Babru

Itinerary:
Title: A Symphony of Flavors in Sunny Shimla

As the morning sun peeks over the majestic Himalayan range, illuminating the charming hill station of Shimla, the city softly stirs awake. The day's forecast predicts a warm and welcoming 28°C, perfect for an outdoor foodie adventure across the city...........
---

## Security

**Never commit your API key to the repository!**  
Always use environment variables to keep your key safe.  
If you accidentally commit your key, remove it from your code and git history before pushing.

---

## Customization

- Change the prompts in the script to get different styles of output.
- Save results in a different format by editing the `save_to_file` function.
- Add more features, such as real restaurant recommendations, by integrating other APIs.

---

## Troubleshooting

- **API errors:** Make sure your OpenAI API key is correct and has access to GPT-4.
- **Weather errors:** If weather info is missing, check your internet connection.
- **Rate limits:** The script waits 1 second between cities to avoid hitting API limits.
- **No output file?** Make sure you have write permissions in your folder.

---

## License

MIT License.  
You are free to use, modify, and share!

---

## Credits

- Weather data from [wttr.in](https://wttr.in)
- AI completions from [OpenAI](https://openai.com)

---

## Questions?

Open an issue on [GitHub](https://github.com/prasathsd/Last_minute_Planner) or contact the project maintainer.

---

Enjoy your foodie adventures! 🍽️🌍
