# Constants
import os
import re
MAX_ACCOUNTS = 10
MAX_JOBS = 10
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12

def signUp(signedIn):
  """
    Display the main menu options
    """
  print("\n--- Sign Up ---")
  if signedIn == True:
    print("You are already signed in!\nReturning to previous Page.")
    return
  print("1. Log in")
  print("2. Create a new account")
  print("3. Back to previous page")
  choice = input("Enter your choice: ")
  while not (choice == '1' or choice == '2' or choice == '3'):
    print("Invalid choice")
    choice = input("Enter your choice: ")

  choice = int(choice)
  if choice == 1:
    account = login()
    additional_options(account)
  elif choice == 2:
    account = create_account()
  else:
    return
  

def blog():
  print("\n--- Blog ---")
  print("Under Construction")
  return

  
def careers():
  print("\n--- Careers ---")
  print("Under Construction")
  return

  
def developers():
  print("\n--- Developers ---")
  print("Under Construction")
  return

def general(signedIn):
  while True:
    print("\n--- General ---")
    print("1. Sign Up")
    print("2. Help Center")
    print("3. About")
    print("4. Press")
    print("5. Blog")
    print("6. Careers")
    print("7. Developers")
    print("8. Back to previous page")
    while True:
      try:
        choice = int(input("Enter your choice: "))
      except:
        print("Invalid choice")
        continue
      if choice < 1 or choice > 8:
        print("Invalid choice")
      else:
        break
    #Sign up
    if choice == 1:
      signUp(signedIn)
    #Help Center
    elif choice == 2:
      print("\n--- Help Center ---")
      print("We're here to help")
      #About
    elif choice == 3:
      print("\n--- About ---")
      print("InCollege: Welcome to InCollege, the world's largest college student network with many users in many countries and territories worldwide")
    #Press
    elif choice == 4:
      print("\n--- Press ---")
      print("In College Pressroom: Stay on top of the latest news, updates, and reports")
    #Blog
    elif choice == 5:
      blog()
    #Careers
    elif choice == 6:
      careers()
    #Developers
    elif choice == 7:
      developers()
    else:
      return
    

def browse():
  print("\n--- Browse ---")
  print("Under Construction")
  return
def businessSol():
  print("\n--- Business Solutions ---")
  print("Under Construction")
  return
def directories():
  print("\n--- Directories ---")
  print("Under Construction")
  return

  
def usefulLinks(signedIn, username):
  """
    Useful links group
  """
  while True:
    print("\n--- Useful Links ---")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Back to previous page")
  
    while True:
          try:
            choice = int(input("Enter your choice: "))
          except:
            print("Invalid choice")
            continue
          if choice < 1 or choice > 5:
            print("Invalid choice")
          else:
            break
    #General
    if choice == 1:
      general(signedIn)
    #Browse InCollege
    elif choice == 2:
      browse()
    #Business Solutions
    elif choice == 3:
      businessSol()
    #Directories
    elif choice == 4:
      directories()
    elif choice == 5:
      return

    
def guestControls(signedIn, username):
  print("\n--- Guest Controls ---")
  if signedIn == True:
    settings = get_account_value(username, "default")
    
    email = 'OFF'
    SMS = 'OFF'
    adv = 'OFF'
    if settings[0] == '1':
      email = 'ON'
    if settings[1] == '1':
      SMS = 'ON'
    if settings[2] == '1':
      adv = 'ON'
    print("Current settings:\nEmail: ",email,"\nSMS: ", SMS, "\nTargeted Advertising: ", adv)
    while True: 
      try:
          choice = int(input("\nWould you like to change your settings? [1 = Yes, 2 = No]: "))
      except:
          print("Invalid choice")
          continue
      if choice < 1 or choice > 2:
        print("Invalid choice")
      else:
        break
    if choice == 2:
      return
    else:
      email = str(input("Email: [1 = ON, 0 = OFF]: "))
      SMS = str(input("SMS: [1 = ON, 0 = OFF]: "))
      adv = str(input("Target Advertising: [1 = ON, 0 = OFF]: "))
    with open('accounts.txt', 'r') as f:
      lines = f.readlines()
    try:
      index = lines.index("Username: " + username + "\n")
    except:
      return
    newsettings = email + SMS + adv
    index += 4
    lines[index] = "Default: "+ newsettings + "\n"
    with open('accounts.txt', 'w') as file:
      file.writelines(lines)
    f.close
    print("Changes made successfully!")
  else:
    print("To change controls, please sign in")
    return
  return
def languages(signedIn, username):
  print("\n--- Languages ---")
  if signedIn == True:
    settings = get_account_value(username, "language")
    lang = 'English'
    if settings[0] == 's':
      lang = 'Spanish'
    print("Current settings:\nLanguage: ",lang)
    while True: 
      try:
          choice = int(input("\nWould you like to change your settings? [1 = Yes, 2 = No]: "))
      except:
          print("Invalid choice")
          continue
      if choice < 1 or choice > 2:
        print("Invalid choice")
      else:
        break
    if choice == 2:
      return
    else:
      newlang = str(input("Language: [e = English, s = Spanish]: "))
    with open('accounts.txt', 'r') as f:
      lines = f.readlines()
    try:
      index = lines.index("Username: " + username + "\n")
    except:
      return
    index += 5
    lines[index] = "Language: "+ newlang + "\n"
    with open('accounts.txt', 'w') as file:
      file.writelines(lines)
    f.close
    print("Changes made successfully!")
  else:
    print("To change controls, please sign in")
    return
  return
