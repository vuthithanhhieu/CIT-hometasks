print ([x for x in range(2, 10000) if not [l for l in range(2, x) if not x % l]][:1000])

