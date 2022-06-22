from cmath import log
from timeit import repeat
from tkinter import Variable
displacement=float(input("displacement "))
bore_stroke_ratio=float(input("bore on stroke ratio "))
cylinders=int(input("How many cylinders? "))
engine_type=int(input("Select engine type: 1.Vintage Sports Car  2.Vintage Race Car  3.Modern Sports Car  4.Modern Race Car "))
if engine_type == 1:
    timing=int(input("Select valve timing type: 1.Early  2.Normal  3.Delayed "))
    if timing==1:
        valve=float(-0.1)
        limiter=float(-0.06)
    elif timing==3:
        valve=float(0.1)
        limiter=float(0.06)
    elif timing==2:
        valve=0
        limiter=0
    max_output=100*displacement/1000
    max_output=max_output + max_output * cylinders/100
    max_output_rpm=bore_stroke_ratio*6000    
    max_rpm=bore_stroke_ratio*9500
    max_output_rpm=max_output_rpm+max_output_rpm*valve
    max_rpm=max_rpm+max_rpm*limiter
    space=max_rpm-max_output_rpm
    print(0,"|",0)
    print(max_output_rpm/5,"|",1/2*max_output)
    print(2*max_output_rpm/5,"|",3/4*max_output)
    print(3*max_output_rpm/5,"|",4/5*max_output)
    print(4*max_output_rpm/5,"|",86/100*max_output)
    print(max_output_rpm,"|",max_output)
    print(max_output_rpm+space/4,"|",9/10*max_output)
    print(max_output_rpm+space/2,"|",3/4*max_output)
    print(max_output_rpm+3*space/4,"|",1/2*max_output)
    print(max_rpm,"|",1/4*max_output)
elif engine_type == 2:
    timing=int(input("Select valve timing type: 1.Early  2.Normal  3.Delayed "))
    if timing==1:
        valve=float(-0.1)
        limiter=float(-0.06)
    elif timing==3:
        valve=float(0.1)
        limiter=float(0.06)
    elif timing==2:
        valve=0
        limiter=0
    max_output=105*displacement/1000
    max_output_rpm=bore_stroke_ratio*6000
    max_rpm=bore_stroke_ratio*8000
    max_output=max_output + max_output * cylinders/100
    max_output_rpm=max_output_rpm+max_output_rpm*valve
    max_rpm=max_rpm+max_rpm*limiter
    space=max_rpm-max_output_rpm
    print(0,"|",0)
    print(max_output_rpm/9,"|",0.4*max_output)
    print(2*max_output_rpm/9,"|",0.4*max_output)
    print(3*max_output_rpm/9,"|",0.5*max_output)
    print(4*max_output_rpm/9,"|",0.65*max_output)
    print(5*max_output_rpm/9,"|",0.81*max_output)
    print(6*max_output_rpm/9,"|",0.88*max_output)
    print(7*max_output_rpm/9,"|",0.95*max_output)
    print(8*max_output_rpm/9,"|",0.99*max_output)
    print(max_output_rpm,"|",max_output)
    print(max_output_rpm+space/4,"|",0.98*max_output)
    print(max_output_rpm+space/2,"|",0.81*max_output)
    print(max_output_rpm+3*space/4,"|",0.77*max_output)
    print(max_rpm,"|",0.5*max_output)
elif engine_type == 3:
    timing=int(input("Select valve timing type: 1.Early  2.Normal  3.Delayed  4.Variable "))
    map=int(input("Select engine map type: 1.Conservative  2.Normal  3.Aggressive "))
    if timing==1:
        valve=float(-0.1)
        limiter=float(-0.06)
        vt=float(0)
    elif timing==3:
        valve=float(0.1)
        limiter=float(0.06)
        vt=float(0)
    elif timing==4:
        valve=float(0.04)
        limiter=float(0.03)
        vt=float(0.1)
    elif timing==2:
        valve=0
        limiter=0
        vt=float(0)
    if map==1:
        mp=-0.1
    elif map==3:
        mp=0.1
    elif map==2:
        mp=0
    max_output=113*displacement/1000
    max_output_rpm=bore_stroke_ratio*5400
    max_rpm=bore_stroke_ratio*8000
    max_output=max_output + max_output * cylinders/100+max_output*mp+max_output*vt
    max_output_rpm=max_output_rpm+max_output_rpm*valve
    max_rpm=max_rpm+max_rpm*limiter
    space=max_rpm-max_output_rpm
    print(0,"|",0)
    print(max_output_rpm/6,"|",0.5*max_output)
    print(2*max_output_rpm/6,"|",0.62*max_output)
    print(3*max_output_rpm/6,"|",0.76*max_output)
    print(4*max_output_rpm/6,"|",0.94*max_output)
    print(5*max_output_rpm/6,"|",0.98*max_output)
    print(max_output_rpm,"|",max_output)
    print(max_output_rpm+space/3,"|",0.92*max_output)
    print(2*max_output_rpm+space/3,"|",0.9*max_output)
    print(max_rpm,"|",0.84*max_output)
