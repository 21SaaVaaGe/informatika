import math


def float_to_single(x: float) -> str:
    sign = 0 if x >= 0 else 1
    absolute_x = abs(x)

    if absolute_x == 0.0:
        return f"{sign:1b}" + "0" * 31

    m, e = math.frexp(absolute_x)
    m *= 2
    e -= 1

    bias = 127
    exp = e + bias
    # 3. Мантисса
    frac = m - 1.0
    mantissa_bits = []
    for _ in range(23):
        frac *= 2
        bit = int(frac)
        mantissa_bits.append(str(bit))
        frac -= bit

    exponenta_bits = f"{exp:08b}"
    mantissa_bits_result = ''.join(mantissa_bits)

    return f"{sign:1b}" + exponenta_bits + mantissa_bits_result


def bits_to_hex(bits: str) -> str:
    n = int(bits, 2)
    return f"{n:08X}"


x =  -21.25
bits = float_to_single(x)
hex_str = bits_to_hex(bits)

print("Число:", x)
print("Двоичный формат:", bits)
print('HEX', hex_str)
