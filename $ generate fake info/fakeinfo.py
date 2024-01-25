from faker import Faker

fake = Faker('ru_RU')

def print_frame(value): 
   line = '+' + '-'*(len(value) + 2) + '+' 
   print(line) 
   print('| ' + value + ' |') 
   print(line)


print_frame("ФИО:") 
print(fake.name())

print_frame("Адрес:")
print(fake.address())

print_frame("Номер телефона:")
print(fake.phone_number())

print_frame("IP Address:")
print(fake.ipv4_private())

print_frame("User-Agent:")
print(fake.user_agent())

print_frame("Возраст:")
print(fake.random_int(min=13, max=24))

print_frame("Электронная почта:")
print(fake.email())

print_frame("ИНН:") 
print(fake.random_int(min=1000000000, max=9999999999))

print_frame("СНИЛС:") 
print(fake.random_int(min=10000000000, max=99999999999))