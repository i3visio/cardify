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

import sys
import argparse
import random

import cardify
import cardify.utils as card_utils
import cardify.banner as banner
 
def getParser():
    parser = argparse.ArgumentParser(description='cardify_launcher.py - Researching about Credit Card Numbers.', prog='cardify_launcher.py', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False)
    
    grFunction = parser.add_mutually_exclusive_group(required=True)
    grFunction.add_argument('-G', '--generator', metavar='<NUMBER>', type=int, help='To set the number of credit cards to be generated.') 
    grFunction.add_argument('-V', '--verify', metavar='<CARD>', help = 'To set the: a) credit card to verify or b), if args.file exists, the file where the cards to verify are stored.')

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which the app will work.')      
    groupProcessing.add_argument('-t', '--template', metavar='<TEMPLATE>', required=False, help='To show the starting numbers of the cards to be generated (3xx..x - American Express, 4xx..x - Visa, 5xx..x - MasterCard, 6xx..x - Discover).') 
    groupProcessing.add_argument('-f', '--file', metavar='<INPUT_FILE>', required=False, help='The name of the input file.')
    groupProcessing.add_argument('-q', '--quiet', required=False, action='store_true', default=False, help = 'Activate it to show additional info in the terminal.')
    groupProcessing.add_argument('-s', '--separator', metavar='<CHAR>', required=False, default='-', help = 'To show a different separator rather than "-".')

    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s ' +cardify.__version__, help='shows the version of the program and exists.')

    return parser

# MAIN MENU
# ---------
def main(args):
    if args.verify:
        #verificador
        if not args.quiet:
            print "Starting verification..."
        if args.file:
            tarVer = {}
            if not args.quiet:
                print "Reading file: "+args.file+"..."
            # Opening the input file
            f = open (args.file, "r")
            contenido = f.readlines()
            for linea in contenido:
                num = linea[:len(linea)-1]
                if num not in tarVer:
                    tarVer[num]=card_utils.verifyCardNumber(num, separator = args.separator)
                    if args.verbose:
                        print "La validez del número de tarjeta "+num+"es:\t"+str(tarVer[num])
            f.close()
            if not args.quiet:
                print "Writing down the output file as "+args.file+".verified..."
            # Opening the output file...
            s = open (args.file + ".verified", "w")
            for num in tarVer:
                s.write(str(num)+"\t"+str(tarVer[num])+"\n")
            s.close()
        else:
            print "Is the credit card "+args.verify+" valid? \t"+str(card_utils.verifyCardNumber(args.verify, separator = args.separator))
    else:
        if not args.quiet:
            print "Starting generation..."

        numGenerados = []

        completado=0

        # bucle de generación de tarjetas
        for i in range(args.generator):
            nuevo = card_utils.generateCardNumber(args.template, separator = args.separator)
            while nuevo in numGenerados:
                nuevo = card_utils.generateCardNumber(args.template, separator = args.separator)
            numGenerados.append(nuevo)
            # mostrar mensaje de estado
            if int(float(i+1)/float(args.generator)*100) > completado:
                completado = int(float(i+1)/float(args.generator)*100)
                if not args.quiet:
                    print "Generation process status:\t"+str(completado).rjust(3)+"%"
        if args.file:
            if not args.quiet:
                print "Writing the output file "+args.file+"..."
            try:
                f = open (args.file, "w")
                for num in numGenerados:
                    f.write(str(num)+"\n")
                f.close()
            except:
                f = open ("./verified_numbers.txt", "w")
                for num in numGenerados:
                    f.write(str(num)+"\n")
                f.close()

if __name__ == "__main__":
    print banner.WELCOME_TEXT
    
    # Grabbing the parser
    parser = getParser()

    args = parser.parse_args()

    # Calling the main function
    main(args) 

