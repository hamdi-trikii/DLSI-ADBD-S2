package com.example.my_first_game;

public class Questions {


    private String mQuestions[] = {

            "Guess the Logo ?",
            "You Can Guess the Logo ?",
            "Can you this one ?",
            "Guess the Logo ?",
            "Guess the Logo ?",
            "Can you this one ?",
            "You Can Guess the Logo ?",
            "You Can Guess the Logo ?",
            "Can you this one ?",
            "Guess the Logo ?"
    };

    private String mChoice[] [] = {

            {"AMD","CMD","KMD"},
            {"Smart Phone","Android","Mobile"},
            {"App Store","Android","Software"},
            {"Chrome","Android","Software"},
            {"DELL","MI","HP"},
            {"Drop Box","Android","Software"},
            {"Box","Android","Edge"},
            {"MI","Framework","Facebook"},
            {"Flutter","Framework","Cross Platform"},
            {"Git","Framework","GitHub"}
    };


    private String mImages[] = {
            "q1",  // AMD image
            "q2",  // Android image
            "q3",  // App Store image
            "q4",  // Chrome image
            "q5",  // Dell image
            "q6",  // Drop Box image
            "q7",  // Edge image
            "q8",  // Facebook image
            "q9",  // Flutter image
            "q10",  // GitHub image

    };

    private String mQuestionsType[] = {
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


    private String mCoorectAnswers [] = {
            "AMD",
            "Android",
            "App Store",
            "Chrome",
            "DELL",
            "Drop Box",
            "Edge",
            "Facebook",
            "Flutter",
            "GitHub"
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
