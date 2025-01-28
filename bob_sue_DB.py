import shelve
bob = {'name': 'Bob Jones', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': 'None'}

#DB test
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
