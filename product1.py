
products = []
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入價錢')
	#p = [name,price] 
	##p.append(name)
	##p.append(price)
	products.append([name, price])

	
print(products)

products[0][0]


