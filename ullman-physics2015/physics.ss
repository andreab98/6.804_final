#!r6rs

(library

    (physics)

  (export physics-test
          F->a
          addl
          apply-force-list
          basic-collision
          box-F
          check-bumps
          collision-F
          collision-box
          compute-angle
          compute-euc-dist
                                        ;create-goo-type
          damped-harmonic-F
          elastic->damping
          element-n
          falling-F
          gaussian-lnpdf
          get-color
          get-elastic
          get-field-color
          get-field-strength
          get-goo-ul
          get-goo-lr
          get-goo-resistance
          get-goo-color
          get-init-position
          get-init-velocity
          get-mass
          get-obstacle-ul
          get-obstacle-lr
          get-property
          get-size
          get-spiraler
          get-squiggler
          get-identity
          get-vx
          get-vy
          get-x
          get-y
                                        ;goo-list
          gravitational-F
          make-goo
          make-particle
          make-property
          make-obstacle
          mplus
          mplus2
          mtimes
          mtimes2
          multi-interaction-F
          null-F
          p->v
          path-splitter
          pi
          remove-element
          rk-newtonian
          spiraler-F
          squiggler-F
          strip
          two-particle-collision-F
          two-particle-grav-F
          two-particle-spiraler-F
          two-particle-squiggler-F
          make-obstacle-F
          v->p
          v-change
          xy->radial
          F0
          F1
          F2
          F3
          F4
          F5
          within-obstacle-helper
                                        ;make-goo-F
          make-box
          multi-interaction-F2
                                        ;goo-F
          make-gravitational-well-F
          make-property-based-well
          well-F
          schmoot-well-FA
          kloot-well-FA
          schmoot-well-FB
          kloot-well-FB
          )

  (import (rnrs)
          (scheme-tools)
          (scheme-tools srfi-compat :1))

  (define (physics-test)
    (display "test works"))

  (define pi 3.141592653589793)

  ;; select every nth element from a list
  (define (element-n l n)
    (if (< (length l) n)
        '()
        (pair (list-ref l (- n 1)) (element-n (drop l n) n))))

  ;; assuming path is a combination of q's and p's
  (define (path-splitter path points)
    (let* ((n (floor (/ (length path) points))))
      (element-n (map first path) n)))

  ;; Euclidian distance between 2 2D particles, assuming coords come in as (x1, y1)
  (define (compute-euc-dist particle1 particle2)
    (let ((x1 (first particle1))
          (x2 (first particle2))
          (y1 (second particle1))
          (y2 (second particle2)))
      (expt (+ (expt (- x1 x2) 2) (expt (- y1 y2) 2)) 0.5)))

  ;; get angle theta between 2 2D particles
  (define (compute-angle particle1 particle2)
    (let* ((x1 (first particle1))
           (x2 (first particle2))
           (y1 (second particle1))
           (y2 (second particle2))
           (rx (- x2 x1))
           (ry (- y2 y1))
           (default (atan (/ ry rx))))
      (if (> rx 0)
          (atan (/ ry rx))
          (if (and (< rx 0) (>= ry 0))
              (+ (atan (/ ry rx)) pi)
              (if (and (< rx 0) (< ry 0))
                  (- (atan (/ ry rx)) pi)
                  (if (and (= rx 0) (> ry 0))
                      (/ pi 2)
                      (if (and (= rx 0) (< ry 0))
                          (/ pi -2)
                          0.0)))))))

  ;; go from x y to radial reprsentation

  (define (xy->radial xy)
    (let ((r (compute-euc-dist xy '(0.0 0.0)))
          (theta (compute-angle xy '(0.0 0.0))))
      (list r theta)))

  ;; This probably exists already, but just to be sure
  (define (gaussian-lnpdf val mu var)
    (* -0.5 (+ (+ 1.8378770664093453 (log var) )
               (/ (* (- val mu) (- val mu))
                  var) )) )



  ;; Go from elastic property to spring damping constant c in F = -c*v
  (define (elastic->damping elastic k mass)
    (* (* 2 (sqrt (* k mass))) (/ (- (log elastic)) (sqrt (+ (expt pi 2.0) (expt (log elastic) 2.0))))))


  ;; multiply number through a list
  (define (mtimes n l)
    (map (lambda (x) (* n x)) l))

  ;; multiply number through a list of lists (GOD)
  (define (mtimes2 n ll)
    (map (lambda (l) (mtimes n l)) ll))

  ;; add number through a list
  (define (mplus n l)
    (map (lambda (x) (+ n x)) l))

  ;; add number through a list of lists
  (define (mplus2 n ll)
    (map (lambda (l) (mplus n l)) ll))

  ;; add the lists of two lists together

  (define (addl lla llb . args)
    (if (equal? args '())
        (map (lambda (la lb) (map + la lb)) lla llb)
        (fold (lambda (x y) (addl x y)) (addl lla llb) args)))

  (define (strip l)
    (if (equal? l '())
        '()
        (append (first l) (strip (rest l))) ))

  ;; ;; remove the element indexed by ref from the list l, kind of
  ;; ;; the opposite of list-ref. Assume zero-indexing.
  (define (remove-element l ref)
    (append (take l ref) (drop l (+ ref 1))))

  ;; turn momenta into velocity
  (define (p->v pl ml)
    ;; assuming p and m are both vectors, however
    ;; p is a Nx2 vector-list and m is a N vector
    (map (lambda (pxy m) (list (/ (first pxy) m) (/ (second pxy) m)) ) pl ml))

  ;; turn forces into accelerations
  (define (F->a Fl ml)
    ;; assuming F and m are both vectors, however
    ;; F is a Nx2 vector-list and m is a N vector
    (map (lambda (Fxy m) (list (/ (first Fxy) m) (/ (second Fxy) m)) ) Fl ml))

  ;; turn velocty into momenta
  (define (v->p vl ml)
    ;; assuming v and m are both vectors, however
    ;; v is a Nx2 vector-list and m is an N vector
    (map (lambda (vxy m) (list (* (first vxy) m) (* (second vxy) m))) vl ml))

  (define (make-goo upper-left-point lower-right-point resistance color)
    (list upper-left-point lower-right-point resistance color))
  (define (get-goo-ul goo)
    (first goo))
  (define (get-goo-lr goo)
    (second goo))
  (define (get-goo-resistance goo)
    (third goo))
  (define (get-goo-color goo)
    (fourth goo))

  (define (make-obstacle upper-left-point lower-right-point color)
    (list upper-left-point lower-right-point color))
  (define (get-obstacle-ul obstacle)
    (first obstacle))
  (define (get-obstacle-lr obstacle)
    (second obstacle))

  (define (make-property property-name property)
    (list property-name property))

  (define (make-particle . properties)
    properties)
  ;; We don't want to have to remember property-lists by heart.
  ;; Since they will be in the form (("mass" 30) ("squiggler" #t)) and so on,
  ;; this function allows us to define general property-grabbing functions
  (define (get-property property)
    (lambda (property-list) (second (first (filter (lambda (p) (equal? property (first p))) property-list)))))

  ;; will grab the (float) value of mass from a property list of a particle
  (define get-mass (get-property "mass"))

  (define get-init-position (get-property "init-position"))

  (define get-init-velocity (get-property "init-velocity"))

  (define get-elastic (get-property "elastic"))

  ;; will grab the (truth) value of squiggler-hood from a property list
  (define get-squiggler (get-property "squiggler"))

  ;; will grab the (truth) value of spiraler-hood from a property list
  (define get-spiraler (get-property "spiraler"))

  ;; will grab the (float) value of object size from a property list of a particle
  (define get-size (get-property "size"))

  (define get-color (get-property "color"))

  (define get-field-color (get-property "field-color"))

  (define get-field-strength (get-property "field-strength"))

  (define get-identity (get-property "identity"))

  (define (get-x q) (map first q))

  (define (get-y q) (map second q))

  (define (get-vx v) (map first v))

  (define (get-vy v) (map second v))

  (define (basic-collision pos mom lim)
    (if (< pos (first lim))
        (abs mom)
        (if (> pos (second lim))
            (- (abs mom))
            mom)))

  (define (collision-box xlim ylim)
    (lambda (p q)
      (let ((x (first q))
            (y (second q))
            (px (first p))
            (py (second p)))
        (list (basic-collision x px xlim) (basic-collision y py ylim)))))



  ;; Usually we're going to want several forces acting at once on the
  ;; different particles. We need a way to apply these individually
  ;; and then sum up the results. This function will take in the list of
  ;; forces, apply them to q and v in turn, and then return the summation
  ;; of Fx and Fy for each particle.

  (define (apply-force-list F-list q v properties)
                                        ; we still want this to handle regular forces, so if it's not a list, just
                                        ; apply the force
    (if (not (list? F-list))
        (F-list q v properties)
                                        ;((get-force F-list) q v properties)
        (if (equal? F-list '())
            (make-list (length q) '(0.0 0.0))
            (addl ((first F-list) q v properties) (apply-force-list (rest F-list) q v properties)))))

                                        ;(addl ((get-force (first F-list)) q v properties) (apply-force-list (rest F-list) q v properties)))))



  ;; convenient function for handling multiple-interaction between pairs of particles.
  ;; takes in a force F which describes the interaction between any pair, and computes
  ;; the necessary N^2 interactions, spitting them out as ((Fx1, Fy1) (Fx2, Fy2), ...)

  (define (multi-interaction-F F)
    (lambda (q v properties)
      (let* ((masses (map get-mass properties)))
        (let loop ((n 0) (Fl '()))
          (if (< n (length q))
              ((lambda ()
                 (define main-q (list-ref q n))
                 (define main-v (list-ref v n))
                 (define main-properties (list-ref properties n))
                 (define rest-q (remove-element q n))
                 (define rest-v (remove-element v n))
                 (define rest-properties (remove-element properties n))
                 (define f-main-rest (map  (lambda (q2 v2 properties2)
                                             (F main-q q2 main-v v2 main-properties properties2))
                                           rest-q rest-v rest-properties))
                 (define result (list (sum (map first f-main-rest)) (sum (map second f-main-rest))))

                 (loop (+ n 1) (pair result Fl))))
              (reverse Fl))))))

  ;;integrator step, using Runge-Kutta (RK4)

  ;; No gradient methods necessary for Newton.
  ;; Notice this is written as p and q rather than x and v so
  ;;  it will be more easily integrated into a single framework with
  ;;  Hamiltonian dynamics.

  ;; Note that F is a function of q, v, properties and possibly t
  ;;  F is a procedure that takes in vector-lists q, v and properties
  ;;  and spits out a vector-list of forces in the x and
  ;;  y directions, i.e. ((Fx1, Fy1), (Fx2, Fy2), ...)  *sigh*.
  ;;  Possibly it would be better for F to take in particles.
  ;;  but that would require using "set!" and such.

  ;; a = F/m
  ;; v = integrate a
  ;; x = integrate v

  ;; The noise model adds the appropriate noise at the end of
  ;;   this deterministic procedure.
  ;; NOTETOSELF: There must be a simpler way to do this using
  ;;             some abstraction of a state evaluation.
  ;;
  ;; FIXME: obstacles is a global parameter now
  (define rk-newtonian
    (lambda (q0 v0 Fl properties steps dt)
      (if (= steps 0)
          '()
          (let* ((masses (map get-mass properties))
                 (sizes (map get-size properties))
                 (elasticities (map get-elastic properties))
                 (a0 (F->a (apply-force-list Fl q0 v0 properties) masses))

                 (a_q v0)
                 (a_v a0)

                 (b_q (addl v0 (mtimes2 (/ dt 2) a_v)))
                 (b_v (F->a (apply-force-list Fl (addl q0 (mtimes2 (/ dt 2) a_q))
                                              (addl v0 (mtimes2 (/ dt 2) a_v))
                                              properties)
                            masses))

                 (c_q (addl v0 (mtimes2 (/ dt 2) b_v)))
                 (c_v (F->a (apply-force-list Fl (addl q0 (mtimes2 (/ dt 2) b_q))
                                              (addl v0 (mtimes2 (/ dt 2) b_v))
                                              properties)
                            masses))

                 (d_q (addl v0 (mtimes2 dt c_v)))
                 (d_v (F->a (apply-force-list Fl (addl q0 (mtimes2 dt c_q))
                                              (addl v0 (mtimes2 dt c_v))
                                              properties)
                            masses))

                 (q1temp (addl q0 (mtimes2 (/ dt 6)
                                           (addl a_q
                                                 (mtimes2 2 b_q)
                                                 (mtimes2 2 c_q)
                                                 d_q))))

                 (v1temp (addl v0 (mtimes2 (/ dt 6)
                                           (addl a_v
                                                 (mtimes2 2 b_v)
                                                 (mtimes2 2 c_v)
                                                 d_v))))

                 (fixed-q1-v1 (if (null? obstacles)
                                  (list q1temp v1temp)
                                  (check-bumps sizes elasticities q0 q1temp v1temp obstacles)))
                 (q1 (first fixed-q1-v1))
                 (v1 (second fixed-q1-v1))
                 )


            (pair (list q1 v1) (rk-newtonian q1 v1 Fl properties (- steps 1) dt))))))

  ;;====================== Obstacle Handling ===========================
  ;; takes in positions, velocities and obstacles, returns velocities (and positions?).
  ;; If the object is in an obstacle, reverse its velocity.
  ;; Not sure if this requires the previous position too
  (define (check-bumps sizes elasticities q0 q1 v obstacles)
    (let* ((x-min (map first (map get-obstacle-ul obstacles)))
           (y-min (map second (map get-obstacle-ul obstacles)))
           (x-max (map first (map get-obstacle-lr obstacles)))
           (y-max (map second (map get-obstacle-lr obstacles)))
           (fixed-q1-v1 (map (lambda (collide-list q0s q1s vs)
                               (let* ((collide-transform (filter (lambda (x) x) collide-list)))
                                 (if (null? collide-transform)
                                     (list q1s vs)
                                     (list q0s (map * (first collide-transform) vs)))))
                             (map (lambda (specific-size specific-elasticity specific-q0 specific-q1)
                                    (map (lambda (i j s t)
                                           (if (and (> (+ (first specific-q1) specific-size) i)
                                                    (< (- (first specific-q1) specific-size) j)
                                                    (> (+ (second specific-q1) specific-size) s)
                                                    (< (- (second specific-q1) specific-size) t))
                                               (list (v-change (first specific-q0) i j specific-elasticity)
                                                     (v-change (second specific-q0) s t specific-elasticity))
                                               #f)) x-min x-max y-min y-max)) sizes elasticities q0 q1)
                             q0 q1 v)))
      (list (map first fixed-q1-v1) (map second fixed-q1-v1))))

  (define (v-change a mini maxi e)
    (if (and (> a mini) (< a maxi)) 1.0 (* e -1.0)))




  ;; ==================== End Obstacle Handling =======================

  ;; ======================== List of Forces ===================================

  ;; Force #0: nothing

  (define (null-F q v properties)
    (make-list (length q) '(0.0 0.0)))

  ;; Force #1: damped harmonic oscillator, one-dimensional
  (define (damped-harmonic-F q v)
    (let* ((x-vec (map first q))
           (vx-vec (map first v))
           (centerpoint -50)
           (Fx (map + (map - (mtimes 0.1 vx-vec)) (map - (mplus centerpoint x-vec))))
           (Fy (make-list (length x-vec) 0.0))
           )
      (zip Fx Fy)))

  ;; Force #2: gravitational force between two particles
  (define (two-particle-grav-F q1 q2 v1 v2 properties1 properties2)
    (let* ((r (compute-euc-dist q1 q2))
           (theta (compute-angle q1 q2))
           (mass1 (get-mass properties1))
           (mass2 (get-mass properties2))
           (F (* 100 (/ (* mass1 mass2) (expt r 2.0))))
           (Fx (* F (cos theta)))
           (Fy (* F (sin theta))))
      (list Fx Fy)))

  ;; Force #3: gravitational force between multiple particles
  (define gravitational-F (multi-interaction-F two-particle-grav-F))

  ;; Force #4: Squigglers. The force between them and non-squigglers is
  ;;           proportional to the inverse of the distance, and the direction
  ;;           oscillates as a function of the distance
  (define (two-particle-squiggler-F q1 q2 v1 v2 properties1 properties2)
    (let* ((r (compute-euc-dist q1 q2))
           (theta (compute-angle q1 q2))
           (is-squiggler1 (get-squiggler properties1))
           (is-squiggler2 (get-squiggler properties2))
           (F (/ 10000 (expt r 2.0)))
           (Fy (* -1.0 (* F (sin r))))
           (Fx (* F (cos r))))
      (if (and is-squiggler1  is-squiggler2)
          (list Fx Fy)
          '(0.0 0.0))))

  ;; Force #5: multi-particle squiggle interaction
  (define squiggler-F (multi-interaction-F two-particle-squiggler-F))

  ;; Force #6: Spiralers. The force between them and non-spirals is proportional
  ;;           to the inverse of the distance, and the direction is perpendicular.
  (define (two-particle-spiraler-F q1 q2 v1 v2 properties1 properties2)
    (let* ((r (compute-euc-dist q1 q2))
           (theta (compute-angle q1 q2))
           (is-spiraler1 (get-spiraler properties1))
           (is-spiraler2 (get-spiraler properties2))
           (F (/ 10000 (expt r 2.0)))
           (Fx (* -1.0 (* F (sin theta))))
           (Fy (* F (cos theta))))
      (if (and is-spiraler1 (not is-spiraler2))
          (list Fx Fy)
          '(0.0 0.0))))

  ;; Force #7: multi-particle spiral interaction
  (define spiraler-F (multi-interaction-F two-particle-spiraler-F))

  ;; Force #8: global force. Contains all particles in a box
  (define (box-F q v properties)
    ;; create a 'collision box' global perimeter
    ;; It may be the case that collisions are better handled
    ;; as 'events' in which the velocities are switched, as
    ;; opposed to some sort of Force-law treatment.

    (let* ((k 500000.0) ;; strength of box, basically treat it like powerful tiny springs
           (xlim0 0.0)
           (xlim1 640.0)
           (ylim0 0.0)
           (ylim1 480.0)
           (xvec (get-x q))
           (yvec (get-y q))
           (Fx (map (lambda (pos) (if (< pos xlim0) (* (- k) (- pos xlim0))
                                      (if (> pos xlim1) (* (- k) (- pos xlim1)) 0.0))) xvec))
           (Fy (map (lambda (pos) (if (< pos ylim0) (* (- k) (- pos ylim0))
                                      (if (> pos ylim1) (* (- k) (- pos ylim1)) 0.0))) yvec)))

      (zip Fx Fy)))

  ;; Force #9: collision forces. Each particle gets a tiny strong spring attached
  ;;           to it. Requires a notion of object size.

  (define (two-particle-collision-F q1 q2 v1 v2 properties1 properties2)
    (let* ((k 500000.0) ; spring strength
           (elastic 0.999)
           (r (compute-euc-dist q1 q2))
           (theta (compute-angle q1 q2))
           (mass1 (get-mass properties1))
           (e (get-elastic properties1))
           (c (elastic->damping e k mass1))
           (vr (+ (* (- (first v1) (first v2)) (cos theta)) (* (- (second v1) (second v2)) (sin theta))))
           (size1 (get-size properties1))
           (size2 (get-size properties2))
           (impinge (- r (+ size1 size2 2.0))))
      (if (< impinge 0)
                                        ;(let* ((F (* k impinge))
          (let* ((F (+ (* (- c) vr) (* k impinge)))
                 (Fx (* F (cos theta)))
                 (Fy (* F (sin theta))))
            (list Fx Fy))
          '(0.0 0.0))))

  ;; Force #10: multi-collision formulation.
  (define collision-F (multi-interaction-F two-particle-collision-F))

  ;; Force #11: earth gravity
  (define (falling-F q v properties)
    ;; Global downwards force, causes objects to fall down

    (let* ((g 9.86)
           (masses (map get-mass properties))
           (Fx (make-list (length masses) 0.0))
           (Fy (map (lambda (x) (* x g)) masses)))
      (zip Fx Fy)))

  ;; Force #12: obstacle
  ;; create an obstacle force

  (define (make-obstacle-F obstacles)
    (lambda (q v properties)
      (let* ((x-min (map first (map get-obstacle-ul obstacles)))
             (y-min (map second (map get-obstacle-ul obstacles)))
             (x-max (map first (map get-obstacle-lr obstacles)))
             (y-max (map second (map get-obstacle-lr obstacles)))
             (xvec (get-x q))
             (yvec (get-y q))
             (Fxl (map (lambda (i j s t) (within-obstacle-helper xvec yvec i j s t)) x-min x-max y-min y-max))
             (Fx (fold (lambda (a b) (map (lambda (x y) (+ x y)) a b)) (make-list (length Fxl) 0.0) Fxl))
             (Fyl (map (lambda (i j) (within-obstacle-helper yvec i j)) y-min y-max))
             (Fy (fold (lambda (a b) (map (lambda (x y) (+ x y)) a b)) (make-list (length Fyl) 0.0) Fyl)))
        (zip Fx Fy))))

  (define (within-obstacle-helper xvec yvec x-min x-max y-min y-max)
    (let* ((halfway-x (+ x-min (/ (abs (+ x-min x-max)) 2)))
           (halfway-y (+ y-min (/ (abs (+ y-min y-max)) 2)))
           (k 500000.0)) ;; strength of box, basically treat it like powerful tiny springs
      (map (lambda (x y) (if (and (> x x-min) (< x x-max) (> y y-min) (< y y-max))
                             (list (if (> x halfway-x) (* k (abs (- x-max x))) (* k (abs (- x y-min))))
                                   (if (> y halfway-y) (* k (abs (- y-max y))) (* k (abs (- y y-min)))))
                             '(0.0 0.0)))
           xvec yvec)))


  ;; ====================== END of list of Forces =============================


  (define F0 null-F)
  (define F1 squiggler-F)
  (define F2 gravitational-F)
  (define F3 spiraler-F)
  (define F4 box-F)
  (define F5 collision-F)

;;; GOO AND OBSTACLES
  ;;  (define gooColor "white")
  ;;  (define whole-world-goo (make-goo '(0 0) '(640 480) -0 gooColor))
  ;;  (define goox (make-goo '(320 320) '(320 320) 0 gooColor))

  ;;  (define smooth-goo 0)
  ;;  (define weak-goo -5)
  ;;  (define strong-goo -20)

  ;;  (define (create-goo-type gooStrength gooColor)
  ;;    (lambda (location)
  ;;      (make-goo (first location) (second location) gooStrength gooColor)))

  ;;  (define goo-type1 (create-goo-type strong-goo "yellowgreen"))
  ;;  (define goo-type2 (create-goo-type strong-goo "magenta"))

  ;;  (define goo1-location (list '(0 100) '(200 400)))
  ;;  (define goo2-location (list '(490 100) '(580 350)))

  ;;  (define goo1 (goo-type1 goo1-location))
  ;;  (define goo2 (goo-type2 goo2-location))
  ;;  (define goo-list (list goo1 goo2 goox))



;;; GOO Objects, need to be initialized even if empty
  ;;  (define gooColor "white")
  ;;  (define goo1 (make-goo '(0 100) '(200 400) -200 gooColor))
  ;;  (define goo2 (make-goo '(60 100) '(150 350) -10 gooColor))
  ;;  (define goo3 (make-goo '(490 100) '(580 350) -2 gooColor))
  ;;  (define goo4 (make-goo '(330 100) '(420 350) 15 gooColor))
  ;;  (define whole-world-goo (make-goo '(0 0) '(640 480) -0 gooColor))
  ;;  (define goox (make-goo '(320 320) '(320 320) 0 gooColor))
  ;;  (define goo-list (list goo1 goox))


;;; OBSTACLES, need to be initialized even if empty
  ;; it is assumed that the first obstacle is the border
  ;; "border"
  (define border-width 20)
  (define border-box (make-box '(0 0) '(640 480) border-width "black"))
  (define obstacle1 (make-obstacle '(0 0) '(640 100) "black"))

  (define schmoot-box (make-obstacle '(50 190) '(70 210) "black"))
  (define kloot-box (make-obstacle '(490 190) '(510 210) "black"))

  (define obstaclex (make-obstacle '(0 0) '(0 0) "white"))

  (define invis-obstacle (make-obstacle '(290 180) '(420 350) "white"))
  (define obstacles (append border-box (list obstaclex)))


  ;; ===================== BEGIN Forces ===================

  ;;  (define (make-goo-F goo-list)
  ;;    (lambda (q v properties)
  ;;      (let* ((x-min (map first (map get-goo-ul goo-list)))
  ;;             (y-min (map second (map get-goo-ul goo-list)))
  ;;             (x-max (map first (map get-goo-lr goo-list)))
  ;;             (y-max (map second (map get-goo-lr goo-list)))
  ;;             (sizes (map get-size properties))
  ;;             (masses (map get-mass properties))
  ;;             (resistances (map get-goo-resistance goo-list))
  ;;             (F (map (lambda (in-goo-list qs vs)
  ;;                       (let* ((goo-transform (filter (lambda (x) x) in-goo-list)))
  ;;                         (if (null? goo-transform)
  ;;                             '(0.0 0.0)
  ;;                             (map * (first goo-transform) vs))))
  ;;                     (map (lambda (specific-q specific-size specific-mass)
  ;;                            (map (lambda (i j s t specific-resistance)
  ;;                                   (if (and (> (+ (first specific-q) specific-size) i)
  ;;                                            (< (- (first specific-q) specific-size) j)
  ;;                                            (> (+ (second specific-q) specific-size) s)
  ;;                                            (< (- (second specific-q) specific-size) t))
  ;;                                       (make-list 2 (* specific-mass specific-resistance))
  ;;                                       #f)) x-min x-max y-min y-max resistances)) q sizes masses)
  ;;                     q v)))
  ;;        F)))

  (define (make-box upper-left-corner bottom-right-corner box-width color)
    (let*
        ((box-right
          (make-obstacle (list (- (first bottom-right-corner) box-width) (second upper-left-corner))
                         bottom-right-corner color))
         (box-left
          (make-obstacle upper-left-corner (list box-width (second bottom-right-corner)) color))
         (box-up
          (make-obstacle upper-left-corner (list (first bottom-right-corner) box-width) color))
         (box-down
          (make-obstacle (list (first upper-left-corner) (- (second bottom-right-corner) box-width))
                         bottom-right-corner color)))
      (list box-right box-left box-up box-down)))

                                        ;(define (my-church-force q v properties)
                                        ;  (make-list (length q) '(0.0 0.0)))
  ;; convenient function for handling multiple-interaction between pairs of particles.
  ;; takes in a force F which describes the interaction between any pair, and computes
  ;; the necessary N^2 interactions, spitting them out as ((Fx1, Fy1) (Fx2, Fy2), ...)

  (define (multi-interaction-F2 F)
    (lambda (q v properties)
      (let* ((masses (map get-mass properties)))
        (let loop ((n 0) (Fl '()))
          (if (< n (length q))
              (let* ([main-q (list-ref q n)]
                     [main-v (list-ref v n)]
                     [main-properties (list-ref properties n)]
                     [rest-q (remove-element q n)]
                     [rest-v (remove-element v n)]
                     [rest-properties (remove-element properties n)]
                     [f-main-rest (map  (lambda (q2 v2 properties2)
                                          (F main-q q2 main-v v2 main-properties properties2))
                                        rest-q rest-v rest-properties)]
                     [result (list (sum (map first f-main-rest)) (sum (map second f-main-rest)))])
                (loop (+ n 1) (pair result Fl)))
              (reverse Fl))))))

  ;; Goo Force
                                        ;(define goo-F (make-goo-F goo-list))

  ;; Gravitation well constructs an "invisible" non-collision mass at a given location
  ;; The 'mass' of the well gives its strengh of attraction
  (define (make-gravitational-well-F location mass)
    (lambda (q v properties)
      (let* ((masses (map get-mass properties))
             (grav-well-q location)
             (grav-well-mass mass)
             (rl (map (lambda (k) (compute-euc-dist grav-well-q k)) q))
             (thetal (map (lambda (k) (compute-angle grav-well-q k)) q))
             (Fl (map (lambda (m r)
                        (if (< r 8.0)
                            0.0
                            (* -1 (* (expt 10 5) (/ (* m grav-well-mass) (expt r 2.0))))))
                      masses rl))
             (Fx (map (lambda (F theta) (* F (cos theta))) Fl thetal))
             (Fy (map (lambda (F theta) (* F (sin theta))) Fl thetal)))
        (zip Fx Fy))))

  ;; Gravity well based on a property of the particle

  (define (make-property-based-well location mass desired-property)
    (lambda (q v properties)
      (let* ((masses (map get-mass properties))
             (propertyl (map get-identity properties))
             (grav-well-q location)
             (grav-well-mass mass)
             (rl (map (lambda (k) (compute-euc-dist grav-well-q k)) q))
             (thetal (map (lambda (k) (compute-angle grav-well-q k)) q))
             (Fl (map (lambda (m r)
                        (if (< r 8.0)
                            0.0
                            (* -1 (* (expt 10 5) (/ (* m grav-well-mass) (expt r 2.0))))))
                      masses rl))
             (Fx (map (lambda (F theta property)
                        (if (equal? property desired-property) (* F (cos theta)) 0)) Fl thetal propertyl))
             (Fy (map (lambda (F theta property)
                        (if (equal? property desired-property) (* F (sin theta)) 0)) Fl thetal propertyl)))
        (zip Fx Fy))))

  (define well-F (make-gravitational-well-F '(350.0 200.0) 50000.0))
  (define schmoot-well-FA (make-property-based-well '(60.0 200.0) 5000.0 "schmoot"))
  (define kloot-well-FA (make-property-based-well '(500 200) 5000.0 "kloot"))
  (define schmoot-well-FB (make-property-based-well '(60.0 200.0) 15000.0 "schmoot"))
  (define kloot-well-FB (make-property-based-well '(500 200) 5000.0 "kloot"))
  ;; ===================== END of Forces ===================


                                        ;(define (get-force force-name)
                                        ;  (case force-name
                                        ;    [(collision-F) collision-F]
                                        ;    [(goo-F) goo-F]
                                        ;    [(schmoot-well-FB) schmoot-well-FB]
                                        ;    [(kloot-well-FB) kloot-well-FB]
                                        ;    [else (error force-name "unknown force")]))

  )
