"""
this has cade for the problem small number first. all it does it put the smallest number first.
Jude averitt - September 2026
"""

def main() -> None:
  pass # remove me

  # input
  line = input()
  a, b = line.split()
  a = int(a)
  b = int(b)


  # processing
  if a>b:
    print(F"{b} {a}")

  else:
    print(f"{a} {b}")
  
  # output


if __name__ == "__main__":
  main()
    
