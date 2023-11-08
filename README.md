# Mad Libs

## Live Website

[Mad Libs](https://mad-libs-d618b9c6272d.herokuapp.com/)

## Repository

[GitHub](https://github.com/MariaPadilha32/mad-libs)

## About

Welcome, 

 To the Mad Libs Game, a Python project developed as the third project for the Code Institute course. This is a fun and interactive word game that lets players create humorous and often silly stories by inputting words such as nouns, verbs, colors, animals, and numbers. These words are then inserted into a story template, providing entertainment.

## UX: User experience:

 - As a user of the site, I want the content to be in English for better understanding.
 - As a user of the site, I desire a game that provides entertainment and serves as a distraction.
 - As a user of the site, I value clear and concise rules to gain a better understanding of the game's mechanics.
 - As a user of the site, I appreciate an easy-to-play game, and I expect to grasp it after the first round.
 - As a user of the site, I would like the option to replay the game once I've completed it.

## Initial concept:

 My initial idea for this project was to develop a user-friendly website that would serve as a platform for people seeking an easy and entertaining game, allowing them to enjoy a moment of laughter and creativity with the unpredictable and often hilarious results of Mad Libs.

### Target Audience:

 The target audience for this project is diverse and includes:

 - English language learners who can use Mad Libs as an engaging educational tool to better understand nouns, verbs, adjectives, etc.
 - Friends and groups looking for an enjoyable and light-hearted activity to have a laugh.
 - Anyone in need of a quick and fun distraction from their daily routine.

### Key Objectives:
 - Provide an easy-to-understand and easy-to-play game: The primary goal is to make Mad Libs accessible to users of all ages and students with a minimum of a B1 knolodge of English. The game should be intuitive and enjoyable for both newcomers and experienced players.

 - Create a clean and user-friendly platform: The website's design should be clean and easy on the eyes. It should have an intuitive user interface, expcted the user would understand the game after the first round.

 - Attract and engage users seeking relaxation and entertainment: We aim to create a space where users can unwind, have a good time, and create an crazy and hilarious story.

## Wireframes

 The wireframes are intentionally kept very simple, with clear, direct, and concise information. Additionally, a 'sleep' function is used for a few seconds to give the user the chance to read the necessary information.

 The first wireframe represents the initial page, which includes a welcome message, rules, and a prompt for the user to choose a subject to play. 
![first](https://github.com/MariaPadilha32/mad-libs/assets/137770409/c68d7e2f-5c36-4039-9c68-1b33ca4df252)

 The second wireframe illustrates what the user would see after selecting a subject and entering the keywords. In this case, the user would receive the result of their story and would be asked if they'd like to play again.
![second](https://github.com/MariaPadilha32/mad-libs/assets/137770409/473f72a4-38fc-4a4d-bc72-ba70af617d19)

 If the user's response to the previous question is 'y,' they will return to the subject selection screen and repeat the steps mentioned above. 
![third](https://github.com/MariaPadilha32/mad-libs/assets/137770409/4ee7af07-a029-44b7-a942-7a4d1bb5ee29)

Should the user's answer to the above question be anything other than 'y,' the game will conclude with a friendly message inviting the user to visit my [GitHub repository](https://github.com/MariaPadilha32?tab=repositories). 
![fourth](https://github.com/MariaPadilha32/mad-libs/assets/137770409/651251ee-91fa-425d-b2fc-a3828adcc21d)


## Flow Chart:

[Flow Chart](https://lucid.app/lucidspark/c0d343cc-e2c9-4a59-bc48-6a28f06441e9/edit?invitationId=inv_5f2f08ae-f60d-4907-851e-2313408f12a3&referringApp=slack&page=0_0#) created using [Lucid App](https://lucid.app/users/login#/loggedOut).

![Captura de tela 2023-11-08 130248](https://github.com/MariaPadilha32/mad-libs/assets/137770409/be6c2b39-db3d-4710-af1f-9670f55b4234)

  A short explanation for the FLow Chart above:
 
 1-  When the user runs the program, they will encounter a "welcome message" and the game rules. In Python, this part of the function is straightforward and direct.
 
 2- The second part of the Flow Chart involves the user selecting a subject to play. In Python, this is the primary function that drives the game.
 
 3- The third part includes the various subjects. In Python, each subject is stored in a separate file, with each having its own function separated from the main function.
 
 4- The fourth part prompts the user to enter multiple words. For each subject, the function is located in a different file(as mentioned above).
 
 5- In the fifth part, the Mad Lib will be generated and displayed to the user. Additionally, the user will be asked if they want to continue playing or end the game.
 
 6- The sixth part comes into play if the user decides to play again. The screen is cleared, and the user is presented with options to select a subject (returning to step 2 in the flow chart).
 
 7- The seventh part is activated if the user decides to end the game. In this case, the user will receive a farewell message, and the function will pause and stop.

## How to play

 Mad Libs, a play on "ad lib" (from Latin "ad libitum," meaning "as you wish"), is a word game in which one player prompts another to provide a list of words to substitute for blanks in a story. The resulting story, with these word substitutions, often has a humorous and absurd effect when read aloud.

 - The game starts after the welcome message and explanation is presented.
   - The user is prompted to select one of five subjects, but they won't know the specifics of the story for each subject:
       1) Nursery Rhymes (a twist on "Mary had a little lamb")
       2) Music  (an interpretation of "Smelly Cat")
       3) Movies (a humorous version of "A Nightmare on Elm Street")
       4) Food (a playful recipe for Classic Guacamole)
       5) Random (an unconventional doctor's note)
   - After choosing a subject, the user is asked to provide inputs. They will be prompted to enter specific words or phrases, such as "Enter a Girl's Name," "Enter an Animal," and so on, until all required inputs are provided.
   - Once all inputs are collected, the user is presented with a whimsical and likely humorous story.
   - If the user attempts to submit an empty input, they will receive a message like **Please enter a single word.** or **Please enter only integer numbers.**
   - If the user enters a symbol or number when the input is expected to be a specific type of word, they will receive the message **Please enter a single word.**.
   - If the user inputs a word when a number is expected, they will receive the message **Please enter only integer numbers.**.
   - The game recognizes the distinction between numbers and letters, accepts gibberish, does not correct misspellings, and does not allow words with symbols or space (e.g., "ice-cream" or "Burger King").
   - The game does not have a scoring system; its primary aim is to provide entertainment and humor.
   - At the end of the game, the user has the option to decide whether they'd like to play again or not.

## Features

## Technologies Used:

  ### Languages:
  
   - [Python](https://www.python.org/) was used to create the game itself.

  ### Programming Paradigm:
 
 This project follows a combination of programming paradigms, primarily embracing Procedural Programming and Modularization.

 - Procedural Programming: The code is structured to follow a sequence of statements or commands to achieve a desired output. Functions (methods) are used to encapsulate specific behavior and logic. In this project, functions play a crucial role in managing the game's flow and functionality.

 - Modularization: The project uses a modular approach by separating different subject areas into separate files (e.g., food.py, movies.py, nurseryrhymes.py, etc.). Each file serves as a module, encapsulating related code, which promotes organization and maintainability.

 While the project leans towards procedural programming, the use of modularization allows for a more organized and maintainable codebase, enabling easier management of different aspects of the game.

  ### Other Tools:
  
 - [GitHub](https://github.com/): Used to host the source code of the website
 - [Codeanwhere](https://id.codeanywhere.com/realms/default/protocol/openid-connect/auth?client_id=dashboard&redirect_uri=https%3A%2F%2Fapp.codeanywhere.com%2F&state=30f86e0e-e3b1-4549-846b-d328c0c1fd83&response_mode=fragment&response_type=code&scope=openid&nonce=cc710acb-c72a-4741-87a1-002f681960ce): IDE used to develop the website
 - [Heroku](https://www.heroku.com/auth/login): Used to deploy.
 - [Lucid](https://lucid.app/documents#/documents?folder_id=recent): Used for the flow chart.

  ### Packages:
  
![Captura de tela 2023-11-08 203856](https://github.com/MariaPadilha32/mad-libs/assets/137770409/1ba78a1c-9ffa-4365-ab63-dd2986f5ce96)

 - imporlib: *Purpose*: The importlib package provides a way to dynamically import other Python modules, which means I can load code from different files while your program is running. In my project, I use it to dynamically import the story modules (e.g., foodStories, moviesStories) based on the user's choice of subject. This allows the code to load the appropriate story module as needed.
   
 - Os: *Purpose*: The Os package provides a way to interact with the operating system. It can use to perform tasks such as clearing the screen, working with directories, or executing shell commands. In my project, I use Os to clear the screen based on the user's operating system (with 'cls' for Windows and 'clear' for other systems). This helps keep the user interface clean and clear when the user decides to play again.
   
 - Time: *Purpose*: The time package is used for time-related functions. In my code, I specifically import the sleep function from the time package. In my project, the sleep function is used to introduce pauses in the game. For example, I have added delays between messages or questions to give the user time to read and respond, creating a more user-friendly experience.

   ### Modules:
   
  - food: Handles food-related Mad Lib and input collection.
  - movies: Manages movie-related Mad Lib and input collection.
  - nurseryrhymes: Provides nursery rhyme-based Mad Lib and input collection.
  - randStories: Includes Mad Lib with random themes and associated input collection.
  - music: Manages music-themed Mad Lib and input collection.
  - utils: Houses utility functions, such as get_non_empty_input and get_numeric_input, to ensure correct and user-friendly input from players.
   
## Testing:

  ### Bugs:

  ### Code Validation

  #### Validation Result:

## Debugs

## Deployment

## Content

## Credits 

## Special Thanks

## Acknowledments 


