package com.example.myapplication.Activity;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.myapplication.Domain.FoodDomain;
import com.example.myapplication.Helper.ManagementCart;
import com.example.myapplication.R;

public class ShowDetailActivity extends AppCompatActivity {
    private TextView addtocartBtn;
    private TextView titleTxt , feeTxt,description,numberOrderTxt;
    private ImageView plusBtn,MinusBtn,picFood;
    private FoodDomain object;
    int numberOrder=1;
    private ManagementCart managementCart;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_detail);

        managementCart=new ManagementCart(this);
        initView();
        getBundle();

    }

    private void getBundle() {
        object = (FoodDomain) getIntent().getSerializableExtra("object");
        int drawableResourceId = this.getResources().getIdentifier(object.getPic(), "drawable", this.getPackageName());


        Glide.with(this)
                .load(drawableResourceId)
                .into(picFood);


        titleTxt.setText(object.getTitle());
        feeTxt.setText("$" + object.getFee());
        description.setText(object.getDescription());
        numberOrderTxt.setText(String.valueOf(numberOrder));

        plusBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                numberOrder = numberOrder + 1;
                numberOrderTxt.setText(String.valueOf(numberOrder));
            }
        });


        MinusBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (numberOrder > 1) {
                    numberOrder = numberOrder - 1;
                }
                numberOrderTxt.setText(String.valueOf(numberOrder));
            }
        });
        addtocartBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                object.setNumberInCart(numberOrder);
                managementCart.insertFood(object);
            }
        });
    }

    private void initView() {
        addtocartBtn=findViewById(R.id.addtocartBtn);
        titleTxt=findViewById(R.id.titleTxt);
        feeTxt=findViewById(R.id.priceTxt);
        description=findViewById(R.id.descriptionTxt);
        numberOrderTxt=findViewById(R.id.numberOrderTxt);
        plusBtn=findViewById(R.id.plusBtn);
        MinusBtn=findViewById(R.id.minusBtn);
        picFood=findViewById(R.id.picfood);
    }
}