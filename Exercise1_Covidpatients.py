import random as rand
import datetime

recovered_patients = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15', 'p16','p17','p18','p19','p20']

class City_X_Model:

    def __init__(self, recovered_patients):

        self.recovered_patients = recovered_patients
    
    def split_batchsize_hospital(self,n):
        k, m = divmod(len(recovered_patients), n)
        return (recovered_patients[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

n = int(input("Enter the batch size to test recovered patients in your hospital: - "))
result = City_X_Model.split_batchsize_hospital(recovered_patients,n)

random_patient_1 = rand.choice(next(result))
random_patient_2 = rand.choice(next(result))
random_patient_3 = rand.choice(next(result))
random_patient_4 = rand.choice(next(result))

print(f'{random_patient_1} was tested at {datetime.datetime.now()} in your hospital')
print(f'{random_patient_2} was tested at {datetime.datetime.now()} in your hospital')
print(f'{random_patient_3} was tested at {datetime.datetime.now()} in your hospital')
print(f'{random_patient_4} was tested at {datetime.datetime.now()} in your hospital')