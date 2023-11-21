def convert_age(age_in_years):
   
    days = age_in_years * 365.25
    hours = days * 24

    return days, hours


age_of_person = 25
days_lived, hours_lived = convert_age(age_of_person)

print(f"The person, aged {age_of_person} years, has lived approximately:")
print(f"- {days_lived:.2f} days")
print(f"- {hours_lived:.2f} hours")