def importantLinks(signedIn, username):
  """
    inCollege important links
    """
  while True:
    print("\n--- InCollege Important Links ---")
    print("1. Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. Guest Controls")
    print("10. Languages")
    print("11. Back to previous page")
    while True:
      try:
        choice = int(input("Enter your choice: "))
      except:
        print("Invalid choice")
        continue
      if choice < 1 or choice > 11:
        print("Invalid choice")
      else:
        break
    
    #Copyright Notice
    if choice == 1:
      print("\n--- Copyright Notice ---")
      print("Copyright © 2023 InCollege. All rights reserved.\nThe contents of this website, including but not limited to text, graphics, images, and other material, are protected by copyright law. The content may not be reproduced, distributed, modified, or reposted in any form without the prior written consent of InCollege. \nPlease note that InCollege is not responsible for the content or privacy practices of external websites that may be linked to from this site.")
      
    #About
    elif choice == 2:
      print("\n--- About ---")
      print("Welcome to InCollege, the professional networking platform designed specifically for college students. Our platform is built on the idea that building meaningful connections and authentic relationships with others is the foundation of a successful career. \nAt InCollege, we believe that every college student deserves the opportunity to find their dream job and build a fulfilling career. That's why we've created a platform that makes it easy to showcase your skills, connect with others in your field, and discover new job and internship opportunities that match your unique talents and interests.\nWhether you're a freshman just starting out or a senior ready to launch your career, InCollege has the tools and resources you need to succeed. From internships and job listings to personal branding and networking opportunities, we're here to help you achieve your career goals.")
      #Accessibility
    elif choice == 3:
      print("\n--- Accessibility ---")
      print("At InCollege, we are committed to making our platform accessible to everyone, including individuals with disabilities. We strive to ensure that all of our users have an equal opportunity to access and use our website, regardless of their physical or cognitive abilities.\nTo this end, we have taken a number of steps to make our website as accessible as possible. These steps include:\n\tProviding alt text for all images and graphics on our site, to ensure that users with visual impairments can understand the content\n\tEnsuring that our website can be navigated using a keyboard, for users who may have difficulty using a mouse\n\tMaking sure that our website is compatible with screen reader software, to allow users with visual impairments to navigate our site\nWe are constantly working to improve the accessibility of our platform, and we welcome feedback from our users on how we can better meet their needs. If you have any suggestions or concerns about the accessibility of our website, please don't hesitate to contact us at help@InCollege.com.")
    #User Agreement
    elif choice == 4:
      print("\n--- User Agreement ---")
      print("Welcome to InCollege, the professional networking platform designed for college students. We're excited to have you as a member of our community, and we want to make sure that you understand the terms and conditions of using our platform.\nBy using InCollege, you agree to the following terms:\n\tYou are responsible for the content you post: You are solely responsible for any content you post on our platform, including your profile information, job postings, and messages to other users. \n\tYou agree to only post content that is accurate, truthful, and not in violation of any intellectual property or other legal rights.\n\tYou agree to use InCollege for professional purposes: Our platform is designed for professional networking and job seeking. You agree to only use our platform for these purposes, and not for any illegal, fraudulent, or unethical activities.\n\tYou agree not to harass, intimidate, or otherwise harm other users on our platform.\nBy using InCollege, you agree to these terms and conditions. If you violate any of these terms, we reserve the right to suspend or terminate your account.\nIf you have any questions or concerns about our user agreement, please contact us at help@InCollege.com.")
    #Privacy Policy
    elif choice == 5:
      print("\n--- Privacy Policy ---")
      print("Welcome to InCollege, the professional networking platform designed for college students. At InCollege, we are committed to protecting your privacy and providing you with a secure and trustworthy platform for building your professional network. \nHere's an overview of our privacy policy:\n\tPersonal information we collect: When you create an account on InCollege, we collect personal information from you, such as your name, email address, and other profile information. We may also collect information about your use of our platform, such as your job search activity and connections.\n\tHow we use your personal information: We use your personal information to provide you with a personalized and relevant experience on our platform. For example, we may use your profile information to recommend job opportunities or connections that match your skills and interests.\n\tHow we share your personal information: We may share your personal information with third-party service providers who help us operate and improve our platform. We may also share your information with recruiters and potential employers, but only with your consent.\n\tYour choices and rights: You have the right to access, modify, and delete your personal information on our platform. You can also choose whether or not to receive marketing communications from us.At InCollege, we are committed to providing you with a transparent and trustworthy platform for building your professional network. If you have any questions or concerns about our privacy policy, please contact us at help@InCollege.com.")
      
    #Cookie Policy
    elif choice == 6:
      print("\n--- Cookie Policy ---")
      print("Welcome to InCollege, the professional networking platform designed for college students. Like many websites, we use cookies to enhance your experience and provide you with a more personalized service.\nHere's an overview of our cookie policy:\n\tHow we use cookies: We use cookies to enhance your experience on our platform, such as by remembering your preferences and login information. We also use cookies for analytics and advertising purposes.\n\tHow to manage cookies: You can control and manage cookies on your device through your browser settings. However, please note that disabling cookies may impact the functionality of our platform.\n\tThird-party cookies: We may use third-party cookies for advertising and analytics purposes. These cookies are subject to the privacy policies of the third-party providers.\nBy using InCollege, you consent to our use of cookies in accordance with this policy. If you have any questions or concerns about our cookie policy, please contact us at help@InCollege.com.")
    #Copyright Policy
    elif choice == 7:
      print("\n--- Copyright Policy ---")
      print("Welcome to InCollege, the professional networking platform designed for college students. At InCollege, we respect the intellectual property rights of others and we expect our users to do the same.\nHere's an overview of our copyright policy:\n\tOwnership of content: Users of InCollege own the content they create and share on our platform, such as their profiles, posts, and messages.\n\tProhibited content: Users are not allowed to post or share content that infringes on the copyright or other intellectual property rights of others. This includes but is not limited to, photos, videos, and other copyrighted material that the user does not have the right to use.\n\tReporting copyright infringement: If you believe that your copyright has been infringed on InCollege, please contact us immediately at [contact email address]. We will investigate and take appropriate action, which may include removing the infringing content or terminating the user's account.\nAt InCollege, we are committed to protecting the intellectual property rights of all users of our platform. If you have any questions or concerns about our copyright policy, please contact us at help@InCollege.com.")
    #Brand Policy
    elif choice == 8:
      print("\n--- Brand Policy ---")
      print("Here's an overview of our brand policy:\n\tUse of our name and logo: You may use the InCollege name and logo for the purpose of identifying yourself as a user of our platform. However, you may not use our name or logo in a way that suggests an affiliation with or endorsement by InCollege without our prior written consent.\n\tProhibited uses: You may not use our name or logo in a way that is misleading, defamatory, or otherwise harmful to our brand. You may not use our name or logo in a way that violates the intellectual property rights of others.\n\tReporting misuse of our brand: If you become aware of any unauthorized or improper use of our brand, please contact us immediately at help@InCollege.com. We will investigate and take appropriate action.")
    #Guest Controls
    elif choice == 9:
      guestControls(signedIn, username) ## calls function to edit controls
    #Languages
    elif choice == 10:
      languages(signedIn, username)
    elif choice == 11:
      return


