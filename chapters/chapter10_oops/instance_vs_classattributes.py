class student():
    course = "IT"
    fee=4000000
    timeLine="4years"

shreya = student()
shreya.name = "shreya"#this is an instance attribute
shreya.course="cse"#it is updated here because instance attribute take the preference over class attribute
print(shreya.name,shreya.course,shreya.fee,shreya.timeLine)
priya = student()
sneha=student()