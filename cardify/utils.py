# -*- coding: utf-8 -*-
#
################################################################################
#
#   Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    Cardify is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import random

def _parseCardNumber(parNumTar, separator="-"):
    """
        Auxiliar method to tokenize the credit card number provided. Returns <nIm, nPa>. It admits the '-' as a default separator.
    """
    # If no headers provided... Returning empty lists...
    if not parNumTar:    
        return [], []
    nIm = []
    nPa = []
    aux = ""
    for k in range(len(parNumTar.split(separator))):
        aux += parNumTar.split(separator)[k]    
    for i in range(len(aux)):
        if i%2 == 0:
            #ojo índice 0 = odd
            nIm.append(int(aux[i]))
        else:
            #ojo índice 1 = pair
            nPa.append(int(aux[i]))
    return nIm, nPa

def _calculatePartialSum(nIm, nPa):
    """
        Auxiliar method to work out the partial sum. Odd numbers * 2 (if > 9, we will take the result minus -9. For the pair numbers, as is.
        
        :param nIm: Odd list of integers
        :param nPa: Pair list of integers   
        
        :return: An integer with the sum...     
    """
    suma = 0
    for i in nIm:
        c = i*2
        if (i*2)>9:
            suma += c-9
        else:
            suma += c
    for i in nPa:
        suma += i
    return suma

def verifyCardNumber(numTar, separator = "-"):
    """
        Verification method. Return <boolean>.
        #     1.- Calculates the total sum
        #    2.- Verify if mod10=0 and <= 150    
    """
    numIm, numPa = _parseCardNumber(numTar, separator=separator)
    aux = _calculatePartialSum(numIm, numPa)
    if (aux %10 == 0) & (aux <= 150):
        return True
    return False

def generateCardNumber(header, separator = "-"):
    """
        Generating random credit card numbers. Return <string>. 
            0.- Reading all the numbers provided
            1.- Generating odd numbers
            2.- Generating pair numbers excpeting the last one
            3.- Generating the last number to verify that it matches the condition of mod % 10 == 0    
    """
    # Generating a new number
    numIm, numPa = _parseCardNumber(header, separator = "-")
    # Generating odd numbers
    for i in range(8-len(numIm)):
        numIm.append(random.randrange(0,10))
    # Calculating the partial sum
    suma = _calculatePartialSum(numIm, numPa)
    # Calculating the numbers remaining
    faltan = 8-len(numPa)
    # Generating random numbers
    for i in range(faltan-1):    
        n = random.randrange(0,10)
        suma += n
        numPa.append(n)
    # The last number is manually added to let it match with a valid credit card
    num = 10-(suma%10)
    # Last verification to avoisd using a 10 instead of a 0... 
    if num == 10:
        num = 0
    numPa.append(num)
    
    n = ""
    # Iterating through the list of odd and pair numbers to create the card...
    for i in range(8):
        n += str(numIm[i])+str(numPa[i])
    print "\tGenerated number:\t"+n
    return n

