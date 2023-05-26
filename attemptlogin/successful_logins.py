#!/user/bin/env python3

# This will count successful attempts
successful = 0

# open file to read and save to (success_in_file) list
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as success_in_file:

    # read the list lines
    for line in success_in_file:

        # checking each line that has successful login attempts
        if "-] Authorization failed" in line:

            # counting the amount of times found in list
            successful +=1

# will print my statement with the counted number of attempts
print(f"There are {successful} atempts that were a success!")

# this will print the IP Address from 
print(line.split(" ")[-1])
