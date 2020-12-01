# trav

## Models

#### User Role
- Admin
- Staff
- Normal

#### User Model
- Username
- Email
- Phone Number (International format for easy OTP Verification)
- Location (Auto Detection using JS)
- Profile Photo
- Date & Time Created
- Date & Time Updated
- Date & Time Deleted (Soft Delete)
- Role (Normal as default) * User can't see this during sign up.. only admin can change
- Status (Active / Disabled) *prefferbly boolean

#### Listing Category Model
- name (e.g Laptops/ Clothes/ TVs etc)

#### Listing Model
- id (uuid)
- user (FK User Model)
- category (FK Category Model)
- traveller_origin (Picks the location from user Model)
- destination (Choices of Countries / Major cities as set by Admin)
- description of listing
- cost to purchase listed item (Null before booking)
- cost to move item (Has to be set up)
- delivery_date
- date_posted
- approved (True/ False - admin will approve after review)
- status (booked/ available)
