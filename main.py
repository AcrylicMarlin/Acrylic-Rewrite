with open('./utils/schema.sql') as file:
    
    for schema in file.read().split(';'):
        print(schema)