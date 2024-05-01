package com.example.myapplication.Activity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.LinearLayout;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication.Adaptor.CategoryAdaptor;
import com.example.myapplication.Adaptor.PopularAdaptor;
import com.example.myapplication.Domain.CategoryDomain;
import com.example.myapplication.Domain.FoodDomain;
import com.example.myapplication.R;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    private RecyclerView.Adapter adapter,adapter2;
    private RecyclerView recyclerViewCategoryList, recyclerViewPopularList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerViewCategory();
        recyclerViewPopular();
        bottomNavigation();
    }
    private void bottomNavigation(){


        LinearLayout CartBtn = findViewById(R.id.CartBtn);
        LinearLayout homeBtn = findViewById(R.id.homeBtn);

        CartBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(MainActivity.this, CartListActivity.class));
            }
        });


        homeBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(MainActivity.this,MainActivity.class));
            }
        });
    }
    private  void recyclerViewCategory(){
        LinearLayoutManager linearLayoutManager=new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false);
        recyclerViewCategoryList= findViewById(R.id.recyclerView);
        recyclerViewCategoryList.setLayoutManager(linearLayoutManager);

        ArrayList<CategoryDomain> category=new ArrayList<>();
        category.add(new CategoryDomain("Pizza", "cat_1"));
        category.add(new CategoryDomain( "Burger", "cat_2"));
        category.add(new CategoryDomain( "Hotdog", "cat_3"));
        category.add(new CategoryDomain( "Drink", "cat_4"));
        category.add(new CategoryDomain( "Donut", "cat_5"));


        adapter=new CategoryAdaptor(category);
        recyclerViewCategoryList.setAdapter(adapter);





    }
    private void recyclerViewPopular(){
        LinearLayoutManager linearLayoutManager=new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL,false);
        recyclerViewPopularList=findViewById(R.id.recyclerView3);
        recyclerViewPopularList.setLayoutManager(linearLayoutManager);
        ArrayList<FoodDomain> foodList=new ArrayList<>();
        foodList.add(new FoodDomain("Pepperoni pizza","pizza1","slices pepperoni,mozzerella chesse,fresh oregano,ground black pepper,pizza sauxe",9.76));
        foodList.add(new FoodDomain("cheese Burger","burger","beef,Gouda cheese,Special Sauce, Lettuce,tomato",8.79));
        foodList.add(new FoodDomain("vegerable pizza","pizza3","olive oil,vegetable oil,pitted kalamata,cherry tomatoes ,fresh oregano , basil",8.5));
        adapter2=new PopularAdaptor(foodList);
        recyclerViewPopularList.setAdapter(adapter2);
    }
}