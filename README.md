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

 1 - Opening Screen
 
 ![Captura de tela 2023-11-08 220840](https://github.com/MariaPadilha32/mad-libs/assets/137770409/603e304e-5be6-4665-bac4-6e8786954747)

 2 - Asking the user to pick a subject
 
![Captura de tela 2023-11-08 220846](https://github.com/MariaPadilha32/mad-libs/assets/137770409/736f6390-3807-4d6d-a965-839481b4ca4c)

 3 - After picking the subject, the user will be requested to enter some information
 
 ![Captura de tela 2023-11-08 220904](https://github.com/MariaPadilha32/mad-libs/assets/137770409/525c0896-1380-40b7-9285-a34299a79f27)

 4 - The user should keep entering the information
 
 ![Captura de tela 2023-11-08 221204](https://github.com/MariaPadilha32/mad-libs/assets/137770409/0813cb05-8128-4695-b4ab-5be97fa85e12)

 5 - Empty inputs are not accepted (Error message)
 
 ![Captura de tela 2023-11-08 221216](https://github.com/MariaPadilha32/mad-libs/assets/137770409/c4ab1dc6-4c3a-4446-966c-73792400f192)

 6 - Input does not accept letters and numbers (Error message)
 
 ![Captura de tela 2023-11-08 221239](https://github.com/MariaPadilha32/mad-libs/assets/137770409/fa05ba4a-b1e7-4063-9150-04b0cd1e3103)

 7 - Input does not accept symbols (Error message)
 
 ![Captura de tela 2023-11-08 221335](https://github.com/MariaPadilha32/mad-libs/assets/137770409/b1e35d3c-17fa-40fb-b518-cb03dbb84cad)

 8 - Input for numbers does not accept empty inputs (Error message)
 
 ![Captura de tela 2023-11-08 221356](https://github.com/MariaPadilha32/mad-libs/assets/137770409/bc90093c-221d-4a3b-89b2-a1ccad983897)

 9 - Input for numbers does not accept letters (Error message)

![Captura de tela 2023-11-08 221407](https://github.com/MariaPadilha32/mad-libs/assets/137770409/11cfb4d9-fcc8-419c-a399-1b339d46a01f)

 10 - Input for numbers does not accept symbols

![Captura de tela 2023-11-08 221432](https://github.com/MariaPadilha32/mad-libs/assets/137770409/f4edf167-5399-4d20-87af-97bf8fede967)

 11 - Final result is delivered - after a few seconds, the question "Play again? (y/n)"

![Captura de tela 2023-11-08 221459](https://github.com/MariaPadilha32/mad-libs/assets/137770409/2620f1fa-4331-4f7f-a4a3-e6a4b8e5e6bf)
 
 12 - The user has the opportunity to choose a new subject

![Captura de tela 2023-11-08 221511](https://github.com/MariaPadilha32/mad-libs/assets/137770409/d12a44a0-3f57-4f78-8a05-6170d31f9637)
![Captura de tela 2023-11-08 221522](https://github.com/MariaPadilha32/mad-libs/assets/137770409/8f0352dd-62ae-42d6-8e23-7caea8f64b30)

 13 - After the second round

![Captura de tela 2023-11-08 221556](https://github.com/MariaPadilha32/mad-libs/assets/137770409/7134b8a8-4e78-4de6-a1f3-b7d0529d08e9)

 14 -  Error message when the user tries to input an empty message.

 ![Captura de tela 2023-11-08 221611](https://github.com/MariaPadilha32/mad-libs/assets/137770409/cc9076e1-ce2e-400e-9400-91c5f9c84daa)

 15 - Thank you message when the user ends the game - any input besides "y" will terminate the game.

![Captura de tela 2023-11-08 221623](https://github.com/MariaPadilha32/mad-libs/assets/137770409/03334312-4463-488e-95f4-d7535262a5d1)

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

 - importlib: *Purpose*: The importlib package provides a way to dynamically import other Python modules, which means I can load code from different files while your program is running. In my project, I use it to dynamically import the story modules (e.g., foodStories, moviesStories) based on the user's choice of subject. This allows the code to load the appropriate story module as needed.
   
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

  #### Validation Result:

   To validate my code I used Code Institute's [PEP8 Python Linter](https://pep8ci.herokuapp.com/)

   run.py
    -Before

![run errors](https://github.com/MariaPadilha32/mad-libs/assets/137770409/bcf77f14-d725-492f-adff-1bc81992754c)

    -after

![run clear](https://github.com/MariaPadilha32/mad-libs/assets/137770409/d89016c3-4ecd-409e-b88d-253541ba8936)

   nurseryrhymes.py
    -Before

![nursery errors](https://github.com/MariaPadilha32/mad-libs/assets/137770409/2718ad4c-8eb8-4a08-b1bd-f0e22f96449f)

    -after

![nursery clear](https://github.com/MariaPadilha32/mad-libs/assets/137770409/4a1472e2-ce4d-413d-ad35-9b03f5cf4118)

  music.py
    -Before

No screenshot was taken showing the errors.

    -after

![Captura de tela 2023-11-08 215857](https://github.com/MariaPadilha32/mad-libs/assets/137770409/9e753a1a-607a-4e40-9b8d-33987ddd3cd4)


 movies.py
    -Before

![movies errors](https://github.com/MariaPadilha32/mad-libs/assets/137770409/feafe6e7-c4f0-42f8-aa1d-2c2e356355e8)

    -after

![movies clear](https://github.com/MariaPadilha32/mad-libs/assets/137770409/3f2a71e7-9172-49b9-8857-0274c6ed75b1)

 food.py
    -Before
    
![food errors](https://github.com/MariaPadilha32/mad-libs/assets/137770409/b474151f-61a2-4bcf-beaf-dabae42eb0b6)


    -after

![food clear](https://github.com/MariaPadilha32/mad-libs/assets/137770409/b68ab2d3-2030-40b0-85ce-eaf5fa466948)


randStories.py
    -Before

![random errors](https://github.com/MariaPadilha32/mad-libs/assets/137770409/01868901-e826-4a06-95d2-0a6eb2e5275e)


    -after

![random clear](https://github.com/MariaPadilha32/mad-libs/assets/137770409/751f4966-f22b-41d2-8850-0e7c219ec2ef)


utils.py
    -Before

![utils errors](https://github.com/MariaPadilha32/mad-libs/assets/137770409/a2232e53-682e-4d92-9134-821c3be9243d)

    -after

![utils clear](https://github.com/MariaPadilha32/mad-libs/assets/137770409/38973048-e4c3-495b-8d32-3c92deb16333)

## Bugs:

 I dedicated numerous hours to meticulously test every aspect of this project, ensuring that every feature and functionality was working as intended. The testing phase was a crucial part of the development process, during which I left no stone unturned to identify and address potential issues. This exhaustive testing allowed me to deliver a more robust and reliable application, and I am confident that it will provide a smooth user experience. 
 
 Bugs Encountered: During the development of this project, I encountered several bugs that required debugging. While I didn't document all of them, I'd like to highlight a few key issues and how they were resolved.

Issue 1: The biggest issue I had was on my main function, at the time it looked like this:

![Captura de tela 2023-11-09 090516](https://github.com/MariaPadilha32/mad-libs/assets/137770409/b59f073f-0737-489d-83d1-583da790879d)

After improvement the final result is:

![Captura de tela 2023-11-09 091128](https://github.com/MariaPadilha32/mad-libs/assets/137770409/3ee7e08d-e634-4a84-a8a0-6176017932f9)

The main change are the the Function Calls, the reason is that direct function calls are more straightforward and align with the modular structure of the code. This change simplifies the logic and improves code readability.

 Issue 2: Non-functional Stories: One significant bug I encountered was that the stories were not working as expected. After thorough investigation, I discovered that this was due to my failure to call the necessary functions. This issue was resolved by adding the missing function calls in the appropriate places in the code.

 Issue 3: Small Typos: In the process of debugging, I also encountered several smaller bugs that were often caused by misspellings and minor syntax errors. These seemingly insignificant issues can have a significant impact on the code's functionality. Paying attention to details and thoroughly reviewing the code proved essential in resolving these bugs.

 Issue 4: Not having the correct Packages and Modules in place, once I realized my error it was a very easy fix.

 ![Captura de tela 2023-11-06 213812](https://github.com/MariaPadilha32/mad-libs/assets/137770409/e1f5aee4-034a-48a5-bcf3-ddce8cac9180)
![Captura de tela 2023-11-06 210810](https://github.com/MariaPadilha32/mad-libs/assets/137770409/a665f4a4-0577-4544-921b-3921fbbf38ba)
![Captura de tela 2023-11-06 210436](https://github.com/MariaPadilha32/mad-libs/assets/137770409/d620d695-2658-498b-92ea-eb61f50ba099)
![Captura de tela 2023-11-05 204541](https://github.com/MariaPadilha32/mad-libs/assets/137770409/1d29906e-574c-4081-8f78-3cdbc64f77ba)
![Captura de tela 2023-10-27 190250](https://github.com/MariaPadilha32/mad-libs/assets/137770409/59bd3894-6809-476f-96f1-4dc94219a043)

## Debugs

 - Thorough Testing: Comprehensive testing is vital in identifying and resolving bugs. Ensure that your code is rigorously tested at each stage of development.
 - Logs and Comments: Incorporate detailed logging and comments in MY code to help track the flow of execution. This is invaluable in pinpointing issues.
 - Consult Documentation: Whenever you encounter an issue related to a library or framework, consult the official documentation. It can provide insights and solutions.
 - Learning from Bugs: Each bug is an opportunity for learning and growth. After solving an issue, reflect on what caused it and how to prevent similar bugs in the future.
   
## Deployment

 Mad Libs was created using Codeanywhere and Deployed on Heroku.

 The Deployment process was following step by step the instruction given during [Love Sandwiches](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/) walk-throgh project. 

### GitHub Deployment

 * Sign Up for a GitHub Account: Begin your journey by registering for a free GitHub account at GitHub.com.

 * Create a New Repository: On the main page, click the "+" button and choose "New Repository."

 * Configure Repository Details: Provide a name, description, and set your repository to "public."

 * Access Repository Settings: Navigate to the settings of your newly created repository.

 * Set Up GitHub Pages: Locate the "GitHub Pages" section within your repository settings.

 * Choose Deployment Branch: Select the "main" branch as the one for deployment.

 * Save Your Changes: Save the settings to kickstart the deployment process.

 * Wait for Deployment: Wait for the confirmation message that signals a successful deployment.

 * Access Your Live Site: Once deployed, find the link to your live website.

 * Share the Link: Share the provided link with others.

 * Explore the Deployed Website: Experience your live site by visiting the link.
   
### Heroku Deployment

 * Register on Heroku: Begin the journey by signing up for a Heroku account.

 * App Creation: Initiate the creation of a new app on the Heroku platform.

 * Pick the Hosting Location: Specify the desired hosting region for the app.

 * App Configuration: After creating your app, proceed to its settings.

 * Set Environment Variables: Within the settings, establish environment variables. Create a variable named "PORT" and assign it the value 8000.

 * Amplify Functionality with Buildpacks: Enhance your application's capabilities by adding these buildpacks:

  - Incorporate the Python buildpack.
  - Specify "python" and save your changes.
  - Integrate the Node.js buildpack.
  - Specify "nodejs" and save your changes.

 * Add the Python buildpack.
   
 * Enter "python" and save changes.
   
 * Add the Node.js buildpack.
   
 *  Enter "nodejs" and save changes.
   
 * Deployment Setup: Navigate to the "Deploy" section.

 * Seamless GitHub Integration: Opt for GitHub as the preferred deployment method.

 * Link to Your GitHub Repository: Locate your GitHub repository and establish a connection with Heroku.

 * Manual Deployment: Execute a manual deployment of your chosen branch.

 * Explore Your Deployed App: Once the deployment process concludes, click "View" to access and explore your live application.

## Credits 

### Codes

- The Mad Libs was inspired ny a few Youtube tutorials: [Python Beginner Project #1- Build a Mad Libs Generator | Practice Python Projects](https://www.youtube.com/watch?v=vFNZvZSOqlY).


### Content

 - The Music from music.py, the Doctor's note from randStories.py and the Nursery Rhymes from nurseryrhymes.py were used from [MadTakes](https://www.madtakes.com/index.php?page=-1)

## Special Thanks

 - I would like to express imense gratitute to my friend Lucas, who gave me valuable advice.
 - I would like to thank my mentor [Harry Dhillon] (https://github.com/Harry-Leepz), his guidence has been incredibly helpful  during moments of significant challenge.
 - Special thanks are also due to my classmates on Slack, who have consistently provided their support, assistance, and valuable feedback. Their collective spirit of collaboration has been invaluable.
