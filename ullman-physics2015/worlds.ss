(import (rnrs)
        (physics)
        (scheme-tools)
        (scheme-tools srfi-compat :1)
        (scheme-tools math gsl-bindings))

                                        ;(load "physicsHelperFunctionsAndForces.ss")
                                        ;(load "physicsParticles.ss")
(load "physicsGooAndObstacles.ss")

(define number-of-particles 4)
(define number-of-goos 2)

(define (load-particles-from-saved-world saved-world) (third saved-world))
(define (load-goos-from-saved-world saved-world) (fourth saved-world))

(define small-mass .33)
(define medium-mass 1.0)
(define large-mass 3.0)
(define field+ "1")
(define field- "-1")
(define no-field 0)

(define particle-colors '("red" "yellow" "blue"))
(define field-colors (make-list number-of-particles "black"))
(define goo-colors (list "yellowgreen" "magenta"))

(define (create-particle mass field-type color field-color)
  (make-particle (make-property "mass" mass)
                 (make-property "elastic" .9)
                 (make-property "size" particle-size)
                 (make-property "color" color)
                 (make-property "field-color" field-color)
                 (make-property "field-strength" field-type)))

(define (create-goo-type goo-strength goo-color)
  (lambda (location)
    (make-goo (first location) (second location) goo-strength goo-color)))

(define (draw-goos-from-types goo-types num-goos)
  (repeat num-goos
          (lambda ()
            (let* ((ul (list (gsl-rng-uniform-int 580) (gsl-rng-uniform-int 400)))
                   (xsize (+ (gsl-rng-uniform-int 140) 80))
                   (ysize (+ (gsl-rng-uniform-int 140) 80))
                   (lr (list (+ (first ul) xsize) (+ (second ul) ysize))))

              ((list-ref goo-types (gsl-rng-uniform-int (length goo-types)))
               (list ul lr))))))


(define (create-particles masses fields colors field-colors)
  (map create-particle masses fields colors field-colors))

(define (draw-particles-from-types types num-particles)
  (repeat num-particles
          (lambda ()
            (list-ref types (gsl-rng-uniform-int (length types))))))

(define (draw-simulated-particles masses field-types saved-colors)

  (let* ((real-particles (get-particles-from-world real-world))
         (field-colors (make-list number-of-particles "black")))
    (map create-particle masses field-types saved-colors field-colors)))


(define (draw-simulated-goos strengths saved-world)
  (let* ((saved-goos (load-goos-from-saved-world saved-world))
         (ul-list (map first saved-goos))
         (lr-list (map second saved-goos))
         (colors (map fourth saved-goos)))
    (map make-goo ul-list lr-list strengths colors)))

;; (define (create-world global-force-direction field-force-definitions
;;                       particle-masses particle-colors particle-field-strengths particle-field-colors
;;                       goo-locations goo-strengths goo-colors)
;;   (let* ((global-F (make-global-force global-force-direction))
;;          (field-forces (map make-field-F field-force-definitions))
;;          (particles (create-particles particle-masses particle-field-strengths
;;                                       particle-colors particle-field-colors))
;;          (goos (create-goos goo-locations goo-strengths goo-colors))
;;          (goo-F (make-goo-F goos))
;;          (forces (append (list collision-F global-F goo-F) field-forces)))
;;     (list forces particles goos)))

(define (create-world global-force-direction field-force-definitions
                      particle-types goo-types)
  (let* ((global-F (make-global-force global-force-direction))
         (field-forces (map make-field-F field-force-definitions))
         (particles (draw-particles-from-types particle-types number-of-particles))
         (goos (draw-goos-from-types goo-types number-of-goos))
         (goo-F (make-goo-F goos))
         (forces (append (list collision-F global-F goo-F) field-forces)))
    (list forces particles goos (list global-force-direction field-force-definitions))))

(define (create-simulated-world global-force-direction field-force-definitions
                                masses field-types goo-strengths saved-world)

  (let* ((global-F (make-global-force global-force-direction))

         (field-forces (map make-field-F field-force-definitions))
         (saved-particle-colors (map get-color (load-particles-from-saved-world saved-world)))
         (particles (draw-simulated-particles masses field-types saved-particle-colors))
                                        ;(goos (draw-goos-from-types goo-types 2))
         (goos (draw-simulated-goos goo-strengths saved-world))
         (goo-F (make-goo-F goos))
         (forces (append (list collision-F global-F goo-F) field-forces)))
    (list forces particles goos)))

(define (get-forces-from-world world)
  (first world))
(define (get-particles-from-world world)
  (second world))
(define (get-goos-from-world world)
  (third world))

(define (generate-path world q0 v0)
  (let* ((forces (get-forces-from-world world))
         (particles (get-particles-from-world world))
         (observed-path (rk-newtonian q0 v0 forces particles path-length dt)))
    observed-path))

(define (simulate-and-compare noise global-force-direction field-force-definitions
                              particle-masses particle-field-strengths
                              goo-strengths real-world)
  (let ([num-particles (length particle-list)])
    (assert (= (length particle-masses) num-particles))
    (let* ([simulated-world (create-simulated-world global-force-direction field-force-definitions
                                                    particle-masses particle-field-strengths goo-strengths real-world)]
           [inferred-path (generate-path simulated-world q0 v0)])
      (values (list (map get-mass (get-particles-from-world simulated-world)) (map get-color (get-particles-from-world simulated-world)))
              (log-score:noisy=* observed-path inferred-path noise)))))
;;              (+ (log-score:noisy=* 1.0 (get-mass (first (get-particles-from-world simulated-world))) noise)
;;                 (log-score:noisy=* observed-path inferred-path noise))))))

