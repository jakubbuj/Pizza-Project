import mysql.connector
from OrderProcessing import *
from mysql.connector import Error
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime, timedelta
import bcrypt
from tkinter import Toplevel, Button, Frame, Label



def resize_image(image_path, size):
    image = Image.open(image_path)
    return image.resize(size, Image.Resampling.LANCZOS)

discounted_total = None
logged_in_username = None
cart = []
bdaycart = []
modified_bdaycart = []
birthday_discount_applied = False
Birthday = False


root = Tk()
root.title("Login")
root.geometry("1000x600")
root.configure(bg="#f0f0f0")

# Add a label with the restaurant name "MYPIZZALAB"
restaurant_title = Label(root, text="MYPIZZALAB", bg="#f0f0f0", font=("Courier", 24, 'bold', 'italic'))
restaurant_title.pack(pady=10)


# Assuming you have the label defined at the beginning of your login window function
feedback_label_pass = Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
feedback_label_pass.pack(pady=10)


image_path = "pizza-cartoon-ai-generate-png.png"
resized_image = resize_image(image_path, (100, 100))
image_display = ImageTk.PhotoImage(resized_image)

image_label = Label(root, image=image_display, bg="#f0f0f0")
image_label.pack(pady=10)

myLabel = Label(root, text="Welcome! Please log in.", bg="#f0f0f0", font=("Arial", 14, 'bold'))
myLabel.pack(pady=10)

label_username = Label(root, text="Username:", bg="#f0f0f0", font=("Arial", 12))
label_password = Label(root, text="Password:", bg="#f0f0f0", font=("Arial", 12))
entry_username = Entry(root, relief=SOLID, borderwidth=1)
entry_password = Entry(root, show='*', relief=SOLID, borderwidth=1)
label_username.pack(pady=5)
entry_username.pack(pady=5)
label_password.pack(pady=5)
entry_password.pack(pady=5)


# Global tree variables for each menu
pizza_tree = None
desserts_tree = None
drink_tree = None

