
import consul_entry as ce

# Putting several keys and values

ce.PutKv(key="foo/bar1", val="val1")
ce.PutKv(key="foo/bar2", val="val2")
ce.PutKv(key="foo/bar3", val="val3")
ce.PutKv(key="keys1", val="val1")



# Get all keys under /foo
ce.GetKv(key="foo", recurse=True)

# Get all keys
ce.GetKv(key="",recurse=True)

# Delete all the keys under /foo
ce.DeleteKv(key='foo/', recurse=True)

# Get all the remaining keys
ce.GetKv(key="", recurse=True)

# Delete 'keys1' key
ce.DeleteKv(key='keys1')

# Get all the remaining keys
ce.GetKv(key="", recurse=True)