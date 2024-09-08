# Rain

## Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

- Prototype: def rain(walls)
- walls is a list of non-negative integers.
- Return: Integer indicating total amount of rainwater retained.
- Assume that the ends of the list (before index 0 and after index walls[-1]) are not walls, meaning they will not retain water.
- If the list is empty return 0

```
ronald@ubuntu:~/$ cat 0_main.py
#!/usr/bin/python3
"""
0_main
"""
rain = __import__('0-rain').rain

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))

ronald@ubuntu:~/$ 
ronald@ubuntu:~/$ ./0_main.py
6
6
ronald@ubuntu:~/$ 
```

Visual representation of the walls `[0, 1, 0, 2, 0, 3, 0, 4]`

<img width="342" alt="85ef782020ac6efdc7004b62ea86724a552285b4" src="https://github.com/Ronnie5562/alu-interview/assets/110787129/04410fad-00b2-4be8-90e4-bccab78126df">

Visual representation of the walls `[2, 0, 0, 4, 0, 0, 1, 0]`

<img width="341" alt="9a27c3e4e214e55b3c0b8b1439fdc99b4a184ff5" src="https://github.com/Ronnie5562/alu-interview/assets/110787129/9e8c4625-58d3-4782-b255-cd9598326a46">


# AUTHOR

## [`Abimbola Ronald`](https://www.linkedin.com/in/abimbola-ronald-977299224/)
