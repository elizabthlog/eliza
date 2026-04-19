try:
    message = input("Enter a short note/message: ")
    
    file = open("notes.txt", "w")  
    file.write(message + "\n")
    file.close()

    print("\nMessage saved successfully!")

except Exception as e:
    print("Error while writing to file:", e)



try:
    file = open("notes.txt", "r")  
    print("\nContent of the file:")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found!")


try:
    new_note = input("\nEnter another note: ")
    
    file = open("notes.txt", "a") 
    file.write(new_note + "\n")
    file.close()

    file = open("notes.txt", "r")
    print("\nUpdated content:")
    print(file.read())
    file.close()

except Exception as e:
    print("Error while appending:", e)