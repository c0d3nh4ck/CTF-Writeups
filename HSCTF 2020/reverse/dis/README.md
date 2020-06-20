## Python Bytecode Disassembler

##### refer these links for more information :-
> [dis — Python Bytecode Disassembler — PyMOTW 3](https://pymotw.com/3/dis/)
> [Python bytecode \| Yet Another Python Internals Blog](https://pythoninternal.wordpress.com/2014/07/14/python-bytecode/)
> [dis — Disassembler for Python bytecode — Python 3.8.3 documentation](https://docs.python.org/3/library/dis.html)


 1. **LOAD_CONST**      -> loads a constant value on the stack
 2. **LOAD_GLOBAL**     -> loads a global name on the stack
 3. **LOAD_FAST**       -> loads a local variable on the stack
 4. **BUILD_LIST**      -> building a list i.e. $a = [0,1]$
 5. **CALL_FUNCTION**   -> calls a function of name loaded by LOAD_GLOBAL
 6. **BINARY_MULTIPLY** -> implements when a multiplication $*$ operator is used
 7. **BINARY_SUBTRACT** -> implements when a subtraction $-$ operator is used
 8. **BINARY_ADD**      -> implements when a additon $+$ operator is used
 9. **STORE_FAST**      -> stores value of in a local varibale
 10. **STORE_SUBSCR**    -> stores value in an array i.e. TOS1[TOS] = TOS2
10. **RETURN_VALUE**    -> returns the last value loaded on stack
11. **YIELD_VALUE**     -> yields the last value loaded on stack (for generator function)
12. **SETUP_LOOP**      -> pushes a loop block on the stack
13. **GET_ITER**        -> uses the iterator which is on top of the stack i.e. range(10)
14. **FOR_ITER**        -> goes through the iterator and pushes the next value on the stack 
15. **POP_BLOCK**       -> to remove the loop block from the block stack when loop has ended
16. **LIST_APPEND**     -> used to implement list comprehensions
17. **MAP_ADD**         -> used to implement dictionary comprehensions
18. **COMPARE_OP**      -> performs a Boolean operation in if and else statements



[reverse engineering - Convert python disassembly from dis.dis back to codeobject - Stack Overflow](https://stackoverflow.com/questions/56817475/convert-python-disassembly-from-dis-dis-back-to-codeobject)
[Python Decompiler Online](https://python-decompiler.com/)