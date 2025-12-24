phone_book = {}
def add_contact():
    name = input("enter the name:").strip().lower()
    phone_num = int(input("enter the number:").strip())
    phone_book[name] = phone_num
    print()
    print("---------contact saved successfully!-------")
    print(phone_book)



def read_contact():
    search_name = input("enter the searching name:").strip().lower()
    if search_name in phone_book.keys():
        print()
        print('----------------------')
        print(f"the number for {search_name.capitalize()} is : {phone_book[search_name]}") 
    else:
        print("Contact is not available.....?")


def update_contact():
    update_name = input("enter the name:").strip().lower()
    update_num=int(input("Enter the new number to update:".strip()))
    phone_book[update_name]=update_num
    print()
    print()
    print("-------------Contact saved successfully!--------------")
def delete_contact():
    delete_name=input("Enter the name:").strip().lower()
    del phone_book[delete_name]
    print()
    print("-------------Contact Deleted successfully!--------------")
    print(phone_book)
def main():
    while(True):
        print("choose the task from below options:")
        print("""
              1.Add contact
              2.Read contact
              3.Update contact
              4.Delete contact""")
        print()
        choice=int(input("Enter the choice:"))
        if choice ==1:
            add_contact()
        elif choice ==2:
            read_contact()
        elif choice ==3:
            update_contact()
        elif choice ==4:
            delete_contact()
        else:
             break
if __name__ == '__main__':
    main()
