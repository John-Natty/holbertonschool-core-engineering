#!/usr/bin/env python3

language = "Python"
version = 3
pi_value = 3.14159
pi_approx = format(pi_value, ".2f")
computation_valid = version == 3 and pi_value > 3.14

print(f"Language: {language}")
print(f"Version: {version}")
print(f"Pi approx: {pi_approx}")
print(f"Computation valid: {computation_valid}")
