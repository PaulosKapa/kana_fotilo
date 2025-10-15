#εισαγωγη βιβλιοθηκης για το gpio του raspberry pi 
import RPi.GPIO as GPIO
#εισαγωγη βιβλιοθηκης για διαχειριση χρονου
import time
#τροπος αριθμησης των pins
GPIO.setmode(GPIO.BCM)
#pin για trig (βγαζει ηχο), echo (λαμβανει ηχο), servo motor
TRIG = 23
ECHO = 24
SERVO = 17
checkNext = False
#τιμες που θα μπορει να παρει το servo
#degrees = [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.5]
degrees = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
#πινακας με μετρησεις του υπερηχου
measurements = []
#η αποσταση που θεωρουμε πως ειναι πολυ κοντα στον υπερηχο
tooClose = 5.0
print ("Distance Measurement In Progress")
#διαχωρισμος σε input και output 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(SERVO, GPIO.OUT)
#setup για υπερηχο
GPIO.output(TRIG, False)
print ("Waiting For Sensor To Settle")
#setup για servo
pwm = GPIO.PWM(SERVO, 50)
pwm.start(7.5)
time.sleep(2)
#μεταβλητη για επαναληψη
i = 0
while True:
    #βγαζει υπερηχο
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    #σταματαει να βγαζει υπερηχο
    GPIO.output(TRIG, False)
    #μεγιστος χρονος που θα περιμενει ο κωδικας για να επιστρεψει υπερηχος
    timeout = time.time() + 0.03  
    #μεθοδος ληψης υπερηχου
    while GPIO.input(ECHO) == 0 and time.time() < timeout:
        pass
    pulse_start = time.time()

    while GPIO.input(ECHO) == 1 and time.time() < timeout:
        pass
    pulse_end = time.time()
     #περιπτωση που δεν ληφθηκες υπερηχος
    pulse_duration = pulse_end - pulse_start
    if pulse_duration <= 0 or pulse_duration > 0.03:
        print("Timeout — no echo")
        continue
    #αποσταση = χρονος * ταχυτητα
    distance = pulse_duration * 17150
    #μειωνω σε δυο ψηφια
    distance = round(distance, 2)
    #προσθετουμε τη μετρηση στον πινακα measurements    
    measurements.append(distance)
    #αν η αποσταση απο το αντικειμενο ειναι πολυ μικρη
    if(distance <= tooClose or checkNext == True):
        #αν ειμαστε στην 2η επαναληχη και η αποσταση στην πρωτη επαναληψη ηταν μεγαλυτερη απο το οριο
        if(i == 1):
            if(measurements[0]>tooClose):
                time.sleep(0.5)
                #μετακινηση του servo στο διαμερισμο 0
                duty = 2.5 + (degrees[0] / 180.0) * 10  
                pwm.ChangeDutyCycle(duty) 
                time.sleep(0.5)                
                print(measurements[0], i)
                checkNext = False
            else:
                checkNext = True
        
        #για 3+ επαναληψεις       
        elif(i-2>=0):
                j=1
                #στις 3+ επαναληψεις θα ελεγχουμε τις 2 προηουμενες μετρησεις
                while (j<3):
                    if(measurements[i-j]>tooClose):
                        time.sleep(0.5)
                        #πηγαινει το servo στον αντιστοιχο διαμερισμο. ΠΧ αν ειμαστε στη μετρηση 3 θα κοιταξει τις μετρησεις 2 και 1 ο κωδικας
                        #αν η μετρηση 2 εχει αοσταση μεγαλυτερη απο το οριο, τοτε θα παει στο διαμερισμο 2, δηλαδη θα γραψει 3.5 στο servo 
                        duty = 2.5 + (degrees[i-j] / 180.0) * 10
                        pwm.ChangeDutyCycle(duty)
                        time.sleep(0.5)
                        print(measurements[i-j], i, j)   
                        checkNext = False
                        break
                    else:
                        checkNext = True                     
                    j+=1

    i+=1  
    #στις 10 επαναληψεις διαγραφουμε τον πινακα και ξανααρχιζουμε.
    if(len(measurements)>10):
        measurements.clear()
        i = 0
   

pwm.stop()
GPIO.cleanup()