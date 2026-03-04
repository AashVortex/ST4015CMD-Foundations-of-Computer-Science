import base64
import os

def encode_file(file_path):
    """Encode any file (text or image) to Base64."""
    with open(file_path, "rb") as f:
        encoded_data = base64.b64encode(f.read())
    return encoded_data.decode("utf-8")

def decode_file(encoded_string, output_path):
    """Decode Base64 string back to a file (binary safe)."""
    decoded_data = base64.b64decode(encoded_string)
    with open(output_path, "wb") as f:
        f.write(decoded_data)

def write_message(file_path, message):
    """Write a message to a text file (for text encoding example)."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(message)

def main():
    choice = input("Choose an option (encode/decode): ").lower()

    if choice == "encode":
        file_path = input("Enter the path of the file to encode (text/image): ")

        # If the user wants to write a message to a text file
        if not os.path.exists(file_path):
            message = "Hello, it's me Aashish Singh"
            write_message(file_path, message)
            print(f"Message written to {file_path}")

        encoded_string = encode_file(file_path)
        print("\nEncoded Base64 string:\n")
        print(encoded_string[:100] + "...")  # Print first 100 chars for brevity

        save = input("\nSave encoded string to a text file? (y/n): ").lower()
        if save == "y":
            output_file = input("Enter output filename (e.g., encoded.txt): ")
            with open(output_file, "w") as out_file:
                out_file.write(encoded_string)
            print(f"Encoded data saved to {output_file}")

    elif choice == "decode":
        encoded_file = input("Enter the path to the Base64 text file: ")
        with open(encoded_file, "r") as f:
            encoded_string = f.read()

        output_file = input("Enter output filename (text or image, e.g., output.txt or output.png): ")
        decode_file(encoded_string, output_file)
        print(f"File decoded and saved as {output_file}")

    else:
        print("Invalid choice! Please choose 'encode' or 'decode'.")

if __name__ == "__main__":
    main()