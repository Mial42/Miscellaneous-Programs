def insertion_sort(arr): #Copied as instructed
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j = j - 1
            arr[j] = cur


def selection_sort(arr):
    for k in range(len(arr) - 1): #k being the first unsorted index
        temp_minimum = arr[k] 
        temp_min_index = j = k
        while j < len(arr):
            if arr[j] < temp_minimum:
                temp_min_index = j
                temp_minimum = arr[j]
            j = j + 1
        swap_placeholder = arr[k]
        arr[k] = arr[temp_min_index]
        arr[temp_min_index] = swap_placeholder


if __name__ == '__main__':
    import timeit
    import random
    #generate increasing arrays
    #The increasing arrays will not be changed by the sorts, so I only need to generate them once    
    increasing_1000 = list(range(0, 1000))
    increasing_2500 = list(range(0, 2500))
    increasing_5000 = list(range(0, 5000))
    increasing_7500 = list(range(0, 7500))
    increasing_10000 = list(range(0, 10000))
    
    #generate decreasing arrays
    decreasing_insertion_1000 = [x for x in range(999, -1, -1)]
    decreasing_selection_1000 = list(decreasing_insertion_1000)
    decreasing_insertion_2500 = [x for x in range(2499, -1, -1)]
    decreasing_selection_2500 = list(decreasing_insertion_2500)
    decreasing_insertion_5000 = [x for x in range(4999, -1, -1)]
    decreasing_selection_5000 = list(decreasing_insertion_5000)
    decreasing_insertion_7500 = [x for x in range(7499, -1, -1)]
    decreasing_selection_7500 = list(decreasing_insertion_7500)
    decreasing_insertion_10000 = [x for x in range(9999, -1, -1)]
    decreasing_selection_10000 = list(decreasing_insertion_10000)

    #generate random arrays
    random_insertion_1000 = [random.randint(0, 1000) for x in range(1000)]
    random_selection_1000 = list(random_insertion_1000)
    random_insertion_2500 = [random.randint(0, 2500) for x in range(2500)]
    random_selection_2500 = list(random_insertion_2500)  
    random_insertion_5000 = [random.randint(0, 5000) for x in range(5000)]
    random_selection_5000 = list(random_insertion_5000)  
    random_insertion_7500 = [random.randint(0, 7500) for x in range(7500)]
    random_selection_7500 = list(random_insertion_7500)
    random_insertion_10000 = [random.randint(0, 10000) for x in range(10000)]
    random_selection_10000 = list(random_insertion_10000)

    #Sorting the arrays and printing the runtimes
    #Increasing Insertion Sort
    runtime = timeit.timeit('insertion_sort(increasing_1000)', setup='from __main__ import insertion_sort, increasing_1000', number=1) #Copied from the Project 1 PDF
    print('1000 Increasing Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('insertion_sort(increasing_2500)', setup='from __main__ import insertion_sort, increasing_2500', number=1) #Copied from the Project 1 PDF
    print('2500 Increasing Insertion: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('insertion_sort(increasing_5000)', setup='from __main__ import insertion_sort, increasing_5000', number=1) #Copied from the Project 1 PDF
    print('5000 Increasing Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('insertion_sort(increasing_7500)', setup='from __main__ import insertion_sort, increasing_7500', number=1) #Copied from the Project 1 PDF
    print('7500 Increasing Insertion: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('insertion_sort(increasing_10000)', setup='from __main__ import insertion_sort, increasing_10000', number=1) #Copied from the Project 1 PDF
    print('10000 Increasing Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    print() #for legibility
    #Increasing Selection Sort
    runtime = timeit.timeit('selection_sort(increasing_1000)', setup='from __main__ import selection_sort, increasing_1000', number=1) #Copied from the Project 1 PDF
    print('1000 Increasing Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('selection_sort(increasing_2500)', setup='from __main__ import selection_sort, increasing_2500', number=1) #Copied from the Project 1 PDF
    print('2500 Increasing Selection: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('selection_sort(increasing_5000)', setup='from __main__ import selection_sort, increasing_5000', number=1) #Copied from the Project 1 PDF
    print('5000 Increasing Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('selection_sort(increasing_7500)', setup='from __main__ import selection_sort, increasing_7500', number=1) #Copied from the Project 1 PDF
    print('7500 Increasing Selection: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('selection_sort(increasing_10000)', setup='from __main__ import selection_sort, increasing_10000', number=1) #Copied from the Project 1 PDF
    print('10000 Increasing Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    print() #for legibility
    #Decreasing Insertion Sort
    runtime = timeit.timeit('insertion_sort(decreasing_insertion_1000)', setup='from __main__ import insertion_sort, decreasing_insertion_1000', number=1) #Copied from the Project 1 PDF
    print('1000 Decreasing Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('insertion_sort(decreasing_insertion_2500)', setup='from __main__ import insertion_sort, decreasing_insertion_2500', number=1) #Copied from the Project 1 PDF
    print('2500 Decreasing Insertion: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('insertion_sort(decreasing_insertion_5000)', setup='from __main__ import insertion_sort, decreasing_insertion_5000', number=1) #Copied from the Project 1 PDF
    print('5000 Decreasing Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('insertion_sort(decreasing_insertion_7500)', setup='from __main__ import insertion_sort, decreasing_insertion_7500', number=1) #Copied from the Project 1 PDF
    print('7500 Decreasing Insertion: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('insertion_sort(decreasing_insertion_10000)', setup='from __main__ import insertion_sort, decreasing_insertion_10000', number=1) #Copied from the Project 1 PDF
    print('10000 Decreasing Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    print() #for legibility
    #Decreasing Selection Sort
    runtime = timeit.timeit('selection_sort(decreasing_selection_1000)', setup='from __main__ import selection_sort, decreasing_selection_1000', number=1) #Copied from the Project 1 PDF
    print('1000 Decreasing Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('selection_sort(decreasing_selection_2500)', setup='from __main__ import selection_sort, decreasing_selection_2500', number=1) #Copied from the Project 1 PDF
    print('2500 Decreasing Selection: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('selection_sort(decreasing_selection_5000)', setup='from __main__ import selection_sort, decreasing_selection_5000', number=1) #Copied from the Project 1 PDF
    print('5000 Decreasing Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('selection_sort(decreasing_selection_7500)', setup='from __main__ import selection_sort, decreasing_selection_7500', number=1) #Copied from the Project 1 PDF
    print('7500 Decreasing Selection: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('selection_sort(decreasing_selection_10000)', setup='from __main__ import selection_sort, decreasing_selection_10000', number=1) #Copied from the Project 1 PDF
    print('10000 Decreasing Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    print() #for legibility
    #Random insertion sort
    runtime = timeit.timeit('insertion_sort(random_insertion_1000)', setup='from __main__ import insertion_sort, random_insertion_1000', number=1) #Copied from the Project 1 PDF
    print('1000 Random Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('insertion_sort(random_insertion_2500)', setup='from __main__ import insertion_sort, random_insertion_2500', number=1) #Copied from the Project 1 PDF
    print('2500 Random Insertion: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('insertion_sort(random_insertion_5000)', setup='from __main__ import insertion_sort, random_insertion_5000', number=1) #Copied from the Project 1 PDF
    print('5000 Random Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('insertion_sort(random_insertion_7500)', setup='from __main__ import insertion_sort, random_insertion_7500', number=1) #Copied from the Project 1 PDF
    print('7500 Random Insertion: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('insertion_sort(random_insertion_10000)', setup='from __main__ import insertion_sort, random_insertion_10000', number=1) #Copied from the Project 1 PDF
    print('10000 Random Insertion: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    print() #for legibility
    #Random selection sort
    runtime = timeit.timeit('selection_sort(random_selection_1000)', setup='from __main__ import selection_sort, random_selection_1000', number=1) #Copied from the Project 1 PDF
    print('1000 Random Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('selection_sort(random_selection_2500)', setup='from __main__ import selection_sort, random_selection_2500', number=1) #Copied from the Project 1 PDF
    print('2500 Random Selection: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('selection_sort(random_selection_5000)', setup='from __main__ import selection_sort, random_selection_5000', number=1) #Copied from the Project 1 PDF
    print('5000 Random Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    runtime = timeit.timeit('selection_sort(random_selection_7500)', setup='from __main__ import selection_sort, random_selection_7500', number=1) #Copied from the Project 1 PDF
    print('7500 Random Selection: ' + '{:.6f}'.format(runtime))
    runtime = timeit.timeit('selection_sort(random_selection_10000)', setup='from __main__ import selection_sort, random_selection_10000', number=1) #Copied from the Project 1 PDF
    print('10000 Random Selection: ' + '{:.6f}'.format(runtime)) #Copied from the Project 1 PDF
    print() #for legibility
