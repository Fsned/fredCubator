Project to handle passwords safely and locally, without the need to remember some account and login to see your passwords, but instead keep them on a local USB-stick, as well as the server script to decode and fetch them.

Files:

- *DB.py
database to contain stored passwords and their references

- server.py
script for external storage device, to create and fetch posts in DB

- client.py
script for pc, to communicate with server to request existing or new passwords.