import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

from OrderProcessing import apply_discount, assign_delivery_person, calculate_estimated_delivery_time, earnings_report, place_order, update_customer_info

class TestPizzaOrderSystem:
    def __init__(self):
        self.connection_params = {
            'host': 'localhost',
            'database': 'pizza_project',
            'user': 'root',
            'password': 'JakubJakub123#'
        }

    # Test connection to the database
    def test_db_connection(self):
        try:
            connection = mysql.connector.connect(**self.connection_params)
            if connection.is_connected():
                print("Database connection test passed!")
            else:
                print("Database connection test failed.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                connection.close()

    # Test for placing an order
    def test_place_order(self):
        try:
            place_order(1, [1, 2], [1], [1], 25.00)  # Valid order scenario
            place_order(1, [2], [], [], 15.00)  # No items scenario
            place_order(999, [1, 2], [1], [1], 25.00)  # Invalid customer ID
            place_order(1, [999], [1], [1], 25.00)  # Invalid pizza ID
        except Error as e:
            print(f"Test place_order: Error: {e}")

    # Test for updating customer info
    def test_update_customer_info(self):
        try:
            update_customer_info(1, 'John Doe', '555555555', 'Maple Street', '123', '12345', 'M', '1990-05-15')
            update_customer_info(999, 'Jane Doe', '555555555', 'Oak Street', '124', '54321', 'F', '1985-02-10')
            update_customer_info(1, 'John Doe', '555555555', 'Maple Street', '123', '12345', 'M', 'invalid-date')
        except Error as e:
            print(f"Test update_customer_info: Error: {e}")

    # Test for applying a discount
    def test_apply_discount(self):
        try:
            apply_discount(1, 'SUMMER2024')  # Valid discount code
            apply_discount(1, 'INVALIDCODE')  # Invalid discount code
            apply_discount(999, 'SUMMER2024')  # Non-existent order
        except Error as e:
            print(f"Test apply_discount: Error: {e}")

    # Test for assigning a delivery person
    def test_assign_delivery_person(self):
        try:
            assign_delivery_person(1, '12345')  # Valid postal code
            assign_delivery_person(1, '54321')  # No available delivery person
            assign_delivery_person(1, '99999')  # Invalid postal code
        except Error as e:
            print(f"Test assign_delivery_person: Error: {e}")

    # Test for calculating estimated delivery time
    def test_calculate_estimated_delivery_time(self):
        try:
            calculate_estimated_delivery_time(1)  # Delivery person assigned
            calculate_estimated_delivery_time(999)  # No delivery person assigned
        except Error as e:
            print(f"Test calculate_estimated_delivery_time: Error: {e}")

    # Test for earnings report
    def test_earnings_report(self):
        try:
            earnings_report()  # All orders
            earnings_report('region', '12345')  # Filtered by region
            earnings_report('gender', 'M')  # Filtered by gender
            earnings_report('age', 30)  # Filtered by age
        except Error as e:
            print(f"Test earnings_report: Error: {e}")

    # Run all tests
    def run_all_tests(self):
        print("Starting tests...")
        self.test_db_connection()
        self.test_place_order()
        self.test_update_customer_info()
        self.test_apply_discount()
        self.test_assign_delivery_person()
        self.test_calculate_estimated_delivery_time()
        self.test_earnings_report()
        print("Tests completed.")

# Example of how to run the tests
if __name__ == '__main__':
    test_system = TestPizzaOrderSystem()
    test_system.run_all_tests()
