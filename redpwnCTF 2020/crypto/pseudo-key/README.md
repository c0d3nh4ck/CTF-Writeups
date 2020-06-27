## Writeup

- **Given information in .txt file**

```
Ciphertext: z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut
Pseudo-key: iigesssaemk
```

- **there are many possible keys :-** 
	
> For example an a in the pseudo-key can correspond to an a in the actual key, as a = 0 and 0 * 2 = 0 (mod 26) or it could correspond to an n as n = 13 and 13 * 2 = 26 = 0 (mod 26)

> So for each possible key and for each index there are two possibilities, the actual key is human-readable (i.e. should make sense, not a bunch of random chars)

- **script to find one of possible indices of the key**  

```python
for i in range(len(pk)):
     for c in chr_to_num:
         ky[i] = c
         x = chr_to_num[ky[i]]
         if num_to_chr[(2 * x) % 26] == pk[i]:
             break
```

> output -> ['e', 'e', 'd', 'c', 'j', 'j', 'j', 'a', 'c', 'g', 'f']


- **script to find the other possible indices of the key** 

```python
for i in range(11):
     ky[i] = chr(ord(ky[i])+13)
```

> output -> ['r', 'r', 'q', 'p', 'w', 'w', 'w', 'n', 'p', 't', 's']


- **matching the indices that are human readable**

> key - `redpwwwnctf`

- **script to find the flag **

```python
ky = ["a"]*37
for i in range(len(ct)):
	for c in chr_to_num:
		ky[i] = c
		x = chr_to_num[ky[i]]
		m = encrypt(''.join(ky),key)
		if m[i] == ct[i]:
			break
```

## Flag
flag{i_guess_pseudo_keys_are_pseudo_secure}