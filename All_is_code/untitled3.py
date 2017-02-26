import re

def py_parsing( ):
   N,Q = map(int, input().split() )
   tagStack = []
   regexParam = re.compile( r'\w+ = "[a-zA-Z0-9]+"' )
   regexTagOpen = re.compile( r'<(\w+)' )
   regexTagClose = re.compile( r'<\/(\w+)>' )
   parseDict = {}
   for lineNo in range( N ):
       line = input()
       if line[1] == '/': #closing
           tag = re.findall( regexTagClose, line )[ 0 ]
           if tag != tagStack.pop(): 
               return "Not Found!"
       else: #opening
           prevTag = -1
           if len(tagStack) > 0: 
               prevTag = tagStack[ -1 ]
           tag = re.findall( regexTagOpen, line )[ 0 ]
           tagStack.append( tag )
           params = re.findall( regexParam, line )
           # update prevTag to point to this one if not -1
           if prevTag != -1: 
               parseDict[ prevTag ][ "next" ] = tag
           parseDict[ tag ] = {}
           if len(params) == 0: 
               continue
           for param in params:
               paramTuple = param.split( " = " )
               parseDict[ tag ][ paramTuple[0] ] = paramTuple[ 1 ].strip( '"' )
   if len( tagStack ) > 0: 
       return "Not Found!"
   soln = []
   for lineNo in range( Q ):
       line = input()
       tagsParams = line.split( '~' )
       if len( tagsParams ) < 2: 
           soln.append( "Not Found!" )
           continue
       paramToQuery = tagsParams[ 1 ]
       tags = tagsParams[ 0 ].split( '.' )
       prevTag = -1
       works = True
       for i,tag in enumerate( tags ):
           if tag not in parseDict: 
               works = False
               break;
           if i > 0:
               if not ( parseDict[ tags[ i - 1 ] ].has_key( "next" ) and parseDict[ tags[ i - 1 ] ][ "next" ] == tag ): 
                   works = False
                   break;
       if works and paramToQuery in parseDict[ tags[ -1 ] ]:
           soln.append( parseDict[ tags[ -1 ] ][ paramToQuery ] )
       else:
           soln.append( "Not Found!" )
   return soln
       
   
for elem in py_parsing():
   print(elem)