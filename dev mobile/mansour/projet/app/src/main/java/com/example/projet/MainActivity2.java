package com.example.projet;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity2 extends AppCompatActivity implements View.OnClickListener  {
    private TextView nomtext,prenomtext,emailtext,telephonetext,adressetext,sexetext,activitetexte;





    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        Button button = findViewById(R.id.button10);
        button.setOnClickListener(this);




        nomtext = findViewById(R.id.nom);
        prenomtext = findViewById(R.id.prenom);
        emailtext = findViewById(R.id.email);
        telephonetext = findViewById(R.id.telephone);
        adressetext = findViewById(R.id.adresse);
        sexetext = findViewById(R.id.sexe);
        activitetexte = findViewById(R.id.activite);











        nomtext.setText(getIntent().getStringExtra("nom"));
        prenomtext.setText(getIntent().getStringExtra("prenom"));
        emailtext.setText(getIntent().getStringExtra("email"));
        telephonetext.setText(getIntent().getStringExtra("telephone"));
        adressetext.setText(getIntent().getStringExtra("adresse"));



        Bundle extras = getIntent().getExtras();
        String sexe = extras.getString("sexe");
        String styles = extras.getString("loisirs");
        sexetext.setText(sexe);
        activitetexte.setText(styles);










    }
    @Override
    public void onClick(View v) {

        Intent u= new Intent(MainActivity2.this,MainActivity3.class);
        startActivity(u);


}}