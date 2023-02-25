# NitroType
#### Python-based library for interacting with [NitroType](https://nitrotype.com)

# Progress
95%, finished basic features will add more later!

# Examples/Usage
##### Account Creating
```py
from nitrotype import Client

client = Client(token="") # account generating requires no token so :), feel free to still add your account token. The library will just ignore it for this certain request only.
new_account = client.create(
    username="NTPythonTest",
    password="",
    email="",  # email is not required.
    wpm="115",
    accuracy="95",
    tz="",  # timezone is not required either.
)
print(new_account)
```
##### Open/Claim Mystery Box
```py
from nitrotype import Client

client = Client(token="your nt auth token.")
redeem = client.daily()
print(redeem)
```
##### Change Username
```py
from nitrotype import Client

client = Client(token="your nt auth token.")
new_user = client.change_user("new username.") # username must be 6+ chars.
print(new_user)
```
##### Change Social Settings
```py
from nitrotype import Client

client = Client(token="your nt auth token.")
new_settings = client.social(
    status=True, # True = Online, False = Offline
    allowFriendRequests=True,
    lookingForTeam=True
) 
print(new_settings)
```
##### Change Account Settings
```py
from nitrotype import Client

client = Client(token="your nt auth token.")
new_settings = client.account(
    firstname="",
    lastname="",
    email="",
    password="" # password can be left as none.
) 
print(new_settings)
```