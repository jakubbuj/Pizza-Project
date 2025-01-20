import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import random
import time
import threading

# Function to add registration
def add_registration(username, hashed_password, date):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM Registration WHERE username = %s", (username,))
        if cursor.fetchone():
            print("Error: Username already exists.")
            return False

        # Insert into Registration table (assuming it has username, password and birthdate columns)
        cursor.execute("""
            INSERT INTO Registration (username, passkey, birthdate)
            VALUES (%s, %s, %s)
        """, (username, hashed_password.decode('utf-8'), date))
        print('success')
        connection.commit()
        return True

    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to place an order
def place_order(customer_id, pizza_ids, drink_ids, dessert_ids, order_price, discount_id, zipcode):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        update_delivery_person_availability()

        # Get current date and time
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        deliverypersons = get_delivery_persons(zipcode)

        if not deliverypersons:
            print("No delivery persons available.")
            return None

        assign_delivery_person(deliverypersons[0]['id'])

        if discount_id == None:
            discount_id = 1  
        
        # Insert into Orders table
        cursor.execute("""
            INSERT INTO Orders (customer_id, date, time, order_price, discount_id, deliveryperson_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (customer_id, current_date, current_time, order_price, discount_id, deliverypersons[0]['id']))

        order_number = cursor.lastrowid

        print("Inserting SQL statements into Orders completed")

        # Insert into PizzaOrders, DrinkOrders, and DessertOrders tables
        for pizza_id, quantity in pizza_ids:
                cursor.execute("""
                    INSERT INTO PizzaOrders (pizza_id, order_number, quantity)
                    VALUES (%s, %s, %s)
                """, (pizza_id, order_number, quantity))

        print("Inserting SQL statements into Pizzaorders completed")

        # Always insert into DrinkOrders with a placeholder if no drinks are ordered
        if drink_ids:
            for drink_id in drink_ids:
                cursor.execute("""
                    INSERT INTO DrinkOrders (order_number, drink_id)
                    VALUES (%s, %s)
                """, (order_number, drink_id, ))
        else:
            # # Insert a placeholder if no drinks were ordered
            # cursor.execute("""
            #     INSERT INTO DrinkOrders (order_number, drink_id)
            #     VALUES (%s, NULL)
            # """, (order_number,))

            print("Inserting SQL statements into drinkorders completed")
        

        # Only insert into DessertOrders if there are desserts
        if dessert_ids:
            for dessert_id in dessert_ids:
                cursor.execute("""
                    INSERT INTO DessertOrders (order_number, dessert_id)
                    VALUES (%s, %s)
                """, (order_number, dessert_id, ))
        else:
            # # Insert a placeholder for dessert if none are ordered
            # cursor.execute("""
            #     INSERT INTO DessertOrders (order_number, dessert_id)
            #     VALUES (%s, NULL)
            # """, (order_number,))

            print("Inserting SQL statements into dessertsorders completed")
         
        
        connection.commit()

        print(f"Order {order_number} placed successfully")

        try:
            fill_order_confirmation(order_number, order_price, discount_id)
            print("Order confirmation filled successfully.")
        except Exception as e:
            print(f"Error while filling order confirmation: {e}")

        return order_number
    
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def assign_delivery_person(deliveryperson_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Set the delivery person to be unavailable for the next 15 minutes
        unavailable_until = datetime.now() + timedelta(minutes=30)

        update_query = """
        UPDATE DeliveryPerson 
        SET is_available = FALSE, unavailable_until = %s 
        WHERE deliveryperson_id = %s
        """
        cursor.execute(update_query, (unavailable_until, deliveryperson_id))
        connection.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_delivery_person_availability():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Set delivery persons to available if their unavailable_until time has passed
        update_query = """
        UPDATE deliveryperson 
        SET is_available = TRUE, unavailable_until = NULL 
        WHERE unavailable_until < NOW()
        """
        cursor.execute(update_query)
        connection.commit()
        # Log the number of rows affected (number of delivery persons updated)
        print(f"{cursor.rowcount} delivery person(s) availability updated.")

    except Error as e:
        print(f"Error while updating delivery person availability: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def fill_order_confirmation(order_number, order_price, discount_id):
    print("filling out order confirmation")

    """Fill in the order confirmation details."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Get current date and time
        current_date = datetime.now().date()
        current_time = datetime.now().time()    

        # Estimate time for order (this can be changed to your restaurant's logic)
        estimated_time = 30 #(now + datetime.timedelta(minutes=30)).time()  # Example: 30 minutes from now
        
        # Check if a discount was used
        discount_used = 1 if discount_id != 1 else 0

        # Insert order confirmation details into the table
        insert_confirmation_query = """
            INSERT INTO OrderConfirmation (order_number, date, time, order_price, estimate_time, discount_used)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_confirmation_query, (order_number, current_date, current_time, order_price, estimated_time, discount_used))
        connection.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_delivery_persons(zipcode):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Step 1: Check for unavailable delivery persons
        unavailable_query = """
        SELECT dp.deliveryperson_id, dp.name, dp.unavailable_until, COUNT(o.order_number) as active_orders
        FROM deliveryperson dp
        LEFT JOIN orders o 
        ON dp.deliveryperson_id = o.deliveryperson_id 
        AND o.date = CURDATE()  
        WHERE dp.zip_code = %s 
        AND dp.is_available = FALSE 
        GROUP BY dp.deliveryperson_id
        """
        
        cursor.execute(unavailable_query, (zipcode,))
        unavailable_delivery_persons = cursor.fetchall()

        now = datetime.now()
        assigned_persons = []

        # Step 2: Check unavailable persons
        for dp in unavailable_delivery_persons:
            unavailable_until = dp[2]
            active_orders = dp[3]

            # Check if they were assigned less than 3 minutes ago
            if unavailable_until and (now - unavailable_until).total_seconds() <= 180:
                # They can be assigned if they have fewer than 3 active orders
                if active_orders < 3:
                    assigned_persons.append({'id': dp[0], 'name': dp[1]})
                    print(f"Assigned recently busy delivery person: {dp[1]}")
                    return assigned_persons  # Return immediately upon finding an eligible person
            # If they have been unavailable for more than 3 minutes, skip them.

        # Step 3: If no suitable unavailable persons were found, check for available ones
        available_query = """
        SELECT dp.deliveryperson_id, dp.name, dp.unavailable_until, COUNT(o.order_number) as active_orders
        FROM deliveryperson dp
        LEFT JOIN orders o 
        ON dp.deliveryperson_id = o.deliveryperson_id 
        AND o.date = CURDATE()  
        WHERE dp.zip_code = %s 
        AND dp.is_available = TRUE 
        GROUP BY dp.deliveryperson_id
        HAVING COUNT(o.order_number) < 3
        """
        
        cursor.execute(available_query, (zipcode,))
        available_delivery_persons = cursor.fetchall()

        if available_delivery_persons:
            # If there are available delivery persons, return them
            delivery_person_list = [{'id': dp[0], 'name': dp[1]} for dp in available_delivery_persons]
            print("Available delivery person found.")
            return delivery_person_list

        # If no delivery persons available or recently busy, return None
        print(f"No delivery persons available or recently busy for zip code: {zipcode}")
        return None  

    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to update customer info
def update_customer_info(customer_id, name, phonenumber, streetname, streetnumber, zipcode, gender, birthdate):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Customer_Info
            SET name=%s, phonenumber=%s, streetname=%s, streetnumber=%s, zipcode=%s, gender=%s, birthdate=%s
            WHERE customer_id=%s
        """, (name, phonenumber, streetname, streetnumber, zipcode, gender, birthdate, customer_id))

        connection.commit()
        print(f"Customer {customer_id} information updated successfully")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# retreiving code for discount
def get_discount_codes():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()
        
        cursor.execute("SELECT discount_id, discount_code FROM discount WHERE discount_id != 1")
        codes = cursor.fetchall()
        
        # If there are codes available, choose one at random
        if codes:
            return random.choice(codes)  # Return a random code ad its id
        else:
            return None  # No codes available

    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#function to get username Id 
def get_user_id(username):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()
        
        cursor.execute("SELECT customer_id FROM registration WHERE username = %s", (username,))
        result = cursor.fetchone()

       # Check if result is None
        if result:
            customer_id = result[0]  # Extract customer_id from result
            print(f"Customer ID is {customer_id}")
            return customer_id
        else:
            print(f"No customer found with the username: + {username}")
            return None  # Return None if no customer is found

    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# for updating number of pizzas for each customer            
def update_number_of_pizzas(customer_id, pizzaorders):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Assuming `pizzaorders` is a list of tuples, where each tuple contains (pizza_id, quantity)
        total_pizzas_in_order = sum(quantity for pizza_id, quantity in pizzaorders)
        # Check if the customer already exists in the CustomerPizzaOrders table
        cursor.execute("""
            SELECT number_of_pizzas
            FROM numberforpizzas
            WHERE customer_id = %s
        """, (customer_id,))

        result = cursor.fetchone()

        if result is None:
              # Customer not found, insert a new record with the total from this order
             cursor.execute("""
                INSERT INTO numberforpizzas(customer_id, number_of_pizzas)
                VALUES (%s, %s)
            """, (customer_id, total_pizzas_in_order))
             print(f"Added new customer {customer_id} with total pizzas: {total_pizzas_in_order}")
        else:
            # Customer exists, update their total pizzas ordered
            current_total = result[0]
            new_total = current_total + total_pizzas_in_order
            cursor.execute("""
                UPDATE numberforpizzas
                SET number_of_pizzas = %s
                WHERE customer_id = %s
            """, (new_total, customer_id))
            print(f"Updated total pizzas for customer {customer_id}. New total: {new_total}")

        connection.commit()
        

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to add a new customer
def add_customer(id, username, name, phonenumber, streetname, streetnumber, gender, zipcode):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        try:
            # Fetch the birthdate from the registration table
            cursor.execute("SELECT birthdate FROM registration WHERE username = %s", (username,))
            birthdate = cursor.fetchone()

        
            if birthdate:
                # Add customer info along with the fetched birthdate
                cursor.execute("""
                    INSERT INTO customer_info (customer_id, name, phonenumber, streetname, streetnumber, zipcode, gender, birthdate)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (id, name, phonenumber, streetname, streetnumber, zipcode, gender, birthdate[0]))
                connection.commit()
                print("Customer info added successfully!")
            else:
                print("Error: Birthdate not found for this username.")
            
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()
            
    except Error as e:
        print(f"Error: {e}")

# Function to generate earnings report
def earnings_report(filter_by=None, filter_value=None):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        if filter_by is None:
            cursor.execute("""
                SELECT SUM(order_price) FROM Orders
            """)
            total_earnings = cursor.fetchone()[0]

            if total_earnings is None:
                total_earnings = 0  # Handle case where no orders exist

            print(f"Total earnings: ${total_earnings:.2f}")
        else:
            if filter_by == 'region':
                cursor.execute("""
                    SELECT SUM(order_price) FROM Orders
                    JOIN Customer_Info ON Orders.customer_id = Customer_Info.customer_id
                    WHERE Customer_Info.zipcode = %s
                """, (filter_value,))
            elif filter_by == 'gender':
                cursor.execute("""
                    SELECT SUM(order_price) FROM Orders
                    JOIN Customer_Info ON Orders.customer_id = Customer_Info.customer_id
                    WHERE Customer_Info.gender = %s
                """, (filter_value,))
            elif filter_by == 'age':
                cursor.execute("""
                    SELECT SUM(order_price) FROM Orders
                    JOIN Customer_Info ON Orders.customer_id = Customer_Info.customer_id
                    WHERE YEAR(CURDATE()) - YEAR(Customer_Info.birthdate) = %s
                """, (filter_value,))
            else:
                print("Invalid filter criteria")
                return

            total_earnings = cursor.fetchone()[0]

            if total_earnings is None:
                total_earnings = 0  # Handle case where no filtered orders exist

            print(f"Total earnings for {filter_by} = {filter_value}: ${total_earnings:.2f}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# # Test connection to the database
# def test_db_connection():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='piz',
#             user='root',
#             password='ninaanna'
#         )
#         if connection.is_connected():
#             print("Database connection test passed!")
#         else:
#             print("Database connection test failed.")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if connection.is_connected():
#             connection.close()

# # Test for placing an order
# def test_place_order():
#     try:
#         # Ensure valid customer and pizza IDs exist in the database.
#         # Modify the IDs as per your actual database records.

#         # Valid order scenario - update customer ID, pizza IDs as per actual data
#         place_order(1, [1, 2], [1], [1], 25.00)  
        
#         # No items scenario - Valid customer but no items (assuming pizza ID 2 exists)
#         place_order(1, [2], [], [], 15.00)  
        
#         # Invalid customer ID - Assuming customer ID 999 does not exist
#         place_order(999, [1, 2], [1], [1], 25.00)  
        
#         # Invalid pizza ID - Assuming pizza ID 999 does not exist
#         place_order(1, [999], [1], [1], 25.00)  
    
#     except Error as e:
#         print(f"Test place_order: Error: {e}")

# # Test for updating customer info
# def test_update_customer_info():
#     try:
#         # Ensure customer ID 1 exists
#         update_customer_info(1, 'John Doe', '555555555', 'Maple Street', '123', '12345', 'M', '1990-05-15')
        
#         # Non-existent customer ID - Assuming customer ID 999 does not exist
#         update_customer_info(999, 'Jane Doe', '555555555', 'Oak Street', '124', '54321', 'F', '1985-02-10')
        
#         # Invalid data type (birthdate) - Will fail gracefully
#         update_customer_info(1, 'John Doe', '555555555', 'Maple Street', '123', '12345', 'M', 'invalid-date')
    
#     except Error as e:
#         print(f"Test update_customer_info: Error: {e}")

# # Test for applying a discount
# def test_apply_discount():
#     try:
#         # Valid discount code scenario - Ensure 'SUMMER2024' exists in your DB
#         apply_discount(1, 'SUMMER2024')  
        
#         # Invalid discount code scenario
#         apply_discount(1, 'INVALIDCODE')  
        
#         # Non-existent order ID - Assuming order ID 999 does not exist
#         apply_discount(999, 'SUMMER2024')  
    
#     except Error as e:
#         print(f"Test apply_discount: Error: {e}")

# # Test for assigning a delivery person
# def test_assign_delivery_person():
#     try:
#         # Valid postal code with available delivery person - Update with a valid postal code
#         assign_delivery_person(1, 12345)  
        
#         # No available delivery person - Simulate an unavailable region (postal code 54321)
#         assign_delivery_person(1, '54321')  
        
#         # Invalid postal code - Assuming '99999' is not valid
#         assign_delivery_person(1, '99999')  
    
#     except Error as e:
#         print(f"Test assign_delivery_person: Error: {e}")

# # Test for calculating estimated delivery time
# def test_calculate_estimated_delivery_time():
#     try:
#         # Delivery person assigned - Ensure order ID 1 has an assigned delivery person
#         calculate_estimated_delivery_time(1)  
        
#         # No delivery person assigned - Simulate no delivery person for order ID 999
#         calculate_estimated_delivery_time(999)  
    
#     except Error as e:
#         print(f"Test calculate_estimated_delivery_time: Error: {e}")

# # Test for earnings report
# def test_earnings_report():
#     try:
#         # All orders
#         earnings_report()  
        
#         # Filtered by region - Ensure '12345' is a valid region
#         earnings_report('region', '12345')  
        
#         # Filtered by gender - Assuming valid gender 'M'
#         earnings_report('gender', 'M')  
        
#         # Filtered by age - Assuming valid age group 30
#         earnings_report('age', 30)  
    
#     except Error as e:
#         print(f"Test earnings_report: Error: {e}")

# # Run all tests
# def run_all_tests():
#     print("Starting tests...")

#     # Test DB connection
#     test_db_connection()

#     # Run all function tests
#     test_place_order()
#     test_update_customer_info()
#     test_apply_discount()
#     test_assign_delivery_person()
#     test_calculate_estimated_delivery_time()
#     test_earnings_report()

#     print("Tests completed.")

# # Run all tests in sequence
# if __name__ == '__main__':
#     run_all_tests()


# Example usages:
# earnings_report()  # Get total earnings
# earnings_report('region', '12345')  # Get earnings filtered by region (postal code)
# earnings_report('gender', 'M')  # Get earnings filtered by gender (Male)
# earnings_report('age', 30)  # Get earnings filtered by age (30 years old)

# Test placing an order for customer with ID 1
# place_order(1, [1, 2], [1], [1], 25.00)  # Example order
