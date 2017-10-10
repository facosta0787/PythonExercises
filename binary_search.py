# -*- coding: utf-8 -*-
import os

def binarySearchSort(nums,numFind,posIni,posEnd):
    nums.sort()
    return binarySearch(nums,numFind,posIni,posEnd)

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
    numbers = [1,125,2,7,12,90,104,34,54,67,87,110,4,5,115]
    numberToFind = int(input('Ingrese un número a buscar: '))

    if binarySearchSort(numbers,numberToFind,0,len(numbers) - 1):
        print('Si')
    else:
        print('No')
