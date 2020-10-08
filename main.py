import csv
import copy
import numpy as np
from AG import ag
from AG import popinicial
from simulador import simula

def main():
    resultAG = ag(popinicial(1000))
    simula(resultAG)

main()
