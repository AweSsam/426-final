# Musical Chairs: Seat and Room Admin View

> > Team Members: Sameera Poddutoori, Dharshini Raman, Kayla Casey, Tyler Smith

## Overview

We plan on adding additional functionality to the CSXL website that allows CSXL administrators to better manage rooms and their respective seats.

##### Some features we will add will be:

- A User Interface graphic that shows a map of rooms with their respective seats in the XL.
- Functionality to list, add, and delete rooms and seats in the XL.

> We have the data that supports the implementation of this feature in the user interface. We strongly believe that adding these features will greatly benefit administrators in effectively managing the spaces within the XL system.

#### Key Personas:

- Sol Student - Sol is a CS major who will visit the CSXL space. Sol can view the layout of the rooms and seats, but has no access to edit.
- Amy Ambassador - Amy is an ambassador to the CSXL who is volunteering at the check-in desk. They have the ability to view the available rooms and seats in the CSXL to better manage reservations and the space, but Amy does not have access to add or delete rooms or seats.
- Rhonda Root - As an administrator who oversees the CSXL, Rhonda also has access to the same interface and permissions as Amy in adding, deleting, and viewing the space.

#### Stories:

- Story A: View
  As Sol, Amy, or Rhonda, I will be able to view an interactive page that display the rooms in the CSXL space and see which areas have seating. The seats in these rooms will be identified through a numbering system and the display will be used throughout the execution of this page. This feature enables all personas to have a visual representation of the space available to them.

- Story B: Add
  As Rhonda, I will be able to add new rooms and seating to the CSXL space and add them to specific locations. This feature will be used when there is a necessity to add extra spaces. This feature allows admin to ensure an accurate layout when utilizing spaces to add new seating or rooms.

- Story C: Delete
  As Rhonda, I will be able to delete exisiting rooms and seating to the CSXL space and remove their existence. This feature will be used least frequently, as we continue to expand the CSXL space. This feature allows admin to prioritize layout and save space.

#### Mock-up:

The focus of this project is to implement seat and room views for our internal and external customers. Below is a mock-up of the view Amy Ambassador would see when looking at our page. Our vision is to have a model of the CSXL lab with accurate table and chair locations, where the chairs are labeled by a number and their status: available, occupied, deleted, etc... On the lefthand side is a menu of different seating zones and key for the seat colors on the map. The menu for the seating zones is clickable and will trigger a dropdown where Amy can change the status of the seats which will update in the map.

We intend to have a view for students as well, which will only include the status of the seats and a key.

Our stretch goal for this implementation is where Amy would be able to click directly on the seat that she wants to modify and will be able to change the status of the seat. This feature would not be available to students. If we wanted the map to be interactive for students, we would work towards allowing them to reserve a chair if it is open or to end their reservation when they leave.

![Alt text](<Comp 590 mock-up -37.jpg>)
