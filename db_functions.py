import psycopg2 as psycopg2


def set_connection():
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    cur = conn.cursor()


#Insert in database
def insert_product():
    pass

def insert_store():
    pass

def insert_local():
    pass

#Get info
def get_product():
    pass

def get_stores():
    pass

def get_locals():
    pass

#Delete
def delete_product():
    pass

def delete_stores():
    pass

def delete_locals():
    pass

#Update
def update_product():
    pass

def update_stores():
    pass

def update_locals():
    pass