def add_account(username, password, first_name, last_name, uni, major):
  """
  Add username, password, first name, and last name to account list
  """
  with open('accounts.txt', 'a') as f:
    
    f.write("Username: " + username + "\n")
    f.write("Password: " + password + "\n")
    f.write("First Name: " + first_name + "\n")
    f.write("Last Name: " + last_name + "\n")
    f.write("Default: " + '111' + "\n")
    f.write("Language: " + 'e' + "\n")
    f.write("University: " + uni + "\n")
    f.write("Major: " + major + "\n")

def add_job(username, poster, title, description, employer, location, salary):
  """
  Add poster, title, description, employer, location, and salary to job list
  """
  with open('jobs.txt', 'a') as f:
    f.write("User: " + username + "\n")
    f.write("Poster: " + poster + "\n")
    f.write("Title: " + title + "\n")
    f.write("Description: " + description + "\n")
    f.write("Employer: " + employer + "\n")
    f.write("Location: " + location + "\n")
    f.write("Salary: " + salary + "\n")
    f.write("Applicants: " + "\n")
    f.write("Saved: " + "\n")


def additional_options(username):
  """
  Display the additional options
  """
  while True:
    print("\n--- Options Menu ---")
    print("1. Job Search/Internship")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. Useful Links")
    print("5. InCollege Important Links")
    print("6. Show my Network")
    print("7. Friend Requests")
    print("8. View Profile")
    print("9. Edit profile")
    print("10. Create profile")
    print("11. Return to main menu (Log Out)")
    # checks if user input for choice is valid
    while True:
      try:
        choice = int(input("Enter your choice: "))
      except:
        print("Invalid choice")
        continue
      if choice < 1 or choice > 11:
        print("Invalid choice")
      else:
        break
    # does selected choice
    match choice:
      case 1:
        job_menu(username)
      case 2:
        find_connection(username)
      case 3:
        skills_menu(username)
      case 4:
        usefulLinks(True, username)
      case 5:
        importantLinks(True, username)
      case 6:
        showNetwork(username)
      case 7:
        displayRequests(username)
      case 8:
        viewProfile(username)
      case 9:
        print("1. Change existing info\n 2. Finish Profile")
        while True:
          try:
            choice = int(input("Enter your choice: "))
          except:
            print("Invalid choice")
            continue
          if choice < 1 or choice > 2:
            print("Invalid choice")
          else:
            break
        if choice == 1:
          editProfile(username)
        finishProfile(username)
      case 10:
        createProfile(username)
      case 11:
        return

def convert_into_uppercase(a):
    return a.group(1) + a.group(2).upper()

#allows users to edit existing information. Function goes through each line and asks user if they wish to edit the existing information
def editProfile(username):
  try:
    f = open(username + "Profile.txt", 'r')
  except IOError:
    print("You have no profile")
    return
  lines = f.readlines()
  cnt=0
  for line in lines:
      sepword = line.split(":", 1)
      if "Experience" in sepword[0]:
        cnt = cnt + 1
        continue
      print("Would you like to change " + sepword[0] +"?\n1.Yes\n2.No\n3.Return to menu")
      try:
        choice = int(input("Select: "))
      except:
        print("Invalid choice")
      if choice < 1 or choice > 3:
        print("Invalid choice")
      if choice == 3:
        break
      if choice == 2:
        cnt = cnt+1
        continue
        lines[cnt] = line
      if choice == 1:
        inp = input("Enter input ")
        lines[cnt] = line.replace(sepword[1], inp + "\n")
        cnt = cnt+1
  with open(username + "Profile.txt", 'w') as f:
    f.writelines(lines)
    
