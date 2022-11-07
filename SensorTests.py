import serial as s
import time
import csv


def forceValueLog(serPort):
    #Create File
    today = time.localtime()
    month, year, day, hour, minute = today.tm_mon, today.tm_year, today.tm_mday, today.tm_hour, today.tm_min
    file_name = '/Users/marissaklein/Desktop/4_27_ThrusterForce/ForceThermoValues'+str(month)+str(year)+str(day)+str(hour)+str(minute)+'.csv'
    header = ['Unix Time','Arduino Force Value','Actual Force','Thermocouple Value One','Thermocouple Value Two']
    f = open(file_name,'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()
    
    while(True):
        try:
            #Read Serial Port
            ser = s.Serial(serPort,9600) #Needs Serial Port, times out after 10 seconds
            buffer = ser.readline()
            line = ser.readline()
            ser.close()
            
            #Decode line
            true_line = line.decode("unicode_escape")
            val = []
            val.append(true_line)
            
            values = true_line.split(',')

            
            #Print forces and thermocouple
            force_val = values[0]
            thermo_val_one = values[1]
            thermo_val_two = values[2]
            actualForce = float(force_val)/1614.2204
            
            
            print(force_val)
            print(actualForce)
            print(thermo_val_one)
            print(thermo_val_two)
            print('')
            
            #Log to CSV
            csv_log = [time.time(),force_val,actualForce,thermo_val_one,thermo_val_two] #Unix time, Arduino Output, Actual Force, and thermocouple Output
            f = open(file_name,'a')
            writer = csv.writer(f)
            writer.writerow(csv_log)
            f.close()
        
        #Kill function with keyboard interrupt
        except KeyboardInterrupt:
            break
        
 
