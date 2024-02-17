# 1


# -------------------------------   2   ------------------------------------

# hint (i'am linux user) i dont know if this command execute in your machine or not """os.path.expanduser('~')""" but its for get path from desktop

import os, sqlite3

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Create the directory if it doesn't exist
python_dir_path = os.path.join(desktop_path, 'python')

if not os.path.exists(python_dir_path):
    os.makedirs(python_dir_path)
    print("Directory 'python' created on the desktop.")
else:
    print("Directory 'python' already exists on the desktop.")


# create file index.py
main_file_path = os.path.join(python_dir_path, 'index.py')
with open(main_file_path, 'w') as file:
    file.write("# Your Python code goes here")

# create db file 
db_file_path = os.path.join(python_dir_path, 'elzero.db')

db = sqlite3.connect(db_file_path)

cr = db.cursor()


cr.execute('''
          CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            email TEXT NOT NULL UNIQUE,
            birthdate DATE UNIQUE
          )
          ''')

print("Table 'users' created in the database.")



# ---------------------------------  3   ------------------------------------

dummy_users = [
    {"id": 1, "name": "Emily Davis", "email": "emily@example.com", "birthdate": "1990-12-15"},
    {"id": 2, "name": "Christopher Martinez", "email": "chris@example.com", "birthdate": "1988-07-25"},
    {"id": 3, "name": "Emma Thompson", "email": "emma@example.com", "birthdate": "1995-03-08"},
    {"id": 4, "name": "Daniel Anderson", "email": "daniel@example.com", "birthdate": "1986-09-03"},
    {"id": 5, "name": "Sophia Walker", "email": "sophia@example.com", "birthdate": "1992-11-20"}
]


# Insert dummy users
for user in dummy_users:
    user_tuple = (user.get('id'), user.get('name'), user.get('email'), user.get('birthdate'))
    
    # get user if exist in db
    cr.execute(f'select * from users where id = ?', (user.get("id"),))
    
    fetched_user = cr.fetchone()
    
    if fetched_user:
      error_message = f'this email {fetched_user[2]} already used :|'
      raise Exception(error_message)
    else:
      cr.execute("""
          INSERT INTO users(id, name, email, birthdate)
          VALUES(?,?,?,?)
      """, user_tuple)

# Commit the transaction
db.commit()



# ---------------------------------  4  ------------------------------------




user_id = int(input('Enter user id: ').strip())

# first get user from database
cr.execute('SELECT * FROM USERS WHERE id = ?', (user_id,))

user = cr.fetchone()

print(user)

if user:
  # delete user 
  cr.execute('DELETE FROM USERS WHERE id = ?', (user[0],))
  db.commit()
else: 
  raise Exception('User Not Found.')







