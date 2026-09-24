"""A JSON file-based database."""

import json

def database_manager( command:str, database_file:str="C:/Users/harithvarakesan.bs/Documents/assignments/pythonTIPS/Assignment4/database.json"):
    """Accepts a command (CREATE, READ, UPDATE, DELETE) and performs the corresponding operation on a JSON file database."""
    with open(database_file, "r", encoding="utf-8") as file:
        records = json.load(file)
        command = command.upper()
        if command=="CREATE":
            name = input("Enter the name for the new record: ")
            new_data = {"id": len(records) + 1, "name": name}
            records.append(new_data)
            print(f"Database created successfully.")
        elif command=="READ":
            for record in records:
                print(record)
            print(f"Database read successfully.")
        elif command=="UPDATE":
            update_id = int(input("Enter the ID of the record to update: "))
            for record in records:
                if record["id"] == update_id:
                    updated_name = input("Enter the new name: ")
                    record["name"] = updated_name
            print(f"Database updated successfully.")
        elif command=="DELETE":
            delete_id = int(input("Enter the ID of the record to delete: "))
            records = [record for record in records if record["id"] != delete_id]
            print(f"Data deleted successfully from the database.")
        else:
            print("Invalid command. Please use CREATE, READ, UPDATE, or DELETE.")
            return
        json.dump(records, open(database_file, "w", encoding="utf-8"), indent=4)
        return

if __name__ == "__main__":
    entered_command = input("Enter a command (CREATE, READ, UPDATE, DELETE): ")
    database_manager(entered_command)