# Input chat data
chat = {}
n = int(input("Enter number of chats: "))
for _ in range(n):
    name, mssg = input("enter the name and message").split(':')
    if name in chat:
        chat[name].append(mssg)
    else:
        chat[name] = [mssg]

# Menu
while True:
    print("\n1.Total messages 2.Unique users 3.Total words 4.Avg words/message 5.Longest message")
    print("6.Most active user 7.User message count 8.Most frequent word 9.First & Last message 10.Check user 11.Repeated words 12.Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        count = 0
        for msgs in chat.values():
            if msgs:
                count += len(msgs)
        print("Total messages:", count)

    elif choice == '2':
        users = []
        for user in chat:
            if user not in users:
                users.append(user)
        print("Unique users:", users)

    elif choice == '3':
        total = 0
        for msgs in chat.values():
            for m in msgs:
                if m:
                    total += len(m.split())
        print("Total words:", total)

    elif choice == '4':
        total_msgs = 0
        total_words = 0
        for msgs in chat.values():
            if msgs:
                total_msgs += len(msgs)
                for m in msgs:
                    if m:
                        total_words += len(m.split())
        avg = total_words / total_msgs if total_msgs else 0
        print("Average words per message:", round(avg,2))

    elif choice == '5':
        longest = ""
        for msgs in chat.values():
            for m in msgs:
                if m and len(m) > len(longest):
                    longest = m
        print("Longest message:", longest if longest else "No messages")

    elif choice == '6':
        max_user = None
        max_msgs = 0
        for user, msgs in chat.items():
            if len(msgs) > max_msgs:
                max_msgs = len(msgs)
                max_user = user
        print("Most active user:", max_user if max_user else "No users")

    elif choice == '7':
        user = input("Enter username: ")
        print(f"{user} has sent {len(chat.get(user, []))} messages")

    elif choice == '8':
        user = input("Enter username: ")
        msgs = chat.get(user, [])
        word_counts = {}
        for m in msgs:
            if m:
                for w in m.split():
                    word_counts[w] = word_counts.get(w, 0) + 1
        most_common = None
        max_count = 0
        for w, c in word_counts.items():
            if c > max_count:
                most_common = w
                max_count = c
        print(f"Most frequent word by {user}:", most_common if most_common else "No words")

    elif choice == '9':
        user = input("Enter username: ")
        msgs = chat.get(user, [])
        if msgs:
            print("First message:", msgs[0])
            print("Last message:", msgs[-1])
        else:
            print("No messages from this user")

    elif choice == '10':
        user = input("Enter username: ")
        if user in chat and chat[user]:
            print("User present")
        else:
            print("User not found")

    elif choice == '11':
        word_counts = {}
        for msgs in chat.values():
            for m in msgs:
                if m:
                    for w in m.split():
                        word_counts[w] = word_counts.get(w, 0) + 1
        repeated = []
        for w, c in word_counts.items():
            if c > 1:
                repeated.append(w)
        print("Repeated words:", repeated)

    elif choice == '12':
        print("Exiting...")
        break

    else:
        print("Invalid choice")
