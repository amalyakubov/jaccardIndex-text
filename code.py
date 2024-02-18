def calculateJaccardIndex(textA, textB):
    setA = set(textA.lower().split())
    setB = set(textB.lower().split())

    intersection = setA.intersection(setB)
    union = setA.union(setB)

    return float(len(intersection)) / len(union)
