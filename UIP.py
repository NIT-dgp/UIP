from scheduler import scheduler

if __name__ == "__main__":
  print("Press 1 to connect to internet or any other key to use this application in offline mode")
  offline = int(input()) != 1
  scheduler(offline)
