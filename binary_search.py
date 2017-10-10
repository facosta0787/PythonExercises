# -*- coding: utf-8 -*-
import os
def binarySearch(nums,numFind,posIni,posEnd):

    if posIni > posEnd:
        return False

    mid = int((posIni + posEnd) / 2)

    if nums[mid] == numFind:
        return True
    elif nums[mid] > numFind:
        return binarySearch(nums,numFind,posIni,mid - 1)
    else:
        return binarySearch(nums,numFind,mid + 1,len(numbers))


# Enter point
if __name__ == '__main__':
    os.system('cls')
    numbers = [1,2,4,5,7,12,34,54,67,87,90,104,110,115,125]
    numberToFind = int(input('Ingrese un número a buscar: '))

    if binarySearch(numbers,numberToFind,0,len(numbers) - 1):
        print('Si')
    else:
        print('No')
