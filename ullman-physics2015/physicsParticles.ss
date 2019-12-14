(define ratio '(1.0 5.0 10.0 1.0 2.0 3.0))
(define particle-size 40.0)

(define small-mass .33)
(define medium-mass 1.0)
(define large-mass 3.0)
(define field+ "1")
(define field- "-1")
(define no-field 0)

(define (create-particle-type color mass field-color field-type)
  (lambda (init-pos init-vel)
    (make-particle (make-property "init-position" init-pos)
                   (make-property "init-velocity" init-vel)
                   (make-property "color" color)
                   (make-property "mass" mass)
                   (make-property "field-color" field-color)
                   (make-property "field-strength" field-type)
                   (make-property "size" particle-size)
                   (make-property "elastic" 1.0))))

(define particle-type1 (create-particle-type
                          "red" medium-mass "black" field+))

(define particle-type2 (create-particle-type
                         "yellow" small-mass "white" field+))

(define particle-type3 (create-particle-type
                         "blue" large-mass "black" field+))


(define particle1
  (particle-type1 '(150.0 200.0)
                  '(2000.0 0.0)))

(define particle2
  (particle-type2 '(450.0 200.0)
                  '(-500.0 0.0)))

(define particle3
  (particle-type3 '(520.0 200.0)
                  '(1000.0 0.0)))
  

(define particle4
  (make-particle (make-property "init-position" '(500.0 300.0))
                 (make-property "init-velocity" '(-2800.0 1800.0))
                 (make-property "mass" (third ratio))
                 (make-property "size" 10.0)
                 (make-property "elastic" 1.0)))

(define particle5
  (make-particle (make-property "init-position" '(100.0 400.0))
                 (make-property "init-velocity" '(-3000.0 -1000.0))
                 (make-property "mass" (third ratio))
                 (make-property "size" 15.0)
                 (make-property "elastic" 1.0)))

(define particle6
  (make-particle (make-property "init-position" '(150.0 370.0))
                 (make-property "init-velocity" '(-1000.0 4000.0))
                 (make-property "mass" (third ratio))
                 (make-property "size" 12.0)
                 (make-property "elastic" 1.0)))
