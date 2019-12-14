(import (rnrs)
        (physics)
        (scheme-tools)
        (scheme-tools math gsl-bindings)
        (scheme-tools srfi-compat :1))


(define world-number (second (command-line)))
(define scenario-number (third (command-line)))

(load "physicsParticles.ss")
(load "physicsGooAndObstacles.ss")
(load "physicsHelperFunctionsAndForces.ss")
(load "worlds.ss")
                                        ; by loading a world we're loading also the initial conditions q0 v0, and the observed-path
(load (string-append
       "saved-worlds/world" world-number "/world" world-number
       "_" scenario-number  ".ss"))


(define rng (gsl-rng-alloc gsl-rngt-taus))
                                        ;(display (list (gsl-gaussian 1 rng)
                                        ;             (gsl-beta 1 1 rng)
                                        ;            (gsl-rng-uniform-pos rng)))

;;;
(define dt 0.001)
(define path-length 400) ;; path length has no influence on inference time..
(define (write-to-file output filename)
  (begin
    (if (file-exists? filename)
        (delete-file filename)
        '())
    (let ((output-port (open-output-file filename)))
      (write output output-port))))

(define (save-output filename func)
  (begin
    (if (file-exists? filename)
        (delete-file filename)
        '())
    (with-output-to-file filename
      func)))
(define (log-score:noisy= x y noise)
  (- (* noise (expt (- x y) 2))))

(define (log-score:noisy=* a b noise)
  (if (and (list? a)
           (list? b))
      (sum (map (lambda (i j) (log-score:noisy=* i j noise)) a b))
      (log-score:noisy= a b noise)))

;;;

(define (load-particles-from-saved-world saved-world) (third saved-world))
(define (load-goos-from-saved-world saved-world) (fourth saved-world))


(define (simulate-and-compare noise global-force-direction field-force-definitions
                              particle-masses particle-field-strengths
                              goo-strengths real-world)
  (let* ([simulated-world (create-simulated-world global-force-direction field-force-definitions
                                                  particle-masses particle-field-strengths goo-strengths saved-world)]
         [inferred-path (generate-path simulated-world q0 v0)])

    (values (list (map get-mass (get-particles-from-world simulated-world))
                  (map get-color (load-particles-from-saved-world saved-world))
                  (map get-goo-strength (get-goos-from-world simulated-world))
                  (map get-goo-color (load-goos-from-saved-world saved-world))
                  field-force-definitions
                  (map get-field-strength (get-particles-from-world simulated-world))
                  global-force-direction)
                                        ;(cut-number-precision-path inferred-path)
            (cut-number-precision-paths inferred-path observed-path)
            (log-score:noisy=* observed-path inferred-path noise))))


(define (main)
  (let* ([particles (load-particles-from-saved-world saved-world)]
         [particle-colors (map get-color particles)]
         [goos (load-goos-from-saved-world saved-world)]
         [goo-colors (map get-goo-color goos)]
         [field-support (list field+ field- no-field)] ; comment out?
         [noise-params (list 1.5)] ; don't touch
         [global-F-support (list 'none 'up 'down 'left 'right)] ; comment out?
         [global-F-params (list 'none 'up 'down 'left 'right)] ; working
         [mass-params (mass-params-from-colors particle-colors)] ; working
         [field-params (list (map get-field-strength particles))] ; Leave for now
         [goo-params (goo-params-from-colors goo-colors)] ; working
                                        ;[force-field-params (list '(("1" "1" "attract")))]
         [force-field-params (get-all-field-params)] ; working
         [real-world-params (list real-world)] ; don't touch
         [force-params (list (list collision-F goo-F))] ; useless, comment out?
         [all-params (all-combinations (list noise-params global-F-params
                                             force-field-params
                                             mass-params field-params
                                             goo-params
                                             real-world-params))])
    (for-each (lambda (params)
                (let-values ([(result inferred-path score) (apply simulate-and-compare params)])
                  (pe (list result inferred-path score) "\n")))
              all-params)))

(save-output (string-append
              "inference/world"
              world-number
              "/world" world-number "_" (third (command-line))) main)
                                        ; "inference/world1/world1_1" main)