;; (define (simulate-and-compare noise global-force-direction field-force-definitions
;;                               particle-masses particle-colors particle-field-strengths
;;                               particle-field-colors goo-locations goo-strengths goo-colors)
;;     (let ([num-particles (length particle-list)])
;;     (assert (= (length masses) num-particles))
;;     (let* ([simulated-world (create-world global-force-direction field-force-definitions
;;                       particle-types goo-types)]
;;            [inferred-path (generate-path simulated-world q0 v0)])
;;       (values (map get-mass (get-particles-from-world world))
;;               (+ (log-score:noisy=* 1.0 (get-mass (first particles)) noise)
;;                  (log-score:noisy=* observed-path inferred-path noise))))))

;;; Goo types

(define smooth-magenta (create-goo-type smooth-goo "darkmagenta"))
(define weak-brown (create-goo-type weak-goo "brown"))
(define strong-green (create-goo-type strong-goo "yellowgreen"))

(define smooth-green (create-goo-type smooth-goo "yellowgreen"))
(define weak-magenta (create-goo-type weak-goo "darkmagenta"))
(define strong-brown (create-goo-type strong-goo "brown"))

(define smooth-brown (create-goo-type smooth-goo "brown"))
(define weak-green (create-goo-type weak-goo "yellowgreen"))
(define strong-magenta (create-goo-type strong-goo "darkmagenta"))

(define goo-combination1 (list smooth-magenta weak-brown strong-green))
(define goo-combination2 (list smooth-green weak-magenta strong-brown))
(define goo-combination3 (list smooth-brown weak-green strong-magenta))

;;; Particle types
(define small-red0 (create-particle small-mass "0" "red" "black"))
(define medium-red- (create-particle medium-mass "-1" "red" "black"))
(define large-red+ (create-particle large-mass "1" "red" "black"))

(define small-blue- (create-particle small-mass "-1" "blue" "black"))
(define medium-blue+ (create-particle medium-mass "1" "blue" "black"))
(define large-blue0 (create-particle large-mass "0" "blue" "black"))

(define small-yellow+ (create-particle small-mass "1" "yellow" "black"))
(define medium-yellow0 (create-particle medium-mass "0" "yellow" "black"))
(define large-yellow- (create-particle large-mass "-1" "yellow" "black"))

(define fieldless-small  (create-particle small-mass "0" "yellow" "black"))
(define fieldless-medium (create-particle medium-mass "0" "red" "black"))
(define fieldless-large (create-particle large-mass "0" "blue" "black"))

(define particle-combination1 (list small-blue- medium-yellow0 large-red+))
(define particle-combination2 (list small-red0 medium-blue+ large-yellow-))
(define particle-combination3 (list small-yellow+ medium-red- large-blue0))

(define particle-fieldless-combination
  (list fieldless-small fieldless-medium fieldless-large))

;;; Different worlds

(define world1 (create-world 'none
                             '(("1" "1" "attract") ("1" "-1" "repel")
                               ("-1" "1" "repel"))
                             particle-fieldless-combination goo-combination1))

(define world2 (create-world 'none
                             '(("1" "1" "attract") ("-1" "-1" "attract")
                               ("1" "-1" "none") ("-1" "1" "none"))
                             particle-combination1 goo-combination2))

(define world3 (create-world 'none
                             '(("1" "1" "attract") ("-1" "-1" "attract")
                               ("1" "-1" "repel") ("-1" "1" "repel"))
                             particle-combination2 goo-combination3))

(define world4 (create-world 'none
                             '(("1" "1" "repel") ("-1" "-1" "repel")
                               )
                             particle-combination3 goo-combination1))

(define world5 (create-world 'none
                             '(("1" "1" "repel") ("-1" "-1" "repel")
                               ("1" "-1" "attract") ("-1" "1" "attract"))
                             particle-combination1 goo-combination1))

(define world6 (create-world 'none
                             '(("1" "1" "attract")
                               ("1" "-1" "attract") ("-1" "1" "attract"))
                             particle-combination2 goo-combination2))

(define world7 (create-world 'left
                             '(("1" "1" "attract") ("-1" "-1" "attract"))
                             particle-combination2 goo-combination2))

(define world8 (create-world 'right
                             '(("1" "1" "attract") ("-1" "-1" "attract")
                               ("1" "-1" "repel") ("-1" "1" "repel"))
                             particle-combination3 goo-combination3))

(define world9 (create-world 'down
                             '(("1" "1" "repel") ("-1" "-1" "repel")
                               ("1" "-1" "attract") ("-1" "1" "attract"))
                             particle-combination1 goo-combination3))

(define world10 (create-world 'up
                              '(("1" "1" "attract")
                                ("1" "-1" "attract") ("-1" "1" "attract"))
                              particle-combination3 goo-combination1))


(define real-world world10) ;; CHANGE ME***
(define real-world-name "world10") ;; CHANGE ME***
