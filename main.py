from meteor_data_class import MeteorDataEntry

def convert_to_float(value, default=0.0):
    """Helper function to convert a string to float, returning default if conversion fails."""
    try:
        return float(value)
    except ValueError:
        return default

def process_meteor_data(file_path):
    """Reads and processes meteorite landing data from a text file."""
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            # Split the line into fields
            new_list = line.split('\t')

            # Ensure the list has exactly 12 elements, padding with empty strings if necessary
            new_list += [""] * (12 - len(new_list))

            # Convert necessary fields to float safely
            new_list[4] = convert_to_float(new_list[4])  # Mass
            new_list[6] = convert_to_float(new_list[6])  # Year

            # Filter meteorites based on mass or year
            if new_list[4] > 2_900_000 or new_list[6] >= 2013:
                meteor_entry = MeteorDataEntry(*new_list)
                print(meteor_entry)  # Print meteorite information

if __name__ == '__main__':
    process_meteor_data("meteorite_landings_data.txt")
