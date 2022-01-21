grammar ApplEdible;
prog: suite? ;
suite: header? stmt+ ;
stmt : (simple_stmt | compound_stmt) '.'? ;
simple_stmt
    : (SET CDISC_DOMAIN_VARIABLE? ('to' | 'as' 'following:'?))? expr_rhs                                
    | (SET CDISC_DOMAIN_VARIABLE? ('to' | 'as' 'following:'?))? expr_rhs ','? IF condition_list
        ((','|'.')? ELSE (SET CDISC_DOMAIN_VARIABLE? ('to' | 'as' 'following:'?))? expr_rhs ','? IF condition_list)*
        ((','|'.')? ELSE (SET CDISC_DOMAIN_VARIABLE? ('to' | 'as' 'following:'?))? expr_rhs)?           
    | if_stmt                   
    | ('do'|'Do') 'nothing'
    ;
compound_stmt
    : (IF condition_list (THEN | ',') simple_stmt)+                         
    ;
if_stmt: IF condition_list ','? THEN? simple_stmt ((','|'.')? ELSE if_stmt)* ((','|'.')? ELSE simple_stmt)? ;
condition_list: condition (','? venn_op condition)* ;
condition
    : '(' condition_list ')'    
    | selective_test            
    | quantified_test           
    ;
selective_test
    : selective_test (venn_op comp_op expr_rhs)+ 
    | sel_expr comp_op expr_rhs                  
    | sel_expr comp_op partial_term              
    | sel_expr comp_op expr_rhs
    ;
quantified_test
    : ('there' BE)? 'at' 'most' val_number OBSERVATION? selective_test
    | ('there' BE)? 'at' 'least' val_number OBSERVATION? selective_test
    | 'all' OBSERVATION? 'of'? selective_test
    | 'any' OBSERVATION? 'of'? selective_test
    | 'there'? ('exists' | 'exist') selective_test
    | selective_test 'for' 'any' CDISC_DOMAIN OBSERVATION?
    | selective_test 'for' 'all' CDISC_DOMAIN OBSERVATION?
    ;
expr_rhs
    : '(' expr_rhs ')'           
    | sel_expr      
    | prim_expr     
    | exprlist      
    | term          
    ;
exprlist
    : prim_expr (',' prim_expr)*
    | '[' exprlist  ']'
    ;
prim_expr
    : prim_expr (calc_op prim_expr)+    
    | val_number                        
    | val_string                        
    | 'True'                            
    | 'False'                           
    ;
term: val_month                         
    | 'None'                            
    | 'NULL'                            
    | 'null'                            
    | 'blank'                           
    | 'empty'                           
    | 'missing'                         
    | 'nonmissing'                      
    | 'non-missing'                     
    ;
partial_term
    : 'a'? 'complete' ('date'| 'dates')?                        
    | 'a'? 'partial'  ('date'| 'dates')?                        
    | 'a'? 'complete' ('datetime'| 'datetimes' | 'date time')?  
    | 'a'? 'partial'  ('datetime'| 'datetimes' | 'date time')?  
    ;
comp_op
    : '='                   
    | '=='                  
    | BE ('equal' 'to')?    
    | BE? 'equal' 'to'      
    | 'equals' 'to'?        
    | 'Equals'              
    | '<'                   
    | '>'                   
    | '>='                  
    | '<='                  
    | BE? 'less' 'than' OP_OR 'equal' 'to'        
    | BE? 'greater' 'than' OP_OR 'equal' 'to'     
    | BE? 'equal' 'to' OP_OR 'greater' 'than'     
    | BE? 'less' 'than'                           
    | BE? 'greater' 'than'                        
    | '!='                                        
    | BE? 'not' 'equal' 'to'?                     
    | 'not' 'equals' 'to'?                        
    | 'ne'                                        
    | BE 'not' 'earlier' 'than'                   
    | BE 'not' 'later' 'than'                     
    | BE 'not'                                    
    | BE 'after'                                  
    | BE 'before'                                 
    | OP_CONTAINS                                 
    | OP_STARTS_WITH                              
    | OP_HAS ('values'| 'value')? 'of'?           
    | BE? 'in'                                    
    | BE? 'not' 'in'                              
    ;
venn_op
    : OP_AND                        
    | OP_OR                         
    ;
order_op
    : ('asc'  | 'ascending')          
    | ('dsc'  | 'decending')          
    ;
calc_op
    : '+'                            
    | '-'                            
    | ('–' | 'minus')                
    | '*'                            
    | '/'                            
    ;
sel_expr
    : '(' sel_expr ')'                    
    | sel_expr ((','|OP_AND) sel_expr)+   
    | sel_expr WHERE condition_list
    | selection
    | SUPP_DOMAIN_VARIABLE WHERE SUPP_DOMAIN_VARIABLE (BE | '=') val_string
    | sel_expr calc_op sel_expr  
    | sel_expr calc_op expr_rhs  
    | prim_expr calc_op sel_expr
    ;
selection
    : CDISC_DOMAIN_VARIABLE         
    ;
transformer
    : converter
    | 'upcase'
    | 'uppercase'
    ;
converter
    : 'converted' 'to' 'numeric' 'date'          
    | 'converted' 'to' 'numeric' 'datetime'      
    | 'converted' 'to' 'character'               
    ;
