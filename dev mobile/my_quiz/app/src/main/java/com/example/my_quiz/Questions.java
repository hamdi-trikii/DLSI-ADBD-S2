package com.example.my_quiz;

public class Questions {
    private String mQuestions[]={
            "Guess the Logo?",
            "You Can Guess the Logo?",
            "Can you this one?",
            "Guess the Logo?",
            "Guess the Logo?",
            "Can you this one?",
            "You Can Guess the Logo?",
            "You Can Guess the Logo?",
            "Can you this one?",
            "Guess the Logo?"
    };
    private String mChoice[][]={
        {"AMD","CMD","KMD"},
        {"Mobile","Android","Smart Phone"},
        {"playstore","Android","Software"},
        {"Chrome","Android","Software"},
        {"Dell","Mi","HP"},
        {"Drop Box","Android","Software"},
        {"Box","Android","Edge"},
        {"Mi","Framework","Facebook"},
        {"Flutter","Framework","Cross Platform"},
        {"Git","Framework","Github"}

    };
    private String mImages[]={
      "q1", // AMD image
      "q2", // Android image
      "q3", // app store image
      "q4", // chrome image
      "q5", // Dell image
      "q6", // Drop Box image
      "q7", // Edge image
      "q8", // Facebook image
      "q9", // Flutter image
      "q10"/* Github image */
    };
    private String mQuestionsType[]={
            "radiobutton",
            "radiobutton",
            "radiobutton",
            "radiobutton",
            "radiobutton",
            "radiobutton",
            "radiobutton",
            "radiobutton",
            "radiobutton",
            "radiobutton",
    };
    private String mCoorectAnswers[]={
            "AMD",
            "Android",
            "playstore",
            "Chrome",
            "Dell",
            "Drop Box",
            "Edge" ,
            "Facebook" ,
            "Flutter" ,
            "Github",
    };

    public String getQuestions(int q) {
        String questions = mQuestions[q];
        return questions;
    }

    public String[] getChoice(int q) {
        String[] choice = mChoice[q];
        return choice;
    }

    public String getImages(int q) {
        String img = mImages[q];
        return img;
    }

    public String getType(int q) {
        String type = mQuestionsType[q];
        return type;
    }

    public int getLength(){
        return mQuestions.length;
    }

    public String getCoorectAnswers(int q) {

        String correct = mCoorectAnswers[q];

        return correct;
    }
}
