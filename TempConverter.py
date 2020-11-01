#Zwolfy on Github

#Check for number input
while True:
    try:
        temp = float(input('\nEnter a temperature: '))
        break
    except:
        print('Please enter numbers only!\n')

tempType =  input('Is this temperature in Fahrenheit/Celcius/Kelvin?  Enter C, F or K: ').upper().strip()

#Checks for correct response
while tempType[0] != 'C' and tempType[0] != 'F' and tempType[0] != 'K':
    tempType = input('\nError: Please enter C, F or K: ').upper().strip()

#Convert temps
if tempType == 'F':
    tempF = temp
    tempC = round((tempF - 32)/1.8, 2)
    tempK = round((tempF + 459.67)/1.8, 2)
elif tempType == 'C':
    tempC = temp
    tempF = round((tempC * 1.8) + 32, 2)
    tempK = round(tempC + 273.15, 2)
elif tempType == 'K':
    tempK = temp
    tempC = round(tempK - 273.15, 2)
    tempF = round((tempK * 1.8 ) - 459.67, 2)

#Print values
print('\nConverstion table:')    
print(tempC, 'C')
print(tempK, 'K')
print(tempF, 'F')
    