val_string: ('the'? ('text' | 'texts'))? STRING+;
val_date: DATE;
val_time: TIME;
val_number: NUMBER ;
val_month
    : 'January'   
    | 'Feburary'  
    | 'March'     
    | 'April'     
    | 'May'       
    | 'June'      
    | 'July'      
    | 'August'    
    | 'September' 
    | 'October'   
    | 'November'  
    | 'December'  
    ;
header
    : 'Option' ~':'* ':'              
    ;

OP_CONTAINS : 'contains';
OP_STARTS_WITH: 'starts with';
OP_HAS : 'has';
OP_AND : 'and' | 'And' ;
OP_OR : 'or' | 'Or' ;
DATE_UNIT: 'day' | 'month';
TIME_UNIT: TIME_HOUR_UNIT | TIME_MINUTE_UNIT | TIME_SECOND_UNIT ;
fragment TIME_HOUR_UNIT: 'hour' | 'hours';
fragment TIME_MINUTE_UNIT: 'minute' | 'minutes';
fragment TIME_SECOND_UNIT: 'second' | 'seconds';
SUPP_DOMAIN_VARIABLE : 'S' 'U' 'P' 'P' CDISC_DOMAIN '.' CDISC_VARIABLE_START CDISC_VARIABLE_START CDISC_VARIABLE_CONTINUE+ ;
CDISC_DOMAIN : CDISC_DOMAIN_LETTER CDISC_DOMAIN_LETTER
                (CDISC_DOMAIN_LETTER
                 (CDISC_DOMAIN_LETTER
                  (CDISC_DOMAIN_LETTER
                   (CDISC_DOMAIN_LETTER)?)?)?)?;
CDISC_DOMAIN_VARIABLE : '['? (CDISC_DOMAIN '.')? CDISC_VARIABLE_START CDISC_VARIABLE_START CDISC_VARIABLE_CONTINUE+ ']'?;
STRING : '\'' ~[\\\r\n\f']* '\'' | '"'~[\\\r\n\f"]* '"' ;
fragment INTEGER : NON_ZERO_DIGIT DIGIT* ;
fragment FLOAT_NUMBER : POINT_FLOAT | EXPONENT_FLOAT ;
NUMBER : INTEGER | FLOAT_NUMBER | NUMBER_ONE | NUMBER_ZERO;
fragment NUMBER_ONE : 'one' | 'One';
fragment NUMBER_ZERO: [0] | 'zero' ;
TIME : DIGIT DIGIT ':' DIGIT DIGIT (':' DIGIT DIGIT)? ;
DATE : [012] DIGIT ;
WHITESPACE : (' ' | '\t')+ -> skip ;
NEWLINE : ('\r'? '\n' | '\r')+ -> skip ;
COMMENT_BLOCK : '/*' .*? '*/' -> skip ;
COMMENT_LINE : ('//' | 'NOTE:') ~[\r\n\f]* -> skip ;
COMMENT_PARTIAL : '#' ~[\r\n\f#]* '#'? -> skip ;
STUDY_SPECIFIC : ('Study specific' | 'study specific') '.'? -> skip;
MISC : 'Please' -> skip ;
SEMICOLON : ';' -> skip ;
IF : 'if' | 'If' | 'In case' 'of'?;
THEN : 'then' | 'Then' ;
ELSE : 'else' | 'Else' | 'otherwise' ','? | 'Otherwise' ','? ;
SET : 'set' | 'Set' ;
IMPUTE: 'impute' | 'Impute' ;
BE: 'is' | 'are' ;
TO : 'to' | 'To' ;
AS : 'as' | 'As' ;
WITH : 'with' ;
WHERE : 'where' | 'Where' ;
OBSERVATION : 'observation' | 'observations' | 'record' | 'records' ;
ONLY : 'Only' | 'only' ;
WHEN : 'when' | 'When' ;
ORDER_BY: 'order by' | 'sorted by' ;
NAME : ID_START ID_CONTINUE* ;
fragment CDISC_DOMAIN_LETTER
 : [\p{Lu}] ;
fragment CDISC_DOMAIN_ITEM_LETTER
 : [\p{Ll}] ;
fragment CDISC_VARIABLE_START
 : [A-Z] ;
fragment CDISC_VARIABLE_CONTINUE
 : [\p{Letter}]
 | DIGIT
 ;
fragment NON_ZERO_DIGIT
 : [1-9]
 ;
fragment DIGIT
 : [0-9]
 ;
fragment POINT_FLOAT
 : INT_PART? FRACTION
 ;
fragment INT_PART
 : DIGIT+
 ;
fragment FRACTION
 : '.' DIGIT+
 ;
fragment EXPONENT_FLOAT
 : ( INT_PART | POINT_FLOAT ) EXPONENT
 ;
fragment EXPONENT
 : [eE^] [+-]? DIGIT+
 ;
fragment ID_START
 : [\p{Lu}]    
 | [\p{N}]     
;
fragment ID_CONTINUE
 : ID_START
 | [\p{Mn}]    
 | [\p{Mc}]    
 | [\p{Nd}]    
 | [\p{Pc}]    
 ;
