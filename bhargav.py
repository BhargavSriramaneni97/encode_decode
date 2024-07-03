import base64

name = "Bhargav"
es = base64.b64encode(name.encode('utf-8')).decode('utf-8')
print(es)

encstr = 'Qmhhcmdhdg=='
db = base64.b64decode(encstr)
ds = db.decode('utf-8')
print(ds)