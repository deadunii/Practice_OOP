# Задача:
# написать класс vulnerability в котором можно будет:
# 1)Создать уязвимость
# 2)Создать описание уязвимости (при инициализации)
# 3)Сравнивать уязвимости
# 4)Повысить или понизить ранг уязвимости

class Vulnerability:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._rang = 0

    @property
    def rang(self):
        return self._rang

    @rang.setter
    def rang(self, value):
        self._rang += value

    def __lt__(self, other):
        return f'True. Ранг {self._name} ниже {other._name} на {self._rang - other._rang}' if self._rang > other._rang else f'False. Ранг {self._name} выше {other._name} на {other._rang - self._rang} '

    def __gt__(self, other):
        return f'True. Ранг {self._name} выше {other._name} на {other._rang - self._rang}' if self._rang < other._rang else f'False. Ранг {self._name} ниже {other._name} на {self._rang - other._rang} '


Broken_Access_Control = Vulnerability('Broken Access Control',
                                      "Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification, or destruction of all data or performing a business function outside the user's limits.")
Broken_Access_Control.rang = 1

Cryptographic_Failures = Vulnerability('Cryptographic Failures',
                                       "The first thing is to determine the protection needs of data in transit and at rest. For example, passwords, credit card numbers, health records, personal information, and business secrets require extra protection, mainly if that data falls under privacy laws, e.g., EU's General Data Protection Regulation (GDPR), or regulations, e.g., financial data protection such as PCI Data Security Standard (PCI DSS).")
Cryptographic_Failures.rang = 2
print(Broken_Access_Control > Cryptographic_Failures)
print(Broken_Access_Control < Cryptographic_Failures)
print(f"Старый ранг Cryptographic Failures:", Cryptographic_Failures.rang)
Cryptographic_Failures.rang = 3
print(f"Новый ранг Cryptographic Failures:", Cryptographic_Failures.rang)
print(f"Старый ранг Broken_Access_Control:", Broken_Access_Control.rang)
Broken_Access_Control.rang = -1
print(f"Новый ранг Broken_Access_Control:", Broken_Access_Control.rang)
