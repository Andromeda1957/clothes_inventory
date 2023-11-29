import sqlalchemy as sa
import dbconnect

def main():
    engine = dbconnect.connect()

    with engine.connect() as con:
        shirts = con.execute(sa.text('SELECT * FROM shirts'))
        pants = con.execute(sa.text('SELECT * FROM pants'))
        for shirt in shirts:
            print(row)
            print(row[0])


if __name__ == '__main__':
    main()
