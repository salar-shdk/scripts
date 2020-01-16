#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from instagram_private_api import Client, ClientCompatPatch

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == '-h' :
        print('[username] [password] [target_username] [pages_count]')
        exit()
    target = args[2]
    pages = int(args[3])
    user_name = args[0]
    password = args[1]
    max=0

    api = Client(user_name, password)
    

    for r in range(pages):
        #print('max',max)
        activitys = api.news(max_id = max)
        print(activitys)
        #if r>0: print(activitys)
        #print(activitys['next_max_id'])
        max = activitys['next_max_id']
        #print(activitys)
        for i in activitys['stories']:
            #print(i,'\n\n\n')
            if target in i['args']['text'] and 'following' in i['args']['text']:
                print('started following :')
                row_ids = i['args']['text'].split('following ')[1][:-1]
                more=False
                if 'others' in row_ids:
                    row_ids = row_ids.split('and ')[0].replace(',','and')
                    more = True
                for k in row_ids.split('and '):
                    print('https://www.instagram.com/'+k)
                if more : print('and some others')
            elif target in i['args']['text'] and 'liked' in i['args']['text']:
                ids = []
                for k in i['args']['media']:
                    ids.append(k['id'])
                res=[]
                for k in ids:
                    res.append(api.media_info(k))
                print('liked :')
                for k in res:
                    print('http://instagram.com/p/'+k['items'][0]['code'])
        
    #evaluate_method(api.getTotalFollowers, [user_id], 'api.getTotalFollowers')
    #evaluate_method(getTotalFollowers, [api, user_id], 'getTotalFollowers')

