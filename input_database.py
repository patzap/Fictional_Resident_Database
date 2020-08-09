import sqlite3
from Residents import Residents
from Suite import Suite


conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE residents(

            res_id INT PRIMARY KEY,
            res_name TEXT,
            date_occup TEXT,
            care_type TEXT,
            style_suite TEXT
    )""") 


def add_residents(res):

    with conn:
        c.execute("""INSERT INTO residents VALUES (:res_id, :res_name, :date_occup, :care_type, :style_suite)""", 
                                                    {'res_id': res.res_id, 
                                                    'res_name': res.res_name, 
                                                    'date_occup': res.date_occup,
                                                    'care_type': res.care_type,
                                                    'style_suite': res.style_suite})

def update(res):

    res_input = input("Choose 1 for update care type OR 2 for style of suite")

    if res_input == 1:

        print("Choose the style of suite you prefer")


def remove(res):

    with conn:
        c.execute("""DELETE FROM residents WHERE res_name = :res_name""", {'res_name': res.res_name})

        


def name_res(res_name):
    c.execute("""SELECT * FROM residents WHERE res_name = :res_name""", {'res_name': res.res_name})
    return c.fetchall()

'''
def name_res():
    c.execute("""SELECT * FROM residents """)
    return c.fetchall()
'''

res1 = Residents(1, 'Master Roshi', "2018-07-11", 'Independant', 'Septile')

add_residents(res1)

#remove(res1)

res = name_res('Master Roshi')

print(res)








