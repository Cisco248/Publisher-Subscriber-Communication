"""This Is Group - 14 Mini Project
        Publisher Subscriber
        Group Members - 22UG2 - 0195 Vimukthi Malshan
                        22UG2 - 0120 Nirmal Senevirathna
                        22UG2 - 0004 Lahiru Dilshan
                        22UG2 - 0034 Nethmini Naduni
                        22UG2 - 0200 Imal Lakpriya
                        22UG2 - 0588 Lakshan Janith
                        
                        ************************
                        Subscriber Side Prrogram
                        ************************
                        """
import socket
import pandas as pd
import json

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def subscriber_program():                                                                       # Start The Subscriber Function
    host = socket.gethostname()
    port = 2023

    subscriber_socket = socket.socket()
    subscriber_socket.connect((host, port))

    try:             
        print("")
        subscriber_id = input(" ---> Input The Subscriber ID: ")                                # Get the Subscriber ID
        subscriber_socket.send(subscriber_id.encode())                                          # Encoding the Subscriber ID data
        subscriber_data = subscriber_socket.recv(1024).decode()                                 # Send the Subscriber ID Data to Publisher
        print(" <--- " + subscriber_data)                                                       # After Print The Subscriber ID
        
        print("")
        rec_data = subscriber_socket.recv(4096).decode()                                        # Recieving the csv file Data
        stock_data = json.loads(rec_data)

        for row in stock_data:                                                                  # Before the Print List it's data
            print(f"{row}\n")                                                                   # Print Listed Data
                
        
        print("")    
        stock_code = input(" ---> Enter the Stock Code: ")                                      # Get the Subscriber Stock Code
        subscriber_socket.send(stock_code.encode())                                             # Encoding the Subscriber Stock Code Data
        stock_code_data = subscriber_socket.recv(1024).decode()                                 # Send the Subscriber Stock Code Data to Publisher
        print(" <--- " + stock_code_data)                                                       # After Print The Subscriber ID
        stock_code_to_update = stock_code                                                       # Selected Stock Code Update

        print("")
        bid_amount = input(" ---> Enter the Bid Amount: ")                                      # Get the Subscriber Bid Amount
        subscriber_socket.send(bid_amount.encode())                                             # Encoding the Subscriber Bid Amount Data
        bid_amount_data = subscriber_socket.recv(1024).decode()                                 # Send the Subscriber Bid Amount Data to Publisher
        print(" <--- " + bid_amount_data)                                                       # After Print The Subscriber Bid Amount
        new_base_price = bid_amount                                                             # Selected Stock Code Update There Bid Amount Value 
        
        processed_subscriber_id_data = (subscriber_id.encode())                                 # Send the Subscriber ID Value to Publisher Save Bid Function
        subscriber_socket.send(processed_subscriber_id_data)
        
        processed_stock_code_data = (stock_code.encode())                                       # Send the Subscriber Stock Code Value to Publisher Save Bid Function
        subscriber_socket.send(processed_stock_code_data)
        
        processed_bid_amount_data = (bid_amount.encode())                                       # Send the Subscriber Bid Amount Value to Publisher Save Bid Function
        subscriber_socket.send(processed_bid_amount_data)
        
        bid_id = int(processed_subscriber_id_data) 
        bid_code = (processed_stock_code_data.decode('utf-8')) 
        bid_value = float(processed_bid_amount_data)
        print("")
        
        print("\t********************")
        print(f"\tUpdate Successful..!\n\t--------------------\n \tSubscriber ID : {bid_id}\n \tStock Code : {bid_code}\n \tHighest Bid : {bid_value}")
        print("\t********************")                                                         # After Print The Subscriber Deatils like a Updated!
        
        csv_file_path = 'Desktop\\Publisher - Subscriber Mini Project\\data.csv'                # Update the Subscriber Bid Amount 
        data_file = pd.read_csv(csv_file_path)
        data_file.loc[data_file['Stock_Code'] == stock_code_to_update, 'Base_Price'] = new_base_price
        data_file.to_csv(csv_file_path, index=False)

    except Exception as e:
        print("")
        print("An error occurred:", str(e))
        print("")
    finally:
        subscriber_socket.close()                                                               # Close the Subscriber Connection
        print("")
        print(" <--> Have a Lucky Day !!!...")                                                  # Finall Message After close connection
        print("")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':                                                                      # Start The Main Function Tasks
    subscriber_program()
