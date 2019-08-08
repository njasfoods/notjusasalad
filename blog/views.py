from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name':"Al"})


def results(request):
    name = request.POST["name"]
    age = int(request.POST["age"])
    sex = request.POST["sex"]
    height = float(request.POST["height"])
    weight = float(request.POST["weight"])
    physical = int(request.POST["physical"])

    class Person:

        def __init__(self, sex, weight, height, age, physical):
            self.sex = sex
            self.weight = float(weight)
            self.height = float(height)
            self.age = int(age)
            self.physical = int(physical)

        def bmr(self):
            rmr = int((10 * self.weight) + (6.25 * self.height) - (5 * self.age))
            if (self.sex == 'm'):
                rmr_f = rmr + 5

                def phys():
                    if (self.physical == 1):
                        mfe = rmr_f * 1.2
                        return mfe
                    elif (self.physical == 2):
                        mfe = rmr_f * 1.375
                        return mfe
                    elif (self.physical == 3):
                        mfe = rmr_f * 1.55
                        return mfe
                    elif (self.physical == 4):
                        mfe = rmr_f * 1.725
                        return mfe
                    elif (self.physical == 5):
                        mfe = rmr_f * 1.9
                        return mfe
                    else:
                        return rmr_f

                return phys()
            else:
                rmr_f = rmr - 161

                def phys():
                    if (self.physical == 1):
                        mfe = rmr_f * 1.2
                        return mfe
                    elif (self.physical == 2):
                        mfe = rmr_f * 1.375
                        return mfe
                    elif (self.physical == 3):
                        mfe = rmr_f * 1.55
                        return mfe
                    elif (self.physical == 4):
                        mfe = rmr_f * 1.725
                        return mfe
                    elif (self.physical == 5):
                        mfe = rmr_f * 1.9
                        return mfe
                    else:
                        return rmr_f

                return phys()

    class Nutrition:

        def __init__(self, bmr):
            self.bmr = int(bmr)
            self.protein_1 = self.bmr * 0.15 / 4
            self.protein_2 = self.bmr * 0.25 / 4

            self.fat_1r = self.bmr * 0.29 / 9
            self.fat_1k = self.bmr * 0.50 / 9
            self.fat_2k = self.bmr * 0.75 / 9
            self.fat_1m = self.bmr * 0.35 / 9
            self.fat_1m = self.bmr * 0.40 / 9

            self.carb_1 = self.bmr * 0.45 / 4
            self.carb_2 = self.bmr * 0.65 / 4

    person = Person(sex,weight,height,age,physical).bmr()
    macros = Nutrition(person)

    return render(request, "results.html",
                  {"name": name, "age": age, "sex": sex, "height": height,
                   "weight": weight, "physical": physical,"bmr": person})
