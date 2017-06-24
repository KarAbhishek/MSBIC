def gcd(n, n2):
    st = set()
    for num in range(n, 0, -1):
        if n % num == 0:
            st.add(n)
    for num in range(n2, 0, -1):
        if n2 % num == 0 and n2 in st:
            return n2