elif engine_type == 4:
    timing=int(input("Select valve timing type: 1.Early  2.Normal  3.Delayed  4.Variable "))
    map=int(input("Select engine map type: 1.Conservative  2.Normal  3.Aggressive "))
    if timing==1:
        valve=float(-0.1)
        limiter=float(-0.06)
        vt=float(0)
    elif timing==3:
        valve=float(0.1)
        limiter=float(0.06)
        vt=float(0)
    elif timing==4:
        valve=float(0.04)
        limiter=float(0.03)
        vt=float(0.1)
    elif timing==2:
        valve=0
        limiter=0
        vt=float(0)
    if map==1:
        mp=-0.1
    elif map==3:
        mp=0.1
    elif map==2:
        mp=0
    max_output=125*displacement/1000
    max_output_rpm=bore_stroke_ratio*6700
    max_rpm=bore_stroke_ratio*8000
    max_output=max_output + max_output * cylinders/100+max_output*mp+max_output*vt
    max_output_rpm=max_output_rpm+max_output_rpm*valve
    max_rpm=max_rpm+max_rpm*limiter
    space=max_rpm-max_output_rpm
    print(0,"|",0)
    print(max_output_rpm/16,"|",0.28*max_output)
    print(2*max_output_rpm/16,"|",0.3*max_output)
    print(3*max_output_rpm/16,"|",0.33*max_output)
    print(4*max_output_rpm/16,"|",0.42*max_output)
    print(5*max_output_rpm/16,"|",0.45*max_output)
    print(6*max_output_rpm/16,"|",0.51*max_output)
    print(7*max_output_rpm/16,"|",0.61*max_output)
    print(8*max_output_rpm/16,"|",0.67*max_output)
    print(9*max_output_rpm/16,"|",0.7*max_output)
    print(10*max_output_rpm/16,"|",0.77*max_output)
    print(11*max_output_rpm/16,"|",0.81*max_output)
    print(12*max_output_rpm/16,"|",0.82*max_output)
    print(13*max_output_rpm/16,"|",0.83*max_output)
    print(14*max_output_rpm/16,"|",0.89*max_output)
    print(15*max_output_rpm/16,"|",0.97*max_output)
    print(max_output_rpm,"|",max_output)
    print(max_output_rpm+space/2,"|",0.95*max_output)
    print(max_rpm,"|",0.8*max_output)
turbo=float(input("Do you want a turbo? 1.Yes 2.Two, please 3.No "))
if turbo==1:
    size=float(input("Select turbo size 1.Small 2.Large "))
    if size==1:
        print("[TURBO_0]")
        print("LAG_DN=0.99")
        print("LAG_UP=0.995")
        print("MAX_BOOST=1.2")
        print("WASTEGATE=1")
        print("DISPLAY_MAX_BOOST=1")
        print("REFERENCE_RPM=",max_rpm*0.25)
        print("GAMMA=2.5")
        print("COCKPIT_ADJUSTABLE=1")
        input("Press esc to exit")
    elif size==2:
        print("[TURBO_0]")
        print("LAG_DN=0.98")
        print("LAG_UP=0.97")
        print("MAX_BOOST=1.6")
        print("WASTEGATE=1.4")
        print("DISPLAY_MAX_BOOST=1.4")
        print("REFERENCE_RPM=",max_rpm*0.5)
        print("GAMMA=2")
        print("COCKPIT_ADJUSTABLE=1")
        input("Press esc to exit")
elif turbo==2:
        print("[TURBO_0]")
        print("LAG_DN=0.998")
        print("LAG_UP=0.99")
        print("MAX_BOOST=0.7")
        print("WASTEGATE=0.7")
        print("DISPLAY_MAX_BOOST=0.7")
        print("REFERENCE_RPM=",max_rpm*0.2)
        print("GAMMA=2.3")
        print("COCKPIT_ADJUSTABLE=0")
        print("[TURBO_1]")
        print("LAG_DN=0.998")
        print("LAG_UP=0.99")
        print("MAX_BOOST=0.7")
        print("WASTEGATE=0.7")
        print("DISPLAY_MAX_BOOST=0.7")
        print("REFERENCE_RPM=",max_rpm*0.2)
        print("GAMMA=2.3")
        print("COCKPIT_ADJUSTABLE=0")
        input("Press esc to exit")
else:
    input("Press esc to exit")
