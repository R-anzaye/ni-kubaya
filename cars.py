import sqlite3

class Car:
    def __init__(self, vin, make, model, year):
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year

    
    def save(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()

        # Check if the car already exists by its VIN
        cursor.execute("SELECT * FROM cars WHERE vin=?", (self.vin,))
        existing_car = cursor.fetchone()

        if existing_car:
            # Car exists, so update it
            cursor.execute("""
                UPDATE cars SET make=?, model=?, year=? WHERE vin=?
            """, (self.make, self.model, self.year, self.vin))
        else:
            # Car does not exist, so insert it
            cursor.execute("""
                INSERT INTO cars (make, model, year, vin) VALUES (?,?,?,?)
            """, (self.make, self.model, self.year, self.vin))

        conn.commit()
        conn.close()
        
    @staticmethod
    def get_all():
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars")
        cars = cursor.fetchall()
        conn.close()
        return cars

    @staticmethod
    def find_by_make(make):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE make=?", (make,))
        cars = cursor.fetchall()
        conn.close()
        return cars


    @classmethod
    def find_by_id(cls, vin):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE vin=?", (vin,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return cls(*result)  
        else:
            return None


    def delete(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cars WHERE vin=?", (self.vin,))
        conn.commit()
        conn.close()