# Steam-Game-NLP-Analysis (Civlization-6)

### Steam Game Web Scraping
The purpose of this project to build a web scraping script to obtain review data related to the game you are interested in and do an NLP analysis to uncover why players like or dislike this game.

### Dataset
The dataset is obtained from Steam under the Civlization 6 ***browse all reviews page***. We will be using the browse all reviews page and replace the game id that you are interested in. In Each game main page, the url will contain the game id in the format of **/app/game-id-number/game-name/** like this example https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/.

The dataset after web scarping contains 10663 reviews with the following columns:
* User Steam ID
* Profile URL
* Review Content
* Review Length (Approximately)
* Recommended or Not Recommended
* Play Hours on Record
* Date Posted
* Number of Award of a Review
* Number of Helpful and Funny of a Review

### Hypothesis Test Findings
1. Players who recommend playing Civilization 6 **DOES tends** to have longer hours of play in record compare to players who don't recommend it.
2. Players who don't recommend playing Civilization 6 **DOES tends** to write longer reviews in overall word counts and character lengths compare to players who recommend playing it.

### What about People Like or Dislike playing Civilization 6?
#### Recommend Side:
1. The word “Gandhi” being mentioned a lot because of the Internet meme – “Nuclear Gandhi” - Fans love this Joke!
2. The word “gud” is related to “git gud”, a slang refer to getting better at a skill, especially in video games - Fans want to improve their skills!
3. They also like:
     * The playing style of "Nuclear Bomb"
     * Graphic
     * Long hours of Play
     * Replayability 
     * Uniqueness of Every Game Turn
#### Not Recommend Side:
1. The game has spyware that collects players' information
2. the ai issue
3. the game will crash and unplayable
4. Mac book users 
5. DLC, updates, and extended version
6. Ask for a fix
7. Comparison with Civilization 5

