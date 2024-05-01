package com.example.projet;

import static com.example.projet.R.*;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity1 extends AppCompatActivity  {

    private Button button2;
    private Button button3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(layout.activity_main1);
          button2 = findViewById(R.id.button2);

          button3 = findViewById(R.id.button3);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent o = new Intent(MainActivity1.this,MainActivity.class);
                startActivity(o);
            }
        });
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent l = new Intent(MainActivity1.this,MainActivity4.class);
                startActivity(l);


            }


        });

            }


    }




