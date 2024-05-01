package com.example.projet;

import static com.example.projet.R.*;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
private EditText nomtext,prenomtext,emailtext,telephonetext,adressetext;
private String nom;
private String prenom;
private String email;
private String telephone;
private String adresse;
    private String sexe;
RadioButton radioButton;
RadioGroup radioGroup;
RadioButton radioButtonHomme , radioButtonFemme;
CheckBox checkBox,checkBox2,checkBox3,checkBox4;











    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(layout.activity_main);
        Button button = findViewById(id.button);
        button.setOnClickListener(this);
        nomtext = findViewById(id.editTextText);
        prenomtext = findViewById(id.editTextText2);
        emailtext = findViewById(id.editTextTextEmailAddress);
        telephonetext = findViewById(id.editTextPhone);
        adressetext = findViewById(id.editTextTextPostalAddress);
        radioGroup = findViewById(id.radioGroup);
        radioButtonHomme = findViewById(R.id.radioButton2);
        radioButtonFemme = findViewById(R.id.radioButton);
        checkBox = findViewById(id.checkBox);
        checkBox2 = findViewById(id.checkBox2);
        checkBox3 = findViewById(id.checkBox3);
        checkBox4 = findViewById(id.checkBox4);


    }
    @Override
    public void onClick(View v){

         nom =nomtext.getText().toString();
         prenom =prenomtext.getText().toString();
        email =emailtext.getText().toString();
        telephone = telephonetext.getText().toString();
        adresse =adressetext.getText().toString();
        sexe =  radioButtonHomme.isChecked() ? "Homme" : "Femme";
        String activite = "";
        if (checkBox.isChecked()) {
            activite += "peinture, ";
        }
        if (checkBox2.isChecked()) {
            activite += "tennis, ";
        }
        if (checkBox3.isChecked()) {
            activite += "football, ";

        }
        if (checkBox4.isChecked()) {
            activite += "danse, ";

        }
        if (activite.length() > 0) {
            activite = activite.substring(0, activite.length() - 2);}


        Intent i = new Intent(MainActivity.this,MainActivity2.class);
        i.putExtra("nom",nom);
        i.putExtra("prenom",prenom);
        i.putExtra("email",email);
        i.putExtra("telephone",telephone);
        i.putExtra("adresse",adresse);
        i.putExtra("sexe",sexe);
        i.putExtra("loisirs",activite);

        startActivity(i);

    }
    public void checkButton(View v){
        int radioId = radioGroup.getCheckedRadioButtonId();
        radioButton = findViewById(radioId);
        Toast.makeText(this,"votre sexe est  : " +radioButton.getText(),Toast.LENGTH_LONG).show();

    }



}




