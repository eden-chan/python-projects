import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data['Primary Fur Color'].value_counts()
print(fur_colors)
gray_squirrel_count = fur_colors['Gray']
red_squirrel_count = fur_colors['Cinnamon']
black_squirrel_count = fur_colors['Black']

fur_color_count = {'Colors': ["Gray", "Cinnamon", "Black"],
                   "Squirrel Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]}
df = pandas.DataFrame(fur_color_count)
df.to_csv('Squirrel_fur_count')


