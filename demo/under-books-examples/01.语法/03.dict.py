if __name__ == '__main__':
    d = {
        'Michael': 95,
        'Bob': 75,
        'Tracy': 85
    }
    print('d[\'Michael\'] =', d['Michael'])
    print('d[\'Bob\'] =', d['Bob'])
    print('d[\'Tracy\'] =', d['Tracy'])

    print("'Thomas' in d =", 'Thomas' in d)
    print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))