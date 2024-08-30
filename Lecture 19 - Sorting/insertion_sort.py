class InsertionSort:

    def __call__(self, cards):
        n = len(cards)

        for i in range(1,n):
            card_to_insert = cards[i]
            j = i - 1
            while j >= 0 and cards[j] > card_to_insert:
                cards[j+1] = cards[j]
                j -= 1
            cards[j+1] = card_to_insert


mysort = InsertionSort()
nums = [1,2,5,10,7,2,20,15,4]
mysort(nums)
print(nums)