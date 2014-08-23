
from xmlrpc.client import ServerProxy
# Create Connection to remote host

def test_rpc_connection():
    s = ServerProxy('http://localhost:15000', allow_none=True)
    key1 = 'foot'
    value1 = 'bart'
    key2 = 'slist'
    value2 = [1,2,3]
    s.set(key1, value1)  # call set method to set key value (foo->bar)
    s.set(key2, value2) # # call set method to set key value 
    s.keys() # Read keys
    assert s.get(key1) == value1  # get value for key foo
    assert s.get(key2) == value2
    s.delete(key1)  # delete key spam
    s.exists(key1)  # check if key exists
    return 
    
test_rpc_connection()