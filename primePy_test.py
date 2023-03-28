# You may run primes.about() afer importing the package. The following is a list of all included methods.
from primePy import primes

# primes.check(n) returns True if n is a prime number.
prime_check = 123456
print("{}은 소수인가: {}".format(prime_check, primes.check(prime_check)))
print()

# primes.factor(n) returns the lowest prime factor of n.
factor = 12345
print("{}의 소인수 중 가장 작은수는 {}입니다.".format(factor, primes.factor(factor)))
print()

# primes.facors(n) returns all the prime factors of n with multiplicity.
print("{}의 소인수는 {} 입니다.".format(factor, primes.factors(factor)))
print()

# primes.first(n) returns first n many prime.
first_prime = 10
print("1부터 처음 {}개의 소수는 {} 입니다.".format(first_prime, primes.first(first_prime)))
print()

# primes.upto(n) returns all the prime less than or equal to n.
upto_prime = 100
print("{} 보다 작은 수 중에 소수는 {} 입니다.".format(upto_prime, primes.upto(upto_prime)))
print()

# primes.between(m,n) returns all the prime between m and n.
between_min = 100
between_max = 1000
print("{}과 {}사이에 소수는 {} 입니다.".format(between_min, between_max, primes.between(between_min, between_max)))
print()
print("{}과 {}사이에 소수는 {}개가 있습니다.".format(between_min, between_max, len(primes.between(between_min, between_max))))
print()

# primes.phi(n) returns the Euler's phi(n) i.e., the number of integers less than n which have no common factor with n.
# 1부터 n까지의 정수 가운데 n과 서로소인 것들의 개수
primes_phi = 80
print("{}보다 작은 정수 중에 {}서로소 인 수의 갯수는 {}개 입니다.".format(primes_phi, primes_phi, primes.phi(primes_phi)))
print()
