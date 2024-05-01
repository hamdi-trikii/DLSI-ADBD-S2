package com.example.myapplication.Adaptor;

import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.myapplication.Activity.ShowDetailActivity;
import com.example.myapplication.Domain.FoodDomain;
import com.example.myapplication.R;

import java.util.ArrayList;

public class PopularAdaptor extends RecyclerView.Adapter<PopularAdaptor.ViewHolder> {
    ArrayList<FoodDomain> popularFood;


    public PopularAdaptor(ArrayList<FoodDomain> popularFood){
        this.popularFood =popularFood;
    }

    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View inflate= LayoutInflater.from(parent.getContext()).inflate(R.layout.viewholder_popular,parent,false);

        return new ViewHolder(inflate);
    }



    @Override
    public void onBindViewHolder(@NonNull PopularAdaptor.ViewHolder holder,  int position) {
        position=holder.getAdapterPosition();
        holder.title.setText(popularFood.get(position).getTitle());
        holder.fee.setText(String.valueOf(popularFood.get(position).getFee()));

        int drawableResourceId = holder.itemView.getContext().getResources().getIdentifier(popularFood.get(position).getPic() ,"drawable", holder.itemView.getContext().getPackageName());
    Glide.with(holder.itemView.getContext())
                .load(drawableResourceId)
                .into(holder.pic);

        int finalPosition = position;
        holder.addBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent=new Intent(holder.itemView.getContext(), ShowDetailActivity.class);
                intent.putExtra("object", popularFood.get(finalPosition));
                holder.itemView.getContext().startActivity(intent);
            }
        });

    }

    @Override
    public int getItemCount() {
        return popularFood.size();
    }

    public  class ViewHolder extends RecyclerView.ViewHolder{
        TextView title,fee;
        ImageView pic;
        TextView addBtn;


        public ViewHolder(@NonNull  View itemview){
            super(itemview);
            title=itemview.findViewById(R.id.title);
            fee =itemview.findViewById(R.id.fee);
            pic=itemview.findViewById(R.id.pic);
            addBtn=itemview.findViewById(R.id.addBtn);




        }


    }
}
