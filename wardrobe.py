import sys
import sqlalchemy
import dbconnect

def get_items(engine, item):
    query = f"SELECT * FROM {item}"

    with engine.connect() as sql:
        items = sql.execute(sqlalchemy.text(query))

    return items

def add_item(engine, table, item_id, item_type):
    query = f"INSERT INTO {table} VALUES ('{item_id}', '{item_type}');"
    
    with engine.connect() as sql:
        sql.execute(sqlalchemy.text(query))
        sql.commit()

def delete_item(engine, table, item_id):
    query = f"DELETE FROM {table} WHERE id={item_id}"

    with engine.connect() as sql:
        sql.execute(sqlalchemy.text(query))
        sql.commit()

def update_item(engine, table, item_id, item_type):
    query = f"UPDATE {table} SET type = '{item_type}' WHERE id = {item_id};"
    
    with engine.connect() as sql:
        sql.execute(sqlalchemy.text(query))
        sql.commit()

def list_shirts(shirts):
    print('\n-------------------------------------------------------')
    print('Shirts:')

    for shirt in shirts:
        print(f'Shirt id: {shirt[0]} Shirt type: {shirt[1]}')

    print('-------------------------------------------------------\n')

def list_pants(pants):
    print('\n-------------------------------------------------------')
    print('Pants:')

    for pant in pants:
        print(f'Pant id: {pant[0]} Pant type: {pant[1]}')

    print('-------------------------------------------------------\n')

def find_pants(pants):
    pass

def find_shirts(shirts):
    pass

def build_outfit(shirts, pants):
    pass

def help_menu():
    print('python3 wardrobe.py <option> <id> <type>')
    print('Options: ')
    print('\tshirt <id>')
    print('\tpants <id')
    print('\taddshirt <id> <type>')
    print('\taddpants <id> <type>')
    print('\tupdateshirt <id> <type>')
    print('\tupdatepants <id> <type>')
    print('\tdeleteshirt <id>')
    print('\tdeletepants <id>')
    print('\tlistshirts')
    print('\tlistpants')

def main():
    engine = dbconnect.connect()
    shirts = get_items(engine, 'shirts')
    pants = get_items(engine, 'pants')
   
    if len(sys.argv) < 2:
        help_menu()
        exit()
    
    if sys.argv[1] == 'addshirt':
        add_item(engine, 'shirts', sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'addpants':
        add_item(engine, 'pants', sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'updateshirt':
        update_item(engine, 'shirts', sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'updatepants':
        update_item(engine, 'pants', sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'listshirts':
        list_shirts(shirts)
    elif sys.argv[1] == 'listpants':
        list_pants(pants)
    elif sys.argv[1] == 'deleteshirt':
        delete_item(engine, 'shirts', sys.argv[2])
    elif sys.argv[1] == 'deletepants':
        delete_item(engine, 'pants', sys.argv[2])
    elif sys.argv[1] == 'shirts':
        build_outfit(shirts, pants)
    elif sys.argv[1] == 'pants':
        build_outfit(shirts, pants)
    else:
        help_menu()


if __name__ == '__main__':
    main()
