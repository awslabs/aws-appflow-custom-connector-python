parser grammar CustomConnectorQueryFilterParser;

options  { tokenVocab=CustomConnectorQueryFilterLexer; }

// 'queryfilter' is the root node for the filter expression
queryfilter
: expression EOF
;

expression
: LPAREN expression RPAREN                       #parenExpression  // supports parenthesis expressions
// logical operators support
| NOT expression                                 #notExpression
| left=expression op=andBinary right=expression     #aNDBinaryExpression
| left=expression op=orBinary right=expression     #oRBinaryExpression
| left=identifier op=gtComparator right=value #greaterThanComparatorExpression
| left=identifier op=geComparator right=value #greaterThanEqualToComparatorExpression
| left=identifier op=ltComparator right=value #lesserThanComparatorExpression
| left=identifier op=leComparator right=value #lesserThanEqualToComparatorExpression
| left=identifier op=eqComparator right=value #equalToComparatorExpression
| left=identifier op=eqComparator right=boolean #booleanEqualToComparatorExpression
| left=identifier op=neComparator right=value #notEqualToComparatorExpression
| left=identifier op=neComparator right=boolean #booleanNotEqualToComparatorExpression
| left=identifier op=likeComparator right=value #likeComparatorExpression
| (left=identifier op=betweenComparator (l1=value op1=andBinary right=value)) #betweenExpression
| identifier #identifierExpression
// Following is a leaf node in the parse tree
// This allows validation and transformations of values.
| value #valueExpression
| identifier op=inOperator LPAREN value (COMMA value)* RPAREN  # inExpression  // Supports SQL like 'IN' operator
;

gtComparator
: GT ;

geComparator
: GE ;

ltComparator
: LT ;

leComparator
: LE ;

eqComparator
: EQ ;

neComparator
: NE ;

likeComparator
: LIKE ;

betweenComparator
: BETWEEN ;

andBinary
: AND ;

orBinary
: OR
;

boolean
 : TRUE | FALSE
 ;

identifier
:IDENTIFIER ;

inOperator
:IN ;

// Following is to support different String formats in the value expression
string
 : SINGLE_STRING
 | DOUBLE_STRING
 | EMPTY_DOUBLE_STRING
 | EMPTY_SINGLE_STRING
 | NULL
 ;

value
: string #stringValueExpression
| DECIMAL #decimalValueExpression
| DATE #isoDate
| DATETIME #isoDateTime
;