#allows users to finish existing profile. User cannot exit once they enter this function, but adding extra experiences is optional
def finishProfile(username):
  inputs = ["User Title", "About", "Experience1", "Experience2", "Experience3", "School", "Degree", "Years attended"]
  experience = ["Job Title", "Employer", "Date started", "Date ended", "Location", "Description"]
  try:
    f = open(username + "Profile.txt", 'r')
  except IOError:
    print("You have no profile")
    return
  lines = f.readlines()
  with open(username + "Profile.txt", 'w') as fnew:
    cnt = 0
    expcnt = 1
    #if we reached max amount of lines in old file but profile is not yet complete
    for x in inputs:
      if cnt >= len(lines):
        choice = input("What to place in " + x + ": ")
        if x == "Degree" or x == "School":
          result = re.sub("(^|\s)(\S)", convert_into_uppercase, choice)
          fnew.write(x + ":" + result + "\n")
        else:
          fnew.write(x + ":" + choice + "\n")
        continue
      sepword = lines[cnt].split(":", 1)
      #if part of profile is not experience and part of profile is present, copy into new file
      if x == sepword[0] and "Experience" not in x:
        print("CASE 1" + sepword[0] + " " + x)
        fnew.write(lines[cnt])
        cnt = cnt + 1
      #if part of profile is experience and part of profile is present, copy all parts of experience into new file
      if x == sepword[0] and "Experience" in x:
        fnew.write(lines[cnt])
        cnt = cnt + 1
        for y in experience:
          fnew.write(lines[cnt])
          cnt = cnt + 1
        expcnt += 1
      #if part of profile is not experience and part of profile is not present, get input and insert part of profile into new file
      if x != sepword[0] and "Experience" not in x:
        print("CASE 3 " + sepword[0] + " " + x)
        choice = input("What to place in " + x + ": ")
        fnew.write(x + ":" + choice + "\n")
      #if part of profile is not experience and part of profile is not present, get input for all parts of experience and insert part of profile into new file
      if x != sepword[0] and "Experience" in x:
        print("Add experience?\n1.Yes\n2.No")
        try:
          inp = int(input("Select: "))
        except:
          print("Invalid choice")
        if inp < 1 or inp > 2:
          print("Invalid choice")
        if inp == 1:
          fnew.write("Experience" + str(expcnt) + ":" + "\n")
          expcnt += 1
          for y in experience:
            choose = input("What to place in " + y + ": ")
            fnew.write(y + ":" + choose + "\n")
        if inp == 2:
          continue
        
        
  print("Profile completed")
def createProfile(username):
  print("Press tab to quit. Progress will be saved")

  with open(username + "Profile.txt", 'w+') as f:
    inputs = ["User Title", "About"]
    f.readline()
    
    for x in inputs:
      choice = input("Enter " + x + ": ")
      if choice == "\t":
        return
      f.write(x + ":" + choice + "\n")

    while True:
      try:
        num = int(input("Enter your experience:\nHow many experiences would you like to add?(must be 3 or less). Press tab to quit: "))
      except:
        print("Invalid choice")
        continue
      if int(num) < 1 or int(num) > 3:
        print("Invalid choice")
      elif num == "\t": 
        return
      else:
        break

    experiences = ["Job Title", "Employer", "Date started", "Date ended", "Location", "Description"] * num
    cnt = 1
    for x in experiences:
      if x == "Job Title":
        f.write("Experience" + str(cnt) + ":" + "\n")
        cnt = cnt + 1
      choice = input("Enter " + x + ": ")
      f.write(x + ":" + choice + "\n")
    #f.readline()
    education = ["School", "Degree", "Years attended"]
    for x in education:
      choice = input("Enter " + x + ": ")
      if choice == "\t":
        return
      if x == "Degree":
        result = re.sub("(^|\s)(\S)", convert_into_uppercase, choice)
        f.write(x + ":" + result + "\n")
      
      elif x == "School":
        result = re.sub("(^|\s)(\S)", convert_into_uppercase, choice)
        f.write(x + ":" + result + "\n")
      else: f.write(x + ":" + choice + "\n")

    

    
    
def viewProfile(username):
  try:
    f = open(username + "Profile.txt", 'r')
  except IOError:
    print("\nYou have no profile, create one?")
    choice = int(input("Press 1 for Yes: "))
    if(choice == 1): createProfile(username)
    return

  lines = f.readlines()
  print("\n")
  for line in lines:
    print(line)
  f.close()
  
def displayRequests(username):
  try:
    f = open(username + "Requests.txt", 'r')
  except IOError:
    print("You have no new friend requests")
    
    return
  lines = f.readlines()
  
  for line in lines:
    l = line.strip()
    print("Pending request from: " + l)
    print("Accept or deny request? (0=deny, 1=accept)")
    while True:
      try:
        choice = int(input("Enter your choice: "))
      except:
        print("Invalid choice")
        continue
      if choice < 0 or choice > 1:
        print("Invalid choice")
      else:
        break
    if choice == 0:
      print("Request denied successfully.")
    elif choice == 1:
      print(l)
      addToFriendList(username, l)
      print("Request accepted successfully!")

  os.remove(username + "Requests.txt")
  print("You have no new friend requests")

def friendRequest(username1, username2):
  try:
    f = open(username1 + "Requests.txt", 'r')
    # file exists
    f.close
  except IOError:
    f = open(username1 + "Requests.txt", 'w+')
    f.close
  f = open(username1 + "Requests.txt", 'a')
  f.write(username2 + "\n")
  f.close()
  print("Friend request sent!")
def addToFriendList(username1, username2):
  #If the request was accepted, it will add eachother to their friend lists.
  try:
      f = open(username1 + "Friends.txt", 'r')
    # file exists
      f.close
  except IOError:
      f = open(username1 + "Friends.txt", 'w+')
      f.close
      return
  f = open(username1 + "Friends.txt", 'a')
  f.write(username2 + "\n")
  f.close()
  try:
      f = open(username2 + "Friends.txt", 'r')
    # file exists
      f.close
  except IOError:
      f = open(username2 + "Friends.txt", 'w+')
      f.close
      return
  f = open(username2 + "Friends.txt", 'a')
  f.write(username1 + "\n")
  f.close()
  return
#validate selection choice
def selectFriend(friendCount):
  while True:
    try:
      choice = int(input("Select friend: "))
    except:
      print("Invalid choice")
    if choice < 1 or choice > friendCount:
      print("Invalid choice")
    else:
      return choice
#view the profile of selected friend in Network
def viewNetwork(username):
  try:
    f = open(username + "Profile.txt", 'r')
  except IOError:
    print("This person does not have a profile")
    return
     
  lines = f.readlines()
  for line in lines:
    print("\n" + line)
  f.close()
  
