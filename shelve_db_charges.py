from bob_sue_DB import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.5
db['sue'] = sus
db['tom'] = tom
db.close()
