#Переменные
QuantityOfHomeworks = 12
QuantutyOfHours = 1.5
NameOfCourse = "Python"
TimeForOneTask = QuantutyOfHours / QuantityOfHomeworks
print("Курс: " + str(NameOfCourse) + ", всего задач: " + str(QuantityOfHomeworks) + ", затрачено часов: " + str(QuantutyOfHours) + ", среднее время выполнения: " + str(TimeForOneTask) + " часа.")
#print("Курс:",NameOfCourse,", всего задач:",QuantityOfHomeworks,", затрачено часов:",QuantutyOfHours,", среднее время выполнения:",TimeForOneTask,"часа.") - некрасивый вывод (присутствует пробел перед запятыми)