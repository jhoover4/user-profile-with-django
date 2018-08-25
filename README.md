# User Profile with Django

This is the seventh project in Treehouse Python tech degree.

Will be hosted on Heroku upon completion.

## Description

For this project, you’ll build a form that takes in details about a registered user and displays those details on a 
profile page. The profile page should only be visible once the user has logged in. The profile page should include 
first name, last name, email, date of birth, confirm email, short bio and the option to upload an avatar.

You’ll also set up validation for email, date of birth and the biography. You’ll also create a "change password page" 
that updates the user’s password. This page will ask for current password, new password and confirm password. Set up 
validation which checks that the current password is valid, that the new password and confirm password fields match, 
and that the new password follows the following policy:

- Must not be the same as the current password
- Minimum password length of 14 characters.
- Must use of both uppercase and lowercase letters
- Must include of one or more numerical digits
- Must include of special characters, such as @, #, $
- Cannot contain the username or parts of the user’s full name, such as his first name

## Extra Credit

- Add additional form fields to build a more complex form with additional options,
such as city/state/country of residence, favorite animal or hobby.
- JavaScript is utilized for a date dropdown for the Date of Birth validation feature.
- JavaScript is utilized for text formatting for the Bio validation feature.
- Add an online image editor to the avatar. Include the basic functionality: rotate, crop and flip. PNG mockup supplied.
- A password strength “meter” is displayed when validating passwords.