#Show network of logged in user
def showNetwork(username1):
  while True:
    try:
        f = open(username1 + "Friends.txt", 'r')
      # file exists
        f.close
    except IOError:
        f = open(username1 + "Friends.txt", 'w+')
        print("No friends to list")
        f.close
        return
    if os.path.getsize(username1 + "Friends.txt") == 0:
        print("No friends to list") 
        return
    with open(username1 + "Friends.txt", 'r') as f:
      print("\n--- Your Network ---")
      lines = f.readlines()
      j = 1
      for line in lines:
        l = line.replace("\n", "")
        print(str(j)+ ".", l)
        j += 1
    f.close
    print("What would you like to do?\nEnter 1 to view someone's profile\nEnter 2 to remove a friend\nEnter 0 to go back to the previous page.")
    try:
      choice = int(input("Enter your choice: "))
    except:
      print("Invalid choice")
    match choice:
      case 0: #Go back to previous page
        return
        
      case 1: #view a friend's profile in network list
        choice = selectFriend(j-1)
        with open(username1 + "Friends.txt", 'r') as f:
          select = 1
          for line in lines:
            if select == choice:
              l = line.replace("\n", "")
              viewNetwork(l)
            select+=1
                  
      case 2: #remove friend in network list
        choice = selectFriend(j-1)
        with open(username1 + "Friends.txt", 'w') as f:
          comp = 1
          for line in lines:
            if comp != choice:
              f.write(line)
            comp += 1
          print("Friend removed successfully")
        
def create_friend_list(username):
    try:
      f = open(username + "Friends.txt", 'r')
    # file exists
      f.close
    except IOError:
      f = open(username + "Friends.txt", 'w+')
      f.close
      
def create_account():
  """
  Create a new user account
  """
  # sees if file exists or not, if not create file
  try:
    f = open("accounts.txt", 'r')
    # file exists
    f.close
  except IOError:
    f = open("accounts.txt", 'w+')
    f.close

  # checks if maximum number of accounts have been made
  with open('accounts.txt', 'r') as f:
    lines = f.readlines()
  if len(lines)/8 >= MAX_ACCOUNTS:
    print("All permitted accounts have been created, please come back later")
    return "-1"

  # gets user inputs for account information
  print("--- Create New Account ---")
  username = input("Enter a username: ")
  # checks if username is unique
  while not is_unique_username(username):
    print("Username already in use")
    username = input("Enter a username: ")
  password = input("Enter a password: ")
  # checks if password is meets specified conditions
  while not is_valid_password(password):
    print(
      "Password must be 8-12 characters long, contain at least one capital letter, one digit and one special character"
    )
    password = input("Enter a password: ")
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  uni = input("Enter your university: ")
  major = input("Enter your major: ")
  # adds account to account list
  add_account(username, password, first_name, last_name, uni, major)
  create_friend_list(username)
  print("Account created successfully")
  return username


def display_success_story():
    success_story = "Meet Jimmy, a recent college graduate who struggled to find a job in his field. But with the help of InCollege, Jimmy was able to land his dream job at a top tech company. By using the resources and network provided by InCollege, Jimmy was able to showcase his skills and stand out from other applicants. He is now a successful software engineer, and credits InCollege for playing a significant role in his career success."
    print(success_story)


def find_connection(username):
  """
  Search for contact in InCollege system
  """
  # sees if file exists or not, if not create file
  try:
    f = open("accounts.txt", 'r')
    # file exists
    f.close
  except IOError:
    f = open("accounts.txt", 'w+')
    f.close
  with open('accounts.txt', 'r') as f:
    lines = f.readlines()
    
  print("\n--- Member Search ---")
  print("\nWould you like to search for a member by:")
  print("1. Last name")
  print("2. University")
  print("3. Major")
  print("4. Return to previous page")
  # checks if user input for choice is valid
  names = []
  while True:
    try:
      choice = int(input("Enter your choice: "))
    except:
      print("Invalid choice")
      continue
    if choice < 1 or choice > 4:
      print("Invalid choice")
    else:
      break
  # does selected choice
  if choice == 1:
    firstLine = "Last Name: "
    search = input("Enter their last name: ")
    Fsub = 1
    Lsub = 0
    Usub = 3
  elif choice == 2:
    firstLine = "University: "
    search = input("Enter their University: ")
    Fsub = 4
    Lsub = 3
    Usub = 6
  elif choice == 3:
    firstLine = "Major: "
    search = input("Enter their major: ")
    Fsub = 5
    Lsub = 4
    Usub = 7
  elif choice == 4:
    return
    
  contactFound = False
  i = 0
  j = 1
  for line in lines:
    if line == firstLine + search + "\n":
      Fname = lines[i - Fsub]
      Lname = lines[i - Lsub]
      Uname = lines[i - Usub]
      Fname = Fname.replace("First Name: ", "")
      Fname = Fname.replace("\n", "")
      Lname = Lname.replace("Last Name: ", "")
      Lname = Lname.replace("\n", "")
      Uname = Uname.replace("Username: ", "")
      Uname = Uname.replace("\n", "")
      names.append(Fname)
      names.append(Lname)
      names.append(Uname)
      print(str(j) + "." ,Fname, Lname)
      contactFound = True
      j+=1
    i += 1

  # if contact not found, return to menu 
  if contactFound == False:
    print("No Matches Found")
    return username

  print("Who would you like to add as a friend? (Enter number)\n Enter 0 to go back to previous page")
  while True:
    try:
      choice = int(input("Enter your choice: "))
    except:
      print("Invalid choice")
      continue
    if choice < 0 or choice > j:
      print("Invalid choice")
    else:
      break
  choice -= 1
  Fname = names[choice * 3]
  Lname = names[(choice * 3) + 1]
  Uname = names[(choice * 3) + 2]
  if not username == "-1":
    if not choice == -1:
      friendRequest(Uname, username)
    return username
    
