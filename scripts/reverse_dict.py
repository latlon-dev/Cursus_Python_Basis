### input
english_dutch = {'dog': 'hond', 'tree': 'boom',
                 'sun': 'zon', 'chair': 'stoel'}
prices = {'apple': 2, 'box': 5, 'cat': 100, 'dog': 100, 'banana': 2}
# dutch_english =  reverse_dict(english_dutch)
### gewenst resultaat :
# {'hond': 'dog', 'boom': 'tree', 
# 'zon': 'sun', 'stoel': 'chair'} 

def reverse_dict(d):
    reversed_d = {} 
    for key in d:
        #reversed_d[d[key]] = key
        reversed_d.update({d[key]:key})
    return reversed_d

reversed_prices = reverse_dict(prices)
