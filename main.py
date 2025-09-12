from utils import recognize_voice_in_tamil, classify_image, estimate_co2_saved
from recommender import get_recommendations
from map_generator import show_nearby_ngos


def main():
    print("Welcome to AgroWaste Reuse Recommendation System")

    choice = input("Enter '1' for Image Input or '2' for Voice Input in Tamil: ")

    if choice == '1':
        image_path = 'images/3.jpg'
        waste_type = classify_image(image_path)
    elif choice == '2':
        waste_type = recognize_voice_in_tamil()
    else:
        print("Invalid choice")
        return

    print(f"Identified Agro-Waste Type: {waste_type}")

    suggestions = get_recommendations(waste_type)
    print("\nRecommended Reuse Methods:")
    for s in suggestions:
        print(f"- {s}")

    co2_saved = estimate_co2_saved(waste_type)
    print(f"\nEstimated CO₂ Emissions Saved: {co2_saved} kg")

    print("\nDisplaying nearby NGOs...")
    show_nearby_ngos(waste_type)


if __name__ == "__main__":
    main()
