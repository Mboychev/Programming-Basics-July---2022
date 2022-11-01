count_pages = int(input())
pages = int(input())
days = int(input())
time_per_book = count_pages // pages
hours_per_day = time_per_book // days
print(hours_per_day)

