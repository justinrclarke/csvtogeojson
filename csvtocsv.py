import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def write_csv(file_path, data, selected_columns):
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for row in data:
            new_row = [row[col] for col in selected_columns]
            csv_writer.writerow(new_row)

def select_columns(data):
    print("Available columns:")
    for index, column in enumerate(data[0]):
        print(f"{index}: {column}")
    
    selected_columns = input("Enter column numbers separated by commas (e.g., 0,2,3): ").strip().split(',')
    selected_columns = [int(col) for col in selected_columns]
    return selected_columns

def main():
    input_file = input("Enter the path to the input CSV file: ")
    output_file = input("Enter the path to the output CSV file: ")

    # Read the CSV file
    data = read_csv(input_file)

    # Select columns to keep
    selected_columns = select_columns(data)

    # Write the selected columns to a new CSV file
    write_csv(output_file, data, selected_columns)
    
    print("New CSV file created successfully.")

if __name__ == "__main__":
    main()
