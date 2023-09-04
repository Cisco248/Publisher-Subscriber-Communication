"""This Is Group - 14 Mini Project
        Publisher Subscriber
        Group Members - 22UG2 - 0195 Vimukthi Malshan
                        22UG2 - 0120 Nirmal Senevirathna
                        22UG2 - 0004 Lahiru Dilshan
                        22UG2 - 0034 Nethmini Naduni
                        22UG2 - 0200 Imal Lakpriya
                        22UG2 - 0588 Lakshan Janith
                        
                        ***********************
                        Publisher Side Prrogram
                        ***********************
                        """

import socket
import csv
import threading
import json
import pandas as pd

host = socket.gethostname()
port = 2023
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(5)

#----------------------------------------------------------------------------------------------------------

class Publisher:                                                                                            # This class act like Virtual Publisher
    def __init__(self, conn):
        self.conn = conn

    def sub_id(self):                                                                                       # This function receiving the Subscriber ID
        s_id = conn.recv(1024).decode()
        if not s_id:
            breakpoint
        print("Successfully Connected Subscriber: " + str(s_id))
        subscriber_id_data = "Successfully Connected..! Subscriber: " + str(s_id)
        conn.send(subscriber_id_data.encode())
        pass

    def sub_stock(self):                                                                                    # This function receiving the Stock Code
        stock_code = conn.recv(1024).decode()
        if not stock_code:
            breakpoint
        print("Successfully Entered Stock Code: " + str(stock_code))
        stock_code_data = "Successfully..! Your Stock Code: " + str(stock_code)
        conn.send(stock_code_data.encode())
        pass
        
    def sub_bid(self):                                                                                      # This function receiving the Subscriber Bid Amount
        bid_amount = conn.recv(1024).decode()
        if not bid_amount:
            breakpoint
        print("Bid Value: " + str(bid_amount))
        bid_amount_data = "Successful..! Your Bid Value: " + str(bid_amount)
        conn.send(bid_amount_data.encode())
        pass
        
    def save_bid(self, subscriber_id, stock_code, bid_amount):                                              # This function receiving the Subscriber Details after save details
        
        processed_subscriber_id_data = conn.recv(1024).decode()
        subscriber_id = processed_subscriber_id_data
        
        processed_stock_code_data = conn.recv(1024).decode()
        stock_code = processed_stock_code_data
        
        processed_bid_amount_data = conn.recv(1024).decode()
        bid_amount = processed_bid_amount_data
        
        print(f"Bidding Details : ", processed_subscriber_id_data, processed_stock_code_data, processed_bid_amount_data)
        with open("sym.txt", "a") as file:
            file.write("{} : {} : {}\n".format(subscriber_id, stock_code, bid_amount))

#----------------------------------------------------------------------------------------------------------

def csv_data():                                                                                             # Read the csv file after send the Subscriber
    with open(r'C:\\Users\\Lahiru\\Desktop\\Publisher - Subscriber Mini Project\\data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        selected_rows = rows[:8]
        stock_data = []
        for row in selected_rows:
            sr1 = "Stock Code: " + row['Stock_Code']
            sr2 = "Base Price: " + row['Base_Price']
            sr3 = "Security: " + row['Security']
            sr4 = "Profit: " + row['Profit']
            stock_data.append([sr1, sr2, sr3, sr4])

    stock_data_json = json.dumps(stock_data)
    conn.send(stock_data_json.encode())

#---------------------------------------------------------------------------------------------------------

def handle_client(conn, address):                                                                          # This Function Handle the Clients
    print("Connected Client From: " + str(address))
    
    publisher = Publisher(conn)
    publisher.sub_id()
    csv_data()  
    publisher.sub_stock()
    publisher.sub_bid()
    publisher.save_bid('subscriber_id', 'stock_code', 'bid_amount')
    
    conn.close()                                                                                           # Close the connection
    
#--------------------------------------------------------------------------------------------------------

if __name__ == "__main__":                                                                                 # Start Main fuctions tasks
    while True:
        conn, address = server_socket.accept()
        subscriber_thread = threading.Thread(target=handle_client, args=(conn, address))
        subscriber_thread.start()
