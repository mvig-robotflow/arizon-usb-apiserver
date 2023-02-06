# ARIZON driver

## Protocol

| Field        | Content |
| ------------ | ------- |
| Head         | 0xFE    |
| Status       | 1 Byte  |
| Data         | 3 Byte  |
| XOR checksum | 1 Byte  |

- Status: 4 bits of address + 4 bits represents number of digits
- Data: 3 bytes of signed integers, no digit, big-endian.
- Checksum: xor() of first 5 bytes
