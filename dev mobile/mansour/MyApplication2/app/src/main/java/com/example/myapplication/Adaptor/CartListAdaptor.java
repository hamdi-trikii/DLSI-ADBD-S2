package com.example.myapplication.Adaptor;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.myapplication.Domain.FoodDomain;
import com.example.myapplication.Helper.ManagementCart;
import com.example.myapplication.Interface.ChangeNumberItemsListener;
import com.example.myapplication.R;

import java.util.ArrayList;

public class CartListAdaptor extends RecyclerView.Adapter<CartListAdaptor.ViewHolder> {
    private ArrayList<FoodDomain> foodDomains;
    private ManagementCart managementCart;
    private ChangeNumberItemsListener changeNumberItemsListener;

    public CartListAdaptor(ArrayList<FoodDomain> foodDomains, Context context, ChangeNumberItemsListener changeNumberItemsListener) {
        this.foodDomains = foodDomains;
        this.managementCart =new ManagementCart(context);
        this.changeNumberItemsListener = changeNumberItemsListener;
    }

    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View inflate= LayoutInflater.from(parent.getContext()).inflate(R.layout.viewholder_cart,parent,false);
        return new ViewHolder(inflate);

    }

    @Override

    public void onBindViewHolder(@NonNull CartListAdaptor.ViewHolder holder,  int position) {
        position=holder.getAdapterPosition();
        holder.title.setText(foodDomains.get(position).getTitle());
        holder.feeEachItem.setText(String.valueOf(foodDomains.get(position).getNumberInCart()));
        holder.totalEachItem.setText(String.valueOf(Math.round((foodDomains.get(position).getNumberInCart()*foodDomains.get(position).getFee())*100)/100));
        holder.num.setText(String.valueOf(foodDomains.get(position).getNumberInCart()));
        int drawableResourceId = holder.itemView.getContext().getResources().getIdentifier(foodDomains.get(position).getPic(),"drawable",holder.itemView.getContext().getPackageName());

        Glide.with(holder.itemView.getContext())
                .load(drawableResourceId)
                .into(holder.pic);
        holder.plusItem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                managementCart.plusNumberFood(foodDomains,holder.getAdapterPosition(),new ChangeNumberItemsListener(){
                    public void changed(){
                        notifyDataSetChanged();
                        ChangeNumberItemsListener.changed();
                    }
                });
            }
        });
        holder.minusItem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                managementCart.minusNumberFood(foodDomains, holder.getAdapterPosition(), new ChangeNumberItemsListener() {
                    private void changed(){
                        notifyDataSetChanged();
                        ChangeNumberItemsListener.changed();
                    }
                });
            }
                });

    }



    @Override
    public int getItemCount() {
        return foodDomains.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView title,feeEachItem;
        ImageView pic,plusItem,minusItem;
        TextView totalEachItem,num;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            title=itemView.findViewById(R.id.titleTxt);
            feeEachItem=itemView.findViewById(R.id.feeEachItem);
            pic=itemView.findViewById(R.id.picCart);
            totalEachItem=itemView.findViewById(R.id.totalEachItem);
            num=itemView.findViewById(R.id.numberItemTxt);
            plusItem=itemView.findViewById(R.id.plusCartBtn);
            minusItem=itemView.findViewById(R.id.minusCartBtn);
        }
        }
    }

