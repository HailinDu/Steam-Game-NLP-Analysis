# Steam-Game-NLP-Analysis (Civlization-6)
![Civ6](https://raw.githubusercontent.com/HailinDu/Steam-Game-NLP-Analysis-Civlization-6/main/Images/Civ6.PNG)
### Steam Game Web Scraping
The purpose of this project to build a web scraping script to obtain review data related to the game you are interested in and do an NLP analysis to uncover why players like or dislike this game.


![Review](https://raw.githubusercontent.com/HailinDu/Steam-Game-NLP-Analysis-Civlization-6/main/Images/Reviews.PNG)
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
![word](https://raw.githubusercontent.com/HailinDu/Steam-Game-NLP-Analysis-Civlization-6/main/Images/Words_Importance.PNG)
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
4. Mac book users may encounter gaming issues
5. DLC, updates, and extended version
6. Ask for a fix
7. Comparison with Civilization 5

### Models Comparsion 
We have total 5 models in this NLP Analysis using Text without Stopswords:
1. Naive Bayes - 80.07% accuracy 
2. Random Forest - 78.48% accuracy 
3. Logistic Regression - 81.76% accuracy 
4. Stochastic Gradient Descent - 81.81% accuracy 
5. Support-Vector Machine - 82.51% accuracy 

![models](https://raw.githubusercontent.com/HailinDu/Steam-Game-NLP-Analysis-Civlization-6/main/Images/Models.png)

## Flask Development 
We can create a web application for anyone who is interested in this game to see if the game fits the gamer by typing a few words or a few sentences. 

**Predict - Result 1**

![predict1](https://github.com/HailinDu/Steam-Game-NLP-Analysis/blob/main/Images/Predict1.PNG)
![result1](https://github.com/HailinDu/Steam-Game-NLP-Analysis/blob/main/Images/Result1.PNG)

**Predict - Result 2**
![predict2](https://github.com/HailinDu/Steam-Game-NLP-Analysis/blob/main/Images/Predict2.PNG)
![result2](https://github.com/HailinDu/Steam-Game-NLP-Analysis/blob/main/Images/Result2.PNG)

##### Reference
[israel-dryer](https://github.com/israel-dryer/Steam-Game-Review-Scraper) - Steam-Game-Review-Scraper
