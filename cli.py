import sys
import sqlite3
from cars import Car
from maintenance import Maintenance
from comments import Comment

def list_cars():
    cars = Car.get_all()
    for car in cars:
        print(car)

def find_car_by_make():
    make = input("Enter the car's make: ")
    cars = Car.find_by_make(make)
    for car in cars:
        print(car) if car else print(f'Car with make {make} not found')

def find_car_by_vin():
    vin = input("Enter the car's VIN: ")
    conn = sqlite3.connect("car_management.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE vin=?", (vin,))
    car = cursor.fetchone()
    conn.close()
    print(car) if car else print(f'Car with VIN {vin} not found')

def create_car():
    make = input("Enter the car's make: ")
    model = input("Enter the car's model: ")
    year = int(input("Enter the car's year: "))
    vin = input("Enter the car's VIN: ")
    try:
        car = Car(make, model, year, vin)
        car.save()
        print(f'Success: {car}')
    except Exception as exc:
        print("Error creating car:", exc)

def update_car():
    vin = input("Enter the car's VIN: ")
    car = Car.find_by_id(vin)  # Correctly finds a car by VIN
    if car:
        make = input("Enter the car's new make: ")
        model = input("Enter the car's new model: ")
        year = int(input("Enter the car's new year: ")) 
        car.make = make
        car.model = model
        car.year = year
        car.save()
        print(f'Success: {car}')
    else:
        print(f'Car with VIN {vin} not found')
def delete_car():
    vin = input("Enter the car's VIN: ") 
    car = Car.find_by_id(vin)
    if car:
        car.delete()
        print(f'Car {vin} deleted') 
        print(f'Car with VIN {vin} not found')
def list_maintenances():
    maintenances = Maintenance.get_all()
    for maintenance in maintenances:
        print(maintenance)

def find_maintenance_by_id():
    id_ = input("Enter the maintenance's id: ")
    maintenance = Maintenance.find_by_id(id_)
    print(maintenance) if maintenance else print(f'Maintenance with id {id_} not found')

def create_maintenance():
    car_vin = input("Enter the car's VIN: ")  # Changed from car_id to car_vin based on the class initialization
    maintenance_type = input("Enter the maintenance type: ")
    description = input("Enter the maintenance description: ")
    date_performed = input("Enter the date performed: ")
    try:
        maintenance = Maintenance(car_vin, maintenance_type, description, date_performed)
        maintenance.save()
        print(f'Success: {maintenance}')
    except Exception as exc:
        print("Error creating maintenance:", exc)

def update_maintenance():
    car_vin = input("Enter the maintenance's VIN: ")
    maintenance_type = input("Enter the maintenance's new type: ")
    description = input("Enter the maintenance's new description: ")
    date_performed = input("Enter the maintenance's new date performed: ")
    try:
        maintenance = Maintenance(car_vin, maintenance_type, description, date_performed)
        maintenance.save()
        print(f'Success: {maintenance}')
    except Exception as exc:
        print("Error updating maintenance:", exc)

def delete_maintenance():
    car_vin = input("Enter the maintenance's VIN: ")
    maintenance = Maintenance.find_by_id(car_vin)
    if maintenance:
        maintenance.delete()
        print(f'Maintenance {car_vin} deleted')
    else:
        print(f'Maintenance with VIN {car_vin} not found')
def list_comments():
    comments = Comment.get_all()
    for comment in comments:
        print(comment)

def find_comment_by_id():
    id_ = input("Enter the comment's id: ")
    comment = Comment.find_by_id(id_)
    print(comment) if comment else print(f'Comment with id {id_} not found')

def create_comment():
    maintenance_id = input("Enter the maintenance's id: ")
    comment_text = input("Enter the comment: ")
    try:
        comment = Comment(maintenance_id, comment_text)
        comment.save()
        print(f'Success: {comment}')
    except Exception as exc:
        print("Error creating comment:", exc)

def update_comment():
    id_ = input("Enter the comment's id: ")
    comment = Comment.find_by_id(id_)
    if comment:
        new_comment_text = input("Enter the comment's new text: ")
        comment.update(new_comment=new_comment_text)
        print(f'Success: Updated comment with id {id_}')
    else:
        print(f'Comment with id {id_} not found')

def delete_comment():
    id_ = input("Enter the comment's id: ")
    comment = Comment.find_by_id(id_)
    if comment:
        comment.delete()
        print(f'Comment {id_} deleted')
    else:
        print(f'Comment with id {id_} not found')
def main():
    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. List all cars")
        print("2. Find car by make")
        print("3. Find car by id")
        print("4. Create car")
        print("5. Update car")
        print("6. Delete car")
        print("7. List all maintenances")
        print("8. Find maintenance by id")
        print("9. Create maintenance")
        print("10. Update maintenance")
        print("11. Delete maintenance")
        print("12. List all comments")
        print("13. Find comment by id")
        print("14. Create comment")
        print("15. Update comment")
        print("16. Delete comment")
        
        choice = input("> ")

        if choice == "0":
            print("Goodbye!")
            sys.exit()
        elif choice == "1":
            list_cars()
        elif choice == "2":
            find_car_by_make()
        elif choice == "3":
            find_car_by_vin()
        elif choice == "4":
            create_car()
        elif choice == "5":
            update_car()
        elif choice == "6":
            delete_car()
        elif choice == "7":
            list_maintenances()
        elif choice == "8":
            find_maintenance_by_id()
        elif choice == "9":
            create_maintenance()
        elif choice == "10":
            update_maintenance()
        elif choice == "11":
            delete_maintenance()
        elif choice == "12":
            list_comments()
        elif choice == "13":
            find_comment_by_id()
        elif choice == "14":
            create_comment()
        elif choice == "15":
            update_comment()
        elif choice == "16":
            delete_comment()
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
