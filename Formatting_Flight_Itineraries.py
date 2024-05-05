def format_itineraries(itineraries):
    formatted_itineraries = []
    for idx, itinerary in enumerate(itineraries, start=1):
        travelers_name, origin, destination = itinerary
        itinerary = f"Itinerary {idx}: {travelers_name} - From {origin} to {destination}"
        formatted_itineraries.append(itinerary)
    return '\n'.join(formatted_itineraries)


itineraries = [("Myron", "Texas", "Japan"), ("Daniela", "Texas", "South Korea")]
f_string = format_itineraries(itineraries)
print(f_string)

