# MeanHash
A new hash for password hashing
## Use Case
The main use case for the hash is to store password in a safe way where the backend of any app doesn't have acces to the real password of the registered users.
![Use case diagram](https://github.com/SergioLV/MeanHash/blob/main/MeanHash-UseCase.png)

## Flow chart
Here, the backend of the app interacts with the user registration flow, hashing the password and asociating it with a username. After that, when a user tries to log in, we can check for registered users hashing the login password and comparing it with the one stored at the app's database.
![Flow chart diagram](https://github.com/SergioLV/MeanHash/blob/main/MeanHash%20Flowchart.png)

## Calculate the hash of a string 
```
python meanHash.py -i string
```

## Calculate the hash of a file
```
python meanHash.py -f file
```

## Calculate entropy
```
python meanHash.py -e string
```

