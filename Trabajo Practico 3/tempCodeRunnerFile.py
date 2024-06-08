for i in range(len(super_heroes)):
    if 'traje' in super_heroes[i]['biografia'] or 'armadura' in super_heroes[i]['biografia']:
        print(i, super_heroes[i]['nombre'], super_heroes[i]['biografia'])