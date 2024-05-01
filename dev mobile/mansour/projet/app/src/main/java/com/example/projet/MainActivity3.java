package com.example.projet;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity3 extends AppCompatActivity implements View.OnClickListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        Button button = findViewById(R.id.button8);
        button.setOnClickListener(this);
    }
    @Override
    public void onClick(View v){
        Intent u= new Intent(MainActivity3.this,MainActivity1.class);
        startActivity(u);

    }
}