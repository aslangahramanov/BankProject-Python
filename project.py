# Register

# Login

# Kartlar

# Kocurme Funksionalligi

# Odenis etme funksionalligi


# user_data = [
#             {"id": {"type": "SERIAL PRIMARY KEY"}},
#             {"name": {"type": "VARCHAR", "length": 100, "is_null": True}}, 
#             {"surname": {"type": "VARCHAR", "length": 100, "is_null": True}}, 
#             {"email": {"type": "VARCHAR", "length": 100, "is_null": True}}]




# query_data = []



# for field in user_data:
#     for col_name, col_properties in field.items():
#         col_type = col_properties.get("type")
#         col_length = col_properties.get("length")
#         col_is_null =  " NOT NULL" if col_properties.get("is_null") else ""
        
#         col_length = f"({col_length})" if col_length else ""
        
#         query_data.append(f"{col_name} {col_type}{col_length}{col_is_null}")



# query_str = ",".join(query_data)



# query = f"CREATE TABLE user({query_str})"
        
        
# print(query)
        
        
# # CREATE TABLE user(
# #     id SERIAL PRIMARY KEY,
# #     name VARCHAR(255) NOT NULL,
# # )
        
        
        




    
    

# INSERT INTO users (name, surname, email) VALUES('', '', '')
    
    
    
    
    
# def insert_column(datas):
#     keys = []
#     values = []
    
#     for col_name, col_value in datas.items():
#         keys.append(col_name)
#         values.append(col_value)


#     keys_str = ", ".join(keys)
#     values_str = ", ".join(values)
    
#     query = f"INSERT INTO users ({keys_str}) VALUES ({values_str})"
    
#     print(query)
    
# insert_column(user_data)
    