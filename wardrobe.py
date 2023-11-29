import sqlalchemy
import dbconnect
import sys

def get_shirts(engine):
    query = 'SELECT * FROM shirts'

    with engine.connect() as sql:
        shirts = sql.execute(sqlalchemy.text(query))

    return shirts

def get_pants(engine):
    query = 'SELECT * FROM pants'

    with engine.connect() as sql:
        pants = sql.execute(sqlalchemy.text(query))

    return pants

def add_shirts(engine, shirt_id, shirt_type):
    query = f"INSERT INTO shirts VALUES ('{shirt_id}', '{shirt_type}');"
    
    with engine.connect() as sql:
        sql.execute(sqlalchemy.text(query))
        sql.commit()

def add_pants(engine, pant_id, pant_type):
    query = f"INSERT INTO pants VALUES ('{pant_id}', '{pant_type}');"
    with engine.connect() as sql:
        sql.execute(sqlalchemy.text(query))
        sql.commit()

def list_shirts(shirts):
    print('\n-------------------------------------------------------')
    print('Shirts:')
    for shirt in shirts:
        print(f'Shirt id: {shirt[0]} Shirt type: {shirt[1]}')

def list_pants(pants):
    print('\nPants:')
    for pant in pants:
        print(f'Pant id: {pant[0]} Pant type: {pant[1]}')
    print('-------------------------------------------------------\n')

def main():
    engine = dbconnect.connect()
    shirts = get_shirts(engine)
    pants = get_pants(engine)
    
    #add_shirts(engine, '1', 'tshirt')
    #add_pants(engine, '1', 'jeans')
    list_shirts(shirts)
    list_pants(pants)


    
    

if __name__ == '__main__':
    main()
