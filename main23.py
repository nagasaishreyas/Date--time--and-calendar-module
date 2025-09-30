stu = {'id1':
     {'name': ['shreyas'],
       'grade': [7],
       'email'; ['shreyaskuntumallgmail.com']
       },
  'id1':
     {'name': ['shreyuyas'],
       'grade': [9],
       'email'; ['shreyaskuntumalla@g.com']
       },
   'id1':
     {'name': ['shrsytheyas'],
       'grade': [8],
       'email'; ['shrentumalla@gmail.com']
       },
   'id1':
     {'name': ['shreyaguyedguysdfs'],
       'grade': [1],
       'email'; ['shreyauntumalla@gmail.com']
       }
     
}

res = {}

for key,value in stu.item():
    if value not in res.values():
        res[key] = value