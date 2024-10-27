from settings import connection

# CREATE TABLE
# INSERT INTO
# SELECT * FROM


cursor = connection.cursor()


def create_table(fields, table_name):
    try:
    
        query_data = []
        
        for field in fields:
            for col_name, col_properties in field.items():
                col_type = col_properties.get("type")
                col_length = col_properties.get("length")
                col_is_null =  " NOT NULL" if col_properties.get("is_null") else ""
                
                col_length = f"({col_length})" if col_length else ""
                
                query_data.append(f"{col_name} {col_type}{col_length}{col_is_null}")
                
        query_str = ",".join(query_data)
        query = f"CREATE TABLE {table_name}({query_str})"
        
        cursor.execute(query)
        connection.commit()
        
        print("CREATE TABLE SUCCESFULL")
    
    except Exception as e:
        print(f"{e}")
    
    
    
    


def insert_column(datas):
    try:
        keys = []
        values = []
        
        for col_name, col_value in datas.items():
            keys.append(col_name)
            values.append(f"'{col_value}'")


        keys_str = ", ".join(keys)
        values_str = ', '.join(values)
        
        query = f"INSERT INTO users ({keys_str}) VALUES ({values_str})"
        
        cursor.execute(query)
        connection.commit()
        
        
        print("Successfully inserted")
        
    except Exception as e:
        print(e)
    
    
    
    
# SELECT name, surname FROM users
    
    
    
def select_column(table_name, fields=None):
    if not fields:
        query = f"SELECT * FROM {table_name}"
    else:
        query = f"SELECT {fields} FROM {table_name}"
        
    cursor.execute(query)
    data = cursor.fetchall()
    
    print(data)
        
    

