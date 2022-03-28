# Warships Battle #
**Warships Battle is a terminal game written in Python, wich runs in the Code Institute mock terminal on Heroku** 

**Users can try to compete against computer by finding all battleships that are hidden under computer map.
Each battleship occupies one square on the board** 
[Click to live version of this project](https://warships-battle.herokuapp.com/)
![Am I responsive screen-shot](/assets/images/am-i-responsive.png)

 ## How to play
 Ultimate Battleships is based on the classic pen-and-paper game. More about it on [Battleship game](https://en.wikipedia.org/wiki/Battleship_(game))
 After you enter your nickname, you will see a short introduction and then you can start the game by pressing ENTER
 In the introduction is represented also the legend of the map  
    *? as undiscovered location
    *X as HIT!
    *O as MISS!
![Short introduction](/assets/images/intro.png)
 On your map you can find your ship's marked as @ sign.
 Computer ship's are hidden on it's map unless they are hitted.
 You have maximum 30 turns to hit all 6 ships from Computer map.
 The winner is the one who hit all ships first
## Features
* Random board generation
    * Ships are randomly placed on both the player and computer boards
    * The player cannot see where the computer's ships are
 ![Maps](/assets/images/maps.png)
 * Play against the computer
 * Accepts user input
 * Input validation and error-checking
    * You cannot enter coordinates outside the size of the board
    * You must enter numbers
    * You cannot enter the same guess twice
   ![Input validation](/assets/images/input-validation.png)
 ## Testing
 I have manually tested this project by doing the following:
 * Passed the code throungh a PEP8 linter and confirmed there are no problemns
 * Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
 * Tested in my local terminal and the Code Institute Heroku terminal
 ## Validator Testing
 * PEP8
    * No errors were returned from PEP8online.com
## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
* Steps for deployment:
     * Fork or clone this repository
     * Create a new Heroku app
     * Set the buildbacks to Python and NodeJS in that order
     * Link the Heroku app to the repository
     * Click on Deploy
  ## Credits
  * Code Institute for the deployment terminal
  * All the tutorials you can find on google about battleship games for understanding how to write logic in writing code
  * Stack Overflow, w3schools for examples
  
