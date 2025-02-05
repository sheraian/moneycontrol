import json


def split_json_file(file_name, num_files=6):
    # Load the JSON file
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Calculate chunk size
    chunk_size = len(data) // num_files

    # Split the data into chunks
    for i in range(num_files):
        start_index = i * chunk_size
        end_index = start_index + chunk_size if i < num_files - 1 else len(data)
        chunk = data[start_index:end_index]
        chunk_file_name = f'final_part_{i + 1}.json'

        # Save each chunk as a separate JSON file
        with open(chunk_file_name, 'w', encoding='utf-8') as chunk_file:
            json.dump(chunk, chunk_file, indent=4, ensure_ascii=False)

        print(f'Saved {chunk_file_name}')


# Run the function
split_json_file('final.json')