class PhoneBook:

    def __init__(self):
        self.phone_book = {}

    
    def add_contact(self, number, name):
    
        self.phone_book[number] = name

    def delete_number(self, number):

        self.phone_book.pop(number)

    def find_contact(self, number):

        if number in self.phone_book.keys():
            return self.phone_book[number]
        else:
            return 'not_found'
        
if __name__ == '__main__':
    phone_book = PhoneBook()
    n_lines = int(input())
    lines = [input() for _ in range(0, n_lines)]
    for line in lines:
        if line.startswith('add'):
            phone_book.add_contact(line.split(' ')[1], line.split(' ')[2])
        elif line.startswith('del'):
            phone_book.delete_number(line.split(' ')[1])
        elif line.startswith('find'):
            print(phone_book.find_contact(line.split(' ')[1]))