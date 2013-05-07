#! /usr/bin/env python

import argparse, os, pprint
pp=pprint.PrettyPrinter(indent=4)

def parse_args(parse_inputs=None):
    parser = argparse.ArgumentParser(
            description='''This script is meant to show some features of argparse. 
            The ArgumentParser is initiated with ArgumentDefaultsHelpFormatter, so that defaults are shown. 
            Also, try for example ./demo.py @some_args.txt. As you can see, using argparse is a very easy way to document code''',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter, #With this option default settings are shown
            fromfile_prefix_chars='@' #you can specify 
            )
    parser.add_argument('--dir', default=os.getcwd(), 
            help='This option takes a default. Also, no type is specified, so it will be stored as ')  
    parser.add_argument('-n','--number',   action='store', type=int,required=True ,help='standard err directory, required by qstat')
    parser.add_argument('--under-score',  action='store',  help='This will be stored as under_score' )
    parser.add_argument('--batch-queue',  help='here is an argument that only takes certain choices',  
            default='hepshort.q',
            choices=['hepshort.q', 'hepmedium.q', 'heplong.q'])
    parser.add_argument('-v',dest='verbose',action='store_true',  help='No specification needed, stored True')
    parser.add_argument('--multiple-values', help='Can store multiple arguments',nargs='+',default=['foo','bar'])
    return parser.parse_args(parse_inputs)


if __name__ == '__main__':
    args=parse_args()
    print('\nparse_args returns a namespace, \n')
    pp.pprint(args)
    print('\nbut you can turn it into a dictionary using \'vars()\':\n')
    args_dict=vars(args)
    pp.pprint(args_dict)#This is pretty printer, also a nice function
    print('''
I strongly recommend reading the full documentation, since this demo only shows a limmited number of features. 
You can for example automatically have files opened that are parsed using argparse, or use groupings.''')
    



