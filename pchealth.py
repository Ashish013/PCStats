# Under Development for upcoming project:
# The module is made functional as of now but may not be for long.

#if __name__=="__main__":
    #print("This is a module to be exeuted by main file")

if __name__=="__main__":
    
    import psutil
    import sys
    from psutil._common import bytes2human

    class SystemInfo():

    """
    A class used to return SystemInfo
    ...

    Attributes
    ----------
    None
    
    ...

    Methods
    -------
    userinfo(self)
        Prints the user info 
        
    batteryinfo(self)
        Prints the battery stats.

    system_temp(self)
        Prints the system's temperature

    fan_speed(self)
        Prints the system's fan_speed

    memory_info(self)
        Prints memory stats of system

    virt_memory(self)
        Prints the virtual memory stats of system

    """
        
        def userinfo(self):
            print("User Info:")
            uinfo = psutil.users()
            print("The users connected to the sysytem at present are : ",end='')
            for term in range(0,len(uinfo)):
                print(f"{uinfo[term].name}",end=",")
            print("\n")



        def batteryinfo(self):
            print("Battery Info:")
            battery = psutil.sensors_battery()

            if battery!= None:
                sec = battery.secsleft
                min ,sec = divmod(sec,60)
                hour,min = divmod(min,60)
                if hour >=0:
                    print(f"Time remaining for complete discharge is {hour}hr: {min}min: {sec}sec")
                    print(f"Battery percentage left: {battery.percent}%")
                    if battery.power_plugged == True:
                        print("Charger: Connected")
                    else:
                        print("Charger: Not Connected")
                    print("\n")
                else:
                    print(f"Battery percentage left: {battery.percent}%")
                    print("\n")

                if battery.percent < 20 and battery.power_plugged == False:
                    print(f"Please connect charger.\nBattery Percentage left is {battery.percent}%\n")   
                if battery.percent > 90 and battery.power_plugged == True:
                    print(f"Please disconnect charger.\nBattery Percentage is {battery.percent}%\n")            
            else:
                print("Battery Status Information can't be determined!")
                print("\n")



        def system_temp(self):
            print("System's Temperature:")
            try:
                temp = psutil.sensors_temperature()
                if len(temp) !=0:
                    print("The hardware and their respective temperatuers are: ")
                    for key,value in temp:
                        print(f"{key:^6}  {value[0].current:^6} C")
                else:
                    print("This functionality is not supported by your System\n")
            except:
                print("This functionality is not supported by current Operating System\n")


        def fan_speed(self):
            print("Fan Speed :")
            try:
                fans = psutil.sensors_fans()
                if len(fans)!= 0 :
                    for hardware,fan in fans:
                        print(f"{fan.label:^6}  {fan.current:^6}")
                else:
                    print("This functionality is not supported by your System\n")
            except:
                    print("This functionality is not supported by current Operating System\n")



        def memory_info(self):
            print("Disk Usage: ")
            lis=[]
            template = "{0:^16} {1:^16} {2:^16} {3:^16}"
            disks = psutil.disk_partitions(all=False)
            for disk in disks:
                lis.append(disk.device)
            for drive in lis:
                print(drive)
                memory = psutil.disk_usage(drive)
                print(template.format("Total Memory ","Free Memory","Used Memory","Percent of memory available"))
                print(template.format(bytes2human(memory.total),bytes2human(memory.used),bytes2human(memory.free),str(memory.percent)+ "%"))
            print("\n")



        def virt_memory(self):
            print("Virtual Memory Stats: ")
            template = "{0:^16} {1:^16} {2:^16} {3:^16} {4:^16}"
            virtual = psutil.virtual_memory()
            print(template.format("Total ","Available memory","Used memory","Free memory","Percent"))
            print(template.format(bytes2human(virtual.total),bytes2human(virtual.available),bytes2human(virtual.used),bytes2human(virtual.free),str(virtual.percent)+ "%"))
            print("\n")
        

# To demonstrate the usecases of the module:


info = SystemInfo()

info.userinfo()
info.batteryinfo()
info.system_temp()
info.fan_speed()
info.memory_info()
info.virt_memory()
