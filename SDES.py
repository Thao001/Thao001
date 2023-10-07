class SDES:
    # Permutation tables
    P10_TABLE = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    P8_TABLE = [5, 2, 6, 3, 7, 4, 9, 8]
    P4_TABLE = [1, 3, 2, 0]
    IP_TABLE = [1, 5, 2, 0, 3, 7, 4, 6]
    EP_TABLE = [3, 0, 1, 2, 1, 2, 3, 0]
    IP_NI_TABLE = [3, 0, 2, 4, 6, 1, 7, 5]

    # S-boxes
    SBOX0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 0, 2]
    ]
    SBOX1 = [
        [0, 1, 2, 3],
        [2, 3, 1, 0],
        [3, 0, 1, 2],
        [2, 1, 0, 3]
    ]

    KEY_LENGTH = 10
    DATA_LENGTH = 8

    @staticmethod
    def permute(input_str, table):
        output_str = ''.join(input_str[i] for i in table)
        return output_str

    @staticmethod
    def ls(key, n):
        left_half = key[:5]
        right_half = key[5:]
        shifted_left = left_half[n:] + left_half[:n]
        shifted_right = right_half[n:] + right_half[:n]
        return shifted_left + shifted_right

    @staticmethod
    def subkey(k, p10_table, p8_table):
        p10_key = SDES.permute(k, p10_table)
        k1 = SDES.permute(SDES.ls(p10_key, 1), p8_table)
        k2 = SDES.permute(SDES.ls(SDES.ls(p10_key, 1), 1), p8_table)
        return k1, k2

    @staticmethod
    def function(right_half, k, sbox0, sbox1, p4_table):
        expanded = SDES.permute(right_half, SDES.EP_TABLE)
        xored = bin(int(expanded, 2) ^ int(k, 2))[2:].zfill(8)
        s0_input = xored[:4]
        s1_input = xored[4:]
        s0_row = int(s0_input[0] + s0_input[3], 2)
        s0_col = int(s0_input[1:3], 2)
        s1_row = int(s1_input[0] + s1_input[3], 2)
        s1_col = int(s1_input[1:3], 2)
        s0_output = format(sbox0[s0_row][s0_col], '02b')
        s1_output = format(sbox1[s1_row][s1_col], '02b')
        s_output = s0_output + s1_output
        return SDES.permute(s_output, p4_table)

    @staticmethod
    def encrypt(p, k):
        k1, k2 = SDES.subkey(k, SDES.P10_TABLE, SDES.P8_TABLE)
        p = SDES.permute(p, SDES.IP_TABLE)
        l0, r0 = p[:4], p[4:]
        l1 = r0
        f_result = SDES.function(r0, k1, SDES.SBOX0, SDES.SBOX1, SDES.P4_TABLE)
        r1 = format(int(l0, 2) ^ int(f_result, 2), '04b')
        f_result = SDES.function(r1, k2, SDES.SBOX0, SDES.SBOX1, SDES.P4_TABLE)
        r2 = format(int(l1, 2) ^ int(f_result, 2), '04b')
        return SDES.permute(r2 + r1, SDES.IP_NI_TABLE)

    @staticmethod
    def decrypt(c, k):
        k1, k2 = SDES.subkey(k, SDES.P10_TABLE, SDES.P8_TABLE)
        c = SDES.permute(c, SDES.IP_TABLE)
        r2, l2 = c[:4], c[4:]
        f_result = SDES.function(l2, k2, SDES.SBOX0, SDES.SBOX1, SDES.P4_TABLE)
        l1 = format(int(r2, 2) ^ int(f_result, 2), '04b')
        f_result = SDES.function(l1, k1, SDES.SBOX0, SDES.SBOX1, SDES.P4_TABLE)
        r1 = format(int(l2, 2) ^ int(f_result, 2), '04b')
        return SDES.permute(r1 + l1, SDES.IP_NI_TABLE)

    @staticmethod
    def encrypt_asc(p, k):
        mi = ""
        for char in p:
            asc_in = ord(char)
            in_binary = format(asc_in, '08b')
            out = SDES.encrypt(in_binary, k)
            asc_out = int(out, 2)
            mi += chr(asc_out)
        return mi

    @staticmethod
    def decrypt_asc(c, k):
        ming = ""
        for char in c:
            asc_in = ord(char)
            in_binary = format(asc_in, '08b')
            out = SDES.decrypt(in_binary, k)
            asc_out = int(out, 2)
            ming += chr(asc_out)
        return ming
