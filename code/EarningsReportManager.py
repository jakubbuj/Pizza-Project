import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

class EarningsReportManager:
    def __init__(self):
        self.connection_params = {
            'host': 'localhost',
            'database': 'piz',
            'user': 'root',
            'password': 'ninaanna'
        }

    def generate_report(self, filter_by=None, filter_value=None):
        connection = None  # Initialize connection to None

        try:
            # Establish the connection
            connection = mysql.connector.connect(**self.connection_params)
            cursor = connection.cursor()

            if filter_by is None:
                cursor.execute("SELECT SUM(order_price) FROM Orders")
                total_earnings = cursor.fetchone()[0] or 0
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
                        WHERE TIMESTAMPDIFF(YEAR, Customer_Info.birthdate, CURDATE()) = %s
                    """, (filter_value,))
                else:
                    print("Invalid filter criteria")
                    return

                total_earnings = cursor.fetchone()[0] or 0
                print(f"Total earnings for {filter_by} = {filter_value}: ${total_earnings:.2f}")

        except Error as e:
            print(f"Error: {e}")
        finally:
            # Ensure that connection is closed only if it was successfully opened
            if connection and connection.is_connected():
                cursor.close()
                connection.close()


# Example of how to use the EarningsReportManager
if __name__ == '__main__':
    earnings_manager = EarningsReportManager()
    earnings_manager.generate_report()  # Get total earnings
    earnings_manager.generate_report('region', '12345')  # Get earnings filtered by region
    earnings_manager.generate_report('gender', 'female')  # Get earnings filtered by gender
    earnings_manager.generate_report('age', 20)  # Get earnings filtered by age
