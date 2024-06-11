import sqlite3

class Maintenance:
    def __init__(self, car_vin, maintenance_type, description, date_performed):
        self.car_vin = car_vin
        self.maintenance_type = maintenance_type
        self.description = description
        self.date_performed = date_performed

    def save(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        
        # Fetch the existing record to compare
        cursor.execute("SELECT * FROM maintenance WHERE car_vin=?", (self.car_vin,))
        existing_record = cursor.fetchone()
        
        # Compare fields to decide between INSERT or UPDATE
        if existing_record and existing_record[1] == self.maintenance_type and existing_record[2] == self.description and existing_record[3] == self.date_performed:
            # No changes detected, do nothing
            pass
        elif existing_record:
            # Update existing record
            cursor.execute("""
                UPDATE maintenance SET maintenance_type=?, description=?, date_performed=?
                WHERE car_vin=?
            """, (self.maintenance_type, self.description, self.date_performed, self.car_vin))
        else:
            # Insert new record
            cursor.execute("""
                INSERT INTO maintenance (car_vin, maintenance_type, description, date_performed)
                VALUES (?,?,?,?)
            """, (self.car_vin, self.maintenance_type, self.description, self.date_performed))
        
        conn.commit()
        conn.close()
    @classmethod
    def get_all(cls):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM maintenance")
        maintenances = cursor.fetchall()
        conn.close()
        return maintenances

    @classmethod
    def find_by_id(cls, car_vin):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM maintenance WHERE car_vin=?", (car_vin,))
        maintenance_tuple = cursor.fetchone()
        conn.close()
        if maintenance_tuple:
            return cls(*maintenance_tuple[1:])
        else:
            return None

    def delete(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM maintenance WHERE car_vin=?", (self.car_vin,))
        conn.commit()
        conn.close()
