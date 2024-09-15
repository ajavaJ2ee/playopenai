from avro import schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

# Define the Avro schema
schema_json = '''
{
    "type": "record",
    "name": "Person",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}
'''

avro_schema = schema.parse(schema_json)

# Define the Avro message
message = {"name": "Alice", "age": 30}

# Validate the message against the schema
try:
    # Write the message to a temporary file
    with open('temp.avro', 'wb') as f:
        writer = DataFileWriter(f, DatumWriter(), avro_schema)
        writer.append(message)
        writer.close()

    # Read the message back from the temporary file and validate it
    with open('temp.avro', 'rb') as f:
        reader = DataFileReader(f, DatumReader())
        for record in reader:
            pass
        reader.close()

    print("Message is valid")
except schema.AvroException as e:
    print("Schema error: %s" % e)
except ValueError as e:
    print("Validation error: %s" % e)
finally:
    # Delete the temporary file
    import os
    os.remove('temp.avro')
