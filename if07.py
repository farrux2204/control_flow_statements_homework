def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    x=0
    if a>0:
        a%2==1
        x="positive odd number"
    if a>0:
        a%2==0
        x="positive even number"
    if a<0:
        a%2==1
        x="negative odd number"
    if a<0:
        a%2==0  
        x="negative even number"
    if a==0:       
        x="the number is zero"
    return x
print(main(0))