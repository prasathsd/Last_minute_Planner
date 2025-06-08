import requests
import openai
import time
import os

# Set your OpenAI API key here
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_weather(city: str) -> str:
    """Fetch weather information for a city using wttr.in"""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3", timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")
        return "Weather information unavailable"

def ask_gpt(prompt: str, model="gpt-4") -> str:
    """Query OpenAI GPT-4 with a prompt and return the response"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error querying GPT: {e}")
        return "Unable to get response from GPT"

def save_to_file(tours, filename="foodie_tours.txt"):
    """Save the generated tours to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        for tour in tours:
            f.write(f"\n{'='*50}\n")
            f.write(f"FOODIE TOUR: {tour['city']}\n")
            f.write(f"{'='*50}\n\n")
            f.write(f"Weather: {tour['weather']}\n")
            f.write(f"Dining Recommendation: {tour['dining_type']}\n")
            f.write(f"Iconic Dishes:\n")
            for dish in tour['dishes']:
                f.write(f"- {dish}\n")
            f.write(f"\nItinerary:\n{tour['itinerary']}\n")

def main():
    print("Welcome to the Foodie Day Tour Generator!\n")
    cities_input = input("Enter cities (comma-separated): ")
    cities = [city.strip() for city in cities_input.split(",") if city.strip()]

    tours = []
    for city in cities:
        print(f"\nGenerating tour for {city}...")
        weather = get_weather(city)
        print(f"Weather: {weather}")

        dining_prompt = (
            f"Given the current weather in {city}: {weather}\n"
            "Should we recommend indoor or outdoor dining today? Provide a brief explanation."
        )
        dining_type = ask_gpt(dining_prompt)
        print(f"Dining recommendation: {dining_type}")

        dishes_prompt = (
            f"What are 3 iconic dishes from {city}? "
            "List them in a simple format like:\n1. Dish name\n2. Dish name\n3. Dish name"
        )
        dishes_response = ask_gpt(dishes_prompt)
        dishes = [line.split('.', 1)[-1].strip() for line in dishes_response.split('\n') if line.strip() and line[0].isdigit()]
        print(f"Iconic dishes: {', '.join(dishes)}")

        itinerary_prompt = (
            f"Create a fun, narrative-style foodie itinerary for {city} including:\n"
            f"- Breakfast, lunch, and dinner recommendations using these iconic dishes:\n" +
            "\n".join([f"- {dish}" for dish in dishes]) + "\n"
            f"- The dining should be {dining_type}\n"
            "- Include cultural context and interesting facts\n"
            "- Format it as a story-like experience"
        )
        itinerary = ask_gpt(itinerary_prompt)
        print(f"\nItinerary:\n{itinerary}\n")

        tours.append({
            "city": city,
            "weather": weather,
            "dining_type": dining_type,
            "dishes": dishes,
            "itinerary": itinerary
        })
        time.sleep(1)  # Avoid rate limits

    save_to_file(tours)
    print("\nAll tours have been saved to 'foodie_tours.txt'.")

if __name__ == "__main__":
    main()
