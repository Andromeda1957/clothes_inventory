import sqlalchemy


engine = sqlalchemy.create_engine('mysql+pymysql://dbuser:dbpass@127.0.0.1:3306/clothes_inventory', echo=True)
check = sqlalchemy.inspect(engine)
check.get_table_names()
