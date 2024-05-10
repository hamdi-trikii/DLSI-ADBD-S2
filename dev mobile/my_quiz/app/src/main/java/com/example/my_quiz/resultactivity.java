package com.example.my_quiz;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.content.Intent;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class resultactivity extends AppCompatActivity {
    TextView txtCorrectText;
    TextView txtPercentText;
    private int totlalQuestions;
    private int finalScore;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_resultactivity);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        //***********************************************
        txtCorrectText=findViewById(R.id.correct_textview);
        txtPercentText=findViewById(R.id.percent_textview);

        Intent intent =getIntent();
        totlalQuestions=intent.getIntExtra("totalQuestions",0);
        finalScore=intent.getIntExtra("finalScore",0);
        int mPercentScore=finalScore*100/totlalQuestions;
        txtPercentText.setText(String.format("%s%%",Integer.toString(mPercentScore)));
        String final_Score_Text=getString(R.string.txtCorrectScore,finalScore,totlalQuestions);
        txtCorrectText.setText(final_Score_Text);


    }

    public void restartGame(View view) {
        super.onBackPressed();
    }
}