# if contact found and not a member, asks user to join InCollege and present options
  print("--- You are not Logged in, do you want to join InCollege? ---")
  print("1. Log in")
  print("2. Sign up to join " + Fname + "!")
  print("3. Return to main menu")
  # checks if user input for choice is valid
  while True:
      try:
        choice = int(input("Enter your choice: "))
      except:
        print("Invalid choice")
        continue
      if choice < 1 or choice > 3:
        print("Invalid choice")
      else:
        break
  # does selected choice
  match choice:
    case 1:
      username = login()
    case 2:
      username = create_account()
  return username
  
    
def get_account_value(username, value):
  """
  Return password, first name, or last name for desired account
  """
  # sees if file exists or not, if not create file
  try:
    f = open("accounts.txt", 'r')
    # file exists
    f.close
  except IOError:
    f = open("accounts.txt", 'w+')
    f.close
  with open('accounts.txt', 'r') as f:
    lines = f.readlines()
    
  # checks if username exists in account list
  try:
    index = lines.index("Username: " + username + "\n")
  except:
    return "-1"
  
  # gets desired value for account
  match value:
    case "password":
      index += 1
    case "first name":
      index += 2
    case "last name":
      index += 3
    case "default":
      index += 4
    case "language":
      index += 5
  return lines[index].strip().split(": ")[1]

  
def is_unique_username(username):
  """
  Check if the username is unique
  """
  with open('accounts.txt', 'r') as f:
    lines = f.readlines()
  f.close
  
  # checks if username exists in account list
  try:
    index = lines.index("Username: " + username + "\n")
  except:
    return True

  print("Not a unique username")
  return False


def is_valid_password(password):
  """
  Check if the password meets the requirements
  """
  if len(password) < MIN_PASSWORD_LENGTH or len(
      password) > MAX_PASSWORD_LENGTH:
    return False
  if not any(c.isdigit() for c in password):
    return False
  if not any(c.isupper() for c in password):
    return False
  if not any(c in "!@#$%^&*()_+-=[]{};:,.<>?/\\|" for c in password):
    return False
  return True

#Delete a job in the job postings list
def delete_job(username):
  mjob = []
  try:
    f = open("jobs.txt", 'r')
  except IOError:
    print("No jobs listed\n")
    f.close()
    return
  lines = f.readlines()
  if len(lines) == 0: #return if number of jobs listed is 0
    print("No jobs listed\n")
    f.close()
    return
  f.close()
  cnt = 0
  #Find jobs listed by user
  while cnt < len(lines):
    mjob.append(lines[cnt])
    cnt+=1
  job_index = print_jobs(username, mjob, "user")
  if len(job_index) == 0: #return if no job listed by user
    print("No jobs listed\n")
    return
  #Ask user to choose what job to delete
  while True:
    try:
      choice = int(input("Select job to delete or press 0 to return to previous page: "))
    except:
      print("Invalid choice")
      continue
    if choice == 0:
      f.close()
      return
    elif choice < 1 or choice > len(job_index):
      print("Invalid choice")
    else:
      break
  cnt = 0
  index = job_index[choice-1]
  #Delete job from list
  with open('jobs.txt', 'w') as f: 
    while cnt < len(lines):
      if cnt == index:
        cnt+=9
        continue
      else:
        f.write(lines[cnt])
        cnt+=1
  f.close()
  

def job_menu(username):
  """
  Display the job menu options
  """
  while True:
    print("\n--- Job Search/Internship ---")
    print("1. Post a job")
    print("2. Look for a job")
    print("3. Delete a job listing")
    print("4. Return to previous page")
    # checks if user input for choice is valid
    while True:
      try:
        choice = int(input("Enter your choice: "))
      except:
        print("Invalid choice")
        continue
      if choice < 1 or choice > 6:
        print("Invalid choice")
      else:
        break
    # does selected choice
    if choice == 1:
      post_job(username)
    elif choice == 2:
      search_job(username)
    elif choice == 3:
      delete_job(username)
    elif choice == 4:
      return

    
def login():
  """
  Log in to an existing account
  """
  print("\n--- Login ---")
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if verify_account(username, password) == True:
    return username
  else:
    print("Incorrect username / password, please try again")
    username =login()
    return username


def main_menu(username):
  """
  Display the main menu options
  """
  print("\n--- InCollege ---")
  display_success_story()
  print("--- Main Menu ---")
  print("1. Log in")
  print("2. Create a new account")
  print("3. Find existing member of InCollege")
  print("4. Watch video about why to join InCollege")
  print("5. Useful Links")
  print("6. InCollege Important Links")
  # checks if user input for choice is valid
  while True:
      try:
        choice = int(input("Enter your choice: "))
      except:
        print("Invalid choice")
        continue
      if choice < 1 or choice > 6:
        print("Invalid choice")
      else:
        break
  # does selected choice
  match choice:
    case 1:
      username = login()
    case 2:
      username = create_account()
    case 3:
      username = find_connection(username)
    case 4:
      # plays video until user inputs "STOP"
      print("Video is now playing")
      while True:
        choice = input("Type STOP to end video\n")
        if choice == "STOP":
          print("Video ended")
          break
        else:
          print("Video is still playing")
    case 5:
      usefulLinks(False, username)
    case 6:
      importantLinks(False, username)
  return username


def post_job(username):
  """
  Post a job
  """
  # sees if file exists or not, if not create file
  try:
    f = open("jobs.txt", 'r')
    # file exists
    f.close
  except IOError:
    f = open("jobs.txt", 'w+')
    f.close
    
  # checks if maximum number of jobs have been posted
  with open('jobs.txt', 'r') as f:
    lines = f.readlines()
  if len(lines)/9>= MAX_JOBS:
    print("All permitted jobs have been posted, please come back later")
    return
  
  # gets user inputs for job information
  print("\n--- Post New Job ---")
  poster = get_account_value(username, "first name") + " " + get_account_value(username, "last name")
  title = input("Enter the job title: ")
  description = input("Enter the job description: ")
  employer = input("Enter the employer name: ")
  location = input("Enter the location: ")
  while True:
    try:
      salary = int(input("Enter the salary: $"))
      break
    except:
      print("Invalid salary")
  
  # adds job to job list
  add_job(username, poster, title, description, employer, location, str(salary))
  print("Job posted successfully")
  return
  
