def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {'firstname':'Facundo',
    'lastname':'Garcia'}
    super_list = [
        {'firstname':'Facundo','lastname':'Garcia'},
        {'firstname':'Miguel','lastname':'Garcia'},
        {'firstname':'Juan','lastname':'Torres'},
        {'firstname':'Pepe','lastname':'Garcia'},
        {'firstname':'Felipe','lastname':'Martinez'},
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,1.5,5.6]
    }

    for key,value in super_dict.items():
        print(key,"-",value)
if __name__ == '__main__':
    run()