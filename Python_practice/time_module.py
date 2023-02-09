import time

print (time.ctime(0))  # konwertuje czs wyrazany w sekundach do czynelnego stringa, od czasu kiedy komputer mysli
                        # ze zaczał istnieć, tak zwanego punktu referyncyjnego


print (time.time())  # zwraca sekundy które mineły od punku referyncyjengo (epoch)


print (time.ctime(time.time())) # aktualny czas

time_object = time.localtime()

print(time_object)




localtime = time.strftime(" %B %d %Y %H:%M:%S ",time_object) # <--- Tworzenie wsłasnego formatu daty po wiecej info znaleść 'time.strftime'
print(localtime)


time_string = '20 April, 2020'
time_object2 = time.strptime(time_string, "%d %B, %Y")  
print(time_object2)


# (year, month, day, hour, minute, second, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)