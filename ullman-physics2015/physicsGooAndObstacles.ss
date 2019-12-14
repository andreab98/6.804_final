;;; GOO Objects, need to be initialized even if empty

(define smooth-goo 0.0)
(define weak-goo -5.0)
(define strong-goo -20.0)

(define (get-goo-strength goo) (third goo))

 (define gooColor "horizontal")
 (define whole-world-goo (make-goo '(0 0) '(640 480) -0 gooColor))
 (define goox (make-goo '(320 320) '(320 320) 0 gooColor))

 (define smooth-goo 0)
 (define weak-goo -5)
 (define strong-goo -20)
 
 (define (create-goo-type gooStrength gooColor)
   (lambda (location)
     (make-goo (first location) (second location) gooStrength gooColor)))
 
 (define goo-type1 (create-goo-type strong-goo "horizontal"))
 (define goo-type2 (create-goo-type strong-goo "diagonal"))

 (define goo1-location (list '(0 100) '(200 400)))
 (define goo2-location (list '(490 100) '(580 350)))
 (define goo-locations (list goo1-location goo2-location))

 (define goo1 (goo-type1 goo1-location))
 (define goo2 (goo-type2 goo2-location))
 (define goo-list (list goo1 goo2 goox))

;The next thing is for the purposes of inference
(define (create-goos goo-strengths goo-colors goo-locations)
  (map (lambda (t c l) ((create-goo-type t c) l)) goo-strengths goo-colors goo-locations))


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
