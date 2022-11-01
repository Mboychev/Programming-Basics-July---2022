count_pens = int(input())
count_markers = int(input())
count_detergent = int(input())
percent_discount = int(input())
price_pens = count_pens * 5.8
price_markers = count_markers * 7.2
price_detergent = count_detergent * 1.2
total_price = price_pens + price_markers + price_detergent
discount = percent_discount / 100
discount_price = total_price - (total_price * discount)
print(discount_price)