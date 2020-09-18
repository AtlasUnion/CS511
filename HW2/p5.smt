(declare-const p1 Bool)
(declare-const p2 Bool)
(declare-const p3 Bool)
(declare-const p4 Bool)

;; CNF
(declare-fun cnf (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause1 (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause2 (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause3 (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause4 (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause5 (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause6 (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause7 (Bool Bool Bool Bool) Bool)
(declare-fun cnf_clause8 (Bool Bool Bool Bool) Bool)

(assert (= (cnf_clause1 p1 p2 p3 p4) (or p1 (or (not p2) (or p3 p4)))))
(assert (= (cnf_clause2 p1 p2 p3 p4) (or (not p1) (or p2 (or p3 p4)))))
(assert (= (cnf_clause3 p1 p2 p3 p4) (or p1 (or p2 (or p3 (not p4))))))
(assert (= (cnf_clause4 p1 p2 p3 p4) (or (not p1) (or (not p2) (or p3 (not p4))))))
(assert (= (cnf_clause5 p1 p2 p3 p4) (or p1 (or (not p2) (or (not p3) (not p4))))))
(assert (= (cnf_clause6 p1 p2 p3 p4) (or (not p1) (or p2 (or (not p3) (not p4))))))
(assert (= (cnf_clause7 p1 p2 p3 p4) (or p1 (or p2 (or (not p3) p4)))))
(assert (= (cnf_clause8 p1 p2 p3 p4) (or (not p1) (or (not p2) (or (not p3) p4)))))

(assert (= (cnf p1 p2 p3 p4) 
        (and (cnf_clause1 p1 p2 p3 p4) (and (cnf_clause2 p1 p2 p3 p4) (and (cnf_clause3 p1 p2 p3 p4) (and (cnf_clause4 p1 p2 p3 p4) (and (cnf_clause5 p1 p2 p3 p4) (and (cnf_clause6 p1 p2 p3 p4) (and (cnf_clause7 p1 p2 p3 p4) (cnf_clause8 p1 p2 p3 p4))))))))))

;; DNF
(define-fun dnf_clause1 () Bool
            (and (not p1) (and (not p2) (and (not p3) (not p4)))))
(define-fun dnf_clause2 () Bool
            (and p1 (and p2 (and (not p3) (not p4)))))
(define-fun dnf_clause3 () Bool
            (and (not p1) (and p2 (and (not p3) p4))))
(define-fun dnf_clause4 () Bool
            (and p1 (and (not p2) (and (not p3) p4))))
(define-fun dnf_clause5 () Bool
            (and (not p1) (and (not p2) (and p3 p4))))
(define-fun dnf_clause6 () Bool
            (and p1 (and p2 (and p3 p4))))
(define-fun dnf_clause7 () Bool
            (and (not p1) (and p2 (and p3 (not p4)))))
(define-fun dnf_clause8 () Bool
            (and p1 (and (not p2) (and p3 (not p4)))))
(define-fun dnf () Bool
            (or dnf_clause1 (or dnf_clause2 (or dnf_clause3 (or dnf_clause4 (or dnf_clause5 (or dnf_clause6 (or dnf_clause7 dnf_clause8))))))))

;; bidirectional
(define-fun bidirectional () Bool
            (= (not p1) (= (not p2) (= (not p3) (not p4)))))

(assert (not (= (cnf p1 p2 p3 p4) dnf)))
(check-sat)

(assert (not (= dnf bidirectional)))
(check-sat)
