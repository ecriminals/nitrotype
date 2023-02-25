from nitrotype import Client

client = Client(token="your nt token")
change_username = client.change_user("reaper")
print(change_username)
