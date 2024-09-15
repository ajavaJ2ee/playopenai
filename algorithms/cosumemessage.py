import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumReader

# Load the Avro schema from a file
#user_file= open()
#csv_file=open('csv_file.txt','r')

#schema = avro.schema.Parse(open("user.avsc", "r"))
schema = avro.schema.parse((open("user.avsc", "r").read()))

# Open the Avro data file for reading
reader = DataFileReader(open("user.avro", "r"), DatumReader())

# Iterate over the records in the data file
for record in reader:
    # Deserialize the record using the schema
    name = record["name"]
    age = record["age"]
    address = record.get("address")  # Use .get() to handle optional field

    # Do something with the deserialized data (e.g. print it)
    print(f"Name: {name}, Age: {age}, Address: {address}")

# Close the data file
reader.close()
