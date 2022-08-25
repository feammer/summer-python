import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('food.db')
    curs = conn.cursor()
    custom_input = input("自定义搜索条件\nSELECT * FROM food WHERE ")
    query = 'SELECT * FROM food WHERE ' + custom_input
    curs.execute(query)
    names = [f[0] for f in curs.description]
    for row in curs.fetchall():
        for pair in zip(names, row):
            print('{}: {}'.format(*pair))
        print()
