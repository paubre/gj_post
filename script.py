import csv 
import math 
from tqdm import tqdm
from collections import Counter 

with open('gj-posts-final.csv', 'r') as csvfile: 
    reader = csv.DictReader(csvfile)
    
    nb_ligne = 0
    #average
    sum_actual = 0
    sum_expected = 0
    count = 0

    #minmax
    min_actual = math.inf
    min_expected = math.inf
    max_actual = -math.inf
    max_expected = -math.inf

    #moygroupe
    account_name = " "
    moy_actual_like = 0
    moy_expected_like = 0
    groupe = {}
    l1 = [] 
    l2 = []
    l3 = []
    count_ct = 0

    #topgroupe
    post_url = 0
    topgroupe = " "
    max_groupe = -math.inf
    groupe_moy = {}
    top10 = {}

    #toplikepost
    post_url = 0
    toplike = " "
    max_like = -math.inf
    like = {}
    top10like = {}

    #median
    nb = []

    for row in tqdm(reader, unit='line', total=9755214):
        actual_like_count  = int(row['actual_like_count'])
        expected_like_count = int(row['expected_like_count'])

        nb_ligne += 1
        
        #median
        nb.append(actual_like_count) 

        #average
        sum_actual += actual_like_count
        sum_expected += expected_like_count
        count += 1

        #minmax
        if max_actual < actual_like_count:
            max_actual = actual_like_count
        if max_expected < expected_like_count: 
            max_expected = expected_like_count

        if min_actual > actual_like_count:
            min_actual = actual_like_count
        if min_expected > expected_like_count:
            min_expected = expected_like_count

        #moygroupe
        account_name = (row['account_name'])
        l1 = list([int(row['actual_like_count']), expected_like_count, count_ct])

        if account_name not in groupe:
            count_ct = 1
            groupe[account_name] = l1
        else:
            l2 = groupe[account_name]
            l3 = [l1[i]+l2[i] for i in range(len(l1))]
            groupe[account_name] = l3 

        #toplikepost
        post_url = (row['post_url'])
        like[post_url] = int(row['actual_like_count'])


    #average
    print("average actual like count :", sum_actual/count)
    print("average expected like count :", sum_expected/count)

    #minmax
    print("min actual like count :", min_actual)
    print("min expected like count :", min_expected)
    print("max actual like count :", max_actual)
    print("max expected like count :", max_expected)

    #moygroupe
    for g, n in groupe.items():
        moy_actual_like = (n[0]/n[2])

        groupe_moy[g] = moy_actual_like

        if moy_actual_like > max_groupe:
            topgroupe = g
            max_groupe = moy_actual_like

        moy_expected_like = (n[1]/n[2])
        print("name : %s \taverage actual like count : %s \taverage expected like count : %s" %(g, moy_actual_like, moy_expected_like))

    #top10groupe
    print("top 10 groupe :")
    for key, counter in Counter(groupe_moy).most_common(100):
        print(key, counter)

    print("nombre groupe :", len(groupe))

    #toplikepost
    print("top 10 post like :")
    for key, value in Counter(like).most_common(10):
        print(key, value)

    #median
    nb.sort()
    print("median :", nb[4877606])
    # if nb_ligne % 2 == 0 :
    #     print("median : ", nb[int(nb_ligne/2 - 1)]) #-1 pq liste commence à l'indice 0
    # else:
    #     print("median : ", nb[int(nb_ligne/2 - 2)])





