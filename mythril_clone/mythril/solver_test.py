from z3 import *

# Inicializando variáveis simbólicas
gas = BitVec('gas', 256)
calldatasize1 = BitVec('calldatasize1', 256)
calldatasize2 = BitVec('calldatasize2', 256)
calldata1 = Array('calldata1', BitVecSort(256), BitVecSort(8))
calldata2 = Array('calldata2', BitVecSort(256), BitVecSort(8))
balance = Array('balance', BitVecSort(256), BitVecSort(256))
call_value1 = BitVec('call_value1', 256)
call_value2 = BitVec('call_value2', 256)
sender_2 = BitVec('sender_2', 256)

constraints = [UGT(gas, 2300), 1271270613000041655817448348132275889066893754095 ==
Concat(0,
       If(calldatasize1 <= 12, 0, calldata1[12]),
       If(calldatasize1 <= 13, 0, calldata1[13]),
       If(calldatasize1 <= 14, 0, calldata1[14]),
       If(calldatasize1 <= 15, 0, calldata1[15]),
       If(calldatasize1 <= 16, 0, calldata1[16]),
       If(calldatasize1 <= 17, 0, calldata1[17]),
       If(calldatasize1 <= 18, 0, calldata1[18]),
       If(calldatasize1 <= 19, 0, calldata1[19]),
       If(calldatasize1 <= 20, 0, calldata1[20]),
       If(calldatasize1 <= 21, 0, calldata1[21]),
       If(calldatasize1 <= 22, 0, calldata1[22]),
       If(calldatasize1 <= 23, 0, calldata1[23]),
       If(calldatasize1 <= 24, 0, calldata1[24]),
       If(calldatasize1 <= 25, 0, calldata1[25]),
       If(calldatasize1 <= 26, 0, calldata1[26]),
       If(calldatasize1 <= 27, 0, calldata1[27]),
       If(calldatasize1 <= 28, 0, calldata1[28]),
       If(calldatasize1 <= 29, 0, calldata1[29]),
       If(calldatasize1 <= 30, 0, calldata1[30]),
       If(calldatasize1 <= 31, 0, calldata1[31])), Or(Not(ULE(balance[1004753105490295263244812946565948198177742958590],
           call_value1)),
   balance[1004753105490295263244812946565948198177742958590] ==
   call_value1), True, call_value1 == 0, calldatasize1 == 4562, True, And(Or(calldatasize1 <= 11, calldata1[11] == 0),
    Or(calldatasize1 <= 10, calldata1[10] == 0),
    Or(calldatasize1 <= 9, calldata1[9] == 0),
    Or(calldatasize1 <= 8, calldata1[8] == 0),
    Or(calldatasize1 <= 7, calldata1[7] == 0),
    Or(calldatasize1 <= 6, calldata1[6] == 0),
    Or(calldatasize1 <= 5, calldata1[5] == 0),
    Or(calldatasize1 <= 4, calldata1[4] == 0),
    Or(calldatasize1 <= 3, calldata1[3] == 0),
    Or(calldatasize1 <= 2, calldata1[2] == 0),
    Or(calldatasize1 <= 1, calldata1[1] == 0),
    Or(calldatasize1 <= 0, calldata1[0] == 0)), Power(256, 0) == 1, Power(256, 0) == 1, Or(Not(ULE(Store(Store(balance,
                       51421440056055728346017419001665401074216449311,
                       balance[51421440056055728346017419001665401074216449311] +
                       call_value1),
                 1004753105490295263244812946565948198177742958590,
                 balance[1004753105490295263244812946565948198177742958590] +
                 115792089237316195423570985008687907853269984665640564039457584007913129639935*
                 call_value1)[sender_2],
           call_value2)),
   Store(Store(balance,
               51421440056055728346017419001665401074216449311,
               balance[51421440056055728346017419001665401074216449311] +
               call_value1),
         1004753105490295263244812946565948198177742958590,
         balance[1004753105490295263244812946565948198177742958590] +
         115792089237316195423570985008687907853269984665640564039457584007913129639935*
         call_value1)[sender_2] ==
   call_value2), Or(sender_2 ==
   1004753105490295263244812946565948198177742958590,
   sender_2 ==
   974334424887268612135789888477522013103955028650,
   sender_2 ==
   1271270613000041655817448348132275889066893754095), ULE(4, calldatasize2), Not(ULE(2952712416,
        Concat(If(calldatasize2 <= 0, 0, calldata2[0]),
               If(calldatasize2 <= 1, 0, calldata2[1]),
               If(calldatasize2 <= 2, 0, calldata2[2]),
               If(calldatasize2 <= 3, 0, calldata2[3])))), And(calldata2[3] == 61,
    Not(calldatasize2 <= 3),
    calldata2[2] == 181,
    Not(calldatasize2 <= 2),
    calldata2[1] == 230,
    Not(calldatasize2 <= 1),
    calldata2[0] == 33,
    Not(calldatasize2 <= 0)), call_value2 == 0, 32 <=
115792089237316195423570985008687907853269984665640564039457584007913129639932 +
calldatasize2, And(Or(calldatasize2 <= 15, calldata2[15] == 0),
    Or(calldatasize2 <= 14, calldata2[14] == 0),
    Or(calldatasize2 <= 13, calldata2[13] == 0),
    Or(calldatasize2 <= 12, calldata2[12] == 0),
    Or(calldatasize2 <= 11, calldata2[11] == 0),
    Or(calldatasize2 <= 10, calldata2[10] == 0),
    Or(calldatasize2 <= 9, calldata2[9] == 0),
    Or(calldatasize2 <= 8, calldata2[8] == 0),
    Or(calldatasize2 <= 7, calldata2[7] == 0),
    Or(calldatasize2 <= 6, calldata2[6] == 0),
    Or(calldatasize2 <= 5, calldata2[5] == 0),
    Or(calldatasize2 <= 4, calldata2[4] == 0)), Not(And(Or(calldatasize2 <= 35, calldata2[35] == 0),
        Or(calldatasize2 <= 34, calldata2[34] == 0),
        Or(calldatasize2 <= 33, calldata2[33] == 0),
        Or(calldatasize2 <= 32, calldata2[32] == 0),
        Or(calldatasize2 <= 31, calldata2[31] == 0),
        Or(calldatasize2 <= 30, calldata2[30] == 0),
        Or(calldatasize2 <= 29, calldata2[29] == 0),
        Or(calldatasize2 <= 28, calldata2[28] == 0),
        Or(calldatasize2 <= 27, calldata2[27] == 0),
        Or(calldatasize2 <= 26, calldata2[26] == 0),
        Or(calldatasize2 <= 25, calldata2[25] == 0),
        Or(calldatasize2 <= 24, calldata2[24] == 0),
        Or(calldatasize2 <= 23, calldata2[23] == 0),
        Or(calldatasize2 <= 22, calldata2[22] == 0),
        Or(calldatasize2 <= 21, calldata2[21] == 0),
        Or(calldatasize2 <= 20, calldata2[20] == 0),
        Or(calldatasize2 <= 19, calldata2[19] == 0),
        Or(calldatasize2 <= 18, calldata2[18] == 0),
        Or(calldatasize2 <= 17, calldata2[17] == 0),
        Or(calldatasize2 <= 16, calldata2[16] == 0))), Power(256, 0) == 1, Extract(159, 0, sender_2) ==
1004753105490295263244812946565948198177742958590, Power(256, 0) == 1, Not(extcodesize_Concat(0,
       If(calldatasize1 <= 12, 0, calldata1[12]),
       If(calldatasize1 <= 13, 0, calldata1[13]),
       If(calldatasize1 <= 14, 0, calldata1[14]),
       If(calldatasize1 <= 15, 0, calldata1[15]),
       If(calldatasize1 <= 16, 0, calldata1[16]),
       If(calldatasize1 <= 17, 0, calldata1[17]),
       If(calldatasize1 <= 18, 0, calldata1[18]),
       If(calldatasize1 <= 19, 0, calldata1[19]),
       If(calldatasize1 <= 20, 0, calldata1[20]),
       If(calldatasize1 <= 21, 0, calldata1[21]),
       If(calldatasize1 <= 22, 0, calldata1[22]),
       If(calldatasize1 <= 23, 0, calldata1[23]),
       If(calldatasize1 <= 24, 0, calldata1[24]),
       If(calldatasize1 <= 25, 0, calldata1[25]),
       If(calldatasize1 <= 26, 0, calldata1[26]),
       If(calldatasize1 <= 27, 0, calldata1[27]),
       If(calldatasize1 <= 28, 0, calldata1[28]),
       If(calldatasize1 <= 29, 0, calldata1[29]),
       If(calldatasize1 <= 30, 0, calldata1[30]),
       If(calldatasize1 <= 31, 0, calldata1[31])) ==
    0), Or(Not(ULE(5000, calldatasize1)), calldatasize1 == 5000), Or(Not(ULE(1000000000000000000000,
           balance[1004753105490295263244812946565948198177742958590])),
   balance[1004753105490295263244812946565948198177742958590] ==
   1000000000000000000000), Or(Not(ULE(5000, calldatasize2)), calldatasize2 == 5000), Or(Not(ULE(1000000000000000000000, balance[sender_2])),
   balance[sender_2] == 1000000000000000000000), Or(Not(ULE(100000000000000000000,
           balance[1004753105490295263244812946565948198177742958590])),
   balance[1004753105490295263244812946565948198177742958590] ==
   100000000000000000000), Or(Not(ULE(100000000000000000000,
           balance[1271270613000041655817448348132275889066893754095])),
   balance[1271270613000041655817448348132275889066893754095] ==
   100000000000000000000), Or(Not(ULE(100000000000000000000,
           balance[51421440056055728346017419001665401074216449311])),
   balance[51421440056055728346017419001665401074216449311] ==
   100000000000000000000), And(True,
    And(keccak256_512-1(keccak256_512(Concat(If(calldatasize2 <=
                                        4,
                                        0,
                                        calldata2[4]),
                                        If(calldatasize2 <=
                                        5,
                                        0,
                                        calldata2[5]),
                                        If(calldatasize2 <=
                                        6,
                                        0,
                                        calldata2[6]),
                                        If(calldatasize2 <=
                                        7,
                                        0,
                                        calldata2[7]),
                                        If(calldatasize2 <=
                                        8,
                                        0,
                                        calldata2[8]),
                                        If(calldatasize2 <=
                                        9,
                                        0,
                                        calldata2[9]),
                                        If(calldatasize2 <=
                                        10,
                                        0,
                                        calldata2[10]),
                                        If(calldatasize2 <=
                                        11,
                                        0,
                                        calldata2[11]),
                                        If(calldatasize2 <=
                                        12,
                                        0,
                                        calldata2[12]),
                                        If(calldatasize2 <=
                                        13,
                                        0,
                                        calldata2[13]),
                                        If(calldatasize2 <=
                                        14,
                                        0,
                                        calldata2[14]),
                                        If(calldatasize2 <=
                                        15,
                                        0,
                                        calldata2[15]),
                                        If(calldatasize2 <=
                                        16,
                                        0,
                                        calldata2[16]),
                                        If(calldatasize2 <=
                                        17,
                                        0,
                                        calldata2[17]),
                                        If(calldatasize2 <=
                                        18,
                                        0,
                                        calldata2[18]),
                                        If(calldatasize2 <=
                                        19,
                                        0,
                                        calldata2[19]),
                                        If(calldatasize2 <=
                                        20,
                                        0,
                                        calldata2[20]),
                                        If(calldatasize2 <=
                                        21,
                                        0,
                                        calldata2[21]),
                                        If(calldatasize2 <=
                                        22,
                                        0,
                                        calldata2[22]),
                                        If(calldatasize2 <=
                                        23,
                                        0,
                                        calldata2[23]),
                                        If(calldatasize2 <=
                                        24,
                                        0,
                                        calldata2[24]),
                                        If(calldatasize2 <=
                                        25,
                                        0,
                                        calldata2[25]),
                                        If(calldatasize2 <=
                                        26,
                                        0,
                                        calldata2[26]),
                                        If(calldatasize2 <=
                                        27,
                                        0,
                                        calldata2[27]),
                                        If(calldatasize2 <=
                                        28,
                                        0,
                                        calldata2[28]),
                                        If(calldatasize2 <=
                                        29,
                                        0,
                                        calldata2[29]),
                                        If(calldatasize2 <=
                                        30,
                                        0,
                                        calldata2[30]),
                                        If(calldatasize2 <=
                                        31,
                                        0,
                                        calldata2[31]),
                                        If(calldatasize2 <=
                                        32,
                                        0,
                                        calldata2[32]),
                                        If(calldatasize2 <=
                                        33,
                                        0,
                                        calldata2[33]),
                                        If(calldatasize2 <=
                                        34,
                                        0,
                                        calldata2[34]),
                                        If(calldatasize2 <=
                                        35,
                                        0,
                                        calldata2[35]),
                                        4))) ==
        Concat(If(calldatasize2 <= 4, 0, calldata2[4]),
               If(calldatasize2 <= 5, 0, calldata2[5]),
               If(calldatasize2 <= 6, 0, calldata2[6]),
               If(calldatasize2 <= 7, 0, calldata2[7]),
               If(calldatasize2 <= 8, 0, calldata2[8]),
               If(calldatasize2 <= 9, 0, calldata2[9]),
               If(calldatasize2 <= 10, 0, calldata2[10]),
               If(calldatasize2 <= 11, 0, calldata2[11]),
               If(calldatasize2 <= 12, 0, calldata2[12]),
               If(calldatasize2 <= 13, 0, calldata2[13]),
               If(calldatasize2 <= 14, 0, calldata2[14]),
               If(calldatasize2 <= 15, 0, calldata2[15]),
               If(calldatasize2 <= 16, 0, calldata2[16]),
               If(calldatasize2 <= 17, 0, calldata2[17]),
               If(calldatasize2 <= 18, 0, calldata2[18]),
               If(calldatasize2 <= 19, 0, calldata2[19]),
               If(calldatasize2 <= 20, 0, calldata2[20]),
               If(calldatasize2 <= 21, 0, calldata2[21]),
               If(calldatasize2 <= 22, 0, calldata2[22]),
               If(calldatasize2 <= 23, 0, calldata2[23]),
               If(calldatasize2 <= 24, 0, calldata2[24]),
               If(calldatasize2 <= 25, 0, calldata2[25]),
               If(calldatasize2 <= 26, 0, calldata2[26]),
               If(calldatasize2 <= 27, 0, calldata2[27]),
               If(calldatasize2 <= 28, 0, calldata2[28]),
               If(calldatasize2 <= 29, 0, calldata2[29]),
               If(calldatasize2 <= 30, 0, calldata2[30]),
               If(calldatasize2 <= 31, 0, calldata2[31]),
               If(calldatasize2 <= 32, 0, calldata2[32]),
               If(calldatasize2 <= 33, 0, calldata2[33]),
               If(calldatasize2 <= 34, 0, calldata2[34]),
               If(calldatasize2 <= 35, 0, calldata2[35]),
               4),
        Or(And(keccak256_512-1(keccak256_512(Concat(If(calldatasize2 <=
                                        4,
                                        0,
                                        calldata2[4]),
                                        If(calldatasize2 <=
                                        5,
                                        0,
                                        calldata2[5]),
                                        If(calldatasize2 <=
                                        6,
                                        0,
                                        calldata2[6]),
                                        If(calldatasize2 <=
                                        7,
                                        0,
                                        calldata2[7]),
                                        If(calldatasize2 <=
                                        8,
                                        0,
                                        calldata2[8]),
                                        If(calldatasize2 <=
                                        9,
                                        0,
                                        calldata2[9]),
                                        If(calldatasize2 <=
                                        10,
                                        0,
                                        calldata2[10]),
                                        If(calldatasize2 <=
                                        11,
                                        0,
                                        calldata2[11]),
                                        If(calldatasize2 <=
                                        12,
                                        0,
                                        calldata2[12]),
                                        If(calldatasize2 <=
                                        13,
                                        0,
                                        calldata2[13]),
                                        If(calldatasize2 <=
                                        14,
                                        0,
                                        calldata2[14]),
                                        If(calldatasize2 <=
                                        15,
                                        0,
                                        calldata2[15]),
                                        If(calldatasize2 <=
                                        16,
                                        0,
                                        calldata2[16]),
                                        If(calldatasize2 <=
                                        17,
                                        0,
                                        calldata2[17]),
                                        If(calldatasize2 <=
                                        18,
                                        0,
                                        calldata2[18]),
                                        If(calldatasize2 <=
                                        19,
                                        0,
                                        calldata2[19]),
                                        If(calldatasize2 <=
                                        20,
                                        0,
                                        calldata2[20]),
                                        If(calldatasize2 <=
                                        21,
                                        0,
                                        calldata2[21]),
                                        If(calldatasize2 <=
                                        22,
                                        0,
                                        calldata2[22]),
                                        If(calldatasize2 <=
                                        23,
                                        0,
                                        calldata2[23]),
                                        If(calldatasize2 <=
                                        24,
                                        0,
                                        calldata2[24]),
                                        If(calldatasize2 <=
                                        25,
                                        0,
                                        calldata2[25]),
                                        If(calldatasize2 <=
                                        26,
                                        0,
                                        calldata2[26]),
                                        If(calldatasize2 <=
                                        27,
                                        0,
                                        calldata2[27]),
                                        If(calldatasize2 <=
                                        28,
                                        0,
                                        calldata2[28]),
                                        If(calldatasize2 <=
                                        29,
                                        0,
                                        calldata2[29]),
                                        If(calldatasize2 <=
                                        30,
                                        0,
                                        calldata2[30]),
                                        If(calldatasize2 <=
                                        31,
                                        0,
                                        calldata2[31]),
                                        If(calldatasize2 <=
                                        32,
                                        0,
                                        calldata2[32]),
                                        If(calldatasize2 <=
                                        33,
                                        0,
                                        calldata2[33]),
                                        If(calldatasize2 <=
                                        34,
                                        0,
                                        calldata2[34]),
                                        If(calldatasize2 <=
                                        35,
                                        0,
                                        calldata2[35]),
                                        4))) ==
               Concat(If(calldatasize2 <= 4,
                         0,
                         calldata2[4]),
                      If(calldatasize2 <= 5,
                         0,
                         calldata2[5]),
                      If(calldatasize2 <= 6,
                         0,
                         calldata2[6]),
                      If(calldatasize2 <= 7,
                         0,
                         calldata2[7]),
                      If(calldatasize2 <= 8,
                         0,
                         calldata2[8]),
                      If(calldatasize2 <= 9,
                         0,
                         calldata2[9]),
                      If(calldatasize2 <= 10,
                         0,
                         calldata2[10]),
                      If(calldatasize2 <= 11,
                         0,
                         calldata2[11]),
                      If(calldatasize2 <= 12,
                         0,
                         calldata2[12]),
                      If(calldatasize2 <= 13,
                         0,
                         calldata2[13]),
                      If(calldatasize2 <= 14,
                         0,
                         calldata2[14]),
                      If(calldatasize2 <= 15,
                         0,
                         calldata2[15]),
                      If(calldatasize2 <= 16,
                         0,
                         calldata2[16]),
                      If(calldatasize2 <= 17,
                         0,
                         calldata2[17]),
                      If(calldatasize2 <= 18,
                         0,
                         calldata2[18]),
                      If(calldatasize2 <= 19,
                         0,
                         calldata2[19]),
                      If(calldatasize2 <= 20,
                         0,
                         calldata2[20]),
                      If(calldatasize2 <= 21,
                         0,
                         calldata2[21]),
                      If(calldatasize2 <= 22,
                         0,
                         calldata2[22]),
                      If(calldatasize2 <= 23,
                         0,
                         calldata2[23]),
                      If(calldatasize2 <= 24,
                         0,
                         calldata2[24]),
                      If(calldatasize2 <= 25,
                         0,
                         calldata2[25]),
                      If(calldatasize2 <= 26,
                         0,
                         calldata2[26]),
                      If(calldatasize2 <= 27,
                         0,
                         calldata2[27]),
                      If(calldatasize2 <= 28,
                         0,
                         calldata2[28]),
                      If(calldatasize2 <= 29,
                         0,
                         calldata2[29]),
                      If(calldatasize2 <= 30,
                         0,
                         calldata2[30]),
                      If(calldatasize2 <= 31,
                         0,
                         calldata2[31]),
                      If(calldatasize2 <= 32,
                         0,
                         calldata2[32]),
                      If(calldatasize2 <= 33,
                         0,
                         calldata2[33]),
                      If(calldatasize2 <= 34,
                         0,
                         calldata2[34]),
                      If(calldatasize2 <= 35,
                         0,
                         calldata2[35]),
                      4),
               Or(ULT(115792089237316195423570985008687907450123599027852250724239960370997179030810,
                      keccak256_512(Concat(If(calldatasize2 <=
                                        4,
                                        0,
                                        calldata2[4]),
                                        If(calldatasize2 <=
                                        5,
                                        0,
                                        calldata2[5]),
                                        If(calldatasize2 <=
                                        6,
                                        0,
                                        calldata2[6]),
                                        If(calldatasize2 <=
                                        7,
                                        0,
                                        calldata2[7]),
                                        If(calldatasize2 <=
                                        8,
                                        0,
                                        calldata2[8]),
                                        If(calldatasize2 <=
                                        9,
                                        0,
                                        calldata2[9]),
                                        If(calldatasize2 <=
                                        10,
                                        0,
                                        calldata2[10]),
                                        If(calldatasize2 <=
                                        11,
                                        0,
                                        calldata2[11]),
                                        If(calldatasize2 <=
                                        12,
                                        0,
                                        calldata2[12]),
                                        If(calldatasize2 <=
                                        13,
                                        0,
                                        calldata2[13]),
                                        If(calldatasize2 <=
                                        14,
                                        0,
                                        calldata2[14]),
                                        If(calldatasize2 <=
                                        15,
                                        0,
                                        calldata2[15]),
                                        If(calldatasize2 <=
                                        16,
                                        0,
                                        calldata2[16]),
                                        If(calldatasize2 <=
                                        17,
                                        0,
                                        calldata2[17]),
                                        If(calldatasize2 <=
                                        18,
                                        0,
                                        calldata2[18]),
                                        If(calldatasize2 <=
                                        19,
                                        0,
                                        calldata2[19]),
                                        If(calldatasize2 <=
                                        20,
                                        0,
                                        calldata2[20]),
                                        If(calldatasize2 <=
                                        21,
                                        0,
                                        calldata2[21]),
                                        If(calldatasize2 <=
                                        22,
                                        0,
                                        calldata2[22]),
                                        If(calldatasize2 <=
                                        23,
                                        0,
                                        calldata2[23]),
                                        If(calldatasize2 <=
                                        24,
                                        0,
                                        calldata2[24]),
                                        If(calldatasize2 <=
                                        25,
                                        0,
                                        calldata2[25]),
                                        If(calldatasize2 <=
                                        26,
                                        0,
                                        calldata2[26]),
                                        If(calldatasize2 <=
                                        27,
                                        0,
                                        calldata2[27]),
                                        If(calldatasize2 <=
                                        28,
                                        0,
                                        calldata2[28]),
                                        If(calldatasize2 <=
                                        29,
                                        0,
                                        calldata2[29]),
                                        If(calldatasize2 <=
                                        30,
                                        0,
                                        calldata2[30]),
                                        If(calldatasize2 <=
                                        31,
                                        0,
                                        calldata2[31]),
                                        If(calldatasize2 <=
                                        32,
                                        0,
                                        calldata2[32]),
                                        If(calldatasize2 <=
                                        33,
                                        0,
                                        calldata2[33]),
                                        If(calldatasize2 <=
                                        34,
                                        0,
                                        calldata2[34]),
                                        If(calldatasize2 <=
                                        35,
                                        0,
                                        calldata2[35]),
                                        4))),
                  115792089237316195423570985008687907450123599027852250724239960370997179030810 ==
                  keccak256_512(Concat(If(calldatasize2 <=
                                        4,
                                        0,
                                        calldata2[4]),
                                       If(calldatasize2 <=
                                        5,
                                        0,
                                        calldata2[5]),
                                       If(calldatasize2 <=
                                        6,
                                        0,
                                        calldata2[6]),
                                       If(calldatasize2 <=
                                        7,
                                        0,
                                        calldata2[7]),
                                       If(calldatasize2 <=
                                        8,
                                        0,
                                        calldata2[8]),
                                       If(calldatasize2 <=
                                        9,
                                        0,
                                        calldata2[9]),
                                       If(calldatasize2 <=
                                        10,
                                        0,
                                        calldata2[10]),
                                       If(calldatasize2 <=
                                        11,
                                        0,
                                        calldata2[11]),
                                       If(calldatasize2 <=
                                        12,
                                        0,
                                        calldata2[12]),
                                       If(calldatasize2 <=
                                        13,
                                        0,
                                        calldata2[13]),
                                       If(calldatasize2 <=
                                        14,
                                        0,
                                        calldata2[14]),
                                       If(calldatasize2 <=
                                        15,
                                        0,
                                        calldata2[15]),
                                       If(calldatasize2 <=
                                        16,
                                        0,
                                        calldata2[16]),
                                       If(calldatasize2 <=
                                        17,
                                        0,
                                        calldata2[17]),
                                       If(calldatasize2 <=
                                        18,
                                        0,
                                        calldata2[18]),
                                       If(calldatasize2 <=
                                        19,
                                        0,
                                        calldata2[19]),
                                       If(calldatasize2 <=
                                        20,
                                        0,
                                        calldata2[20]),
                                       If(calldatasize2 <=
                                        21,
                                        0,
                                        calldata2[21]),
                                       If(calldatasize2 <=
                                        22,
                                        0,
                                        calldata2[22]),
                                       If(calldatasize2 <=
                                        23,
                                        0,
                                        calldata2[23]),
                                       If(calldatasize2 <=
                                        24,
                                        0,
                                        calldata2[24]),
                                       If(calldatasize2 <=
                                        25,
                                        0,
                                        calldata2[25]),
                                       If(calldatasize2 <=
                                        26,
                                        0,
                                        calldata2[26]),
                                       If(calldatasize2 <=
                                        27,
                                        0,
                                        calldata2[27]),
                                       If(calldatasize2 <=
                                        28,
                                        0,
                                        calldata2[28]),
                                       If(calldatasize2 <=
                                        29,
                                        0,
                                        calldata2[29]),
                                       If(calldatasize2 <=
                                        30,
                                        0,
                                        calldata2[30]),
                                       If(calldatasize2 <=
                                        31,
                                        0,
                                        calldata2[31]),
                                       If(calldatasize2 <=
                                        32,
                                        0,
                                        calldata2[32]),
                                       If(calldatasize2 <=
                                        33,
                                        0,
                                        calldata2[33]),
                                       If(calldatasize2 <=
                                        34,
                                        0,
                                        calldata2[34]),
                                       If(calldatasize2 <=
                                        35,
                                        0,
                                        calldata2[35]),
                                       4))),
               ULT(keccak256_512(Concat(If(calldatasize2 <=
                                        4,
                                        0,
                                        calldata2[4]),
                                        If(calldatasize2 <=
                                        5,
                                        0,
                                        calldata2[5]),
                                        If(calldatasize2 <=
                                        6,
                                        0,
                                        calldata2[6]),
                                        If(calldatasize2 <=
                                        7,
                                        0,
                                        calldata2[7]),
                                        If(calldatasize2 <=
                                        8,
                                        0,
                                        calldata2[8]),
                                        If(calldatasize2 <=
                                        9,
                                        0,
                                        calldata2[9]),
                                        If(calldatasize2 <=
                                        10,
                                        0,
                                        calldata2[10]),
                                        If(calldatasize2 <=
                                        11,
                                        0,
                                        calldata2[11]),
                                        If(calldatasize2 <=
                                        12,
                                        0,
                                        calldata2[12]),
                                        If(calldatasize2 <=
                                        13,
                                        0,
                                        calldata2[13]),
                                        If(calldatasize2 <=
                                        14,
                                        0,
                                        calldata2[14]),
                                        If(calldatasize2 <=
                                        15,
                                        0,
                                        calldata2[15]),
                                        If(calldatasize2 <=
                                        16,
                                        0,
                                        calldata2[16]),
                                        If(calldatasize2 <=
                                        17,
                                        0,
                                        calldata2[17]),
                                        If(calldatasize2 <=
                                        18,
                                        0,
                                        calldata2[18]),
                                        If(calldatasize2 <=
                                        19,
                                        0,
                                        calldata2[19]),
                                        If(calldatasize2 <=
                                        20,
                                        0,
                                        calldata2[20]),
                                        If(calldatasize2 <=
                                        21,
                                        0,
                                        calldata2[21]),
                                        If(calldatasize2 <=
                                        22,
                                        0,
                                        calldata2[22]),
                                        If(calldatasize2 <=
                                        23,
                                        0,
                                        calldata2[23]),
                                        If(calldatasize2 <=
                                        24,
                                        0,
                                        calldata2[24]),
                                        If(calldatasize2 <=
                                        25,
                                        0,
                                        calldata2[25]),
                                        If(calldatasize2 <=
                                        26,
                                        0,
                                        calldata2[26]),
                                        If(calldatasize2 <=
                                        27,
                                        0,
                                        calldata2[27]),
                                        If(calldatasize2 <=
                                        28,
                                        0,
                                        calldata2[28]),
                                        If(calldatasize2 <=
                                        29,
                                        0,
                                        calldata2[29]),
                                        If(calldatasize2 <=
                                        30,
                                        0,
                                        calldata2[30]),
                                        If(calldatasize2 <=
                                        31,
                                        0,
                                        calldata2[31]),
                                        If(calldatasize2 <=
                                        32,
                                        0,
                                        calldata2[32]),
                                        If(calldatasize2 <=
                                        33,
                                        0,
                                        calldata2[33]),
                                        If(calldatasize2 <=
                                        34,
                                        0,
                                        calldata2[34]),
                                        If(calldatasize2 <=
                                        35,
                                        0,
                                        calldata2[35]),
                                        4)),
                   115792089237316195423570985008687907450135178236775982343782317469498047821595),
               URem(keccak256_512(Concat(If(calldatasize2 <=
                                        4,
                                        0,
                                        calldata2[4]),
                                        If(calldatasize2 <=
                                        5,
                                        0,
                                        calldata2[5]),
                                        If(calldatasize2 <=
                                        6,
                                        0,
                                        calldata2[6]),
                                        If(calldatasize2 <=
                                        7,
                                        0,
                                        calldata2[7]),
                                        If(calldatasize2 <=
                                        8,
                                        0,
                                        calldata2[8]),
                                        If(calldatasize2 <=
                                        9,
                                        0,
                                        calldata2[9]),
                                        If(calldatasize2 <=
                                        10,
                                        0,
                                        calldata2[10]),
                                        If(calldatasize2 <=
                                        11,
                                        0,
                                        calldata2[11]),
                                        If(calldatasize2 <=
                                        12,
                                        0,
                                        calldata2[12]),
                                        If(calldatasize2 <=
                                        13,
                                        0,
                                        calldata2[13]),
                                        If(calldatasize2 <=
                                        14,
                                        0,
                                        calldata2[14]),
                                        If(calldatasize2 <=
                                        15,
                                        0,
                                        calldata2[15]),
                                        If(calldatasize2 <=
                                        16,
                                        0,
                                        calldata2[16]),
                                        If(calldatasize2 <=
                                        17,
                                        0,
                                        calldata2[17]),
                                        If(calldatasize2 <=
                                        18,
                                        0,
                                        calldata2[18]),
                                        If(calldatasize2 <=
                                        19,
                                        0,
                                        calldata2[19]),
                                        If(calldatasize2 <=
                                        20,
                                        0,
                                        calldata2[20]),
                                        If(calldatasize2 <=
                                        21,
                                        0,
                                        calldata2[21]),
                                        If(calldatasize2 <=
                                        22,
                                        0,
                                        calldata2[22]),
                                        If(calldatasize2 <=
                                        23,
                                        0,
                                        calldata2[23]),
                                        If(calldatasize2 <=
                                        24,
                                        0,
                                        calldata2[24]),
                                        If(calldatasize2 <=
                                        25,
                                        0,
                                        calldata2[25]),
                                        If(calldatasize2 <=
                                        26,
                                        0,
                                        calldata2[26]),
                                        If(calldatasize2 <=
                                        27,
                                        0,
                                        calldata2[27]),
                                        If(calldatasize2 <=
                                        28,
                                        0,
                                        calldata2[28]),
                                        If(calldatasize2 <=
                                        29,
                                        0,
                                        calldata2[29]),
                                        If(calldatasize2 <=
                                        30,
                                        0,
                                        calldata2[30]),
                                        If(calldatasize2 <=
                                        31,
                                        0,
                                        calldata2[31]),
                                        If(calldatasize2 <=
                                        32,
                                        0,
                                        calldata2[32]),
                                        If(calldatasize2 <=
                                        33,
                                        0,
                                        calldata2[33]),
                                        If(calldatasize2 <=
                                        34,
                                        0,
                                        calldata2[34]),
                                        If(calldatasize2 <=
                                        35,
                                        0,
                                        calldata2[35]),
                                        4)),
                    64) ==
               0),
           False)))]
# Criando um solver Z3

s = Solver()

# Adicionando a restrição ao solver
for constraint in constraints:
    s.add(constraint)
# Verificando a satisfiabilidade
if s.check() == sat:
    print("A restrição é satisfiável.")
else:
    print("A restrição não é satisfiável.")