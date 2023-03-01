lexer grammar CustomConnectorQueryFilterLexer;

// logical operator tokens
AND        : 'AND' | 'and' ;
OR         : 'OR' | 'or' ;
NOT        : 'NOT' | 'not' ;
TRUE       : 'TRUE' |'True'|'true' ;
FALSE      : 'FALSE' | 'False'| 'false' ;
GT         : '>' ;
GE         : '>=' ;
LT         : '<' ;
LE         : '<=' ;
EQ         : '=' ;
NE         : '!=';
LIKE       : 'CONTAINS' | 'contains' ;
BETWEEN    : 'BETWEEN' | 'between' ;
// string literals
LPAREN     : '(' ;
RPAREN     : ')' ;
NULL       : 'null';
IN         : 'IN' | 'in';
LIMIT      : 'LIMIT' | 'limit';
COMMA      : ',';

// represents identifier string in filter expression.
IDENTIFIER : [a-zA-Z][A-Za-z0-9_.-]*;

// represents a positive non-zero integer
POS_INTEGER: [1-9][0-9]+
;

// represents decimal values like 5.0 or -5.0 etc
DECIMAL    :'-'? [0-9]+ ( '.' [0-9]+ )?
;

// represents single quote string like 'grammar' etc
SINGLE_STRING
 : '\'' (~('\'') | STR_ESC)+ '\''
 ;

// represents double quote string like "grammar" etc
DOUBLE_STRING
 : '"'(~('"') | STR_ESC)+ '"'
 ;

// represents empty single quote string like ''
EMPTY_SINGLE_STRING
 : '\'''\''
 ;

// represents empty double quote string like ""
EMPTY_DOUBLE_STRING
 : '"''"'
 ;

fragment STR_ESC
:  '\\' ('"' | '\\'|'\''| 't' | 'n' | 'r') // add more:  Unicode esapes, ...
;
// represents white spaces
WS         : [ \r\t\u000C\n]+ -> skip;

// ISO 8601 Date and Time format
//   Year:
//      YYYY (eg 1997)
//   Year and month:
//      YYYY-MM (eg 1997-07)
//   Complete date:
//      YYYY-MM-DD (eg 1997-07-16)
//   Complete date plus hours and minutes:
//      YYYY-MM-DDThh:mmTZD (eg 1997-07-16T19:20+01:00)
//   Complete date plus hours, minutes and seconds:
//      YYYY-MM-DDThh:mm:ssTZD (eg 1997-07-16T19:20:30+01:00)
//   Complete date plus hours, minutes, seconds and a decimal fraction of a
//second
//      YYYY-MM-DDThh:mm:ss.sTZD (eg 1997-07-16T19:20:30.45+01:00)
//where:
//
//     YYYY = four-digit year
//     MM   = two-digit month (01=January, etc.)
//     DD   = two-digit day of month (01 through 31)
//     hh   = two digits of hour (00 through 23) (am/pm NOT allowed)
//     mm   = two digits of minute (00 through 59)
//     ss   = two digits of second (00 through 59)
//     s    = one or more digits representing a decimal fraction of a second
//     TZD  = time zone designator (Z or +hh:mm or -hh:mm)

// CustomConnector will either support ISO DATE or ISO DateTime

DATE : [0-9] [0-9] [0-9] [0-9] '-' ('0'[1-9] | '1'[0-2]) '-' ('0'[0-9] | '1'[0-9] | '2'[0-9] | '3'[0-1]);
DATETIME : DATE 'T' TIME;

fragment TIME : ('0'[0-9] | '1'[0-9] | '2'[0-4]) ':' [0-5][0-9] ':' [0-5][0-9] ('.' [0-9]+)? 'Z';