#Find a job in the job postings list
def search_job(username):
  """
  Search for job from posted job list
  """
  mjob = []
  try:
    f = open("jobs.txt", 'r')
    f.close
  except IOError:
    print("No jobs listed\n")
    return
  lines = f.readlines()
  if len(lines) == 0: #return if number of jobs listed is 0
    print("No jobs listed\n")
    f.close()
    return
  f.close()
  #choose desired list
  print("\n--- List Selection ---")
  print("1. View full list of jobs")
  print("2. View list of applied jobs")
  print("3. View list of unapplied jobs")
  print("4. View list of saved jobs")
  print("5. Return to previous page")
  while True:
    try:
      choice = int(input("Enter your choice: "))
    except:
      print("Invalid choice")
      continue
    if choice == 0:
      f.close()
      return
    elif choice < 1 or choice > 5:
      print("Invalid choice")
    else:
      break
  cnt = 0
  #return to previous page
  if choice == 5:
    return
  else:
    while cnt < len(lines):
      x = 0
      while x < 7:
        mjob.append(lines[cnt])
        cnt+=1
        x+=1
      #check for applicant status
      line = lines[cnt].split(": ", 1)
      names = line[1].split(", ")
      name_found = "False"
      for name in names:
        if name.strip("\n") == username:
          name_found = "True"
          break
      mjob.append("Applicants: " + name_found)
      cnt+=1
      #check for saved status
      line = lines[cnt].split(": ", 1)
      names = line[1].split(", ")
      name_found = "False"
      for name in names:
        if name.strip("\n") == username:
          name_found = "True"
          break
      mjob.append("Saved: " + name_found)
      cnt+=1
  #print full job list
  if choice == 1:
    job_index = print_jobs(username, mjob, "full")
  #print list of applied jobs
  if choice == 2:
    job_index = print_jobs(username, mjob, "applied")
  #print list of unapplied jobs
  if choice == 3:
    job_index = print_jobs(username, mjob, "unapplied")
  #print list of saved jobs
  if choice == 4:
    job_index = print_jobs(username, mjob, "saved")
  #return if no jobs listed
  if len(job_index) == 0: 
    print("No jobs listed\n")
    return
  #select job to apply to or save
  while True:
    try:
      choice = int(input("Enter your choice or press 0 to return to previous page: "))
    except:
      print("Invalid choice")
      continue
    if choice == 0:
      return
    elif choice < 1 or choice > len(job_index):
      print("Invalid choice")
    else:
      break
  index = job_index[choice-1]
  #select choice for selected job
  print("Press 1 to apply to job")
  print("Press 2 to save/unsave job")
  print("Press 0 to return to previous page")
  cnt = 0
  while True:
    try:
      choice = int(input("Enter your choice: "))
    except:
      print("Invalid choice")
      continue
    if choice == 0:
      return
    #apply to job
    elif choice == 1:
      newindex = index + 7
      with open('jobs.txt', 'w') as f: 
        while cnt < len(lines):
          if cnt == index:
            f.write(lines[cnt])
            line = mjob[cnt].split(": ", 1)
            #user is poster of job
            if line[1] == username + "\n":
              newindex = 0
              print("You cannot apply to a job that you posted yourself")  
          elif cnt == newindex:
            line = mjob[cnt].split(": ", 1)
            #user already in applicant list
            if line[1] == "True":
              f.write(lines[cnt])
              print("Job already applied to")  
            #user enters in appllication information
            else:
              while True:
                grad_date = input("\nEnter your graduation date: ")
                date = grad_date.split("/", 3)
                if len(date) == 3:
                  try:
                    month = int(date[0])
                    day = int(date[1])
                    year = int(date[2])
                  except:
                    print("Invalid Format (MM/DD/YYYY)")
                    continue
                else:
                  print("Invalid Format (MM/DD/YYYY)")
                  continue
                if len(date[0]) == 2 and len(date[1]) == 2 and len(date[2]) == 4:
                  break
                else:
                  print("Invalid Format (MM/DD/YYYY)")
              while True:
                start_date = input("\nEnter your start date for working here: ")
                date = start_date.split("/", 3)
                if len(date) == 3:
                  try:
                    month = int(date[0])
                    day = int(date[1])
                    year = int(date[2])
                  except:
                    print("Invalid Format (MM/DD/YYYY)")
                    continue
                else:
                  print("Invalid Format (MM/DD/YYYY)")
                  continue
                if len(date[0]) == 2 and len(date[1]) == 2 and len(date[2]) == 4:
                  break
                else:
                  print("Invalid Format (MM/DD/YYYY)")
              paragraph = input("\nEnter a paragraph explaining why you think that you would be a good fit for this job: ")
              #add user to applicant list for selected job
              line = lines[cnt].split(": ", 1)
              if line[1] == "\n":
                f.write(lines[cnt].strip("\n") + username + "\n")
              else:
                f.write(lines[cnt].strip("\n") + ", " + username + "\n")
              print("Job successfully applied to") 
          else:
            f.write(lines[cnt])
          cnt+=1
        break
    #save/unsave selected job
    elif choice == 2:
      newindex = index + 8
      with open('jobs.txt', 'w') as f: 
        while cnt < len(lines):
          if cnt == newindex:
            line = mjob[cnt].split(": ", 1)
            #remove user from saved list for selected job
            if line[1] == "True":
              line = lines[cnt].split(": ", 1)
              names = line[1].split(", ")
              firstname = True
              newline = "Saved: "
              for name in names:
                if name != username and name != username + "\n":
                  if firstname == False:
                    newline = newline + name
                    firstname = True
                  else:
                    newline = newline + ", " + name
              f.write(newline + "\n")
              print("Job unsaved")
            #add user to saved list for selected job
            else:
              line = lines[cnt].split(": ", 1)
              if line[1] == "\n":
                f.write(lines[cnt].strip("\n") + username + "\n")
              else:
                f.write(lines[cnt].strip("\n") + ", " + username + "\n")
              print("Job saved") 
          else:
            f.write(lines[cnt])
          cnt+=1
        break
    else:
       print("Invalid choice")
  f.close()

    
