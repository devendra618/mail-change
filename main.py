def mail_domain_change(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_mail = email[:index] + "@" + new_domain
        return new_mail
    return email
        
print(mail_domain_change("devendradhakad@gmail.com","gmail.com","dhakad.com"))
