# Musical Chairs: Seat and Room View Specs

Team Members: Sameera Poddutoori, Dharshini Raman, Kayla Casey, Tyler Smith

> Descriptions and sample data representations of new or modified model representation(s) and API routes supporting your feature’s stories

We used the existing models in seat_details.py and room_details.py, and created new API routes to support our Seat and Room View feature. Our new API routes are in backend/api/room_view.py. We created APIs to get, add, and delete rooms and seats. This is testable in our Fast API docs page.

As we decided at the beginning of this project, we extended the seat and room details models to include new fields: has_whiteboard, has_projector, has_monitor, and sit_stand. After extending these models, we had to extend our entities too.

> Description of underlying database/entity-level representation decisions

We did not create any new entities for rooms or seats because there already existed functioning entities for these models (room_entity and seat_entity). In the second part of sprint 1, we decided to extend these entities to reflect the added fields we intended to add into the seat and room models. After extending these entities and updating their models, we fixed the database to correctly map these new fields accordingly.

> At least one technical and one user experience design choice your team weighed the trade-offs with justification for the decision (we chose X over Y, because…)

One technical choice we made was not allowing Ambassadors to add and delete rooms and seats. We chose to not allow Ambassadors to have this power because this seemed to be more of an admin level permission. We would've had to add another view just for Ambassadors if we allowed them add and delete seats and rooms, but it just didn't seem like a neccessary permission for Ambassadors to have. We chose for Ambassadors to have the same level of permissions as students, which consists of simply viewing available seats and rooms. This will reduce the likelihood of any unwanted tampering with data that should be managed by admins.

One user experience design choice we made to create a table over a list to display what seats and tables are available. We choose a table over a list because a tabular view offers a more understandable layout and is easier to populate with fields rather than a list. Using a table also allowed us to use the codebase for formatting since tables are commonly used and pre-styled in the application.

Another user experience design choice we made was formatting the add room and seats forms to be next to one another and below the room and seats tables so that admin would be able to easily reference the forms or tables when using our page. Some fields in the forms require admin to assign a field to an already existing field in the table (for example when adding a seat you need to specify a room id), so having this layout allows users to easily fill out forms.

Another technical design choice we made was the implementation of a user interface to visually display a room layout with seats populated into it in a grid view. We chose to use a double array to create the grid view instead of cartesian coordinates, meaning that the coordinate system starts at the top left. For example, a seat at (0,0) is seen in the top left corner instead of the bottom left corner. This choice simplified the code and math we needed to make this feature work. With the time constraint that we had, we would not have been able to figure out how to correctly map the seats to this coordinate system, and in the future if we continued this project this is something we would try to change.

> Development concerns: How does a new developer get started on your feature? Brief guide/tour of the files and concerns they need to understand to get up-to-speed.

The files that a developer would need to review to get started on our feature would be:

- frontend/src/app/room-view
- frontend/src/app/seat-details-model-component
- frontend/src/app/admin/room-view
- frontend/src/app/room-view.service.ts
- backend/services/room_view.py
- backend/services/coworking/seat.py
- backend/services/coworking/room.py
- backend/models/coworking/seat_details.py
- backend/models/coworking/room_details.py
- backend/entities/coworking/seat_entity.py
- backend/entities/coworking/room_entity.py
- backend/api/room_view.py

It would be important for them to review the premade models and entities in the backend, and spend a lot of time in our service classes to understand the functionality of our feature. A developer should look at our service classes to understand how our methods function, and they should spend a lot of time with our frontend code because of the important that our frontend plays in our feature.