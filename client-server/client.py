import socket


# create client socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# initialize and empty list to hold the alerts (an array of strings)
alerts = []

# ask user for the operation they want to perform
operation = input(
    """
        Net-Centric Computing Assignment 
        
        Select an option to perform an operation:
        1 - Addidtion
        2 - Subtraction 
        3 - Multiplication
        4 - Division 
        5 - Modulus
         
    """
)

# add operation to alerts
alerts.append(str(operation))

# ask user for the two values on which the operation is performed
first_variable = input('enter the first value: >>>')
second_variable = input('enter the second value: >>> ')

# add the values to the alerts
alerts.append(str(first_variable))
alerts.append(str(second_variable))

# format alerts into [operation,first_varible,second_variable]
alerts = ','.join(alerts)

# send alerts to client-side
socket.sendto(alerts, ('localhost', 1998))

# receive result from server
server_result, server_address = socket.recvfrom(1024*3)
print('server result: ' + server_result)

# close connection between client and server
socket.close()