print("Выберете язык использования / Choose the language of use")
print("1)Русский")
print("2)English")
tx = input("Введите выбор / Enter the choice : ")
if tx == "1":
    #from functools import lru_cache
    import math
    import fractions
    #import numpy as np


    def get_float(input_text):
        while True:
            input_string = input(input_text)
            try :
                if input_string.lower() == "pi" :
                    result = pi
                elif input_string.lower() == "e" or input_string.lower() == "е" :
                    result = e
                elif input_string.lower() == "y" :
                    result = y
                elif input_string.lower() == "дробь" :
                    fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                    result = Fraction(fraction_input)
                elif input_string.lower() == "ф":
                    result = (1 + math.sqrt(5)) / 2
                else :
                    result = float(input_string)
                break
            except ValueError :
                print("Ошибка! Введите число")

        return result

    def block_trigonom() :
        import math
        cos = math.cos
        asin = math.asin
        atan = math.atan
        acos = math.acos
        degrees = math.degrees
        radians = math.radians
        sin = math.sin  # Добавлено для полноты
        tan = math.tan  # Добавлено для полноты
        while True :
            # Ввод числа (или специальных значений)
            num_str = input("Введите число или pi или e или y или 'дробь': ")
            num = None  # Инициализация для избежания ошибок
            try :
                if num_str.lower() == "pi" :
                    num = math.pi
                elif num_str.lower() == "e" :
                    num = math.e
                elif num_str.lower() == "y" :  # Предполагаем, что 'y' означает какое-то другое значение, если нет, удалите
                    num = y  # Замените на реальное значение y, если оно есть
                elif num_str.lower() == "дробь" :
                    fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                    from fractions import Fraction  # Импорт здесь, если он нужен только здесь
                    num = Fraction(fraction_input)
                else :
                    num = float(num_str)
            except ValueError :
                print("Ошибка ввода числа!")
                continue
            except NameError :  # На случай, если 'y' не определено
                print("Ошибка: 'y' не определено. Пожалуйста, введите другое значение.")
                continue
            except ZeroDivisionError :
                print("Ошибка: Деление на ноль в дроби.")
                continue
            operation = input("Введите операцию (sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc): ")

            valid_operations = ["sin", "cos", "tan", "cot", "sec", "csc", "asin", "acos", "atan", "acot", "asec",
                                "acsc"]
            if operation not in valid_operations :
                print("Ошибка! Выберите одну из следующих функций: ", ", ".join(valid_operations))
                break
            gr = input("Укажите единицы измерения для вывода (degrees/radians): ")
            if gr.lower() == "degrees" :
                try :
                    angle_in_radians = None
                    if isinstance(num, (int, float, complex)) :  # Если num - обычное число
                        if gr.lower() == "degrees" :  # Это означает, что пользователь ввел число как градусы
                            angle_in_radians = radians(num)
                        else :  # Пользователь ввел число как радианы
                            angle_in_radians = num
                    elif isinstance(num, Fraction) :  # Если num - дробь
                        pass  # Добавьте здесь обработку дробей, если нужно
                    if operation in ["sin", "cos", "tan", "cot", "sec", "csc"] :
                        result_rad = None
                        if operation == "sin" :
                            result_rad = sin(angle_in_radians)
                        elif operation == "cos" :
                            result_rad = cos(angle_in_radians)
                        elif operation == "tan" :
                            result_rad = tan(angle_in_radians)
                        elif operation == "cot" :
                            if tan(angle_in_radians) == 0 :
                                print("Ошибка: Деление на ноль (тангенс равен 0).!")
                                continue
                            result_rad = 1 / tan(angle_in_radians)
                        elif operation == "sec" :
                            if cos(angle_in_radians) == 0 :
                                print("Ошибка: Деление на ноль (косинус равен 0).!")
                                continue
                            result_rad = 1 / cos(angle_in_radians)
                        elif operation == "csc" :
                            if sin(angle_in_radians) == 0 :
                                print("Ошибка: Деление на ноль (синус равен 0).!")
                                continue
                            result_rad = 1 / sin(angle_in_radians)
                        if gr.lower() == "degrees" :
                            display_value = degrees(result_rad)
                            print(f"{operation}({num}°)" if isinstance(num, (int, float)) else print(
                                f"{operation}({num})"), "=", f"{result_rad:.6f}", " (в градусах)", sep=" ")
                            break
                        else :  # gr.lower() == "radians"
                            print(f"{operation}({num} рад)" if isinstance(num, (int, float)) else print(
                                f"{operation}({num})"), "=", f"{result_rad:.6f}", " (в радианах)", sep=" ")
                            break
                    elif operation in ["asin", "acos", "atan", "acot", "asec", "acsc"] :
                        result_rad = None
                        if operation in ["asin", "acos"] and not (-1 <= num <= 1) :
                            print(
                                f"Ошибка: Арксинус/Арккосинус можно найти только для чисел от -1 до 1. Получено: {num}")
                            continue
                        if operation == "asec" and not (abs(num) >= 1) :
                            print(
                                f"Ошибка: Арксеканс можно найти только для чисел, модуль которых >= 1. Получено: {num}")
                            continue
                        if operation == "acsc" and not (abs(num) >= 1) :
                            print(
                                f"Ошибка: Арккосеканс можно найти только для чисел, модуль которых >= 1. Получено: {num}")
                            continue
                        if operation == "asin" :
                            result_rad = asin(num)
                        elif operation == "acos" :
                            result_rad = acos(num)
                        elif operation == "atan" :
                            result_rad = atan(num)
                        elif operation == "acot" :
                            if num == 0 :
                                result_rad = math.pi / 2
                            else :
                                result_rad = atan(1 / num)
                                if num < 0 :
                                    result_rad += math.pi
                        elif operation == "asec" :
                            if num == 0 :
                                print("Ошибка: Невозможно вычислить арксеканс для 0.")
                                continue
                            result_rad = acos(1 / num)
                        elif operation == "acsc" :
                            if num == 0 :
                                print("Ошибка: Невозможно вычислить арккосеканс для 0.")
                                continue
                            result_rad = asin(1 / num)
                        if gr.lower() == "degrees" :
                            if result_rad is not None :
                                display_value_deg = degrees(result_rad)
                                print(f"{operation}({num})" if not isinstance(num,(int, float)) else f"{operation}({num})","=", f"{display_value_deg:.6f}° (в градусах)", sep=" ")
                        else :
                            if result_rad is not None :
                                print(f"{operation}({num})" if not isinstance(num,(int, float)) else f"{operation}({num})","=", f"{result_rad:.6f} рад (в радианах)", sep=" ")
                    else :
                        print("Неизвестная операция.")
                        break
                except ValueError :
                    print("Ошибка при вычислении. Проверьте введенные данные.")
                    break
                except ZeroDivisionError :
                    print("Ошибка: Деление на ноль при вычислении.")
                    break
                except Exception as e :
                    print(f"Произошла непредвиденная ошибка: {e}")
                    break
            elif gr.lower() == "radians" :
                try :
                    angle_in_radians = None
                    if isinstance(num, (int, float, complex)) :
                        angle_in_radians = num
                    elif isinstance(num, Fraction) :
                        pass
                    if operation in ["sin", "cos", "tan", "cot", "sec", "csc"] :
                        result_rad = None
                        if operation == "sin" :
                            result_rad = sin(angle_in_radians)
                        elif operation == "cos" :
                            result_rad = cos(angle_in_radians)
                        elif operation == "tan" :
                            result_rad = tan(angle_in_radians)
                        elif operation == "cot" :
                            if tan(angle_in_radians) == 0 : print("Ошибка: Деление на ноль."); continue
                            result_rad = 1 / tan(angle_in_radians)
                        elif operation == "sec" :
                            if cos(angle_in_radians) == 0 : print("Ошибка: Деление на ноль."); continue
                            result_rad = 1 / cos(angle_in_radians)
                        elif operation == "csc" :
                            if sin(angle_in_radians) == 0 : print("Ошибка: Деление на ноль."); continue
                            result_rad = 1 / sin(angle_in_radians)

                        print(f"{operation}({num})" if not isinstance(num, (int, float)) else print(
                            f"{operation}({num})"), "=", f"{result_rad:.6f}", " радиан", sep=" ")
                        break

                    # --- Обратные тригонометрические функции ---
                    elif operation in ["asin", "acos", "atan", "acot", "asec", "acsc"] :
                        result_rad = None

                        if operation in ["asin", "acos"] and not (-1 <= num <= 1) :
                            print(
                                f"Ошибка: Арксинус/Арккосинус можно найти только для чисел от -1 до 1. Получено: {num}")
                            continue

                        if operation == "asec" and not (abs(num) >= 1) :
                            print(
                                f"Ошибка: Арксеканс можно найти только для чисел, модуль которых >= 1. Получено: {num}")
                            continue
                        if operation == "acsc" and not (abs(num) >= 1) :
                            print(
                                f"Ошибка: Арккосеканс можно найти только для чисел, модуль которых >= 1. Получено: {num}")
                            continue

                        if operation == "asin" :
                            result_rad = asin(num)
                        elif operation == "acos" :
                            result_rad = acos(num)
                        elif operation == "atan" :
                            result_rad = atan(num)
                        elif operation == "acot" :
                            if num == 0 :
                                result_rad = math.pi / 2
                            else :
                                result_rad = atan(1 / num)
                                if num < 0 : result_rad += math.pi
                        elif operation == "asec" :
                            if num == 0 : print("Ошибка: Невозможно вычислить арксеканс для 0."); continue
                            result_rad = acos(1 / num)
                        elif operation == "acsc" :
                            if num == 0 : print("Ошибка: Невозможно вычислить арккосеканс для 0."); continue
                            result_rad = asin(1 / num)

                        print(f"{operation}({num})" if not isinstance(num, (int, float)) else print(
                            f"{operation}({num})"), "=", f"{result_rad:.6f} рад", sep=" ")
                        break
                    else :
                        print("Неизвестная операция.")
                        break
                except ValueError :
                    print("Ошибка при вычислении. Проверьте введенные данные.")
                    break
                except ZeroDivisionError :
                    print("Ошибка: Деление на ноль при вычислении.")
                    break
                except Exception as e :
                    print(f"Произошла непредвиденная ошибка: {e}")
                    break
            else :
                print("Ошибка! Пожалуйста, выберите 'degrees' или 'radians'.")
                break
    def block_classic() :
            import functools
            import math
            pi = math.pi
            e = math.e
            Fraction = fractions.Fraction
            sqrt = math.sqrt
            cbrt = math.cbrt
            gcd = math.gcd
            log = math.log
            pow = math.pow
            factorial = math.factorial
            y = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495146314472498070824809605040144865428362241739976449235362535003337429373377376739427925952582470949160087352039481656708532331517766115286211995015079847937450857057400299213547861466940296043254215190587755352673313992540129674205137541395491116851028079842348775872050384310939973613725530608893312676001724795378367592713515772261027349291394079843010341777177808815495706610750101619166334015227893586796549725203621287922655595366962817638879272680132431010476505963703947394957638906572967929601009015125195950922243501409349871228247949747195646976318506676129063811051824197444867836380861749455169892792301877391072945781554316005002182844096053772434203285478367015177394398700302370339518328690001558193988042707411542227819716523011073565833967348717650491941812300040654693142999297779569303100503086303418569803231083691640025892970890985486825777364288253954925873629596133298574739302
            while True :
                num1 = get_float("Введите первое число, pi, e, y или 'дробь' или ф: ")
                try :
                    op = input("Введите операцию (1)+, 2)-, 3)*, 4)/, 5)n!, 6)2√, 7)3√, 8)**, 9)НОД, 10)НОК, 11)ost, 12)//, 13)!n, 14) log, 15) log x к y, 16) a⇈b (тетрация), 17)a**2 - b**2: ")
                    if op == "6" :
                        print(sqrt(num1))
                    elif op == "7" :
                        print(cbrt(num1))
                    elif op == "14" :
                        print(log(num1))
                    elif op == "13" :
                        result = 1
                        if num1 == 0 :
                            print("1")
                        elif num1 < 0 :
                            print("Субфакториал отрицательных не существует")
                        else :
                            for i in range(1, int(num1) + 1) :
                                result *= i
                        print(round(result / e))
                    elif op == "5" :
                        result = 1
                        if num1 == 0 :
                            print("1")
                        elif num1 < 0 :
                            print("Факториал отрицательных не существует")
                        else :
                            for i in range(1, int(num1) + 1) :
                                result *= i
                            print(result)

                    else :
                        num2 = get_float("Введите второе число, pi, e, y или 'дробь' или ф: ")
                        if op == '1' :
                            print(num1 + num2)
                        elif op == "15" :
                            print(log(num1, num2))
                        elif op == '2' :
                            print(num1 - num2)
                        elif op == '17' :
                            print(f"{num1} ** 2 - {num2} ** 2 = ({num1} - {num2}) * ({num1} + {num2}) =", (num1 - num2) * (num1 + num2))
                        elif op == '3' :
                            print(num1 * num2)
                        elif op == '8' :
                            print(num1 ** num2)
                        elif op == '16' :
                            print(pow(num1, (pow(num1, num2))))
                        elif op == '12' :
                            try:
                                print(num1 // num2)
                            except ZeroDivisionError :
                                print("Ошибка! Деление на ноль.")
                        elif op == "11" :
                            try:
                                print(f"{num1 // num2} целое число {num1 % num2} остаток")
                            except ZeroDivisionError :
                                print("Ошибка! Деление на ноль.")
                        elif op == "9" :
                            num1 = int(num1)
                            num2 = int(num2)
                            nod = gcd(num1, num2)
                            if num1 == 0 and num2 == 0 :
                                print("НЕ определено")
                            else :
                                print(gcd(num1, num2))
                        elif op == "10" :
                            num1 = int(num1)
                            num2 = int(num2)
                            nok = abs(num1 * num2) // gcd(num1, num2)
                            if num1 == 0 and num2 == 0 :
                                print("НЕ определено")
                            else :
                                print(nok)
                        elif op == '4' :
                            try :
                                print(num1 / num2)
                            except ZeroDivisionError :
                                print("Ошибка! Деление на ноль.")
                        else :
                            print("Недопустимая операция.")
                except ValueError :
                    print("Ошибка ввода второго числа!")
                    break
                break
            return

    def block_compare() :
        global factorial, pi, e, Fraction, sqrt, pow, cbrt, y, num1, num2, op
        factorial = math.factorial
        pi = math.pi
        e = math.e
        Fraction = fractions.Fraction
        sqrt = math.sqrt
        pow = math.pow
        cbrt = math.cbrt
        y = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495146314472498070824809605040144865428362241739976449235362535003337429373377376739427925952582470949160087352039481656708532331517766115286211995015079847937450857057400299213547861466940296043254215190587755352673313992540129674205137541395491116851028079842348775872050384310939973613725530608893312676001724795378367592713515772261027349291394079843010341777177808815495706610750101619166334015227893586796549725203621287922655595366962817638879272680132431010476505963703947394957638906572967929601009015125195950922243501409349871228247949747195646976318506676129063811051824197444867836380861749455169892792301877391072945781554316005002182844096053772434203285478367015177394398700302370339518328690001558193988042707411542227819716523011073565833967348717650491941812300040654693142999297779569303100503086303418569803231083691640025892970890985486825777364288253954925873629596133298574739302
        num1 = get_float("Введите первое число, pi, e, y или 'дробь' или ф: ")
        num2 = get_float("Введите второе число, pi, e, y или 'дробь' или ф: ")
        op = input("Введите операцию 1)<, 2)>, 3)=: ")
        if op == "1" :
            if num1 < num2 :
                print(num1, "меньше, чем", num2)
            else :
                print("неравенство не правильное")
        elif op == "2" :
            if num1 > num2 :
                print(num1, ",больше, чем", num2)
            else :
                print("неравенство не правильное")
        elif op == "3" :
            if num1 == num2 :
                print("Равенство равно")
            else :
                print("Выберите действие")

    def multiplicity() :
        while True :
            try :
                num1_input = get_float("Введите число, pi, e, y или 'дробь' или ф: ")
            except ValueError :
                print("Ошибка! Некорректный ввод первого числа.")
                continue

            try :
                num2_input = get_float("Введите число, на которое будет кратно или нет, pi, e, y или 'дробь' или ф: ")
            except ValueError :
                print("Ошибка! Некорректный ввод второго числа.")
                continue
            if num2_input == 0 :
                print("Ошибка: Деление на ноль невозможно.")
                continue
            if num1_input % num2_input == 0 :
                print("кратно")
            else :
                print("не кратно")

    def block_square() :
        while True :
            op = input(
                "1)Прямоугольника, 2)квадрата, 3)круга, 4)овала(эллипса), 5)треугольника, 6)трапеция, 7)параллелограмм, 8)многоугольник: ")
            if op == "1" :
                num1 = get_float("Введите число A, pi, e, y или 'дробь' или ф: ")
                num2 = get_float("Введите число B, pi, e, y или 'дробь' или ф: ")
                print("S прямоугольника =", num1 * num2)
            elif op == "2" :
                num1 = get_float("Введите число, pi, e, y или 'дробь' или ф: ")
                print("S квадрата =", num1 * num1)
            elif op == "3" :
                num1 = input("Введите r (радиус окружности) или d (диаметр окружности): ")
                if num1 == "d" :
                    num2 = get_float("Введите число: ") / 2
                    print("S окружности =", pi * pow(num2, 2))
                elif num1 == "r" :
                    num2 = get_float("Введите число: ")
                    print("S окружности =", pi * pow(num2, 2))
            elif op == "4" :
                op1 = input("Введите d (длину оси) или r (полу длину оси): ")
                if op1 == "r" :
                    try :
                        num1 = get_float("Введите длину полуоси а: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num1 = Fraction(fraction_input)
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите длину полуоси b: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input)
                        else :
                            num2 = float(num2)
                            print("S эллипса =", pi * num1 * num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    else :
                        print("Выберите из списка")
                elif op1 == "d" :
                    try :
                        num1 = get_float("Введите длину оси а: ")
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите длину оси b: ")
                        if num2.lower() == "pi" :
                            num2 = pi / 2
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e / 2
                        elif num2.lower() == "y" :
                            num2 = y / 2
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input) / 2
                        elif num2.lower() == "ф" :
                            num2 = (1 + sqrt(5)) / 2
                        else :
                            num2 = float(num2) / 2
                            print("S эллипса =", pi * num1 * num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    else :
                        print("Выберите из списка")
            elif op == "5" :
                op4 = input("1)равносторонний, 2)равнобедренный или остроугольного или тупоугольного или разносторонний, 3)прямоугольный: ")
                if op4 == "2" :
                    try :
                        num1 = get_float("Введите длину основания: ")
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите высоту треугольника: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input)
                        elif num2.lower() == "ф" :
                            num2 = (1 + sqrt(5)) / 2
                        else :
                            num2 = float(num2)
                            print("S треугольника =", 0.5 * num1 * num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                elif op4 == "3" :
                    op = input("1)через стороны, 2)через гипотенузу: ")
                    if op == "1" :
                        try :
                            num1 = get_float("Введите длину основания: ")
                        except ValueError :
                            print("Ошибка! Некорректный ввод первого числа.")
                            break
                        try :
                            num2 = input("Введите высоту: ")
                            if num2.lower() == "pi" :
                                num2 = pi
                            elif num2.lower() == "e" or num2.lower() == "е" :
                                num2 = e
                            elif num2.lower() == "y" :
                                num2 = y
                            elif num2.lower() == "дробь" :
                                fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                                num2 = Fraction(fraction_input)
                            elif num2.lower() == "ф" :
                                num2 = (1 + sqrt(5)) / 2
                            else :
                                num2 = float(num2)
                            print("S прямоугольного треугольника =", (num1 * num2) / 2)
                        except ValueError :
                            print("Ошибка! Некорректный ввод первого числа.")
                            break
                    elif op == "2" :
                        try :
                            num1 = input("Введите гипотенузу (c): ")
                            if num1.lower() == "pi" :
                                num1 = pi
                            elif num1.lower() == "e" or num1.lower() == "е" :
                                num1 = e
                            elif num1.lower() == "y" :
                                num1 = y
                            elif num1.lower() == "дробь" :
                                fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                                num1 = Fraction(fraction_input)
                            elif num1.lower() == "ф" :
                                num1 = (1 + sqrt(5)) / 2
                            else :
                                num1 = float(num1)
                        except ValueError :
                            print("Ошибка! Некорректный ввод первого числа.")
                            break
                        try :
                            num2 = input("Введите высоту: ")
                            if num2.lower() == "pi" :
                                num2 = pi
                            elif num2.lower() == "e" or num2.lower() == "е" :
                                num2 = e
                            elif num2.lower() == "y" :
                                num2 = y
                            elif num2.lower() == "дробь" :
                                fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                                num2 = Fraction(fraction_input)
                            elif num2.lower() == "ф" :
                                num2 = (1 + sqrt(5)) / 2
                            else :
                                num2 = float(num2)
                            print("S прямоугольного треугольника =", (num1 * num2) / 2)
                        except ValueError :
                            print("Ошибка! Некорректный ввод первого числа.")
                            break
                elif op4 == "1" :
                    try :
                        num1 = input("Введите высоту: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num1 = Fraction(fraction_input)
                        elif num1.lower() == "ф" :
                            num1 = (1 + sqrt(5)) / 2
                        else :
                            num1 = float(num1)
                            print("S равностороннего треугольника =", (num1 ** 2) / (sqrt(3)))
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
            elif op == "6" :
                try :
                    num1 = input("Введите длину нижнего основания: ")
                    if num1.lower() == "pi" :
                        num1 = pi
                    elif num1.lower() == "e" or num1.lower() == "е" :
                        num1 = e
                    elif num1.lower() == "y" :
                        num1 = y
                    elif num1.lower() == "дробь" :
                        fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                        num1 = Fraction(fraction_input)
                    elif num1.lower() == "ф" :
                        num1 = (1 + sqrt(5)) / 2
                    else :
                        num1 = float(num1)
                except ValueError :
                    print("Ошибка! Некорректный ввод первого числа.")
                    break
                try :
                    num2 = input("Введите длину верхнего основания: ")
                    if num2.lower() == "pi" :
                        num2 = pi
                    elif num2.lower() == "e" or num2.lower() == "е" :
                        num2 = e
                    elif num2.lower() == "y" :
                        num2 = y
                    elif num2.lower() == "дробь" :
                        fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                        num2 = Fraction(fraction_input)
                    elif num2.lower() == "ф" :
                        num2 = (1 + sqrt(5)) / 2
                    else :
                        num2 = float(num2)
                except ValueError :
                    print("Ошибка! Некорректный ввод первого числа.")
                    break
                try :
                    num3 = input("Введите высоту трапеции: ")
                    if num3.lower() == "pi" :
                        num3 = pi
                    elif num3.lower() == "e" or num3.lower() == "е" :
                        num3 = e
                    elif num3.lower() == "y" :
                        num3 = y
                    elif num3.lower() == "дробь" :
                        fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                        num3 = Fraction(fraction_input)
                    elif num3.lower() == "ф" :
                        num3 = (1 + sqrt(5)) / 2
                    else :
                        num3 = float(num3)
                        print("S трапеции =", (num1 + num2) / 2 * num3)
                except ValueError :
                    print("Ошибка! Некорректный ввод первого числа.")
                    break
                else :
                    print("Выберите из списка")
            elif op == "7" :
                op3 = input("1)через сторону и высоту, 2)через сторону и угол, 3)через диагонали: ")
                if op3 == "1" :
                    try :
                        num1 = input("Введите длину основания: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num1 = Fraction(fraction_input)
                        elif num2.lower() == "ф" :
                            num2 = (1 + sqrt(5)) / 2
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите высоту параллелограмма: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input)
                        elif num2.lower() == "ф" :
                            num2 = (1 + sqrt(5)) / 2
                        else :
                            num2 = float(num2)
                            print("S параллелограмма =", num1 * num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    else :
                        print("Выберите из списка")
                elif op3 == "2" :
                    try :
                        num1 = input("Введите длину 1 стороны: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num1 = Fraction(fraction_input)
                        elif num1.lower() == "ф" :
                            num1 = (1 + sqrt(5)) / 2
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите длину 2 стороны: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input)
                        elif num2.lower() == "ф" :
                            num2 = (1 + sqrt(5)) / 2
                        else :
                            num2 = float(num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num3 = input("Введите угол между сторонами a и b: ")
                        if num3.lower() == "pi" :
                            num3 = pi
                        elif num3.lower() == "e" or num3.lower() == "е" :
                            num3 = e
                        elif num3.lower() == "y" :
                            num3 = y
                        elif num3.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num3 = Fraction(fraction_input)
                        elif num3.lower() == "ф" :
                            num3 = (1 + sqrt(5)) / 2
                        else :
                            num3 = radians(float(num3))
                            print("S параллелограмма =", num1 * num2 * (sin(num3)))
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    else :
                        print("Выберите из списка")
                elif op3 == "3" :
                    import math
                    grad = math.degrees
                    try :
                        num1 = input("Введите длину большей диагонали: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num1 = Fraction(fraction_input)
                        elif num1.lower() == "ф" :
                            num1 = (1 + sqrt(5)) / 2
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите длину меньшей диагонали: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input)
                        elif num2.lower() == "ф" :
                            num2 = (1 + sqrt(5)) / 2
                        else :
                            num2 = float(num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num3 = input("Введите угол между диагоналями: ")
                        if num3.lower() == "pi" :
                            num3 = pi
                        elif num3.lower() == "e" or num3.lower() == "е" :
                            num3 = e
                        elif num3.lower() == "y" :
                            num3 = y
                        elif num3.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num3 = Fraction(fraction_input)
                        elif num3.lower() == "ф" :
                            num3 = (1 + sqrt(5)) / 2
                        else :
                            num3 = float(num3)
                            print("S параллелограмма =", 0.5 * num1 * num2 * (sin(rad(num3))))
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    else :
                        print("Выберите из списка")
            elif op == "8" :
                import math
                tan = math.tan
                pi = math.pi
                try :
                    num1 = input("Введите число вершин: ")
                    if num1.lower() == "pi" :
                        num1 = pi
                    elif num1.lower() == "e" or num1.lower() == "е" :
                        num1 = e
                    elif num1.lower() == "y" :
                        num1 = y
                    elif num1.lower() == "дробь" :
                        fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                        num1 = Fraction(fraction_input)
                        
                    else :
                        num1 = float(num1)
                except ValueError :
                    print("Ошибка! Некорректный ввод первого числа.")
                    break
                try :
                    num2 = input("Введите количество рёбер: ")
                    if num2.lower() == "pi" :
                        num2 = pi
                    elif num2.lower() == "e" or num2.lower() == "е" :
                        num2 = e
                    elif num2.lower() == "y" :
                        num2 = y
                    elif num2.lower() == "дробь" :
                        fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                        num2 = Fraction(fraction_input)
                    else :
                        num2 = float(num2)
                    print("S многоугольника =", num1 * num2 ** 2 / (4 * tan(pi / num1)))
                except ValueError :
                    print("Ошибка! Некорректный ввод первого числа.")
                    break

    def block_progressive() :
        op2 = input("1)арифметическая прогрессия 2)геометрическая прогрессия 3)гармоническая прогрессия: ")
        if op2 == "1" :
            a1 = int(input("Введите первый номер члена a1: "))
            d = int(input("Введите разность ар.пр.: "))
            k = int(input("Введите последний номер члена k: "))
            result = ""
            for i in range(k) :
                result += str(a1 + i * d) + " "
            print("Все члены прогрессии:", result)
        elif op2 == "2" :
            b1 = get_float("Введите первый член прогрессии: ")
            q = get_float("Введите знаменатель г.пр.: ")
            n = get_float("Введите номер члена: ")
            bn = b1 * (q ** (n - 1))
            print(bn)
        elif op2 == "3" :
            n = int(input("Введите количество элементов в прогрессии: "))
            print("Гармоническая прогрессия построена ↓")
            for i in range(1, n + 1) :
                print(1 / i)
    def block_addition() :
        while True :
            try :
                op3 = input("Выберите операцию: 1) x̄ - (среднее арифметическое)  2) |a| (модуль)  3) противоположное число  4) n√: ")
            except ValueError :
                print("Ошибка ввода. Пожалуйста, выберите операцию из списка (1, 2, 3 или 4).")
                continue
            if op3 in ["1", "2", "3", "4"] :
                break
            else :
                print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")
        if op3 == "1" :
            total = 0
            while True :
                try :
                    num1 = int(input("Введите количество чисел: "))
                    break
                except ValueError :
                    print("Ошибка введите ЦЕЛОЕ число")
            for i in range(num1) :
                try :
                    num2 = get_float("Введите число, pi, e, y или 'дробь': ")
                except ValueError :
                    print("Ошибка ввода первого числа!")
                    exit()
                total += num2
            print("Среднее арифметическое =", total / num1)
        elif op3 == "2" :
            num = get_float("Введите число: ")
            print(abs(num))
        elif op3 == "3" :
            num = get_float("Введите число: ")
            if num > 0 :
                print("-", num, sep="")
            elif num < 0 :
                print(num * -2 - -num)
            elif num == 0 :
                print("0 не имеет противоположного числа!")
        elif op3 == "4" :
            num1 = get_float("Введите степень корня: ")
            num2 = get_float("Введите число из которого извлекаем корень: ")
            print(num2 ** (1 / num1))
    def block_percentage():
        op0 = input("Выберет 1)процент от числа  2)прибавить процент к числу  3)вычесть процент от числа  4)сколько составляет одно от другого: ")
        if op0 == "1" :
            percent = get_float("Введите число: ")
            value = get_float("Введите процент: ")
            result = (value * percent) / 100
            print(result)
        elif op0 == "2" :
            price = get_float("Введите число: ")
            tax = get_float("Введите процент: ")
            total = price * (1 + tax / 100)
            print(total)
        elif op0 == "3" :
            price = get_float("Введите число: ")
            tax = get_float("Введите процент: ")
            total = price * (1 - tax / 100)
            print(total)
        elif op0 == "4" :
            num1 = get_float("Введите изначальное число: ")
            num2 = get_float("Введите другое число: ")
            total = (num1 / num2) * 100
            print(total)
    def block_sistem():
        def decimal_to_base(decimal_num, base) :
            """
            Конвертирует десятичное число в строку в указанной системе счисления.
            """
            if decimal_num == 0 :
                return '0'
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while decimal_num > 0 :
                remainder = decimal_num % base
                result = digits[remainder] + result
                decimal_num //= base
            return result

        def base_to_decimal(num_str, base) :
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            decimal_num = 0
            power = 0
            for digit in reversed(num_str) :
                digit_value = digits.index(digit.upper())
                if digit_value >= base :
                    raise ValueError(f"Символ '{digit.upper()}' некорректен для основания {base}")
                decimal_num += digit_value * (base ** power)
                power += 1
            return decimal_num

        def display_menu() :
            print("1) Перевести из десятичной системы в другую")
            print("2) Перевести из другой системы счисления в десятичную")

        def main() :
            while True :
                display_menu()
                choice = input("Введите номер действия: ")

                if choice == '1' :
                    try :
                        decimal_num_input = input("Введите десятичное число: ")
                        decimal_num = int(decimal_num_input)
                        base_input = input("Введите целевую систему счисления (от 2 до 36): ")
                        base = int(base_input)

                        if 2 <= base <= 36 :
                            result = decimal_to_base(decimal_num, base)
                            print(f"Результат: {result}")
                        else :
                            print("Ошибка: Некорректная база. Допустимы значения от 2 до 36.")
                    except ValueError :
                        print("Ошибка ввода. Пожалуйста, введите корректное десятичное число и базу.")
                    except Exception as e :
                        print(f"Произошла непредвиденная ошибка: {e}")

                elif choice == '2' :
                    try :
                        num_str = input("Введите число (используйте 0-9 и A-Z): ")
                        base_input = input("Введите систему счисления исходного числа (от 2 до 36): ")
                        base = int(base_input)

                        if 2 <= base <= 36 :
                            result = base_to_decimal(num_str, base)
                            print(f"Результат (десятичное): {result}")
                        else :
                            print("Ошибка: Некорректная база. Допустимы значения от 2 до 36.")
                    except ValueError as ve :
                        print(f"Ошибка: {ve}")
                    except Exception as e :
                        print(f"Произошла ошибка при переводе: {e}. Убедитесь, что символы числа соответствуют указанной базе.")
                else :
                    print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")
        main()
    print("Здравствуйте, вас приветствует умный калькулятор")
    while True :
            print("_____________________Меню_______________________")
            print("1) классика")
            print("2) тригонометрия")
            print("3) сравнение")
            print("4) проверка кратности")
            print("5) S - (площадь)")
            print("6) дополнительно")
            print("7) прогрессии")
            print("8) проценты")
            print("9) Перевод в другие системы счисления")
            print("10) Выход")
            import time
            sin = math.sin
            tan = math.tan
            pi = math.pi
            e = math.e
            Fraction = fractions.Fraction
            factorial = math.factorial
            sqrt = math.sqrt
            pow = math.pow
            cbrt = math.cbrt
            gcd = math.gcd
            y = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495146314472498070824809605040144865428362241739976449235362535003337429373377376739427925952582470949160087352039481656708532331517766115286211995015079847937450857057400299213547861466940296043254215190587755352673313992540129674205137541395491116851028079842348775872050384310939973613725530608893312676001724795378367592713515772261027349291394079843010341777177808815495706610750101619166334015227893586796549725203621287922655595366962817638879272680132431010476505963703947394957638906572967929601009015125195950922243501409349871228247949747195646976318506676129063811051824197444867836380861749455169892792301877391072945781554316005002182844096053772434203285478367015177394398700302370339518328690001558193988042707411542227819716523011073565833967348717650491941812300040654693142999297779569303100503086303418569803231083691640025892970890985486825777364288253954925873629596133298574739302
            vibor = input("Выберете функцию из списка: ")
            if vibor == "1":
                block_classic()
            elif vibor == "2":
                block_trigonom()
            elif vibor == "3":
                block_compare()
            elif vibor == "4":
                multiplicity()
            elif vibor == "5":
                block_square()
            elif vibor == "6":
                block_addition()
            elif vibor == "7":
                blok_progressive()
            elif vibor == "8":
                block_percentage()
            elif vibor == "9":
                block_sistem()
            elif vibor == "10":
                print("Спасибо за пользование калькулятором! До свидания")
                break
            else:
                print("Выберете функцию из списка")
                break
            time.sleep(2)
elif tx == "2":

    import math
    import fractions

    def get_float(input_text) :
        while True :
            input_string = input(input_text)
            try :
                if input_string.lower() == "pi" :
                    result = pi
                elif input_string.lower() == "e" or input_string.lower() == "е" :
                    result = e
                elif input_string.lower() == "y" :
                    result = y
                elif input_string.lower() == "fraction" :
                    fraction_input = input("Enter the numerator/denominator format: ")
                    result = Fraction(fraction_input)
                else :
                    result = float(input_string)
                break
            except ValueError :
                print("Error! Enter the number")

        return result


    def block_trigonom() :
        import math
        from math import pi, sin, cos, tan, degrees, radians, asin, acos, atan

        def get_float(prompt) :
            """
            Prompts the user for input and attempts to convert it to a float.
            Handles 'pi', 'e', and 'y' (interpreted after user's input of 'y'/'n' for continuation) as special cases.
            """
            while True :
                value_str = input(prompt).lower()
                try :
                    if value_str == "pi" :
                        return pi
                    elif value_str == "e" :
                        return math.e
                    elif value_str == "y" :  # This case might need adjustment based on context
                        return "y"  # Special token for "yes"
                    else :
                        return float(value_str)
                except ValueError :
                    print("Invalid input. Please enter a number, 'pi', 'e', or 'y'.")

        while True :
            num_input = get_float("Enter the number, 'pi', 'e', or 'y': ")  # Get the number or constant
            operation = input(
                "Choose an operation (sin, cos, tg, ctg, sec, csc, asin, acos, atg, actg, asec, acsc): ").lower()
            gr = input("Specify angle unit (degrees or radians): ").lower()

            valid_operations = ["sin", "cos", "tg", "ctg", "sec", "csc", "asin", "acos", "atg", "actg", "asec", "acsc"]

            if operation not in valid_operations :
                print("Error! Select a function from the list!")
                break

            if gr == "degrees" :
                # If the user enters a number and specifies 'degrees', we interpret the input as degrees.
                # For calculations, this value needs to be converted to radians.
                # The output can then be displayed in degrees or converted back to degrees.

                angle_in_degrees = num_input
                # Ensure input is a number before converting
                if isinstance(angle_in_degrees, (int, float)) :
                    angle_in_radians = radians(angle_in_degrees)  # Convert degrees to radians for calculations

                    if operation == "sin" :
                        result_rad = sin(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_degrees}° = {result_deg} °")  # Result in degrees is just conversio
                    elif operation == "cos" :
                        result_rad = cos(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_degrees}° = {result_deg} °")
                    elif operation == "tg" :
                        result_rad = tan(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_degrees}° = {result_deg} °")
                    elif operation == "ctg" :
                        result_rad = 1 / tan(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_degrees}° = {result_deg} °")
                    elif operation == "sec" :
                        result_rad = 1 / cos(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_degrees}° = {result_deg} °")
                    elif operation == "csc" :
                        result_rad = 1 / sin(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_degrees}° = {result_deg} °")

                    # Inverse trigonometric functions return angles.
                    # When 'degrees' is specified, we expect the input to be degrees of the *argument* for inverse functions.
                    # The output of inverse functions should also be in degrees as requested by the unit input.
                    elif operation == "asin" :
                        if not -1 <= angle_in_degrees <= 1 :  # Argument for inverse functions is [-1, 1]
                            print("Error: You can only find the arcsine of a value between -1 and 1.")
                        else :
                            result_rad = asin(angle_in_degrees)  # Calculate using the input as a value
                            result_deg = degrees(result_rad)
                            print(f"asin({angle_in_degrees}) = {result_deg}°")
                    elif operation == "acos" :
                        if not -1 <= angle_in_degrees <= 1 :
                            print("Error: You can only find the arccosine of a value between -1 and 1.")
                        else :
                            result_rad = acos(angle_in_degrees)
                            result_deg = degrees(result_rad)
                            print(f"acos({angle_in_degrees}) = {result_deg}°")
                    elif operation == "atg" :
                        result_rad = atan(angle_in_degrees)
                        result_deg = degrees(result_rad)
                        print(f"atan({angle_in_degrees}) = {result_deg}°")
                    elif operation == "actg" :
                        if angle_in_degrees > 0 :
                            result_rad = atan(1 / angle_in_degrees)
                        elif angle_in_degrees < 0 :
                            result_rad = atan(1 / angle_in_degrees) + pi
                        else :  # angle_in_degrees == 0
                            result_rad = pi / 2
                        result_deg = degrees(result_rad)
                        print(f"actg({angle_in_degrees}) = {result_deg}°")
                    elif operation == "asec" :
                        # Arccosecant expects an input value for which to find the angle.
                        # The calculation uses 1/input for acos.
                        if not abs(angle_in_degrees) >= 1 :
                            print("Error: Invalid input for asec. Input must be >= 1 or <= -1.")
                        else :
                            result_rad = acos(1 / angle_in_degrees)
                            result_deg = degrees(result_rad)
                            print(f"asec({angle_in_degrees}) = {result_deg}°")
                    elif operation == "acsc" :
                        # Arccosecant expects an input value for which to find the angle.
                        # The calculation uses 1/input for asin.
                        if not abs(angle_in_degrees) >= 1 :
                            print("Error: Invalid input for acsc. Input must be >= 1 or <= -1.")
                        else :
                            result_rad = asin(1 / angle_in_degrees)
                            result_deg = degrees(result_rad)
                            print(f"acsc({angle_in_degrees}) = {result_deg}°")
                else :
                    print("Error: For 'degrees' mode, please enter a numerical value for calculations.")


            elif gr == "radians" :
                # If the user enters a number and specifies 'radians', we use the input directly
                # as it's already in the format that math functions expect.
                # We then convert the output to degrees for display.

                angle_in_radians = num_input  # Use the entered number as radians

                if isinstance(angle_in_radians, (int, float)) :
                    if operation == "sin" :
                        result_rad = sin(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_radians} radians = {result_deg}°")
                    elif operation == "cos" :
                        result_rad = cos(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_radians} radians = {result_deg}°")
                    elif operation == "tg" :
                        result_rad = tan(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_radians} radians = {result_deg}°")
                    elif operation == "ctg" :
                        result_rad = 1 / tan(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_radians} radians = {result_deg}°")
                    elif operation == "sec" :
                        result_rad = 1 / cos(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_radians} radians = {result_deg}°")
                    elif operation == "csc" :
                        result_rad = 1 / sin(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"{angle_in_radians} radians = {result_deg}°")

                    # Inverse trigonometric functions take values and return angles.
                    # When 'radians' is specified for the unit, we expect the input value for inverse functions.
                    # The output angle will be in radians and can be converted to degrees.
                    elif operation == "asin" :
                        if not -1 <= angle_in_radians <= 1 :  # Argument for inverse functions is [-1, 1]
                            print("Error: You can only find the arcsine of a value between -1 and 1.")
                        else :
                            result_rad = asin(angle_in_radians)  # The input is the value, result is an angle in radians
                            result_deg = degrees(result_rad)
                            print(f"asin({angle_in_radians}) = {result_rad} radians")
                    elif operation == "acos" :
                        if not -1 <= angle_in_radians <= 1 :
                            print("Error: You can only find the arccosine of a value between -1 and 1.")
                        else :
                            result_rad = acos(angle_in_radians)
                            result_deg = degrees(result_rad)
                            print(f"acos({angle_in_radians}) = {result_rad} radians")
                    elif operation == "atg" :
                        result_rad = atan(angle_in_radians)
                        result_deg = degrees(result_rad)
                        print(f"atan({angle_in_radians}) = {result_rad} radians")
                    elif operation == "actg" :
                        if angle_in_radians > 0 :
                            result_rad = atan(1 / angle_in_radians)
                        elif angle_in_radians < 0 :
                            result_rad = atan(1 / angle_in_radians) + pi
                        else :  # angle_in_radians == 0
                            result_rad = pi / 2
                        result_deg = degrees(result_rad)
                        print(f"actg({angle_in_radians}) = {result_rad} radians")
                    elif operation == "asec" :
                        if not abs(angle_in_radians) >= 1 :
                            print("Error: Invalid input for asec. Input must be >= 1 or <= -1.")
                        else :
                            result_rad = acos(1 / angle_in_radians)
                            result_deg = degrees(result_rad)
                            print(f"asec({angle_in_radians}) = {result_rad} radians")
                    elif operation == "acsc" :
                        if not abs(angle_in_radians) >= 1 :
                            print("Error: Invalid input for acsc. Input must be >= 1 or <= -1.")
                        else :
                            result_rad = asin(1 / angle_in_radians)
                            result_deg = degrees(result_rad)
                            print(f"acsc({angle_in_radians}) = {result_rad} radians")
                else :
                    print("Error: For 'radians' mode, please enter a numerical value for calculations.")

            else :
                print("Error! Choose the angle measure of the angle (degrees or radians)!")
                break

            # Ask the user if they wish to continue
            cont = input("Continue? (y/n): ")
            if cont.lower() != 'y' :
                break

    def block_classic() :
        import functools
        import math
        pi = math.pi
        e = math.e
        Fraction = fractions.Fraction
        sqrt = math.sqrt
        cbrt = math.cbrt
        gcd = math.gcd
        log = math.log
        pow = math.pow
        factorial = math.factorial
        y = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495146314472498070824809605040144865428362241739976449235362535003337429373377376739427925952582470949160087352039481656708532331517766115286211995015079847937450857057400299213547861466940296043254215190587755352673313992540129674205137541395491116851028079842348775872050384310939973613725530608893312676001724795378367592713515772261027349291394079843010341777177808815495706610750101619166334015227893586796549725203621287922655595366962817638879272680132431010476505963703947394957638906572967929601009015125195950922243501409349871228247949747195646976318506676129063811051824197444867836380861749455169892792301877391072945781554316005002182844096053772434203285478367015177394398700302370339518328690001558193988042707411542227819716523011073565833967348717650491941812300040654693142999297779569303100503086303418569803231083691640025892970890985486825777364288253954925873629596133298574739302
        while True :
                num1 = get_float("Enter the first number or pi or e or y or fraction: ")
                op = input("Enter the operation 1)+, 2)-, 3)*, 4)/, 5)n!, 6)2√, 7)3√, 8)**, 9)НОД, 10)НОК, 11)ost, 12)//, 13)!n, 14) log, 15) log x к y, 16) a⇈b (тетрация), 17)a**2 - b**2: ")
                if op == "6" :
                    print(sqrt(num1))
                elif op == "7" :
                    print(cbrt(num1))
                elif op == "14" :
                    print(log(num1))
                elif op == "13" :
                    result = 1
                    if num1 == 0 :
                        print("1")
                    elif num1 < 0 :
                        print("The subfactorial of negatives is not defined!")
                    else :
                        for i in range(1, int(num1) + 1) :
                            result *= i
                    print(round(result / e))
                elif op == "5" :
                    result = 1
                    if num1 == 0 :
                        print("1")
                    elif num1 < 0 :
                        print("The factorial of negatives is not defined!")
                    else :
                        for i in range(1, int(num1) + 1) :
                            result *= i
                        print(result)
                else:
                    num2 = get_float("Enter the second number or pi or e or y or fraction: ")
                    if op == '1' :
                        print(num1 + num2)
                    elif op == "15" :
                        print(log(num1, num2))
                    elif op == '2' :
                        print(num1 - num2)
                    elif op == '3' :
                        print(num1 * num2)
                    elif op == '8' :
                        print(num1 ** num2)
                    elif op == '16' :
                        print(pow(num1, (pow(num1, num2))))
                    elif op == '17' :
                        print(f"{num1} ** 2 - {num2} ** 2 = ({num1} - {num2}) * ({num1} + {num2}) =", (num1 - num2) * (num1 + num2))
                    elif op == '12' :
                        try :
                            print(num1 // num2)
                        except ZeroDivisionError :
                            print("Error! Division by zero!")
                    elif op == "11" :
                        try :
                            print(f"{num1 // num2} whole number {num1 % num2} remainder")
                        except ZeroDivisionError :
                            print("Error! Division by zero!")
                    elif op == "9" :
                        num1 = int(num1)
                        num2 = int(num2)
                        nod = gcd(num1, num2)
                        if num1 == 0 and num2 == 0 :
                            print("No certain")
                        else :
                            print(nod)
                    elif op == "10" :
                        num1 = int(num1)
                        num2 = int(num2)
                        nok = abs(num1 * num2) // gcd(num1, num2)
                        if num1 == 0 and num2 == 0 :
                            print("No certain")
                        else :
                            print(nok)
                    elif op == '4' :
                        try :
                            print(num1 / num2)
                        except ZeroDivisionError :
                            print("Error! Division by zero!")
                    else:
                        print("Unacceptable operation!")


    def block_compare() :
        global factorial, pi, e, Fraction, sqrt, pow, cbrt, y, num1, num2, op
        factorial = math.factorial
        pi = math.pi
        e = math.e
        Fraction = fractions.Fraction
        sqrt = math.sqrt
        pow = math.pow
        cbrt = math.cbrt
        y = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495146314472498070824809605040144865428362241739976449235362535003337429373377376739427925952582470949160087352039481656708532331517766115286211995015079847937450857057400299213547861466940296043254215190587755352673313992540129674205137541395491116851028079842348775872050384310939973613725530608893312676001724795378367592713515772261027349291394079843010341777177808815495706610750101619166334015227893586796549725203621287922655595366962817638879272680132431010476505963703947394957638906572967929601009015125195950922243501409349871228247949747195646976318506676129063811051824197444867836380861749455169892792301877391072945781554316005002182844096053772434203285478367015177394398700302370339518328690001558193988042707411542227819716523011073565833967348717650491941812300040654693142999297779569303100503086303418569803231083691640025892970890985486825777364288253954925873629596133298574739302
        num1 = get_float("Enter the first number, pi, e, y or 'fraction': ")
        num2 = get_float("Enter the second number, pi, e, y or 'fraction': ")
        op = input("Enter operation 1)<, 2)>, 3)=: ")
        if op == "1" :
            if num1 < num2 :
                print(num1, "less than", num2)
            else :
                print("inequalities aren't correct")
        elif op == "2" :
            if num1 > num2 :
                print(num1, "more than", num2)
            else :
                print("inequalities aren't correct")
        elif op == "3" :
            if num1 == num2 :
                print("Equality is equal")
            else :
                print("Enter operation")


    def multiplicity() :
        while True :
            try :
                num1_input = get_float("Enter the number, pi, e, y: ")
            except ValueError :
                print("Error! Incorrect number input!")
                continue

            try :
                num2_input = get_float("Enter the number that will be multiple or not, pi, e, y: ")
            except ValueError :
                print("Error! Incorrect number input!")
                continue
            if num2_input == 0 :
                print("Error: Division by zero!")
                continue
            if num1_input % num2_input == 0 :
                print("multiply")
            else :
                print("not multiply")


    def block_square() :
        while True :
            op = input(
                "1)Rectangle, 2)Square, 3)Circle, 4)Oval(ellipse), 5)Triangle, 6)Trapezoid, 7)Parallelogram, 8)Polygon: ")
            if op == "1" :
                num1 = get_float("Enter number A, pi, e, y or 'fraction': ")
                num2 = get_float("Enter number B, pi, e, y or 'fraction': ")
                print("Rectangle area =", num1 * num2)
            elif op == "2" :
                num1 = get_float("Enter number, pi, e, y or 'fraction': ")
                print("Square area =", num1 * num1)
            elif op == "3" :
                num1 = input("Enter r (circle radius) or d (circle diameter): ")
                if num1 == "d" :
                    num2 = get_float("Enter number: ") / 2
                    print("Circle area =", pi * pow(num2, 2))
                elif num1 == "r" :
                    num2 = get_float("Enter number: ")
                    print("Circle area =", pi * pow(num2, 2))
            elif op == "4" :
                op1 = input("Enter d (axis length) or r (semi-axis length): ")
                if op1 == "r" :
                    try :
                        num1 = get_float("Enter semi-axis length a: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "fraction" :
                            fraction_input = input("Enter in format 'numerator/denominator': ")
                            num1 = Fraction(fraction_input)
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Error! Invalid first number input.")
                        break
                    try :
                        num2 = input("Enter semi-axis length b: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "fraction" :
                            fraction_input = input("Enter in format 'numerator/denominator': ")
                            num2 = Fraction(fraction_input)
                        else :
                            num2 = float(num2)
                            print("Ellipse area =", pi * num1 * num2)
                    except ValueError :
                        print("Error! Invalid first number input.")
                        break
                    else :
                        print("Choose from the list")
                elif op1 == "d" :
                    try :
                        num1 = input("Enter axis length a: ")
                        if num1.lower() == "pi" :
                            num1 = pi / 2
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e / 2
                        elif num1.lower() == "y" :
                            num1 = y / 2
                        elif num1.lower() == "fraction" :
                            fraction_input = input("Enter in format 'numerator/denominator': ")
                            num1 = Fraction(fraction_input) / 2
                        else :
                            num1 = float(num1) / 2
                    except ValueError :
                        print("Error! Invalid first number input.")
                        break
                    try :
                        num2 = input("Enter axis length b: ")
                        if num2.lower() == "pi" :
                            num2 = pi / 2
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e / 2
                        elif num2.lower() == "y" :
                            num2 = y / 2
                        elif num2.lower() == "fraction" :
                            fraction_input = input("Enter in format 'numerator/denominator': ")
                            num2 = Fraction(fraction_input) / 2
                        else :
                            num2 = float(num2) / 2
                            print("Ellipse area =", pi * num1 * num2)
                    except ValueError :
                        print("Error! Invalid first number input.")
                        break
                    else :
                        print("Choose from the list")
            elif op == "5" :
                op4 = input(
                    "1)Equilateral, 2)Isosceles or acute or obtuse or scalene, 3)Right: ")
                if op4 == "2" :
                    try :
                        num1 = input("Enter base length: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "fraction" :
                            fraction_input = input("Enter in format 'numerator/denominator': ")
                            num1 = Fraction(fraction_input)
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Error! Invalid first number input.")
                        break
                    try :
                        num2 = input("Enter triangle height: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "fraction" :
                            fraction_input = input("Enter in format 'numerator/denominator': ")
                            num2 = Fraction(fraction_input)
                        else :
                            num2 = float(num2)
                            print("Triangle area =", 0.5 * num1 * num2)
                    except ValueError :
                        print("Error! Invalid first number input.")
                        break
                elif op4 == "3" :
                    op = input("1)via sides, 2)via hypotenuse: ")
                    if op == "1" :
                        try :
                            num1 = input("Enter base length: ")
                            if num1.lower() == "pi" :
                                num1 = pi
                            elif num1.lower() == "e" or num1.lower() == "е" :
                                num1 = e
                            elif num1.lower() == "y" :
                                num1 = y
                            elif num1.lower() == "fraction" :
                                fraction_input = input("Enter in format 'numerator/denominator': ")
                                num1 = Fraction(fraction_input)
                            else :
                                num1 = float(num1)
                        except ValueError :
                            print("Error! Invalid first number input.")
                            break
                        try :
                            num2 = input("Enter height: ")
                            if num2.lower() == "pi" :
                                num2 = pi
                            elif num2.lower() == "e" or num2.lower() == "е" :
                                num2 = e
                            elif num2.lower() == "y" :
                                num2 = y
                            elif num2.lower() == "fraction" :
                                fraction_input = input("Enter in format 'numerator/denominator': ")
                                num2 = Fraction(fraction_input)
                            else :
                                num2 = float(num2)
                            print("Right triangle area =", (num1 * num2) / 2)
                        except ValueError :
                            print("Error! Invalid first number input.")
                            break
                    elif op == "2" :
                        try :
                            num1 = input("Enter hypotenuse (c): ")
                            if num1.lower() == "pi" :
                                num1 = pi
                            elif num1.lower() == "e" or num1.lower() == "е" :
                                num1 = e
                            elif num1.lower() == "y" :
                                num1 = y
                            elif num1.lower() == "fraction" :
                                fraction_input = input("Enter in format 'numerator/denominator': ")
                                num1 = Fraction(fraction_input)
                            else :
                                num1 = float(num1)
                        except ValueError :
                            print("Error! Invalid first number input.")
                            break
                        try :
                            num2 = input("Enter height: ")
                            if num2.lower() == "pi" :
                                num2 = pi
                            elif num2.lower() == "e" or num2.lower() == "е" :
                                num2 = e
                            elif num2.lower() == "y" :
                                num2 = y
                            elif num2.lower() == "fraction" :
                                fraction_input = input("Enter in format 'numerator/denominator': ")
                                num2 = Fraction(fraction_input)
                            else :
                                num2 = float(num2)
                            print("Right triangle area =", (num1 * num2) / 2)
                        except ValueError :
                            print("Error! Invalid first number input.")
                            break
                    elif op4 == "1":
                            try :
                                num1 = input("Enter height: ")
                                if num1.lower() == "pi" :
                                    num1 = pi
                                elif num1.lower() == "e" or num1.lower() == "е" :
                                    num1 = e
                                elif num1.lower() == "y" :
                                    num1 = y
                                elif num1.lower() == "fraction" :
                                    fraction_input = input("Enter in format 'numerator/denominator': ")
                                    num1 = Fraction(fraction_input)
                                else :
                                    num1 = float(num1)
                                    print("Equilateral triangle area =", (num1 ** 2) / (sqrt(3)))
                            except ValueError :
                                print("Error! Invalid first number input.")
                                break
                    elif op == "6":
                            try :
                                num1 = input("Enter lower base length: ")
                                if num1.lower() == "pi" :
                                    num1 = pi
                                elif num1.lower() == "e" or num1.lower() == "е":
                                    num1 = e
                                elif num1.lower() == "y":
                                    num1 = y
                                elif num1.lower() == "fraction":
                                    fraction_input = input("Enter in format 'numerator/denominator': ")
                                    num1 = Fraction(fraction_input)
                                else :
                                    num1 = float(num1)
                            except ValueError :
                                print("Error! Invalid first number input.")
                                break
                            try:
                                num2 = input("Enter upper base length: ")
                                if num2.lower() == "pi" :
                                    num2 = pi
                                elif num2.lower() == "e" or num2.lower() == "е" :
                                    num2 = e
                                elif num2.lower() == "y" :
                                    num2 = y
                                elif num2.lower() == "fraction" :
                                    fraction_input = input("Enter in format 'numerator/denominator': ")
                                    num2 = Fraction(fraction_input)
                                else :
                                    num2 = float(num2)
                            except ValueError :
                                print("Error! Invalid first number input.")
                                break
                            try :
                                num3 = input("Enter trapezoid height: ")
                                if num3.lower() == "pi" :
                                    num3 = pi
                                elif num3.lower() == "e" or num3.lower() == "е" :
                                    num3 = e
                                elif num3.lower() == "y" :
                                    num3 = y
                                elif num3.lower() == "fraction" :
                                    fraction_input = input("Enter in format 'numerator/denominator': ")
                                    num3 = Fraction(fraction_input)
                                else :
                                    num3 = float(num3)
                                    print("Trapezoid area =", (num1 + num2) / 2 * num3)
                            except ValueError :
                                print("Error! Invalid first number input.")
                                break
                            else :
                                print("Choose from the list")
                    elif op == "7" :
                        op3 = input("1)via side and height, 2)via side and angle, 3)via diagonals: ")
                        if op3 == "1" :
                            try :
                                num1 = input("Enter base length: ")
                                if num1.lower() == "pi" :
                                    num1 = pi
                                elif num1.lower() == "e" or num1.lower() == "е" :
                                    num1 = e
                                elif num1.lower() == "y" :
                                    num1 = y
                                elif num1.lower() == "fraction" :
                                    fraction_input = input("Enter in format 'numerator/denominator': ")
                                    num1 = Fraction(fraction_input)
                                else :
                                    num1 = float(num1)
                            except ValueError :
                                print("Error! Invalid first number input.")
                                break
                            try :
                                num2 = input("Enter parallelogram height: ")
                                if num2.lower() == "pi" :
                                    num2 = pi
                                elif num2.lower() == "e" or num2.lower() == "е" :
                                    num2 = e
                                elif num2.lower() == "y" :
                                    num2 = y
                                elif num2.lower() == "fraction" :
                                    fraction_input = input("Enter in format 'numerator/denominator': ")
                                    num2 = Fraction(fraction_input)
                                else :
                                    num2 = float(num2)
                                    print("Parallelogram area =", num1 * num2)
                            except ValueError :
                                print("Error! Invalid first number input.")
                                break
                            else :
                                print("Choose from the list")
            elif op3 == "2" :
                    try :
                        num1 = input("Введите длину 1 стороны: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num1 = Fraction(fraction_input)
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите длину 2 стороны: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input)
                        else :
                            num2 = float(num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num3 = input("Введите угол между сторонами a и b: ")
                        if num3.lower() == "pi" :
                            num3 = pi
                        elif num3.lower() == "e" or num3.lower() == "е" :
                            num3 = e
                        elif num3.lower() == "y" :
                            num3 = y
                        elif num3.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num3 = Fraction(fraction_input)
                        else :
                            num3 = math.radians(float(num3))
                            print("S параллелограмма =", num1 * num2 * (sin(num3)))
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    else :
                        print("Выберите из списка")
            elif op3 == "3" :
                    import math
                    grad = math.degrees
                    try :
                        num1 = input("Введите длину большей диагонали: ")
                        if num1.lower() == "pi" :
                            num1 = pi
                        elif num1.lower() == "e" or num1.lower() == "е" :
                            num1 = e
                        elif num1.lower() == "y" :
                            num1 = y
                        elif num1.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num1 = Fraction(fraction_input)
                        else :
                            num1 = float(num1)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num2 = input("Введите длину меньшей диагонали: ")
                        if num2.lower() == "pi" :
                            num2 = pi
                        elif num2.lower() == "e" or num2.lower() == "е" :
                            num2 = e
                        elif num2.lower() == "y" :
                            num2 = y
                        elif num2.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num2 = Fraction(fraction_input)
                        else :
                            num2 = float(num2)
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    try :
                        num3 = input("Введите угол между диагоналями: ")
                        if num3.lower() == "pi" :
                            num3 = pi
                        elif num3.lower() == "e" or num3.lower() == "е" :
                            num3 = e
                        elif num3.lower() == "y" :
                            num3 = y
                        elif num3.lower() == "дробь" :
                            fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                            num3 = Fraction(fraction_input)
                        else :
                            num3 = float(num3)
                            print("S параллелограмма =", 0.5 * num1 * num2 * (sin(rad(num3))))
                    except ValueError :
                        print("Ошибка! Некорректный ввод первого числа.")
                        break
                    else :
                        print("Выберите из списка")
            elif op == "8" :
                import math
                tan = math.tan
                pi = math.pi
                try :
                    num1 = input("Введите число вершин: ")
                    if num1.lower() == "pi" :
                        num1 = pi
                    elif num1.lower() == "e" or num1.lower() == "е" :
                        num1 = e
                    elif num1.lower() == "y" :
                        num1 = y
                    elif num1.lower() == "дробь" :
                        fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                        num1 = Fraction(fraction_input)
                    else :
                        num1 = float(num1)
                except ValueError :
                    print("Ошибка! Некорректный ввод первого числа.")
                    break
                try :
                    num2 = input("Введите количество рёбер: ")
                    if num2.lower() == "pi" :
                        num2 = pi
                    elif num2.lower() == "e" or num2.lower() == "е" :
                        num2 = e
                    elif num2.lower() == "y" :
                        num2 = y
                    elif num2.lower() == "дробь" :
                        fraction_input = input("Введите в формате 'числитель/знаменатель': ")
                        num2 = Fraction(fraction_input)
                    else :
                        num2 = float(num2)
                    print("S многоугольника =", num1 * num2 ** 2 / (4 * tan(pi / num1)))
                except ValueError :
                    print("Ошибка! Некорректный ввод первого числа.")
                    break


    def block_progressive() :
        op2 = input("1) Arithmetic progression 2) Geometric progression 3) Harmonic progression: ")
        if op2 == "1" :
            a1 = int(input("Enter the first term a1: "))
            d = int(input("Enter the common difference of the arithmetic progression: "))
            k = int(input("Enter the last term number k: "))
            result = ""
            for i in range(k) :
                result += str(a1 + i * d) + " "
            print("All terms of the progression:", result)
        elif op2 == "2" :
            b1 = get_float("Enter the first term of the progression: ")
            q = get_float("Enter the common ratio of the geometric progression: ")
            n = get_float("Enter the term number: ")
            bn = b1 * (q ** (n - 1))
            print(bn)
        elif op2 == "3" :
            n = int(input("Enter the number of elements in the progression: "))
            print("Harmonic progression constructed ↓")
            for i in range(1, n + 1) :
                print(1 / i)


    def block_addition() :
        while True :
            try :
                op3 = input(
                    "Select operation: 1) x̄ - (arithmetic mean)  2) |a| (absolute value)  3) opposite number  4) n√: ")
            except ValueError :
                print("Input error. Please select an operation from the list (1, 2, 3, or 4).")
                continue
            if op3 in ["1", "2", "3", "4"] :
                break
            else :
                print("Invalid selection. Please enter 1, 2, or 3.")
        if op3 == "1" :
            total = 0
            while True :
                try :
                    num1 = int(input("Enter the number of numbers: "))
                    break
                except ValueError :
                    print("Error, please enter an INTEGER")
            for i in range(num1) :
                try :
                    num2 = get_float("Enter a number, pi, e, y, or 'fraction': ")
                except ValueError :
                    print("Error entering the first number!")
                    exit()
                total += num2
            print("Arithmetic mean =", total / num1)
        elif op3 == "2" :
            num = get_float("Enter a number: ")
            print(abs(num))
        elif op3 == "3" :
            num = get_float("Enter a number: ")
            if num > 0 :
                print("-", num, sep="")
            elif num < 0 :
                print(num * -2 - -num)
            elif num == 0 :
                print("0 does not have an opposite number!")
        elif op3 == "4" :
            num1 = get_float("Enter the root degree: ")
            num2 = get_float("Enter the number to take the root of: ")
            print(num2 ** (1 / num1))


    print("Hello, this is a clever calculator!")
    while True :
        print("_____________________Menu_______________________")
        print("1) classic")
        print("2) trigonom")
        print("3) compare")
        print("4) multiplicity")
        print("5) square")
        print("6) addition")
        print("7) progressive")
        print("8) exit")
        import time

        sin = math.sin
        tan = math.tan
        pi = math.pi
        e = math.e
        Fraction = fractions.Fraction
        factorial = math.factorial
        sqrt = math.sqrt
        pow = math.pow
        cbrt = math.cbrt
        gcd = math.gcd
        y = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495146314472498070824809605040144865428362241739976449235362535003337429373377376739427925952582470949160087352039481656708532331517766115286211995015079847937450857057400299213547861466940296043254215190587755352673313992540129674205137541395491116851028079842348775872050384310939973613725530608893312676001724795378367592713515772261027349291394079843010341777177808815495706610750101619166334015227893586796549725203621287922655595366962817638879272680132431010476505963703947394957638906572967929601009015125195950922243501409349871228247949747195646976318506676129063811051824197444867836380861749455169892792301877391072945781554316005002182844096053772434203285478367015177394398700302370339518328690001558193988042707411542227819716523011073565833967348717650491941812300040654693142999297779569303100503086303418569803231083691640025892970890985486825777364288253954925873629596133298574739302
        vibor = input("Select a function from the list: ")
        if vibor == "1" :
            block_classic()
        elif vibor == "2" :
            block_trigonom()
        elif vibor == "3" :
            block_compare()
        elif vibor == "4" :
            multiplicity()
        elif vibor == "5" :
            block_square()
        elif vibor == "6" :
            block_addition()
        elif vibor == "7" :
            blok_progressive()
        elif vibor == "8" :
            print("Goodbye!")
            break
        else :
            print("Error! Select a function from the list!")
            break
        time.sleep(2)
