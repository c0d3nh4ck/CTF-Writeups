## Writeup

### Static Analysis with Ghidra

**main**
```
int main(void)
{
  uint32_t i;
  int unused;
  _Bool pass;
  
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("I hate my data structures class! Why can\'t I just sort by hand?");
  pass = false;
  while( true ) {
    __isoc99_scanf(&DAT_00102058);
    if (8 < i) break;
    nums[i] = nums[i] ^ nums[i + 1];
    nums[i + 1] = nums[i + 1] ^ nums[i];
    nums[i] = nums[i] ^ nums[i + 1];
    pass = check();
  }
  if (pass == false) {
    puts("Try again!");
  }
  else {
    puts("Well done!");
    print_flag();
  }
  return 0;
}
```

**check**
```
_Bool check(void)
{
  uint32_t i;
  _Bool pass;
  
  i = 0;
  while( true ) {
    if (8 < i) {
      return true;
    }
    if (nums[i + 1] < nums[i]) break;
    i = i + 1;
  }
  return false;
}
```

**array of nums**
```
0x555555558060 <nums>:	  0x00000001	0x0000000a	0x00000003	0x00000002
0x555555558070 <nums+16>:	0x00000005	0x00000009	0x00000008	0x00000007
0x555555558080 <nums+32>:	0x00000004	0x00000006	0x00000000	0x00000000
```

**nums = "1a32598746"**

after inspecting the program for a while got to know that we need to sort the array by swaping the indices which will be given as an input to the program as in bubble sort algorithm

### Python script to check for swapped values after input
```python
def fn():
    nums = ['1','a','3','2','5','9','8','7','4','6']
    while True:
        i = input()
        if 8 < i:
            break
        a = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = a
        print(' '.join(nums))
```

**got this array of inputs after to sort the array :-**

```
$ nc 2020.redpwnc.tf 31039
I hate my data structures class! Why can't I just sort by hand?
1
2
3
4
5
6
7
8
1
6
5
4
3
7
6
5
7
6
7
99
Well done!
flag{4ft3r_y0u_put_u54c0_0n_y0ur_c011ege_4pp5_y0u_5t1ll_h4ve_t0_d0_th15_57uff}
```

## flag
flag{4ft3r_y0u_put_u54c0_0n_y0ur_c011ege_4pp5_y0u_5t1ll_h4ve_t0_d0_th15_57uff}