def hash_password(password):
    """Hash a plain-text password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def view_cart():
    global logged_in_username
    global discounted_total
    global cart_window

    if not logged_in_username:
        print("Error: no user is logged in")
        return 
    

    cart_window = Toplevel(menu_window)
    cart_window.title("Your Cart")
    cart_window.geometry("600x500")
    cart_window.configure(bg="#fafafa")

    carttree = ttk.Treeview(cart_window)
    carttree.pack(pady=20)

    carttree['columns'] = ('Name', 'Price', 'Quantity')
    carttree.column('#0', width=0, stretch=NO)

    for col in carttree['columns']:
        carttree.column(col, anchor=CENTER, width=100)
        carttree.heading(col, text=col, anchor=CENTER)

    # Debug print to check if cart has items
    print(f"Current Cart: {cart}")

    for item in cart:
        carttree.insert('', 'end', values=(item['name'], item['price'], item['quantity']))

    total_price = sum(item['price'] * item['quantity'] for item in cart)

    #Checking for the 10% discount
    discount_percentage = check_for_discount(logged_in_username)
    
    #default
    discounted_total = total_price
    discount_id = None

    if discount_percentage == 10:
        discount_info = get_discount_codes()
        if discount_info: 
            discount_id, discount_code = discount_info

            discount_label = Label(cart_window, text=f"It's time for a discount! Enter the code {discount_code}, for a 10'%' discount", bg="#fafafa", font=("Arial", 14, 'bold'))
            discount_label.pack(pady=10)

            discount_code_var = StringVar()

            discount_entry = Entry(cart_window, textvariable=discount_code_var, font=("Arial", 12))
            discount_entry.pack(pady=5)

        def apply_discount():
            entered_code = discount_code_var.get()
            if entered_code == discount_code:  # Check if entered code matches the retrieved code
                discounted_total = total_price * (1 - discount_percentage / 100)
                total_label.config(text=f"Total Price: €{discounted_total:.2f}")
                feedback_label.config(text="Discount applied successfully!", fg="green")
            else:
                feedback_label.config(text="No such discount code!", fg="red")

        
        apply_discount_button = Button(cart_window, text="Apply Discount", command=apply_discount, font=("Arial", 12), bg="#0078D7", fg="black")
        apply_discount_button.pack(pady=10)

        # Feedback label for discount application status
        feedback_label = Label(cart_window, text="", bg="#fafafa", font=("Arial", 12))
        feedback_label.pack(pady=10)
    else:
        # If no discount, just display the total
        feedback_label = Label(cart_window, text="No discounts available.", bg="#fafafa", font=("Arial", 14, 'bold'))
        feedback_label.pack(pady=10)

                

    #debug
    print(f"Total Price: {total_price:.2f}")
    print(f"Discount Applied: {discount_percentage}%")
    print(f"Discounted Price: €{discounted_total:.2f}")

    total_label = Label(cart_window, text=f"Total Price: €{discounted_total:.2f}", bg="#fafafa", font=("Arial", 14, 'bold'))
    total_label.pack(pady=10)

    Button(cart_window, text="Checkout", command=lambda: checkout(discount_id), font=("Arial", 12), bg="black", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)
    Button(cart_window, text="Close", command=cart_window.destroy, font=("Arial", 12), bg="black", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)

def check_for_bday_discount(username):
    print("checking for bday")
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Step 1: Get the birthdate from the Registration table based on the username
        cursor.execute("""
            SELECT birthdate 
            FROM Registration
            WHERE username = %s
        """, (username,))
        result = cursor.fetchone()

        if result is None:
            print(f"No customer found with username: {username}")
            return 0  # No discount since no customer found

        bday = result[0]
        today = datetime.today().date()
        if bday is not None:
            #birthdatelabel = False
            if bday.month == today.month and bday.day == today.day:
                #birthdatelabel = True
                print(f"Happy birthday, {username}! You get a birthday discount!")
                # discount_cart = apply_birthday_discount(cart)
                # Apply discount for one pizza and one drink
                return True
       
        return False
    except Error as e:
        print(f"Error: {e}")
        return 0  # No discount in case of error
    finally:
        if connection.is_connected():

           cursor.close()
           connection.close()

def check_for_discount(username):
    global Birthday
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Step 1: Get the customer_id from the Registration table based on the username
        cursor.execute("""
            SELECT customer_id
            FROM Registration
            WHERE username = %s
        """, (username,))
        result = cursor.fetchone()

        if result is None:
            print(f"No customer found with username: {username}")
            return 0  # No discount since no customer found

        customer_id = result[0]

        # Step 2: Count the total number of pizzas ordered by the customer using customer_id
        cursor.execute("""
            SELECT number_of_pizzas
            FROM numberforpizzas
            WHERE customer_id = %s
        """, (customer_id,))
        total_pizzas = cursor.fetchone()

        if total_pizzas is None or total_pizzas[0] is None:
            total_pizzas_ordered = 0
        else: 
            total_pizzas_ordered = total_pizzas[0]
        print(f"Total pizzas fetched: {total_pizzas_ordered}")
        
        if total_pizzas_ordered is None:
            total_pizzas_ordered = 0  # Assume no pizzas ordered if result is None
        # else:
        #     total_pizzas_ordered = result[0]  # Fixed to result[0], as only one column is retrieved

        if Birthday:
            current_pizzas_in_cart = sum(item['quantity'] for item in modified_bdaycart if item['type'] == 'pizza')
        else:
            current_pizzas_in_cart = sum(item['quantity'] for item in cart if item['type'] == 'pizza')

        current_total_of_pizzas = total_pizzas_ordered + current_pizzas_in_cart

        print(f"Total pizzas ordered: {total_pizzas_ordered}")
        print(f"Current pizzas in cart: {current_pizzas_in_cart}")
        print(f"Current total pizzas: {current_total_of_pizzas}")

        is_friday = datetime.now().weekday() == 4

        # Priority is given to the 20% Friday discount
        if is_friday:
            print("It's Friday! Applying 20% discount.")
            return 20  # 20% discount for Friday

        # If the customer has ordered 10 or more pizzas, apply a 10% discount
        if current_total_of_pizzas % 10 == 0 and current_total_of_pizzas != 0:
            return 10  # 10% discount
        else:
            return 0  # No discount

    except Error as e:
        print(f"Error: {e}")
        return 0  # No discount in case of error
    finally:
        if connection.is_connected():

            cursor.close()
            connection.close()

def checkout(discount_id):
        
        global bdaycart_window
        global cart_window

        print("Proceeding to checkout...")
        if Birthday == True:
            has_pizza = any(item['type'] == 'pizza' for item in bdaycart)  # Assuming your cart structure contains a 'type' key
        else: 
            has_pizza = any(item['type'] == 'pizza' for item in cart)  # Assuming your cart structure contains a 'type' key

        if not has_pizza:
            # If no pizza is in the order, show a warning label and exit the function
            checkout_window = Toplevel(menu_window)
            checkout_window.title("Checkout")
            checkout_window.geometry("300x200")
            checkout_window.configure(bg="#fafafa")

            Label(checkout_window, text="Please order a pizza first!", bg="#fafafa", font=("Arial", 16, 'bold'), fg="red").pack(pady=50)
            return  # Exit the function
        
        
        if Birthday:
            close_window(bdaycart_window)
        else:
            close_window(cart_window)

        
        checkout_window = Toplevel(root)
        checkout_window.title("Checkout")
        checkout_window.geometry("400x600")
        checkout_window.configure(bg="#fafafa")

       
        menu_window.destroy()
        
        Label(checkout_window, text="Enter Your Details", bg="#fafafa", font=("Arial", 16, 'bold')).pack(pady=10)
         
        fields = {
            "Name": StringVar(),
            "Phone Number": StringVar(),
            "Street Name": StringVar(),
            "Street Number": StringVar(),
            "Gender": StringVar(),
        }

        # List of Zip Codes for the Combobox
        zip_codes = ['Select a zip code', '12345', '54321', '98765', '87654', '65432', '43210', '32109', '21098', '10987', '90876']
        
        for field, var in fields.items():
            Label(checkout_window, text=field, bg="#fafafa", font=("Arial", 12)).pack(pady=5)
            Entry(checkout_window, textvariable=var, font=("Arial", 12), relief=SOLID, borderwidth=1).pack(pady=5)

        zip_code_var = StringVar(checkout_window)
        zip_code_var.set(zip_codes[0])

       # Create the Dropdown Menu using OptionMenu
        Label(checkout_window, text="Zip Code", bg="#fafafa", font=("Arial", 12)).pack(pady=5)
        zip_code_dropdown = OptionMenu(checkout_window, zip_code_var, *zip_codes)
        zip_code_dropdown.config(font=("Arial", 12), relief=SOLID, borderwidth=1)
        zip_code_dropdown.pack(pady=5)

        # Function to handle submission
        def submit_details_wrapper():
            zip_code_value = zip_code_var.get()

            if zip_code_value == "Select a zip code":
                print("Error: No Zip Code selected!")
            else:
                print(f"Zip Code selected from dropdown: {zip_code_value}")
                fields["Zip Code"] = zip_code_value  # Add the selected zip code to fields
                
                fields["Username"] = StringVar()
                fields["Username"].set(logged_in_username)

                # Call the submit_details function (you already have it)
                submit_details(discount_id, fields, checkout_window)
      
        Button(checkout_window, text="Submit", command=submit_details_wrapper, font=("Arial", 12), bg="#0078D7", 
                fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=20)
    

# debugging method for printing cart and seeing what is inside
def print_cart(cart):
    """Function to print the current state of the cart."""
    print("Current Cart Items:")
    if not cart:
        print("The cart is empty.")
    else:
        for item in cart:
            print(f"Type: {item['type']}, Price: {item['price']:.2f}€, Quantity: {item['quantity']}")
    print("")  # Just for spacing

def add_to_cart(tree: ttk.Treeview, price_column, item_type):
    print(f"adding to cart {item_type}")
    global bdaycart
    global cart

    selected_item = tree.selection()
   
    
    if selected_item:
        item_data = tree.item(selected_item)['values']

        item_id = item_data[0]
        item_name = item_data[1]
        item_price = item_data[price_column]
      
        # Convert price to float
        try:
            item_price = item_price.replace('€', '').replace(',', '').strip()
            item_price = float(item_price)
        except ValueError:
            print("Error: Invalid price format")
            return

        # Decide which cart to add the item to based on birthday status
        current_cart = bdaycart if Birthday else cart

        # Check if the item is already in the current cart
        existing_item = next((item for item in current_cart if item['id'] == item_id and item['type'] == item_type), None)

        if existing_item:
            # If the item exists, just update its quantity
            existing_item['quantity'] += 1
            print(f"Updated {item_name} quantity to {existing_item['quantity']}")
        else:
            # Add the new item to the appropriate cart
            new_item = {
                'id': item_id,
                'name': item_name,
                'price': item_price,  # Always use the original price
                'quantity': 1,
                'type': item_type
            }
            current_cart.append(new_item)
            print(f"{item_name} has been added to your {'birthday cart' if current_cart == bdaycart else 'cart'}.")
        
        # Debug: Print the current state of the cart
        if current_cart == bdaycart:
            print(f"Birthday Cart Items: {bdaycart}")
        else:
            print(f"Normal Cart Items: {cart}")
        
    else:
        print("Please select an item to add to the cart.")

def submit_details(discount_id, fields, checkout_window):
        #debug
        print("submitting details")

        global logged_in_username
        global modified_bdaycart
        global discounted_total

        customer_data = {}
        for field, var in fields.items():
            if isinstance(var, StringVar):
                customer_data[field] = var.get()
            else:
                customer_data[field] = var  # For Zip Code, which is a string

        # Fetch the customer_id from the registration table
        customer_id = get_user_id(logged_in_username)

        # Check if customer_id is valid
        if customer_id is None:
            print(f"No customer found for username: {logged_in_username}")
       
        add_customer(
            customer_id,
            customer_data["Username"],
            customer_data["Name"],
            customer_data["Phone Number"],
            customer_data["Street Name"],
            customer_data["Street Number"],
            customer_data["Gender"],
            customer_data["Zip Code"]
        )
        #debug
        print("Added customer")

        pizza_ids = []   # holds tuples of id and quantity of orderes item types
        drink_ids = []  
        dessert_ids = [] 
        customer_id = get_user_id(logged_in_username)
        # final_cart = []

        # Assuming 'cart' is a list of items in the user's cart
        if Birthday == False:
            for item in cart:
                item_type = item['type']  # Assuming each item has a 'type' key

                if item_type == 'pizza':
                    pizza_ids.append((item['id'], item['quantity']))  # Append tuple (id, quantity)
                elif item_type == 'drink':
                    drink_ids.append(item['id'])  # Append the drink ID
                elif item_type == 'dessert':
                    dessert_ids.append(item['id'])  # Append the dessert ID
        else:
            for item in bdaycart:
                item_type = item['type']  # Assuming each item has a 'type' key

                if item_type == 'pizza':
                    pizza_ids.append((item['id'], item['quantity']))  # Append tuple (id, quantity)
                elif item_type == 'drink':
                    drink_ids.append(item['id'])  # Append the drink ID
                elif item_type == 'dessert':
                    dessert_ids.append(item['id'])  # Append the dessert ID

        
        # Debugging prints to check what has been added
        print("Pizza Orders:", pizza_ids)
        print("Drink IDs:", drink_ids)
        print("Dessert IDs:", dessert_ids)
                

        print(discounted_total)
        # Place the order and retrieve the order number
        order_number = place_order(customer_id, pizza_ids, drink_ids, dessert_ids, discounted_total, discount_id, customer_data["Zip Code"])
        if order_number is None:  # Check if order_number indicates an error
            show_no_delivery_person_window()  # Open new window to inform the user
        else:
            print(discounted_total)
            show_order_confirmation(order_number)  # Pass order_number to confirmation function

        print(f"order_number returned: {order_number}")
        
        checkout_window.destroy()  # Close the checkout window
        update_number_of_pizzas(customer_id, pizza_ids)

def show_no_delivery_person_window():
    no_delivery_window = Toplevel()
    no_delivery_window.title("No Delivery Persons Available")
    no_delivery_window.geometry("500x300")
    no_delivery_window.configure(bg="#fafafa")

    message_label = Label(no_delivery_window, text="Sorry, there are no available delivery persons now, please wait. ", 
                          bg="#fafafa", font=("Arial", 12))
    message_label.pack(pady=20)

    # Optional: add a button to close the window
    close_button = Button(no_delivery_window, text="Logout", command=root.destroy, 
                          font=("Arial", 12), bg="#0078D7", fg="black")
    close_button.pack(pady=10)

def show_order_confirmation(order_number):
    global discounted_total, confirmation_window
    print("Discounted Total:", discounted_total)  # Debug print

    
    print(f"Trying to show order confirmation for order number: {order_number}")  # Debug print
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Fetch order confirmation details
        fetch_confirmation_query = """
            SELECT date, time, order_price, estimate_time, discount_used
            FROM OrderConfirmation
            WHERE order_number = %s
        """
        cursor.execute(fetch_confirmation_query, (order_number,))
        confirmation_details = cursor.fetchone()
        print("details fetched")
        
        if confirmation_details:
            order_date, order_time, discounted_total, estimate_time, discount_used = confirmation_details
            
            # Fetch delivery person's id 
            fetch_orders_query = """
                SELECT deliveryperson_id
                FROM Orders
                WHERE order_number = %s
            """
            cursor.execute(fetch_orders_query, (order_number,))
            delivery_person_id = cursor.fetchone()
            delivery_id = delivery_person_id[0] if delivery_person_id else "Not assigned"  # Use index 0

            # Fetch delivery person's phone number 
            fetch_delivery_query = """
                SELECT phonenumber, name
                FROM Deliveryperson
                WHERE deliveryperson_id = %s
            """
            cursor.execute(fetch_delivery_query, (delivery_id,))
            delivery_person = cursor.fetchone()

            if delivery_person:
                phone_number, name = delivery_person  # Unpack the results
                print(f"Delivery Person: {name}, Phone Number: {phone_number}")
            else:
                print("No delivery person found with that ID.")

            # Create the confirmation window
            confirmation_window = Toplevel()
            confirmation_window.title("Order Confirmation")
            confirmation_window.geometry("400x600")  # Adjusted height for better spacing
            confirmation_window.configure(bg="#F0F0F0")  # Light gray background

            # Header
            header_frame = Frame(confirmation_window, bg="#0078D7")  # Blue header
            header_frame.pack(fill=X)
            Label(header_frame, text="Order Confirmation", bg="#0078D7", fg="white", font=("Arial", 18, 'bold')).pack(pady=10)

            # Order details section
            details_frame = Frame(confirmation_window, bg="#F0F0F0")
            details_frame.pack(pady=20)

            Label(details_frame, text="Thank you for your order!", bg="#F0F0F0", font=("Arial", 16, 'bold')).pack(pady=10)

            # Display the order details with padding
            Label(details_frame, text=f"Order Date: {order_date}", bg="#F0F0F0", font=("Arial", 12)).pack(pady=5)
            Label(details_frame, text=f"Order Time: {order_time}", bg="#F0F0F0", font=("Arial", 12)).pack(pady=5)
            Label(details_frame, text=f"Estimated Time: {estimate_time}", bg="#F0F0F0", font=("Arial", 12)).pack(pady=5)
            Label(details_frame, text=f"Discount Used: {'Yes' if discount_used else 'No'}", bg="#F0F0F0", font=("Arial", 12)).pack(pady=5)
            Label(details_frame, text=f"Total Price: €{discounted_total:.2f}", bg="#F0F0F0", font=("Arial", 14, 'bold'), fg="#0078D7").pack(pady=10)
            # Display delivery person's phone number and name 
            Label(details_frame, text=f"Delivery Person's Phone: {phone_number}", bg="#F0F0F0", font=("Arial", 12)).pack(pady=5)
            Label(details_frame, text=f"Delivery Person's Name: {name}", bg="#F0F0F0", font=("Arial", 12)).pack(pady=5)
            
            # Timer label
            timer_label = Label(details_frame, bg="#F0F0F0", font=("Arial", 12))
            timer_label.pack(pady=5)

            # Function to update the countdown timer
            def update_timer(countdown_time):
                if countdown_time > 0:
                    minutes, seconds = divmod(countdown_time, 60)
                    time_display = f"{minutes:02}:{seconds:02}"
                    timer_label.config(text=f"Waiting Time: {time_display}")  # Update the label text
                    countdown_time -= 1
                    timer_label.after(1000, update_timer, countdown_time)  # Schedule next update
                else:
                    timer_label.config(text="Order Delivered!")  # Update to show delivery complete

            # Start the countdown (30 minutes in seconds)
            initial_countdown_time = 30 * 60  # 30 minutes
            update_timer(initial_countdown_time)
            statusbutton = Button(confirmation_window, text="Check order status", command=lambda: show_order_status(order_number), font=("Arial", 14), bg="#0078D7", fg="black")
            statusbutton.pack(pady=20)

            # Close button
            close_button = Button(confirmation_window, text="Close", command=confirmation_window.destroy, font=("Arial", 14), bg="#0078D7", fg="black")
            close_button.pack(pady=20)
            cancel_button = Button(confirmation_window, text="CANCEL ORDER", command=lambda: cancelorder(order_number), font=("Arial", 14), bg="#0078D7", fg="black")
            cancel_button.pack(pady=20)

        else:
            print("No confirmation details found for this order.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def cancelorder(order_number):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Fetch order confirmation details
        cursor.execute("""
            SELECT time
            FROM Orders
            WHERE order_number = %s
        """, (order_number, ))
        result = cursor.fetchone()

        if result:
            order_time = result[0]
            
            # Debugging: Print the type of order_time to understand its format
            print(f"order_time type: {type(order_time)}, value: {order_time}")

            # Check if order_time is of type datetime
            if isinstance(order_time, timedelta):
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                order_time = today + order_time
            else:
                # If it's a different format, handle accordingly (e.g., datetime)
                order_time = datetime.combine(datetime.today(), order_time)
            
            elapsed_time = (datetime.now() - order_time).total_seconds() / 60
            
            print(f"elapsed time is {elapsed_time}")

            Ordercancelled = False

            if elapsed_time < 5:
  
                cursor.execute("""
                    DELETE FROM PizzaOrders WHERE order_number = %s
                """, (order_number, ))
                connection.commit()

                cursor.execute("""
                    DELETE FROM Dessertorders WHERE order_number = %s
                """, (order_number, ))
                connection.commit()
                
                cursor.execute("""
                    DELETE FROM Drinkorders WHERE order_number = %s
                """, (order_number, ))
                connection.commit()
                
                cursor.execute("""
                    DELETE FROM Orderconfirmation WHERE order_number = %s
                """, (order_number, ))
                connection.commit()

                cursor.execute("""
                    DELETE FROM Orders WHERE order_number = %s
                """, (order_number, ))
                connection.commit()

                print(f"Order {order_number} cancelled")
                Ordercancelled = True

            else: 
                print(f"Order {order_number} can not be cancelled it's being made")

            status_window = Toplevel(confirmation_window)
            status_window.title("Order Cancellation")
            status_window.geometry("700x600")
            status_window.configure(bg="#fafafa")

            # Create a main frame for better layout management
            main_frame = Frame(status_window, bg="#fafafa")
            main_frame.pack(expand=True, fill='both', padx=20, pady=20)

            # Adding a logo or image (optional)
            # logo_image = PhotoImage(file='path_to_logo.png')  # Replace with your image path
            # logo_label = Label(main_frame, image=logo_image, bg="#fafafa")
            # logo_label.pack(pady=(0, 20))  # Add padding to separate the logo from the rest

            # Status label
            if Ordercancelled:
                status_text = "YOUR ORDER HAS BEEN CANCELLED"
                status_color = "green"
                button_text = "CLOSE"
                button_command = status_window.destroy
            else:
                status_text = "YOUR ORDER CANNOT BE CANCELLED, IT IS TOO LATE"
                status_color = "red"
                button_text = "BACK TO CONFIRMATION"
                button_command = status_window.destroy

            status_label = Label(main_frame, text=status_text, bg="#fafafa", font=("Arial", 16, "bold"), fg=status_color)
            status_label.pack(pady=(20, 10))

            # Button frame for buttons
            button_frame = Frame(main_frame, bg="#fafafa")
            button_frame.pack(pady=(10, 20))

            # Close/Back button
            action_button = Button(button_frame, text=button_text, command=button_command, bg="#0078D7", fg="white", font=("Arial", 14))
            action_button.pack(pady=5)

            # Styling for buttons (optional)
            for button in button_frame.winfo_children():
                button.config(width=20, height=2, borderwidth=1, relief="raised")
                button.bind("<Enter>", lambda e: e.widget.config(relief="sunken"))
                button.bind("<Leave>", lambda e: e.widget.config(relief="raised"))

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    

def show_order_status(order_number):
    global confirmation_window
    
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()

        # Fetch order confirmation details
        cursor.execute("""
            SELECT time, status
            FROM Orders
            WHERE order_number = %s
        """, (order_number, ))
        result = cursor.fetchone()

        if result:
            order_time = result[0]
            current_status = result[1]

            # Debugging: Print the type of order_time to understand its format
            print(f"order_time type: {type(order_time)}, value: {order_time}")

             # Check if order_time is of type datetime
            if isinstance(order_time, timedelta): 
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                order_time = today + order_time
            else:
                # If it's a different format, handle accordingly (e.g., datetime)
                order_time = datetime.combine(datetime.today(), order_time)
            
            elapsed_time = (datetime.now() - order_time).total_seconds() / 60
            
            print(f"elapsed time is {elapsed_time}")

            # Check for negative elapsed time
            if elapsed_time < 0:
                print("Error: Order time is in the future. Please check the order_time stored in the database.")
            if elapsed_time < 5:
                new_status = "In Process"
            elif elapsed_time < 15:
                new_status = "Being Prepared"
            elif elapsed_time < 30:
                new_status = "Out for Delivery"
            else: 
                new_status = "Delivered"

            print(f"new status is {new_status}")

            if new_status != current_status:
                cursor.execute("""
                    UPDATE Orders SET status = %s WHERE order_number = %s
                """, (new_status, order_number ))
                connection.commit()

                print(f"Order {order_number} status updated to {new_status}")
            
            else:
                print(f"Order {order_number} status remains {current_status}")

            status_window = Toplevel(confirmation_window)
            status_window.title("Order Status")
            status_window.geometry("700x600")
            status_window.configure(bg="#fafafa")


            statuslabel = Label(status_window, text=f"Order status for order number: {order_number} is {new_status}", bg="#F0F0F0", font=("Arial", 14), fg="Black")
            statuslabel.pack(pady=5)
            Button(status_window, text=f"Back to order confirmation", command=status_window.destroy, bg="#F0F0F0", font=("Arial", 14), fg="Black").pack(pady=5)

        else:
            print(f"Order {order_number} not found.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def fetch_data(table_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='piz',
            user='root',
            password='ninaanna'
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def open_registration_window():
    registration_window = Toplevel(root)
    registration_window.title("Register")
    registration_window.geometry("1000x500")
    registration_window.configure(bg="#fafafa")
     
    
    Label(registration_window, text="Date of birth YYYY/MM/DD: ", bg="#fafafa", font=("Arial", 12)).pack(pady=5)
    Date_of_birth = Entry(registration_window, relief=SOLID, borderwidth=1)
    Date_of_birth.pack(pady=5)
    Label(registration_window, text="Username:", bg="#fafafa", font=("Arial", 12)).pack(pady=5)
    username_entry = Entry(registration_window, relief=SOLID, borderwidth=1)
    username_entry.pack(pady=5)
    Label(registration_window, text="Password:", bg="#fafafa", font=("Arial", 12)).pack(pady=5)
    password_entry = Entry(registration_window, show='*', relief=SOLID, borderwidth=1)
    password_entry.pack(pady=5)

    feedback_label = Label(registration_window, text="", bg="#fafafa", font=("Arial", 12))
    feedback_label.pack(pady=10)

    # This label will indicate registration completion
    registration_complete_label = Label(registration_window, text="", bg="#fafafa", font=("Arial", 14, 'bold'))
    registration_complete_label.pack(pady=20)

    def register_user():
        username = username_entry.get()
        passkey = password_entry.get()
        date = Date_of_birth.get()

         # Basic validation
        if not username or not passkey or not date:
            feedback_label.config(text="Please fill in all fields.", fg="red")
            return
        
        hashed_password = hash_password(passkey)

        if add_registration(username, hashed_password, date):
            feedback_label.config(text="Registration successful!", fg="green")
            registration_complete_label.config(text="Registration Complete!", fg="blue")
            registration_window.after(2000, registration_window.destroy)  # Auto-close after 2 seconds
        else:
            feedback_label.config(text="Registration failed. Username might already exist.", fg="red")

    
    Button(registration_window, text="Register", command=register_user, font=("Arial", 12), bg="#0078D7", fg="blue", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=20)

def open_menu_window():
    global menu_window
    global Birthday
    menu_window = Toplevel(root)
    menu_window.title("Menu")
    menu_window.geometry("1000x500")
    menu_window.configure(bg="#f0f0f0")

    # Main Frame for layout
    main_frame = Frame(menu_window, bg="#f0f0f0")
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    # Title Label
    title_label = Label(main_frame, text="Welcome to: ", bg="#f0f0f0", font=("Courier", 24, "bold"), fg="#C0392B")  # Dark red color
    title_label.pack(pady=(0, 10))
    mypizzalab = Label(main_frame, text="MYPIZZALAB", bg="#f0f0f0", font=("Courier", 24, 'bold', 'italic'))
    mypizzalab.pack(pady=(0, 10))
    title_label2 = Label(main_frame, text="Here is our Menu: ", bg="#f0f0f0", font=("Courier", 24, "bold"), fg="#C0392B")  # Dark red color
    title_label2.pack(pady=(0, 20))

    def on_enter(e):
        e.widget['bg'] = '#C0392B'  # Darker red on hover
        e.widget['fg'] = 'white'     # Change text color to white

    def on_leave(e):
        e.widget['bg'] = '#E74C3C'   # Original red when not hovered
        e.widget['fg'] = 'white'      # Keep text color white

    # Check for birthday discount
    if check_for_bday_discount(logged_in_username):
        Birthday = True
        # Buttons with improved colors and styling
        Button(main_frame, text='Pizza', command=lambda: switch_window(pizza_menu), 
            font=("Arial", 14), bg="#E74C3C", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=10)
        
        Button(main_frame, text='Desserts', command=lambda: switch_window(desserts_menu), 
            font=("Arial", 14), bg="#E74C3C", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=5)
        
        Button(main_frame, text='Drinks', command=lambda: switch_window(drink_menu), 
            font=("Arial", 14), bg="#E74C3C", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=5)

        Button(main_frame, text="View Cart", command=view_bdaycart, 
            font=("Arial", 14), bg="#28A745", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=10)
        
        Button(main_frame, text="Logout", command=root.destroy, 
            font=("Arial", 14), bg="#DC3545", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=10)
    else:
        Button(main_frame, text='Pizza', command=lambda: switch_window(pizza_menu), 
            font=("Arial", 14), bg="#E74C3C", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=10)
        
        Button(main_frame, text='Desserts', command=lambda: switch_window(desserts_menu), 
            font=("Arial", 14), bg="#E74C3C", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=5)
        
        Button(main_frame, text='Drinks', command=lambda: switch_window(drink_menu), 
            font=("Arial", 14), bg="#E74C3C", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=5)

        Button(main_frame, text="View Cart", command=view_cart, 
            font=("Arial", 14), bg="#28A745", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=10)
        
        Button(main_frame, text="Logout", command=root.destroy, 
            font=("Arial", 14), bg="#DC3545", fg="red", relief='raised', 
            borderwidth=2, padx=20, pady=10).pack(pady=10)

    
def view_bdaycart():
    global discounted_total
    global bdaycart
    global logged_in_username
    global modified_bdaycart
    global bdaycart_window

    if not logged_in_username:
        print("Error: no user is logged in")
        return 
    
    bdaycart_window = Toplevel(menu_window)
    bdaycart_window.title("Your Cart")
    bdaycart_window.geometry("700x600")
    bdaycart_window.configure(bg="#fafafa")

    bdaycarttree = ttk.Treeview(bdaycart_window)
    bdaycarttree.pack(pady=20)

    bdaycarttree['columns'] = ('Name', 'Price', 'Quantity')
    bdaycarttree.column('#0', width=0, stretch=NO)

    for col in bdaycarttree['columns']:
        bdaycarttree.column(col, anchor=CENTER, width=100)
        bdaycarttree.heading(col, text=col, anchor=CENTER)

    for item in bdaycarttree.get_children():
        bdaycarttree.delete(item)

    # Debug print to check if cart has items
    print(f"Current Birthdays Cart: {bdaycart}")

    # Apply the birthday special: one free pizza and one free drink
    pizza_discount_applied = False
    drink_discount_applied = False
    modified_bdaycart = []

    for item in bdaycart:
        modified_item = item.copy()  # Always copy the original item

        if not pizza_discount_applied and "pizza" in item['type'].lower():
            print(f"Free pizza applied to: {item['name']}")
            modified_item['price'] = 0.0
            pizza_discount_applied = True

        elif not drink_discount_applied and "drink" in item['type'].lower():
            # First drink is free
            print(f"Free drink applied to: {item['name']}")
            modified_item['price'] = 0.0
            drink_discount_applied = True
       
        modified_bdaycart.append(modified_item)

        bdaycarttree.insert('', 'end', values=(modified_item['name'], f"€{modified_item['price']:.2f}", modified_item['quantity']))

    # Calculate the total price after applying the birthday offer (free pizza and drink)
    total_price = sum(item['price'] * item['quantity'] for item in modified_bdaycart)

    birth_label = Label(bdaycart_window, text=f"Happy Birthday {logged_in_username}!! We have a special offer for you today. One free pizza and one free drink!", bg="#fafafa", fg="Pink", font=("Arial", 14, 'bold'))
    birth_label.pack(pady=10)

    #Checking for the 10% discount
    discount_percentage = check_for_discount(logged_in_username)
    
    #default
    discounted_total = total_price
    discount_id = None

    if discount_percentage == 10:
        discount_info = get_discount_codes()
        if discount_info: 
            discount_id, discount_code = discount_info

            discount_label = Label(bdaycart_window, text=f"It's time for a discount! Enter the code {discount_code}, for a 10'%' discount", bg="#fafafa", font=("Arial", 14, 'bold'))
            discount_label.pack(pady=10)

            discount_code_var = StringVar()

            discount_entry = Entry(bdaycart_window, textvariable=discount_code_var, font=("Arial", 12))
            discount_entry.pack(pady=5)

        def apply_discount():
            global discounted_total
            entered_code = discount_code_var.get()
            if entered_code == discount_code:  # Check if entered code matches the retrieved code
                discounted_total = total_price * (1 - discount_percentage / 100)
                total_label.config(text=f"Total Price: €{discounted_total:.2f}")
                feedback_label.config(text="Discount applied successfully!", fg="green")
            else:
                feedback_label.config(text="No such discount code!", fg="red")

        
        apply_discount_button = Button(bdaycart_window, text="Apply Discount", command=apply_discount, font=("Arial", 12), bg="#0078D7", fg="black")
        apply_discount_button.pack(pady=10)

        # Feedback label for discount application status
        feedback_label = Label(bdaycart_window, text="", bg="#fafafa", font=("Arial", 12))
        feedback_label.pack(pady=10)
    else:
        # If no discount, just display the total
        feedback_label = Label(bdaycart_window, text="No discounts available.", bg="#fafafa", font=("Arial", 14, 'bold'))
        feedback_label.pack(pady=10)

                

    #debug
    print(f"Total Price: {total_price:.2f}")
    print(f"Discount Applied: {discount_percentage}%")
    print(f"Discounted Price: €{discounted_total:.2f}")

    total_label = Label(bdaycart_window, text=f"Total Price: €{discounted_total:.2f}", bg="#fafafa", font=("Arial", 14, 'bold'))
    total_label.pack(pady=10)

    Button(bdaycart_window, text="Checkout", command=lambda: checkout(discount_id), font=("Arial", 12), bg="black", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)
    Button(bdaycart_window, text="Close", command=bdaycart_window.destroy, font=("Arial", 12), bg="black", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)
     

def switch_window(menu_function):
    menu_window.withdraw()
    menu_function()

def close_window(window):
    window.withdraw()
    menu_window.deiconify()

def check_password():
    global logged_in_username
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='piz',
                user='root',
                password='ninaanna'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM registration WHERE username=%s", (username,))
            result = cursor.fetchone()

            if result:
                stored_hashed_password = result[1]  # Get the hashed password from the result

                # Verify the entered password with the stored hashed password
                if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                    logged_in_username = username
                    open_menu_window()
                    close_window(root)
            
                else:
                    feedback_label_pass.config(text='Login failed: Incorrect password', fg='red')
            else:
                feedback_label_pass.config(text='Login failed: Username not found', fg='red')

        except Error as e:
            feedback_label_pass.config(text=f"Error: {e}", fg='red')

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        feedback_label_pass.config(text="Please enter both username and password.", fg='red')

Button(root, text='Login', command=check_password, font=("Arial", 12), bg="#0078D7", fg="black", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=20)
Button(root, text='You do not have an account? Register!', command=open_registration_window, font=("Arial", 12), bg="#28A745", fg="black", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)

def desserts_menu():
    global desserts_tree
    desserts_window = Toplevel(menu_window)
    desserts_window.title("Desserts")
    desserts_window.geometry("1000x500")
    desserts_window.configure(bg="#fafafa")
    desserts_window.protocol("WM_DELETE_WINDOW", lambda: close_window(desserts_window))

    desserts_tree = ttk.Treeview(desserts_window)
    desserts_tree.pack(pady=20)
    desserts_tree['columns'] = ('ID', 'Name', 'Price')
    desserts_tree.column('#0', width=0, stretch=NO)
    desserts_tree.column('ID', width=0, stretch=NO)


    for col in desserts_tree['columns']:
        desserts_tree.heading(col, text=col, anchor=CENTER)

    rows = fetch_data("Dessert")
    for row in rows:
        dessert_id, name, price = row
        price_with_euro = f"€{price:.2f}" 
        desserts_tree.insert('', 'end', values=(dessert_id, name, price_with_euro))
    
    Button(desserts_window, text="Back to main menu", command=lambda: close_window(desserts_window), font=("Arial", 12), bg="#0078D7", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)
    Button(desserts_window, text="Add to cart", command=lambda: add_to_cart(desserts_tree, 2, 'dessert'), font=("Arial", 12), bg="#28A745", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)

def pizza_menu():
    global pizza_tree, leaf_image  # Declare leaf_image as global to prevent garbage collection
    pizza_window = Toplevel(menu_window)
    pizza_window.title("Pizza")
    pizza_window.geometry("1000x500")
    pizza_window.configure(bg="#fafafa")
    pizza_window.protocol("WM_DELETE_WINDOW", lambda: close_window(pizza_window))

    resized_leaf_image = resize_image("vegetarian-logo.png", (18, 18))  # Resize to 16x16 or preferred size
    leaf_image = ImageTk.PhotoImage(resized_leaf_image)  # Convert to PhotoImage for tkinter

    # Frame for Treeview and Scrollbars
    frame = Frame(pizza_window)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    pizza_tree = ttk.Treeview(pizza_window)
    pizza_tree.pack(fill=BOTH, expand=True, pady=20)
    pizza_tree['columns'] = ('Id', 'Name', 'Description', 'Vegan', 'Price')
    pizza_tree.column('#0', width=50, stretch=NO)  # Use #0 to display the image in the first column
    # Adjust columns based on expected data size
    pizza_tree.column('Id', width=0, stretch=NO)
    pizza_tree.column('Name', anchor=CENTER, width=100)
    pizza_tree.column('Description', anchor=CENTER, width=600)  # Increased width for description
    pizza_tree.column('Vegan', anchor=CENTER, width=80)
    pizza_tree.column('Price', anchor=CENTER, width=80)

    pizza_tree.heading('Name', text='Name', anchor=CENTER)
    pizza_tree.heading('Description', text='Description', anchor=CENTER)
    pizza_tree.heading('Vegan', text='Vegan', anchor=CENTER)
    pizza_tree.heading('Price', text='Price', anchor=CENTER)
   

    rows = fetch_data("Pizza")
    for row in rows:
        pizza_id, name, description, is_vegetarian, is_vegan, price = row
        price_with_euro = f"€{price:.2f}" 
        # If the pizza is vegetarian, add the leaf image in the first column
        if is_vegetarian == 1:
            pizza_tree.insert('', 'end', text="", image=leaf_image, values=(pizza_id, name, description, is_vegan, price_with_euro))
        else:
            pizza_tree.insert('', 'end', text="", values=(pizza_id, name, description, is_vegan, price_with_euro))

    Button(pizza_window, text="Back to main menu", command=lambda: close_window(pizza_window), font=("Arial", 12), bg="#0078D7", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)
    Button(pizza_window, text="Add to cart", command=lambda: add_to_cart(pizza_tree, 4, 'pizza'), font=("Arial", 12), bg="#28A745", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)

def drink_menu():
    global drink_tree
    drink_window = Toplevel(menu_window)
    drink_window.title("Drinks")
    drink_window.geometry("1000x600")
    drink_window.configure(bg="#fafafa")
    drink_window.protocol("WM_DELETE_WINDOW", lambda: close_window(drink_window))
 
    drink_tree = ttk.Treeview(drink_window)
    drink_tree.pack(pady=20)
    drink_tree['columns'] = ('ID', 'Name', 'Price')
    drink_tree.column('#0', width=0, stretch=NO)
    drink_tree.column('ID', width=0, stretch=NO)

    for col in drink_tree['columns']:
        drink_tree.heading(col, text=col, anchor=CENTER)

    rows = fetch_data("Drink")
    for row in rows:
        drink_id, name, price = row
        price_with_euro = f"€{price:.2f}" 
        drink_tree.insert('', 'end', values=(drink_id, name, price_with_euro))

    Button(drink_window, text="Back to main menu", command=lambda: close_window(drink_window), font=("Arial", 12), bg="#0078D7", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)
    Button(drink_window, text="Add to cart", command=lambda: add_to_cart(drink_tree, 2, 'drink'), font=("Arial", 12), bg="#28A745", fg="white", relief=SOLID, borderwidth=1, padx=10, pady=5).pack(pady=10)


root.mainloop()
