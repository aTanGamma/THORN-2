
Adder = open("Adder_ROM.bin", "wb")
Conds = open("Conditions_ROM.bin", "wb")
Carry = open("Carry_ROM.bin", "wb")

G = 0
P = 0
Z = 0
Y = 0

for C in range(2):
    for B in range(256):
        for A in range(256):
            S = A+B
            Y = (A+B+C) & 0xFF
            Adder.write(Y.to_bytes(1))


for B in range(256):
    for A in range(256):
            S = A+B

            if S > 255:
                G = 4
            else:
                G = 0

            if (S & 0xFF) == 255:
                P = 2
            else:
                P = 0

            if (S & 0xFF) == 0:
                Z = 1
            else:
                Z = 0

            Conds.write((G|P|Z).to_bytes(1))


for C in range(2):
    for G in range(256):
        for P in range(256):

            Cn = 0

            Gn = [
                (G & 0x01) >> 0,
                (G & 0x02) >> 1,
                (G & 0x04) >> 2,
                (G & 0x08) >> 3,
                (G & 0x10) >> 4,
                (G & 0x20) >> 5,
                (G & 0x40) >> 6,
                (G & 0x80) >> 7 
            ]
            Pn = [
                (P & 0x01) >> 0,
                (P & 0x02) >> 1,
                (P & 0x04) >> 2,
                (P & 0x08) >> 3,
                (P & 0x10) >> 4,
                (P & 0x20) >> 5,
                (P & 0x40) >> 6,
                (P & 0x80) >> 7 
            ]

            #C0
            if (
                 Gn[0] | 
                (Pn[0] & C)
            ):
                Cn |= 0x01

            #C1
            if (
                 Gn[1] | 
                (Pn[1] & Gn[0]) |
                (Pn[1] & Pn[0] & C)
            ):
                Cn |= 0x02
            
            #C2
            if (
                 Gn[2] |
                (Pn[2] & Gn[1]) |
                (Pn[2] & Pn[1] & Gn[0]) |
                (Pn[2] & Pn[1] & Pn[0] & C)
            ):
                Cn |= 0x04

            #C3
            if (
                 Gn[3] |
                (Pn[3] & Gn[2]) |
                (Pn[3] & Pn[2] & Gn[1]) |
                (Pn[3] & Pn[2] & Pn[1] & Gn[0]) |
                (Pn[3] & Pn[2] & Pn[1] & Pn[0] & C)
            ):
                Cn |= 0x08

            #C4
            if (
                 Gn[4] |
                (Pn[4] & Gn[3]) |
                (Pn[4] & Pn[3] & Gn[2]) |
                (Pn[4] & Pn[3] & Pn[2] & Gn[1]) |
                (Pn[4] & Pn[3] & Pn[2] & Pn[1] & Gn[0]) |
                (Pn[4] & Pn[3] & Pn[2] & Pn[1] & Pn[0] & C)
            ):
                Cn |= 0x10

            #C5
            if (
                 Gn[5] |
                (Pn[5] & Gn[4]) |
                (Pn[5] & Pn[4] & Gn[3]) |
                (Pn[5] & Pn[4] & Pn[3] & Gn[2]) |
                (Pn[5] & Pn[4] & Pn[3] & Pn[2] & Gn[1]) |
                (Pn[5] & Pn[4] & Pn[3] & Pn[2] & Pn[1] & Gn[0]) |
                (Pn[5] & Pn[4] & Pn[3] & Pn[2] & Pn[1] & Pn[0] & C)
            ):
                Cn |= 0x20

            #C6
            if (
                 Gn[6] |
                (Pn[6] & Gn[5]) |
                (Pn[6] & Pn[5] & Gn[4]) |
                (Pn[6] & Pn[5] & Pn[4] & Gn[3]) |
                (Pn[6] & Pn[5] & Pn[4] & Pn[3] & Gn[2]) |
                (Pn[6] & Pn[5] & Pn[4] & Pn[3] & Pn[2] & Gn[1]) |
                (Pn[6] & Pn[5] & Pn[4] & Pn[3] & Pn[2] & Pn[1] & Gn[0]) |
                (Pn[6] & Pn[5] & Pn[4] & Pn[3] & Pn[2] & Pn[1] & Pn[0] & C)
            ):
                Cn |= 0x40

            #C7
            if (
                 Gn[7] |
                (Pn[7] & Gn[6]) |
                (Pn[7] & Pn[6] & Gn[5]) |
                (Pn[7] & Pn[6] & Pn[5] & Gn[4]) |
                (Pn[7] & Pn[6] & Pn[5] & Pn[4] & Gn[3]) |
                (Pn[7] & Pn[6] & Pn[5] & Pn[4] & Pn[3] & Gn[2]) |
                (Pn[7] & Pn[6] & Pn[5] & Pn[4] & Pn[3] & Pn[2] & Gn[1]) |
                (Pn[7] & Pn[6] & Pn[5] & Pn[4] & Pn[3] & Pn[2] & Pn[1] & Gn[0]) |
                (Pn[7] & Pn[6] & Pn[5] & Pn[4] & Pn[3] & Pn[2] & Pn[1] & Pn[0] & C)
            ):
                Cn |= 0x80

            Carry.write(Cn.to_bytes(1))





Adder.close()
Conds.close()
Carry.close()