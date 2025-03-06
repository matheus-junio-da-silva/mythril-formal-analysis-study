(set-option :opt.timeout 25000)
(declare-fun call_value1 () (_ BitVec 256))
(declare-fun balance () (Array (_ BitVec 256) (_ BitVec 256)))
(declare-fun call_value2 () (_ BitVec 256))
(declare-fun sender_2 () (_ BitVec 256))
(declare-fun |2_calldatasize| () (_ BitVec 256))
(declare-fun |2_calldata| () (Array (_ BitVec 256) (_ BitVec 8)))
(assert (or (not (bvule (select balance
                        #x000000000000000000000000affeaffeaffeaffeaffeaffeaffeaffeaffeaffe)
                call_value1))
    (= (select balance
               #x000000000000000000000000affeaffeaffeaffeaffeaffeaffeaffeaffeaffe)
       call_value1)))
(assert true)
(assert (not (= call_value1
        #x0000000000000000000000000000000000000000000000000000000000000000)))
(assert (let ((a!1 (store (store balance
                         #x0000000000000000000000000901d12ebe1b195e5aa8748e62bd7734ae19b51f
                         (bvadd (select balance
                                        #x0000000000000000000000000901d12ebe1b195e5aa8748e62bd7734ae19b51f)
                                call_value1))
                  #x000000000000000000000000affeaffeaffeaffeaffeaffeaffeaffeaffeaffe
                  (bvadd (select balance
                                 #x000000000000000000000000affeaffeaffeaffeaffeaffeaffeaffeaffeaffe)
                         (bvmul #xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                                call_value1)))))
  (or (not (bvule (select a!1 sender_2) call_value2))
      (= (select a!1 sender_2) call_value2))))
(assert (or (= sender_2
       #x000000000000000000000000affeaffeaffeaffeaffeaffeaffeaffeaffeaffe)
    (= sender_2
       #x000000000000000000000000deadbeefdeadbeefdeadbeefdeadbeefdeadbeef)
    (= sender_2
       #x000000000000000000000000aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)))
(assert (or (not (= ((_ extract 255 3) |2_calldatasize|)
            #b0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
    (bvule #b100 ((_ extract 2 0) |2_calldatasize|))))
(assert (and (= (select |2_calldata|
                #x0000000000000000000000000000000000000000000000000000000000000003)
        #x19)
     (not (bvsle |2_calldatasize|
                 #x0000000000000000000000000000000000000000000000000000000000000003))
     (= (select |2_calldata|
                #x0000000000000000000000000000000000000000000000000000000000000002)
        #x9e)
     (not (bvsle |2_calldatasize|
                 #x0000000000000000000000000000000000000000000000000000000000000002))
     (= (select |2_calldata|
                #x0000000000000000000000000000000000000000000000000000000000000001)
        #x1f)
     (not (bvsle |2_calldatasize|
                 #x0000000000000000000000000000000000000000000000000000000000000001))
     (= (select |2_calldata|
                #x0000000000000000000000000000000000000000000000000000000000000000)
        #x6a)
     (not (bvsle |2_calldatasize|
                 #x0000000000000000000000000000000000000000000000000000000000000000))))
(assert (not (= call_value2
        #x0000000000000000000000000000000000000000000000000000000000000000)))
(assert true)
(check-sat)
