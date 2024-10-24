def crc_remainder(message, polynomial):
    poly_length = polynomial.bit_length() 
    augmented_message = message << (poly_length - 1)

    mask = 1 << (augmented_message.bit_length() - 1)

    while augmented_message.bit_length() >= poly_length:
        if augmented_message & mask:  
            augmented_message ^= polynomial << (augmented_message.bit_length() - poly_length)
        mask >>= 1

    return augmented_message

message = int('1010011010', 2) 
polynomial = int('110101', 2) 

remainder = crc_remainder(message, polynomial)

frame_bin = bin(message)[2:]  
generator_bin = bin(polynomial)[2:]  

message_with_zeros = message << 4  
message_with_zeros_bin = bin(message_with_zeros)[2:]  

transmitted_frame = (message << 4) | remainder 
transmitted_frame_bin = bin(transmitted_frame)[2:]  

print(f"Frame: {frame_bin}")
print(f"Generator: {generator_bin}")
print(f"Message after appending 4 zero bits: {message_with_zeros_bin}")
print(f'Remainder: {bin(remainder)[2:]}')
print(f'Transmitted Frame: {transmitted_frame_bin}')
