import patient as p
p.setup_database()
while True:
        print("1.Create new patient record")
        print("2.Update patient record")
        print("3.Delete patient record")
        print("4.View all patient records")
        print("5.Exit")
        choice=input("Choose (1-5):")
        if choice=='1':
            p.create_record()
        elif choice=='2':
            p.update_record()
        elif choice=='3':
            p.delete_record()
        elif choice=='4':
            p.view_record()
        elif choice=='5': 
            break
        else: 
            print("Invalid choice")
