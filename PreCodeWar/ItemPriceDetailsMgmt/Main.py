import SeasonItemPrice

sno1 = 1
sno2 = 2
seasonItem1 = [{2: 90}, {4: 345}]
seasonItem2 = [{2: 145}, {1: 12}, {3: 250}]

seasonItemPrice1 = SeasonItemPrice.SeasonItemPrice(sno1, seasonItem1)
seasonItemPrice2 = SeasonItemPrice.SeasonItemPrice(sno2, seasonItem2)

seasonItemPrices = [seasonItemPrice1, seasonItemPrice2]

for seasonItemPrice in seasonItemPrices:
    if seasonItemPrice.sno == 1:
        print 'yes'
        seasonItem = seasonItemPrice.seasonItem
        print 'seasonItem len = ',len(seasonItem)
        print seasonItem
        for dict in seasonItem:
            for item, price in dict.items():
                print item,'-',price


seasons = set()
seasons.add(1)
seasons.add(2)
seasons.add(1)

print seasons
