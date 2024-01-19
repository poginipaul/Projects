
try:
    import psycopg2 as pg #pip3 install psycopg2-binary
    import os # export VAR=<value>

except ImportError as i_err:
    print(i_err)

db_vars = {
    'host': '192.168.100.164',
    'username': 'paul',
    'password': os.getenv('DB_CONN_PASSWD'), # extract the exported env variable.
    'dbname': 'paul_db',
    'port': 5432
}

def dbase():
    try:
        with pg.connect(
            dbname = db_vars['dbname'],
            user = db_vars['username'],
            password = db_vars['password'],
            host = db_vars['host'],
            port = db_vars['port']
        ) as db_connect:
            db_cursor = db_connect.cursor()

            return db_cursor
    
    except pg.Error as pg_err:
        print(pg_err)

if __name__ == "__main__":
    dbase()        
