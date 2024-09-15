import fastavro

# Define the Avro schema
schema = {
    "type": "record",
    "name": "Person",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}

# Define the Avro message
message = {"name": "Alice", "age": 30}

# Validate the message against the schema
try:
    fastavro.validate(message, schema)
    print("Message is valid")
except fastavro.schema.SchemaError as e:
    print("Schema error: %s" % e)
except fastavro.validation.ValidationError as e:
    print("Validation error: %s" % e)