#Print job postings list and return list of indexes for finding jobs in jobs.txt
def print_jobs(user, mjob, list_type):
  maxnum = 0
  cnt = 0
  job_index = []
  name_found = False
  #print full list of jobs
  if list_type == "full":
    for x in mjob:
      line = x.split(": ", 1)
      if line[0] == "User":
        if maxnum == 0:
          print("\n--- Full Job List ---")
        else:
            print("\n-----------------------")
        job_index.append(cnt)
        maxnum += 1
      elif line[0] == "Poster":
        cnt+=1
        continue
      elif line[0] == "Title":
        print(str(maxnum) + ". " + x)
      elif line[0] == "Applicants":
        if line[1] == "True":
          print("(JOB CURRENLTY APPLIED TO)\n")
      elif line[0] == "Saved":
        if line[1] == "True":
          print("(SAVED JOB)\n")
      else:
        print(x)
      cnt+=1
  #print list of applied jobs
  elif list_type == "applied":
    for x in mjob:
      line = x.split(": ", 1)
      if line[0] == "User":
        #check if user in applicant list
        if mjob[cnt+7] == "Applicants: True":
          if maxnum == 0:
            print("\n--- Applied Job List ---")
          else:
            print("\n-----------------------")
          job_index.append(cnt)
          name_found = True
          maxnum += 1
        else:
          name_found = False
      elif line[0] == "Poster":
        cnt+=1
        continue
      elif line[0] == "Title":
        if name_found == True:
          print(str(maxnum) + ". " + x)
      elif line[0] == "Applicants":
        cnt+=1
        continue
      elif line[0] == "Saved":
        if name_found == True and line[1] == "True":
          print("(SAVED JOB)")
      else:
        if name_found == True:
          print(x)
      cnt+=1
  #print list of unapplied jobs
  elif list_type == "unapplied":
    for x in mjob:
      line = x.split(": ", 1)
      if line[0] == "User":
        #check if user in applicant list
        if mjob[cnt+7] != "Applicants: True":
          if maxnum == 0:
            print("\n--- Unapplied Job List ---")
          else:
            print("\n-----------------------")
          job_index.append(cnt)
          name_found = False
          maxnum += 1
        else:
          name_found = True
      elif line[0] == "Poster":
        cnt+=1
        continue
      elif line[0] == "Title":
        if name_found == False:
          print(str(maxnum) + ". " + x)
      elif line[0] == "Applicants":
        cnt+=1
        continue
      elif line[0] == "Saved":
        if name_found == False and line[1] == "True":
          print("(SAVED JOB)\n")
      else:
        if name_found == False:
          print(x)
      cnt+=1
  #print list of saved jobs
  elif list_type == "saved":
    for x in mjob:
      line = x.split(": ", 1)
      if line[0] == "User":
        #check if user in applicant list
        if mjob[cnt+8] == "Saved: True":
          if maxnum == 0:
            print("\n--- Saved Job List ---")
          else:
            print("\n-----------------------")
          job_index.append(cnt)
          name_found = True
          maxnum += 1
        else:
          name_found = False
      elif line[0] == "Poster":
        cnt+=1
        continue
      elif line[0] == "Title":
        if name_found == True:
          print(str(maxnum) + ". " + x)
      elif line[0] == "Applicants":
        if name_found == True and line[1] == "True":
          print("(JOB CURRENLTY APPLIED TO)\n")
      elif line[0] == "Saved":
        cnt+=1
        continue
      else:
        if name_found == True:
          print(x)
      cnt+=1
  #print list of jobs posted by user
  elif list_type == "user":
    for x in mjob:
      line = x.split(": ", 1)
      if line[0] == "User":
        if line[1] == user + "\n":
          if maxnum == 0:
            print("\n--- Posted Job List ---")
          else:
            print("\n-----------------------")
          job_index.append(cnt)
          name_found = True
          maxnum += 1
        else:
          name_found = False
      elif line[0] == "Poster":
        cnt+=1
        continue
      elif line[0] == "Title":
        if name_found == True:
          print(str(maxnum) + ". " + x)
      elif line[0] == "Applicants":
        cnt+=1
        continue
      elif line[0] == "Saved":
        if line[1] == "True\n":
          print("(SAVED JOB)")
      else:
        if name_found == True:
          print(x)
      cnt+=1
  return job_index
  
  
def skills_menu(username):
  """
  Display the skills menu options
  """
  print("\n--- Learn a new skill ---")
  print("1. Skill 1")
  print("2. Skill 2")
  print("3. Skill 3")
  print("4. Skill 4")
  print("5. Skill 5")
  print("6. Return to previous page")
  # checks if user input for choice is valid
  while True:
    try:
      choice = int(input("Enter your choice: "))
    except:
      print("Invalid choice")
      continue
    if choice < 1 or choice > 6:
      print("Invalid choice")
    else:
      break
  # does selected choice
  if choice >= 1 and choice <= 5:
    print("Under construction")
    skills_menu(username)
  elif choice == 6:
    return
  else:
    print("Invalid choice, please try again")
    skills_menu(username)


def verify_account(username, password):
  """
  Find account in account list
  """
  # checks account lists for matching username and password
  musername = get_account_value(username, "username")
  mpassword = get_account_value(username, "password")
  if username == musername and password == mpassword:
      return True
    
  return False
  

# Main program
if __name__ == "__main__":
  while True:
    account = "-1"
    account = main_menu(account)
    if not account == "-1":
      additional_options(account)
