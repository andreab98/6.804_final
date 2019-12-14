;; (define (get-property2 property)
;;   (lambda (property-list) (second (first (filter (lambda (p) (equal? property (first p))) property-list)))))

(define (cut-number-precision n decimals)
  (let ([precision (expt 10 decimals)])
    (exact->inexact
     (/ (div (* (inexact->exact n) precision) 1)
        precision))))

(define (cut-number-precision-paths inf-path obs-path)
  (if (and (list? inf-path)
           (list? obs-path))
      (map (lambda (i j) (cut-number-precision-paths i j)) inf-path obs-path)
      (cut-number-precision (abs (- inf-path obs-path)) 1)))


(define (insert l n e)
  (if (= 0 n)
      (cons e l)
      (cons (car l)
            (insert (cdr l) (- n 1) e))))

(define (seq start end)
  (if (= start end)
      (list end)
      (cons start (seq (+ start 1) end))))

(define (permute l)
  (if (null? l)
      '(())
      (apply append (map (lambda (p)
                           (map (lambda (n)
                                  (insert p n (car l)))
                                (seq 0 (length p))))
                         (permute (cdr l))))))

(define (remove-duplicates l)
  (cond ((null? l)
         '())
        ((member (car l) (cdr l))
         (remove-duplicates (cdr l)))
        (else
         (cons (car l) (remove-duplicates (cdr l))))))

(define replace (lambda (x b y)
                  (if (null? y )
                      '()
                      (if (equal? (car y) x)
                          (cons b (replace x b (cdr y)))
                          (cons (car y) (replace x b (cdr y)))))))

(define (permute-multiple-colors color-list)
  (let* ((perm (permute (list small-mass medium-mass large-mass))))
    (map (lambda (rep-list cl)
           (let* ((rep1 (replace "blue" (first rep-list) color-list))
                  (rep2 (replace "yellow" (second rep-list) rep1))
                  (rep3 (replace "red" (third rep-list) rep2)))
             rep3)) perm (make-list (length perm) color-list))))


(define (two-colors-help fc)
  (lambda (color-l num-repl)
    (map (lambda (color) (if (equal? color fc) (first num-repl) (second num-repl)))
         color-l)))

(define (permute-two-colors color-list)
  (map (two-colors-help (first color-list)) (make-list 6 color-list)
       (list (list small-mass medium-mass) (list small-mass large-mass)
             (list medium-mass small-mass) (list medium-mass large-mass)
             (list large-mass small-mass) (list large-mass medium-mass))))

(define (mass-params-from-colors color-list)
  (let* ((unique-colors (remove-duplicates color-list))
         (first-color (first unique-colors))
         (n (length unique-colors)))
    (if (equal? n 1)
        (list (make-list number-of-particles small-mass)
              (make-list number-of-particles medium-mass)
              (make-list number-of-particles large-mass))
        (if (equal? n 2)
            (permute-two-colors color-list)
            (if (equal? n 3)
                                        ;(permute (list small-mass medium-mass large-mass))
                (permute-multiple-colors color-list)
                'error)))))

(define (permute-two-goo-colors color-list)
  (map (two-colors-help (first color-list)) (make-list 6 color-list)
       (list (list smooth-goo  weak-goo) (list smooth-goo strong-goo)
             (list weak-goo smooth-goo) (list weak-goo strong-goo)
             (list strong-goo weak-goo) (list strong-goo smooth-goo))))

(define (goo-params-from-colors goo-color-list)
  (let* ((unique-colors (remove-duplicates goo-color-list))
         (n (length unique-colors)))
    (if (equal? n 1)
        (list (make-list number-of-goos smooth-goo)
              (make-list number-of-goos weak-goo)
              (make-list number-of-goos strong-goo))
        (if (equal? n 2)
            (permute-two-goo-colors goo-color-list)
            'error))))

(define field_options_11 (list '("1" "1" "attract") '("1" "1" "repel")  '("1" "1" "none")))
(define field_options__-1_-1 (list '("-1" "-1" "attract") '("-1" "-1" "repel") '("-1" "-1" "none")))
(define field_options_1_-1 (list '("1" "-1" "attract") '("1" "-1" "repel") '("1" "-1" "none")))
                                        ; field options -1 1 are added automatically below


(define (get-all-field-params) (map (lambda (l)
                                      (append l (list (list "-1" "1" (third (third l))))))
                                    (all-combinations (list field_options_11
                                                            field_options__-1_-1
                                                            field_options_1_-1))))
;; (define (add-noise l observation-noise)
;;   (if (not (list? (first l)))
;;       (map (lambda (x) (gaussian x observation-noise)) l)
;;       (map (lambda (x) (add-noise x observation-noise)) l)))

;; ;; creating a particle for inference. Not ideal, assumes we know the hidden properties in advance
;; (define (draw-particle) (make-particle
;;     (make-property "mass" (uniform 0.5 4.5))
;;     (make-property "elastic" 1.0)
;;     (make-property "size" 12.0)))

;; (define (create-particles particle-num)
;;   (repeat particle-num draw-particle))

;; (define (create-random-particles particle-num mass elastic identity)
;;   (repeat particle-num (lambda () (make-particle
;;                                    (make-property "init-position" (list (uniform 35 610) (uniform 35 440.0)))
;;                                    (make-property "init-velocity" (list (uniform -4000.0 4000.0) (uniform -4000 4000)))
;;                                    (make-property "mass" mass)
;;                                    (make-property "elastic" elastic)
;;                                    (make-property "identity" identity)
;;                                    (make-property "size" 12.0)))))

;; (define (create-random-particles-invis particle-num mass elastic identity)
;;   (repeat particle-num (lambda () (make-particle
;;                                    (make-property "init-position" (list (if (flip) (uniform 35 280) (uniform 430 625)) (uniform 35 440.0)))
;;                                    (make-property "init-velocity" (list (uniform -4000.0 4000.0) (uniform -4000 4000)))
;;                                    (make-property "mass" mass)
;;                                    (make-property "elastic" elastic)
;;                                    (make-property "identity" identity)
;;                                    (make-property "size" 12.0)))))

;; ===================== BEGIN Forces ===================
(define (repeat N proc)
  (if (equal? N 0)
      '()
      (append (list (proc)) (repeat (- N 1) proc))))

(define (make-goo-F goo-list)
  (lambda (q v properties)
    (let* ((x-min (map first (map get-goo-ul goo-list)))
           (y-min (map second (map get-goo-ul goo-list)))
           (x-max (map first (map get-goo-lr goo-list)))
           (y-max (map second (map get-goo-lr goo-list)))
           (sizes (map get-size properties))
           (masses (map get-mass properties))
           (resistances (map get-goo-resistance goo-list))
           (F (map (lambda (in-goo-list qs vs)
                     (let* ((goo-transform (filter (lambda (x) x) in-goo-list)))
                       (if (null? goo-transform)
                           '(0.0 0.0)
                           (map * (first goo-transform) vs))))
                   (map (lambda (specific-q specific-size specific-mass)
                          (map (lambda (i j s t specific-resistance)
                                 (if (and (> (+ (first specific-q) specific-size) i)
                                          (< (- (first specific-q) specific-size) j)
                                          (> (+ (second specific-q) specific-size) s)
                                          (< (- (second specific-q) specific-size) t))
                                     (make-list 2 (* specific-mass specific-resistance))
                                     #f)) x-min x-max y-min y-max resistances)) q sizes masses)
                   q v)))
      F)))

(define (make-global-force direction)
  (lambda (q v properties)
    (if (equal? direction 'none)
        (make-list (length q) '(0.0 0.0))
        (let* ((force-strength 100000)
               (pi 3.14159265)
               (angle (case direction
                        ('right 0.0)
                        ('down (/ pi 2))
                        ('left pi)
                        ('up (/ (* 3 pi) 2))
                        (else 'no-such-direction-error)))
               (Fx (* (cos angle) force-strength))
               (Fy (* (sin angle) force-strength)))
          (make-list (length q) (list Fx Fy))))))

;; (define (make-box upper-left-corner bottom-right-corner box-width color)
;;   (let*
;;       ((box-right
;;         (make-obstacle (list (- (first bottom-right-corner) box-width) (second upper-left-corner))
;;                        bottom-right-corner color))
;;        (box-left
;;         (make-obstacle upper-left-corner (list box-width (second bottom-right-corner)) color))
;;        (box-up
;;         (make-obstacle upper-left-corner (list (first bottom-right-corner) box-width) color))
;;        (box-down
;;         (make-obstacle (list (first upper-left-corner) (- (second bottom-right-corner) box-width))
;;                        bottom-right-corner color)))
;;     (list box-right box-left box-up box-down)))

                                        ;(define (my-church-force q v properties)
                                        ;  (make-list (length q) '(0.0 0.0)))
;; convenient function for handling multiple-interaction between pairs of particles.
;; takes in a force F which describes the interaction between any pair, and computes
;; the necessary N^2 interactions, spitting them out as ((Fx1, Fy1) (Fx2, Fy2), ...)

;;  (define (multi-interaction-F2 F)
;;    (lambda (q v properties)
;;      (let* ((masses (map get-mass properties)))
;;        (let loop ((n 0) (Fl '()))
;;          (if (< n (length q))
;;              (begin
;;                 (define main-q (list-ref q n))
;;                 (define main-v (list-ref v n))
;;                 (define main-properties (list-ref properties n))
;;                 (define rest-q (remove-element q n))
;;                 (define rest-v (remove-element v n))
;;                 (define rest-properties (remove-element properties n))
;;                 (define f-main-rest (map  (lambda (q2 v2 properties2)
;;                                             (F main-q q2 main-v v2 main-properties properties2))
;;                                           rest-q rest-v rest-properties))
;;                 (define result (list (sum (map first f-main-rest)) (sum (map second f-main-rest))))

;;                 (loop (+ n 1) (pair result Fl)))
;;              (reverse Fl))))))

;; Force #9: collision forces. Each particle gets a tiny strong spring attached
;;           to it. Requires a notion of object size. Conforms to what we expect from collisions

;; (define (two-particle-collision-F q1 q2 v1 v2 properties1 properties2)
;;   (let* ((k 700000.0) ; spring strength
;;          (elastic 1.0)
;;          (r (compute-euc-dist q1 q2))
;;          (theta (compute-angle q1 q2))
;;          (mass1 (get-mass properties1))
;;          (e (get-elastic properties1))
;;          (c (elastic->damping e k mass1))
;;          (vr (+ (* (- (first v1) (first v2)) (cos theta)) (* (- (second v1) (second v2)) (sin theta))))
;;          (size1 (get-size properties1))
;;          (size2 (get-size properties2))
;;          (impinge (- r (+ size1 size2))))
;;     (if (< impinge 0.1)
;;         (let*
;;             ;((F (* k impinge))
;;              ((F (+ (* (- c) vr) (* k impinge)))
;;                    (Fx (* F (cos theta)))
;;                    (Fy (* F (sin theta))))
;;               (list Fx Fy))
;;          '(0.0 0.0))))

;; Force #10: multi-collision formulation.
;;(define collision-F (multi-interaction-F2 two-particle-collision-F))

;; Goo Force
(define goo-F (make-goo-F goo-list))

;; Field forces

(define (make-two-particle-field-F field-definition)
  (lambda (q1 q2 v1 v2 properties1 properties2)
    (let* ((field1-property (first field-definition))
           (field2-property (second field-definition))
           (field-type (third field-definition))
           (match (and (equal? (get-field-strength properties1) field1-property)
                       (equal? (get-field-strength properties2) field2-property)))
           (r (compute-euc-dist q1 q2))
           (field-multiplier (if (equal? field-type "attract") +1
                                 (if (equal? field-type "repel") -1
                                     0)))
           (theta (compute-angle q1 q2))
           (mass1 (get-mass properties1))
           (mass2 (get-mass properties2))
           (F (if (< r 8.0) 0.0 (* 5000000000 (/ (expt r 2.0)))))
                                        ;(F (if (< r 8.0) 0.0 (* -1000 r)))
           (Fx (* field-multiplier (* F (cos theta))))
           (Fy (* field-multiplier (* F (sin theta)))))
      (if match
          (list Fx Fy)
          (list 0.0 0.0)))))

(define (make-field-F field-definition)
  (multi-interaction-F (make-two-particle-field-F field-definition)))


(define field_++_F (make-field-F '("1" "1" "attract")))
(define field_+-_F (make-field-F '("1" "-1" "repel")))
(define field_-+_F  (make-field-F '("-1" "1" "repel")))



;; Gravitation well constructs an "invisible" non-collision mass at a given location
;; The 'mass' of the well gives its strengh of attraction
;; (define (make-gravitational-well-F location mass)
;;    (lambda (q v properties)
;;      (let* ((masses (map get-mass properties))
;;             (grav-well-q location)
;;             (grav-well-mass mass)
;;             (rl (map (lambda (k) (compute-euc-dist grav-well-q k)) q))
;;             (thetal (map (lambda (k) (compute-angle grav-well-q k)) q))
;;             (Fl (map (lambda (m r)
;;                        (if (< r 8.0)
;;                            0.0
;;                            (* -1 (* (expt 10 5) (/ (* m grav-well-mass) (expt r 2.0))))))
;;                      masses rl))
;;             (Fx (map (lambda (F theta) (* F (cos theta))) Fl thetal))
;;             (Fy (map (lambda (F theta) (* F (sin theta))) Fl thetal)))
;;        (zip Fx Fy))))

;;; ; Gravity well based on a property of the particle

;; (define (make-property-based-well location mass desired-property)
;;    (lambda (q v properties)
;;      (let* ((masses (map get-mass properties))
;;             (propertyl (map get-identity properties))
;;             (grav-well-q location)
;;             (grav-well-mass mass)
;;             (rl (map (lambda (k) (compute-euc-dist grav-well-q k)) q))
;;             (thetal (map (lambda (k) (compute-angle grav-well-q k)) q))
;;             (Fl (map (lambda (m r)
;;                        (if (< r 8.0)
;;                            0.0
;;                            (* -1 (* (expt 10 5) (/ (* m grav-well-mass) (expt r 2.0))))))
;;                      masses rl))
;;             (Fx (map (lambda (F theta property)
;;                        (if (equal? property desired-property) (* F (cos theta)) 0)) Fl thetal propertyl))
;;             (Fy (map (lambda (F theta property)
;;                        (if (equal? property desired-property) (* F (sin theta)) 0)) Fl thetal propertyl)))
;;        (zip Fx Fy))))

;; (define well-F (make-gravitational-well-F '(350.0 200.0) 50000.0))
;; (define schmoot-well-FA (make-property-based-well '(60.0 200.0) 5000.0 "schmoot"))
;; (define kloot-well-FA (make-property-based-well '(500 200) 5000.0 "kloot"))
;; (define schmoot-well-FB (make-property-based-well '(60.0 200.0) 15000.0 "schmoot"))
;; (define kloot-well-FB (make-property-based-well '(500 200) 5000.0 "kloot"))
;; ;; ===================== END of Forces ===================
