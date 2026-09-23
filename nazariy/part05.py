"""5. Standart qiymatga ega parametr (default parameter) qanday belgilanadi? Misol yozing.
"""

def age(year, now=2026):
    return now-year

print(age(2005))
print(age(2005, 2027))


# bu funksiyada default qiymat joriy yil berilgan pastda joriy yil bermasa default 2026 ni oladi.