data = [{
    'id': "TC_002_001",
    'description':'Global notification is enable',
    'globalNotification':True,
    'customNotification':False,
    'expected':0
},
{
    'id': "TC_002_002",
    'description':'Global notification is disable, Custom notification is turn on',
    'globalNotification':False,
    'customNotification':True,
    'expected':1
},
{'id': "TC_002_003",
    'description':'Global notification is disable, Custom notification is turn on',
    'globalNotification':False,
    'customNotification':False,
    'expected':0}
]