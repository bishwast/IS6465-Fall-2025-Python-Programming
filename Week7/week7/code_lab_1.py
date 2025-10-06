import functions as func

value = "no"
print(func.yesNoBooleanConverter(value))

val1 = True
val = func.booleanYesNoConverter(val1)
print(val)

val2 = "c"
print("Move state: ", func.moveQueueValueConverter(val2))

val3 = True
print("Null:", func.nullToBooleanConverter(val3))