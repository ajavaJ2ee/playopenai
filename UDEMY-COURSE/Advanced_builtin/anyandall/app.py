friends=[
    {
        'name':'Abhi',
        'location':'L1'
    },
    {
        'name':'Abhi2',
        'location':'L2'
    },
    {
        'name':'Abhi3',
        'location':'L3'
    },
    {
        'name':'Abhi4',
        'location':'L4'
    }
]

your_location=input('Location please')

friends_nearby=[friend for friend in friends if friend['location']==your_location]
if any(friends_nearby):
    print('Not alone')

