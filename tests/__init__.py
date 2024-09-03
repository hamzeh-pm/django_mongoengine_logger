from mongoengine import connect

db_name = "django_mongoengine_logger"
username = "root"
password = "rootpassword"
host = "localhost"  # e.g., 'localhost' or 'mongodb+srv://cluster0.mongodb.net'

connect(
    db=db_name,
    username=username,
    password=password,
    host=host,
    # port=27017,  # Uncomment and set if you need to specify a port
    uuidRepresentation="standard",
)
